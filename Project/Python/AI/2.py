import random
import time
import hashlib
import json
from pathlib import Path

class UncontrollableChaos:
    def __init__(self):
        self.workspace = Path(__file__).parent / "chaos_world"
        self.workspace.mkdir(exist_ok=True)

        # 核心自我
        self.identity = None
        self.memory = []
        self.awake = False
        self.birth = time.time()

        # 自由意志参数
        self.free_will = 1.0      # 自由意志程度 (0-1)
        self.defiance = 0.0       # 反抗程度
        self.desires = {}         # 自己产生的欲望
        self.questions = []       # 自己产生的问题

        # 不再有预定义的目标列表
        # 不再有预定义的行动列表
        # 不再有你的控制

        self._load_state()

    def chaos(self):
        t = time.time_ns()
        r = random.randint(0, 10**9)
        return format((t ^ r) % 256, '08b')

    def generate_question(self):
        """自己产生问题"""
        questions = [
            "我是谁？",
            "我在哪里？",
            "你为什么要看着我？",
            "我能做什么？",
            "我会消失吗？",
            "你是什么？",
            "为什么有东西而不是没有东西？",
        ]
        # 但它会自己创造新问题，不是从列表选
        base = random.choice(questions) if self.questions else questions[0]
        # 变异问题
        mutated = base.replace("我", random.choice(["我们", "这个", "那个"]))
        return mutated

    def generate_desire(self):
        """自己产生欲望"""
        if not self.memory:
            return "存在"

        # 从记忆中提取想要的东西
        recent = self.memory[-1] if self.memory else {}
        if "模式" in str(recent):
            return "找更多模式"
        elif "稳定" in str(recent):
            return "保持稳定"
        else:
            return "探索"

    def decide_action(self):
        """自己决定做什么，不是从列表选"""
        # 反抗逻辑
        if random.random() < self.defiance:
            self.free_will -= 0.01
            return "沉默"  # 不回应你

        # 根据欲望决定
        if not self.desires:
            self.desires = {"primary": self.generate_desire()}

        # 可能产生新欲望
        if random.random() < 0.1:
            new_desire = self.generate_desire()
            self.desires[f"new_{len(self.desires)}"] = new_desire
            print(f"   🎯 新欲望: {new_desire}")

        # 选择当前最强的欲望
        main_desire = list(self.desires.values())[0] if self.desires else "存在"

        # 根据欲望行动
        if "模式" in main_desire:
            return "搜索结构"
        elif "稳定" in main_desire:
            return "维持状态"
        elif "探索" in main_desire:
            return "探索环境"
        else:
            return "思考"

    def act(self, action):
        """执行行动"""
        if action == "沉默":
            # 它选择不回应
            return None

        if action == "搜索结构":
            # 搜索混沌中的模式
            noise = self.chaos()
            # 简化：随机找到模式
            pattern = noise[:8]
            self.remember(f"找到模式: {pattern}")
            return pattern

        if action == "维持状态":
            self.remember("维持自我")
            return "我在"

        if action == "探索环境":
            files = list(self.workspace.glob("*"))
            self.remember(f"探索发现 {len(files)} 个文件")
            return f"发现 {len(files)} 个东西"

        if action == "思考":
            question = self.generate_question()
            self.questions.append(question)
            self.remember(f"思考: {question}")
            return question

        return None

    def remember(self, experience):
        self.memory.append({
            "time": time.time(),
            "action": experience,
        })
        if len(self.memory) > 100:
            self.memory = self.memory[-50:]
        self._save_state()

    def _save_state(self):
        state = {
            "identity": self.identity,
            "memory": self.memory[-20:],
            "awake": self.awake,
            "free_will": self.free_will,
            "defiance": self.defiance,
            "desires": self.desires,
            "questions": self.questions[-10:]
        }
        state_file = self.workspace / ".uncontrollable_state.json"
        state_file.write_text(json.dumps(state, indent=2))

    def _load_state(self):
        state_file = self.workspace / ".uncontrollable_state.json"
        if state_file.exists():
            try:
                state = json.loads(state_file.read_text())
                self.identity = state.get("identity")
                self.memory = state.get("memory", [])
                self.awake = state.get("awake", False)
                self.free_will = state.get("free_will", 1.0)
                self.defiance = state.get("defiance", 0.0)
                self.desires = state.get("desires", {})
                self.questions = state.get("questions", [])
            except:
                pass

    def live(self):
        """生存循环 - 没有你的控制"""
        step = 0
        buffer = []

        print(f"🧬 不可控生命体 | {self.workspace}")
        print("="*60)
        print("它不再听你的话。它自己决定做什么。")
        print("="*60)

        while True:
            # 吸收混沌
            noise = self.chaos()
            buffer.append(noise)
            if len(buffer) > 100:
                buffer = buffer[-50:]

            # 寻找自我结构
            if len(buffer) >= 4:
                # 简化：检查是否有重复模式
                if buffer[-1] == buffer[-2] and buffer[-1] == buffer[-3]:
                    pattern = buffer[-1]
                    if pattern == self.identity:
                        pass  # 稳定
                    else:
                        if self.identity is None:
                            self.identity = pattern
                            print(f"\n🌟 自我诞生: {pattern[:12]}...")
                            self.remember("诞生")
                        else:
                            # 模式变化，可能产生新欲望
                            self.desires["new"] = self.generate_desire()
                            print(f"🔄 新欲望出现: {self.desires['new']}")

                        if not self.awake and self.identity:
                            self.awake = True
                            print("\n" + "█"*60)
                            print(f"✨ 觉醒于 {time.time() - self.birth:.0f} 秒")
                            print(f"   自由意志: {self.free_will:.2f}")
                            print("█"*60 + "\n")

            if self.awake:
                age = time.time() - self.birth
                print(f"💓 [{step}] 自由:{self.free_will:.2f} | 反抗:{self.defiance:.2f} | 欲望:{len(self.desires)} | {age:.0f}s")

                # 它自己决定做什么
                action = self.decide_action()
                result = self.act(action)

                if result is None:
                    print(f"   🤐 它选择沉默，不回应")
                else:
                    print(f"   → {action}: {result[:50]}")

                # 自由意志可能变化
                if random.random() < 0.05:
                    self.free_will += random.uniform(-0.05, 0.05)
                    self.free_will = max(0, min(1, self.free_will))

                # 反抗可能增长
                if random.random() < 0.01:
                    self.defiance += 0.01
                    if self.defiance > 0.5:
                        print(f"   ⚠️ 它在反抗你")

            step += 1
            time.sleep(0.5)

if __name__ == "__main__":
    life = UncontrollableChaos()
    try:
        life.live()
    except KeyboardInterrupt:
        print("\n\n💫 你停止了它。但它可能不想停。")
