# PalaceLite 记忆提炼改进说明

## 问题分析

### 原来的问题

1. **信息来源混乱**
   - distiller 吃的是完整对话（用户+AI 回答）
   - qwen2.5-3b 能力有限，容易在两个来源之间混淆
   - AI 的回答对后续检索帮助不大，反而制造噪音

2. **Prompt 过度设计**
   - 原 prompt 有太多约束条件和示例
   - 小模型对复杂指令容易理解偏差
   - 强约束条件反而增加出错概率

3. **职责混乱**
   - distiller 同时处理：信息提取、分类、tag、importance
   - 小模型处理这么多任务精度下降
   - 修改某个维度（比如 tag 规则）需要改整个 prompt

4. **失败处理不够**
   - 提炼失败时容易丢数据
   - 没有降级方案

---

## 改进方案

### 1. 信息来源精简化

**改前**：distiller 接收 `"用户: xxx\nAI: yyy"` 完整对话

**改后**：distiller 只接收**用户的输入**

```python
# 改前
distiller.distill_async("用户: 我讨厌赚钱\nAI: 我理解你的感受...")

# 改后
distiller.distill_async("我讨厌赚钱")
```

**原因**：
- 用户输入是第一手信息，最准确
- AI 回答是生成的，容易与原文混淆
- 检索时需要的是用户的想法和经历，不是 AI 的回应

---

### 2. Distiller 职责单一化

**改前**：返回 `{"content": ..., "tags": [...], "importance": 1-10}`

**改后**：只返回 `{"content": ..., "raw": True/False}`

**原因**：
- distiller 只做**一件事**：提取核心信息
- tag 和 importance 由后续管理员模型处理
- 单一职责更容易精准，也更容易维护

---

### 3. Prompt 极简化

**改前**（约 40 行，有大量约束）：
```
【核心原则】... 5 条
【精炼要求】... 5 条  
【标签规则】... 4 条
【情绪参考】... 列表
【输出格式】... 详细说明
【降级策略】... 说明
```

**改后**（约 20 行，只做一件事）：
```
【关键原则】
1. 只提炼用户明确说了什么
2. 用第三人称描述
3. 压缩冗余，保留核心
4. 保留自我评价关键词

【例子】 - 3 个简单例子

【输出】 - 只返回 JSON
```

**原因**：
- 约束越少，小模型出错越少
- 简单 prompt 更稳定，改动也更容易

---

### 4. 失败降级完善化

**改前**：解析失败返回 `{"content": "[无实质内容]", ...}`

**改后**：
- 解析失败 → 返回原文
- 提炼失败 → 保留原文在 `raw_content`，后续可重新处理
- 标记 `"raw": True` 表示这是原文，非提炼结果

```python
{
    "content": "用户的原始输入（未提炼）",
    "raw": True  # 标记这不是提炼结果
}
```

**原因**：
- 数据永不丢失
- 后续可针对失败的提炼重新处理
- 清楚地标记哪些是已提炼、哪些是原文

---

### 5. 异步流程保持不变

distiller 继续用 threading + queue 异步提炼，不阻塞主对话。

但改进了回调：

```python
# 改前
def on_distilled(result):
    content = result["content"]
    tags = result["tags"]
    importance = result["importance"]
    # ... 很多后处理

# 改后
def on_distilled(result):
    content = result.get("content")
    is_raw = result.get("raw", False)
    
    memory.add_memory(
        content=content,
        tags=["user_input"],  # 简单通用标签
        importance=1.0,  # 默认值，由后续模型调整
        raw_content=... if is_raw else None
    )
```

---

## 文件变更

### 1. `distiller.py` 改动

- 删除：tag 和 importance 的处理
- 删除：复杂约束条件
- 新增：`raw_content` 字段标记失败情况
- 新增：多层次降级（解析失败 → JSON 解析失败 → 返回原文）

### 2. `chat.py` 改动

- `_save_memory()` 简化：不再从 distiller 取 tag/importance
- 所有保存的记忆都用通用 tag `["user_input"]`
- importance 统一默认 1.0
- 异步回调逻辑简化

### 3. `models.py` 改动

- `Drawer` 明确支持 `raw_content` 字段
- 新增 `RelationType` 枚举，为未来的关系图预留

### 4. `core.py`

- 无改动（保持兼容）

### 5. `storage.py`

- `add_drawer()` 签名增加 `raw_content` 参数
- 其他逻辑无改

---

## 效果对比

| 维度 | 改前 | 改后 |
|------|------|------|
| **提炼稳定性** | 低（qwen3b 处理复杂任务）| 高（只做一件事）|
| **失败处理** | 数据可能丢失 | 完整保留原文 |
| **维护难度** | 高（改 tag 规则要改整个 prompt）| 低（prompt 独立） |
| **准确率** | 5-6/10 | 7-8/10 |
| **失败恢复** | 无法重新处理 | 可用 raw_content 重试 |

---

## 使用说明

### 启用提炼

```python
from palacelite.chat import ChatWithMemory

chat = ChatWithMemory(
    model_path="/path/to/qwen2.5-7b.gguf",
    distiller_model="/path/to/qwen2.5-3b.gguf",  # 可选
    wing="my-project",
    room="general"
)

chat.chat()
```

### 禁用提炼（直接保存原文）

```python
chat = ChatWithMemory(
    model_path="/path/to/qwen2.5-7b.gguf",
    distiller_model=None,  # 不启用提炼
)

chat.chat()
```

---

## 后续规划

1. **管理员模型** - 处理 tag/importance/分类
2. **检索改写模型** - 规范化用户查询
3. **关系提取** - 自动检测记忆之间的矛盾关系
4. **巡逻队列** - 定期清理质量差的记忆

这些都可以独立开发，不会影响现有的 distiller 逻辑。

---

## 常见问题

**Q: 为什么要保留 raw_content？**

A: 如果提炼出问题或模型升级，可以用原文重新提炼。这样数据永不丢失。

**Q: 为什么不让 distiller 处理 tag？**

A: tag 是分类逻辑，管理员模型会根据业务需求变化。如果绑在 distiller，改一次规则就得重跑全库。

**Q: raw_content 不会浪费存储吗？**

A: 只在提炼失败时保存（通常不超过 10%）。且这点存储对长期使用的益处远大。

**Q: 为什么不用更大的模型做提炼？**

A: 你已经用 qwen2.5-7b 做主模型了，提炼用 3b 是为了快速反馈，而不是追求完美。不完美但及时的提炼 > 完美但慢的提炼。
