# llama.cpp 笔记

## 一句话理解

llama.cpp 是一个轻量级的 C/C++ 大模型推理框架，能在普通 CPU 上高效运行量化后的大语言模型，无需高端 GPU。

```bash
# 基本用法
./main -m model.gguf -p "Hello" -n 100

# 启动 API 服务
./server -m model.gguf --host 127.0.0.1 --port 8080
```

## 安装与编译

### 依赖安装

```bash
# Arch Linux
sudo pacman -S base-devel cmake git

# Ubuntu/Debian
sudo apt install build-essential cmake git
```

### 从源码编译

```bash
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp
make -j$(nproc)

# 启用 Metal 加速（macOS）
LLAMA_METAL=1 make -j$(nproc)

# 启用 CUDA（NVIDIA GPU）
make -j$(nproc) LLAMA_CUDA=1
```

### CMake 方式（推荐）

```bash
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . --config Release -j$(nproc)
```

## 获取模型

### 下载 GGUF 格式模型

GGUF 是 llama.cpp 专用的量化模型格式，从 Hugging Face 下载：

```bash
# 下载 Mistral 7B Q4 量化版
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q4_K_M.gguf

# 下载 DeepSeek-R1 蒸馏版
wget https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf

# 下载 Qwen2.5-Coder
wget https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct-GGUF/resolve/main/qwen2.5-coder-7b-instruct-q4_k_m.gguf
```

### 国内加速下载

```bash
# 使用 modelscope（国内友好）
pip install modelscope
modelscope download --model "unsloth/DeepSeek-R1-Distill-Qwen-1.5B-GGUF" --local_dir "./models"
```

## 基本使用

### 命令行推理

```bash
# 基础推理
./main -m model.gguf -p "什么是人工智能？" -n 256

# 交互模式
./main -m model.gguf --color -i -r "用户：" -p "用户：你好\n助手："

# 带参数的推理
./main -m model.gguf \
    -p "写一首关于代码的诗" \
    -n 512 \
    --temp 0.7 \
    --top-k 40 \
    --top-p 0.9 \
    --repeat_penalty 1.1
```

### 启动 API 服务

```bash
# 启动 OpenAI 兼容 API
./server -m model.gguf --host 0.0.0.0 --port 8080

# 带参数的 API 服务
./server -m model.gguf \
    --host 0.0.0.0 \
    --port 8080 \
    -n 2048 \
    -c 4096 \
    --threads 8 \
    --api-key your-secret-key
```

## 常用参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `-m` | 模型文件路径 | `-m ./models/llama.gguf` |
| `-p` | 提示词 | `-p "Hello"` |
| `-n` | 生成 token 数 | `-n 256` |
| `-i` | 交互模式 | `-i` |
| `--temp` | 温度（0-2，越高越随机） | `--temp 0.7` |
| `--top-k` | Top-K 采样 | `--top-k 40` |
| `--top-p` | Top-P 采样 | `--top-p 0.9` |
| `--repeat_penalty` | 重复惩罚 | `--repeat_penalty 1.1` |
| `-c` | 上下文窗口大小 | `-c 4096` |
| `-t` | 线程数 | `-t 8` |
| `-ngl` | GPU 卸载层数 | `-ngl 32` |
| `--mlock` | 锁定内存 | `--mlock` |
| `--color` | 彩色输出 | `--color` |

## 量化

### 量化类型选择

| 类型 | 大小（7B） | 质量 | 适用场景 |
|------|-----------|------|----------|
| Q2_K | ~2.5GB | 低 | 内存极度受限 |
| Q3_K_S/M | ~3-3.5GB | 中低 | 平衡测试 |
| Q4_0/Q4_K_S | ~3.8-4.0GB | 中等 | 日常使用 |
| Q4_K_M | ~4.1GB | 良好 | **推荐** |
| Q5_K_S/M | ~4.5-4.8GB | 良好 | 质量优先 |
| Q6_K | ~5.5GB | 优秀 | 质量敏感 |
| Q8_0 | ~7.3GB | 优秀 | 几乎无损 |
| F16 | ~14GB | 原版 | 高精度需求 |

### 量化模型

```bash
# 将 FP16 模型量化为 Q4_K_M
./quantize model-f16.gguf model-q4_k_m.gguf Q4_K_M

# 查看支持的量化类型
./quantize --help
```

## Python 客户端

### 调用 API 服务

```python
import requests

def chat(prompt: str, stream: bool = False):
    url = "http://localhost:8080/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "model",
        "messages": [{"role": "user", "content": prompt}],
        "stream": stream,
        "temperature": 0.7,
        "max_tokens": 2048
    }
    
    resp = requests.post(url, headers=headers, json=payload)
    return resp.json()["choices"][0]["message"]["content"]

# 使用
print(chat("什么是 llama.cpp？"))
```

### 流式输出

```python
def chat_stream(prompt: str):
    url = "http://localhost:8080/v1/chat/completions"
    payload = {
        "model": "model",
        "messages": [{"role": "user", "content": prompt}],
        "stream": True,
        "temperature": 0.7
    }
    
    with requests.post(url, json=payload, stream=True) as resp:
        for line in resp.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith('data: '):
                    data = line[6:]
                    if data == '[DONE]':
                        break
                    import json
                    chunk = json.loads(data)
                    content = chunk["choices"][0]["delta"].get("content", "")
                    if content:
                        print(content, end='', flush=True)
```

## Docker 部署

```yaml
# docker-compose.yml
version: '3.8'

services:
  llama:
    image: ghcr.io/ggml-org/llama.cpp:server
    container_name: llama-server
    ports:
      - "8080:8080"
    volumes:
      - ./models:/models:ro
    command:
      - -m
      - /models/model.gguf
      - --host
      - 0.0.0.0
      - --port
      - 8080
    restart: unless-stopped
```

```bash
docker compose up -d
```

## 性能优化

### CPU 优化

```bash
# 使用更多线程
./main -m model.gguf -t 8

# 锁定内存防止交换
./main -m model.gguf --mlock

# NUMA 优化（多 CPU 插槽）
./main -m model.gguf --numa
```

### GPU 加速

```bash
# 卸载 32 层到 GPU
./main -m model.gguf -ngl 32

# 编译时启用 CUDA
make LLAMA_CUDA=1 -j$(nproc)

# 编译时启用 Metal（macOS）
make LLAMA_METAL=1 -j$(nproc)
```

## 模型推荐

| 场景 | 推荐模型 | 大小 | 说明 |
|------|----------|------|------|
| 通用聊天 | Mistral-7B-Instruct | ~4GB | 平衡之选 |
| 通用聊天 | Llama-3-8B-Instruct | ~5GB | 质量更好 |
| 代码 | Qwen2.5-Coder-7B | ~4GB | 代码能力强 |
| 数学推理 | DeepSeek-R1-Distill-Qwen-1.5B | ~1GB | 轻量推理 |
| 中文 | Qwen2-7B-Instruct | ~4GB | 中文友好 |

## 常见问题

### 1. 内存不足

```bash
# 降低上下文窗口
./main -m model.gguf -c 2048

# 使用更低量化
# Q4_K_M → Q3_K_S → Q2_K
```

### 2. 输出重复或乱码

```bash
# 调整重复惩罚
--repeat_penalty 1.15

# 调整温度
--temp 0.6
```

### 3. 推理速度慢

```bash
# 增加线程
-t $(nproc)

# 使用更小量化
# 或使用 GPU 加速
-ngl 32
```

## 快捷命令

```bash
# 常用别名
alias llm='./main -m ~/models/model.gguf -i --color'
alias llm-server='./server -m ~/models/model.gguf --host 0.0.0.0 --port 8080'
```

## 一句话总结

llama.cpp 核心：`make` 编译，下载 `.gguf` 模型，`./main -m model.gguf -p "提示"` 运行。量化选 Q4_K_M 平衡质量与大小。`./server` 启动 API 服务，用 `-ngl` 启用 GPU 加速。普通电脑也能跑 7B-13B 模型。
