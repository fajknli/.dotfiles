#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
带记忆的 AI 对话脚本 - 混合检索版
"""

import sys
import os
import readline
import signal
from pathlib import Path

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

sys.path.insert(0, os.path.expanduser("~/Project/Python/palacelite"))

from palacelite import PalaceLite
from rich.console import Console
from rich.panel import Panel

console = Console()

try:
    from llama_cpp import Llama
    LLAMA_CPP_AVAILABLE = True
except ImportError:
    LLAMA_CPP_AVAILABLE = False
    console.print("[yellow]llama-cpp-python 未安装，使用命令行方式[/yellow]")


class ChatWithMemory:
    def __init__(self, wing_name: str = "default", room_name: str = "chat"):
        # 模型路径
        self.model_path = os.path.expanduser(
            "~/Public/ai/models/mradermacher/mradermacher_Qwen3-4B-Instruct-2507-SOM-MPOA-GGUF_Qwen3-4B-Instruct-2507-SOM-MPOA.Q5_K_M.gguf"
        )
        self.wing = wing_name
        self.room = room_name
        self.memory = PalaceLite()
        self.llm = None

        # 内存中的会话历史（本次对话的累积，确保不丢上下文）
        self.session_history = []

        if not self.memory.get_wing(wing_name):
            self.memory.add_wing(wing_name)
            console.print(f"[yellow]创建 Wing: {wing_name}[/yellow]")

        if not self.memory.get_room(wing_name, room_name):
            self.memory.add_room(wing_name, room_name)
            console.print(f"[yellow]创建 Room: {wing_name}/{room_name}[/yellow]")

        test_mem = self.memory.list_memories(wing_name, room_name)
        console.print(f"[green]记忆系统已加载 (已有 {len(test_mem)} 条记忆)[/green]")
        console.print(f"  Wing: {wing_name}, Room: {room_name}\n")

    def load_model(self):
        """加载模型"""
        if not os.path.exists(self.model_path):
            console.print(f"[red]模型文件不存在: {self.model_path}[/red]")
            return False

        if LLAMA_CPP_AVAILABLE:
            try:
                console.print("[dim]加载模型中...[/dim]")
                self.llm = Llama(
                    model_path=self.model_path,
                    n_ctx=16384,  # 增大上下文窗口
                    n_threads=8,
                    n_gpu_layers=getattr(self, 'gpu_layers', 20),  # 🔥 使用参数值
                    verbose=False
                )
                console.print("[green]模型加载完成[/green]\n")
                return True
            except Exception as e:
                console.print(f"[red]模型加载失败: {e}[/red]")
                return False
        else:
            console.print("[yellow]使用命令行方式[/yellow]")
            return True

    def call_model(self, prompt: str) -> str:
        """调用模型"""
        if self.llm is not None:
            return self._call_llama_cpp(prompt)
        else:
            return self._call_command_line(prompt)

    def _call_llama_cpp(self, prompt: str) -> str:
        """使用 llama-cpp-python 调用"""
        try:
            # ChatML 格式
            formatted_prompt = f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant\n"

            response = self.llm(
                formatted_prompt,
                max_tokens=2048,
                stop=["<|im_end|>", "<|im_start|>"],
                echo=False,
                temperature=0.7,
                top_p=0.8
            )
            return response['choices'][0]['text'].strip()
        except Exception as e:
            return f"[错误] {e}"

    def _call_command_line(self, prompt: str) -> str:
        """使用命令行调用（备用）"""
        import subprocess
        import tempfile

        llama_cli = "/usr/local/bin/llama-cli"

        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
            f.write(prompt)
            prompt_file = f.name

        try:
            cmd = [
                llama_cli,
                "-m", self.model_path,
                "-f", prompt_file,
                "-n", "2048",
                "-e",
                "--no-display-prompt"
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )

            output = result.stdout.strip()
            lines = output.split('\n')
            cleaned = []
            for line in lines:
                if line and not any(x in line.lower() for x in [
                    'loading', 'build', 'model:', 'modalities', 'available',
                    'prompt:', 'generation:', 't/s', '▄', '██'
                ]):
                    cleaned.append(line)

            return '\n'.join(cleaned).strip() or "[模型无输出]"

        except subprocess.TimeoutExpired:
            return "[错误] 超时"
        except Exception as e:
            return f"[错误] {e}"
        finally:
            os.unlink(prompt_file)

    def _build_context(self, user_input: str) -> tuple:
        """
        构建上下文，返回 (context_string, memory_count)
        混合策略：语义相关记忆 + 最近对话 + 本次会话历史
        """
        context_parts = []
        seen_ids = set()

        # 1. 语义相关记忆（5条）
        relevant = self.memory.search(user_input, wing_name=self.wing, top_k=5)
        for r in relevant:
            if r.drawer.id not in seen_ids:
                if "[错误]" not in r.drawer.content:
                    context_parts.append(f"- {r.drawer.content[:250]}")
                    seen_ids.add(r.drawer.id)

        # 2. 最近存储的对话（10条）
        recent_stored = self.memory.list_memories(self.wing, self.room)
        for r in recent_stored[:10]:
            if r.id not in seen_ids:
                if "[错误]" not in r.content:
                    content = r.content[:250]
                    context_parts.append(f"- {content}")
                    seen_ids.add(r.id)

        # 3. 本次会话历史（确保本次对话不丢）
        for msg in self.session_history[-6:]:  # 最近6条
            content = msg[:250]
            if content not in str(context_parts):
                context_parts.append(f"- {content}")

        # 构建最终上下文
        if context_parts:
            # 去重并限制总条数
            unique_parts = []
            seen_content = set()
            for part in context_parts:
                if part not in seen_content:
                    unique_parts.append(part)
                    seen_content.add(part)
                if len(unique_parts) >= 20:  # 最多20条
                    break

            context = "以下是相关的历史对话记录：\n"
            context += "\n".join(unique_parts)
            context += f"\n\n用户: {user_input}"
            memory_count = len(unique_parts)
        else:
            context = user_input
            memory_count = 0

        return context, memory_count

    def chat(self):
        """开始对话"""
        if not self.load_model() and not LLAMA_CPP_AVAILABLE:
            console.print("[red]无法加载模型，退出[/red]")
            return

        os.system('stty sane 2>/dev/null')
        readline.parse_and_bind('set editing-mode emacs')

        def signal_handler(sig, frame):
            console.print("\n[yellow]再见[/yellow]")
            os.system('stty sane 2>/dev/null')
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)

        console.print(Panel.fit("带记忆的 AI 对话", border_style="cyan"))
        console.print("命令: /help /mem /list /stats /clear /quit\n")

        while True:
            try:
                user_input = input("你: ").strip()

                if not user_input:
                    continue

                if user_input.startswith("/"):
                    if self._handle_command(user_input):
                        continue

                # 构建带记忆的上下文
                context, mem_count = self._build_context(user_input)

                console.print(f"[dim]📚 加载了 {mem_count} 条相关记忆[/dim]")
                console.print("[dim]🤔 思考中...[/dim]")

                response = self.call_model(context)

                console.print(f"[bold cyan]AI:[/bold cyan] {response}\n")

                # 更新会话历史
                self.session_history.append(f"用户: {user_input}")
                self.session_history.append(f"AI: {response[:200]}")
                if len(self.session_history) > 20:
                    self.session_history = self.session_history[-20:]

                # 保存记忆
                self.memory.add_memory(
                    content=f"用户: {user_input}",
                    wing_name=self.wing,
                    room_name=self.room,
                    tags=["question"],
                    importance=1
                )
                self.memory.add_memory(
                    content=f"AI: {response[:500]}",
                    wing_name=self.wing,
                    room_name=self.room,
                    tags=["answer"],
                    importance=1
                )
                console.print("[dim]💾 已保存[/dim]\n")

            except KeyboardInterrupt:
                console.print("\n[yellow]再见[/yellow]")
                break
            except EOFError:
                break

    def _handle_command(self, cmd: str) -> bool:
        cmd_lower = cmd.lower().strip()

        if cmd_lower in ["/quit", "/exit", "/q"]:
            console.print("[yellow]再见[/yellow]")
            sys.exit(0)
        elif cmd_lower == "/clear":
            os.system("clear")
        elif cmd_lower == "/help":
            self._show_help()
        elif cmd_lower == "/stats":
            self._show_stats()
        elif cmd_lower.startswith("/mem"):
            query = cmd[4:].strip()
            if query:
                self._search_memory(query)
            else:
                console.print("[red]用法: /mem <搜索内容>[/red]")
        elif cmd_lower == "/list":
            self._list_recent_memories()
        else:
            console.print(f"[red]未知命令: {cmd}[/red]")

        return True

    def _search_memory(self, query: str):
        results = self.memory.search(query, wing_name=self.wing, top_k=5)

        if not results:
            console.print("[yellow]未找到相关记忆[/yellow]\n")
            return

        console.print(f"\n[bold]🔍 搜索 \"{query}\" 的结果:[/bold]\n")
        for i, r in enumerate(results, 1):
            console.print(f"[cyan]{i}.[/cyan] [{r.wing_name}/{r.room_name}] [dim]({r.score:.3f})[/dim]")
            content = r.drawer.content[:200]
            if len(r.drawer.content) > 200:
                content += "..."
            console.print(f"   {content}\n")

    def _list_recent_memories(self):
        memories = self.memory.list_memories(self.wing, self.room)

        if not memories:
            console.print("[yellow]没有记忆[/yellow]\n")
            return

        console.print(f"\n[bold]📋 最近 {min(len(memories), 10)} 条记忆:[/bold]\n")
        for i, m in enumerate(reversed(memories[-10:]), 1):
            content = m.content[:80] + "..." if len(m.content) > 80 else m.content
            console.print(f"[cyan]{i}.[/cyan] {content}")
        console.print()

    def _show_stats(self):
        stats = self.memory.stats()
        memories = self.memory.list_memories(self.wing, self.room)

        console.print(Panel(
            f"Wings: {stats['wings']}\n"
            f"Rooms: {stats['rooms']}\n"
            f"总记忆: {stats['drawers']}\n"
            f"数据库: {stats['db_size_bytes'] / 1024:.1f} KB\n\n"
            f"当前 Wing: {self.wing}\n"
            f"当前 Room: {self.room}\n"
            f"当前记忆数: {len(memories)}\n"
            f"会话历史: {len(self.session_history)} 条",
            title="📊 统计",
            border_style="green"
        ))
        console.print()

    def _show_help(self):
        console.print(Panel(
            "/help  - 帮助\n"
            "/mem <关键词> - 搜索记忆\n"
            "/list - 列出最近记忆\n"
            "/stats - 统计\n"
            "/clear - 清屏\n"
            "/quit - 退出",
            title="❓ 帮助",
            border_style="cyan"
        ))
        console.print()


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--wing", default="default")
    parser.add_argument("-r", "--room", default="chat")
    parser.add_argument("-m", "--model")
    parser.add_argument("-g", "--gpu-layers", type=int, default=20)  # 🔥 新增
    args = parser.parse_args()

    chat = ChatWithMemory(wing_name=args.wing, room_name=args.room)
    if args.model:
        chat.model_path = args.model
    chat.gpu_layers = args.gpu_layers  # 🔥 传给实例
    chat.chat()


if __name__ == "__main__":
    main()
