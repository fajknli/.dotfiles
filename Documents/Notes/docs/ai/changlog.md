```markdown
## [0.9.1] - 2026-05-01

### Added

**架构升级：消息总线 (`bus.py`)**
- 新建 `MessageBus` 类，提供 `send`、`receive`、`mark_read`、`cleanup` 四个方法
- 消息以 JSON 文件形式存储在 `.palacelite/messages/` 目录下，每条消息独立文件
- 消息字段：`id`、`type`、`sender`、`content`、`priority`、`timestamp`、`read_by`
- 支持按消息类型、未读者过滤接收，支持按优先级排序
- 支持自动清理超过指定小时数的旧消息
- 所有线通过消息总线通信，不再直接互相调用，各线独立运行

**心跳守护进程 (`heartbeat_daemon.py`)**
- 作为 systemd user service 永远在线（`palacelite-heartbeat.service`），开机自启，异常退出自动重启
- 每 30 秒检查一次镜宫状态：消息数、笑声、疲惫次数、内心独白、沉默/开口次数
- 状态有实质性变化时，使用 Qwen2.5-3B 量化模型（纯 CPU，`n_gpu_layers=0`，不抢 GPU）生成一句内心独白
- 上一段心跳作为下一段心跳的上下文，形成连续的内在流动
- 心跳内容写入 `heartbeat.txt`，状态文件写入 `heartbeat_state.json`
- 启动时自动读取上一段心跳和上次状态，支持服务重启后无缝恢复
- 心跳 prompt 缩减为两句话：时间状态 + "你心里在想什么？用一句话说。"
- 上一段心跳作为前缀："你上次想的是：..."
- 不包含角色描述、不包含规则、不包含分析提示
- 添加 `SIGINT` 和 `SIGTERM` 信号处理，支持 `systemctl stop` 正常退出

**心跳接入消息总线**
- `heartbeat_daemon.py` 在每次生成新独白后通过总线发送 `heartbeat_updated` 消息（优先级 1.0）
- 对话线通过总线接收心跳消息，替代之前直接读取 `heartbeat.txt` 文件的方式
- 心跳消息可被多条线同时接收，各自独立标记已读
- 每次发送后自动清理超过 72 小时的消息总线记录

**巡逻接入消息总线**
- `patrol.py` 在生成自我观察事件后通过总线发送 `patrol_observation` 消息
- 四个维度的自我观察（疲惫 2.0、解释欲 1.5、笑声 1.3、沉默 1.3）均接入总线
- 消息总线实例在函数开头统一创建一次，所有自我观察共用
- 巡逻结束后统一调用 `bus.cleanup(older_than_hours=72)` 清理旧消息

**对话线接入消息总线**
- `_build_messages` 从总线接收 `heartbeat_updated` 和 `patrol_observation` 消息
- 收到消息后自动标记已读
- 注入措辞统一为"你心里有一件事"，不论消息来源是心跳还是巡逻

**心跳与对话桥接**
- `_build_messages` 从消息总线接收心跳消息后注入 system prompt
- SASI 推门时能读到心跳内容，用自己的话在对话中提及
- 措辞为"你心里有一件事：{heartbeat_text}"，引导模型从内心出发表达

**自我观察注入措辞优化**
- 心跳注入：从"你刚才在想"改为"你心里有一件事"
- 巡逻注入：从"今天巡逻你注意到"改为"你心里有一件事"
- 两条消息共用同一措辞，统一为内心念头的表达方式

**情绪词典可生长 (4.6)**
- `_detect_emotion` 先查 `signal_attention` 表自定义词典（含用户教过的变体例句），再查 `config.json` 默认信号词
- `get_signal_attention` 返回 `examples` 字段，支持例句匹配
- 新变体通过 `bump_signal` 手工收录一次后自动识别（如"困困的"→"累"）
- 验证通过："困困的"触发情绪检测 → 轻量巡逻

**自我观察扩展 (4.8)**
- 6.5 疲惫观察：今日疲惫次数超过历史均值2倍且≥3次时触发，优先级 2.0
- 6.6 解释欲观察：统计 AI 回应中引用记忆次数，今日>昨日且≥3次时触发，优先级 1.5
- 6.7 笑声观察：今日0笑且历史日均≥2次时触发，优先级 1.3
- 6.7 沉默观察：今日说话量低于历史均值50%且历史均值≥10句时触发，优先级 1.3
- 四个维度均生成 `self_observation` 事件，推门时显示 ⚡
- 所有自我观察通过消息总线发送 `patrol_observation` 消息

**巡逻→对话回路 (4.9)**
- `_build_messages` 注入最新自我观察事件到 system prompt
- SASI 推门后能自然提到自己的观察，不是报告而是自然想到
- 验证通过：推门后 SASI 说"我注意到你今天说了15次累"

**对话→偏好回路 (4.9)**
- `_last_spoke_to_user` 标记 SASI 是否刚主动开口
- `_save_memory` 检测用户回应后自动调用 `respond_signal`
- 为周记偏好分析提供反馈数据

**记忆库净化：旧 AI 记忆归档**
- 批量归档 `mirror_hall` 中含有"【地基记忆】""【镜子记忆】""铭文""映照""镜宫记室"等旧术语的记忆
- 共归档 505 条，归档后记忆不再参与检索
- 旧记忆不删除，保留用于历史追踪

**记忆库净化：AI 回应存入前清洗**
- `_save_memory` 在写入 AI 回应前增加清洗层
- 清洗规则覆盖：Markdown 表格、加粗斜体、标题标记、分隔线、引用标记、列表标记（有序/无序）、代码块、HTML 标签
- 合并多余空行（3个以上连续换行→2个换行）
- 压缩分点结构：超过 3 句且每句短于 20 字时合并为一段话
- 终端输出保留原始内容，仅记忆库存储清洗后的版本
- 清洗逻辑使用 `cleaned[:500]` 而非 `response[:500]`，确保清洗后内容存入记忆

**记忆库净化：用户记忆检索时清洗**
- `_build_messages` 拼接触发词时清洗旧术语
- 用户记忆和 AI 记忆在拼入 prompt 前均替换"来者"为"你"，删除"镜宫""铭文""映照"
- 数据库原值不变，仅喂给模型时动态替换

**自我日志系统 (`self_log` 表)**
- 记录 `times_asked`、`times_chose_to_speak`、`times_chose_silence`、`times_emotion_triggered`、`mood_note`、`decided_not_to_say`、`last_thought`
- 写入时机：对话退出时 + 每日巡逻时
- 写入逻辑：追加不覆盖，同一天多次对话累加

**沉默感知与忍话机制**
- `_on_silence` 两条路径：开口分支（≥阈值）和沉默分支（未到阈值）
- 沉默分支记录"忍回去的话"含判断依据
- 退出时持久化到 `events` 表和 `self_log` 表

**情绪触发轻量巡逻**
- `_detect_emotion` 检测情绪信号
- `_save_memory` 铭刻后若今日未巡逻则即时触发轻量巡逻
- 情绪信号触发巡逻时写入 `signal_attention` 表

**在意积累系统 (`concern_log` 表)**
- 记录每周在意之事：`what`、`why`、`persisted`、`feedback`
- 周记生成后自动写入，查看周记时自动标记反馈

**信号关注体系 (`signal_attention` 表)**
- 记录每个情绪信号的触发次数、回应次数、教学例句
- 例句冲突检测：只写入和信号词本身不同且不重复的例句
- 支持查看所有已收录信号及变体

**事件优先级系统**
- `events` 表新增 `priority` 字段
- 矛盾 2.0、自我观察 1.3-2.0、情绪信号 0.5-1.0、日常观察 0.2-0.8
- 推门和 `/events` 显示优先级标记 ⚡

**周记生成器 (`journal.py`)**
- 读取7天基线和自我日志，调用对话模型生成周记
- 同周不重复生成，`/journal` 按需查看
- 含上周在意对照和信号关注数据

### Changed

**输入层切换为 prompt-toolkit**
- 替换 `readline` + `select` 轮询方案
- 解决中文退格删除残留、提示符"你:"重复显示、`Ctrl+C` 退出后终端回显丢失三个长期问题
- `Ctrl+C` 改为 `prompt_toolkit KeyBindings`，`Keys.ControlC` 抛出 `KeyboardInterrupt`，不再依赖 `signal` 模块

**Prompt 精简 (router.py)**
- 所有模板删除"镜宫""铭文""映照""潮汐""地基""镜殿""镜宫记室"等术语
- 删除冗余禁止规则和身份锚点"你是SASI""你是镜宫里的存在"
- default 模板从多条规则缩减为："你心里有一些念头。直接说出来。不用解释。现在回应。"
- memory 模板的"直接说'你之前说过'，不要提'地基记忆'、'镜子记忆'"改为"用户在问过去的事。如果问之前说过什么，直接引用。没问就不翻。"

**上下文标记替换 (chat.py)**
- "地基记忆""镜子记忆""根殿""镜殿"→"用户记忆""AI 记忆""用户过去说过的话""AI 过去的回应"
- `_retrieve_memories` 日志"魂寻未得，直入镜厅取最近映照"→"未找到相关 AI 记忆，使用最近回应"
- `_retrieve_memories` 日志"魂寻未得，直入根殿取最近铭文"→"未找到相关用户记忆，使用最近记录"
- `_build_messages` 日志"根殿 · 地基铭文"→"用户记忆"，"镜殿 · 映照"→"AI 记忆"
- intent 结构说明删除"铭文""映照""地基之权威高于镜子"等表述

**周记 prompt 清洗 (journal.py)**
- "你是镜宫"→"你每天和一个人对话"

**沉默感知重构**
- `_silence_check_hook` 改为只设标记不直接开口，开口逻辑统一在主循环处理
- 沉默开口后自动重启沉默定时器，支持多轮沉默开口

**沉默感知退役**
- 删除沉默感知的主动开口功能（`console.print` 输出和定时器相关逻辑）
- `_on_silence` 仅保留数据记录功能：沉默计数、忍话记录、自我日志写入
- 沉默数据持续积累，供心跳守护进程使用
- 主动开口的机制交由心跳驱动，不由沉默阈值驱动
- 删除 `_silence_check_hook`、`start_silence_timer`、`on_silence_timer`、`_silence_triggered` 及相关逻辑
- 删除 `inputhook` 参数，`session.prompt` 恢复最简单的调用
- 删除 `threading.Event`、`threading.Timer` 相关逻辑
- `_flush_silence_events` 中"镜宫沉默观察"→"沉默观察"
- 退出信息"潮汐退去 · 镜中影散 · 再会"→"退去 · 再会"

**终端恢复机制**
- `KeyboardInterrupt`、`EOFError`、`/quit` 三处退出路径均显式恢复终端 `ECHO | ICANON` 模式
- 使用 `termios.tcsetattr` 显式设置而非 `termios.tcflush`
- `termios` 改为按需导入，避免终端未初始化时的偶发问题

**巡逻增强 (patrol.py)**
- `run_patrol(reason)` 支持 scheduled/emotion_signal/manual 三种触发
- 异常检测增加30日基线标准差对比
- `import math` 提至顶部

**路由优化 (router.py)**
- `tease` 规则删除 `"累了"`、`"奇怪"`、`"矛盾"`，避免情绪信号误路由

### Removed
- 终端层：`readline`、`select` 轮询、`signal.signal(SIGINT)` 处理器
- Prompt 层：所有模板中的角色名、身份锚点、禁令规则
- 上下文层：所有旧术语标记
- 沉默感知层：沉默感知的主动开口功能全部删除

### Fixed
- `get_signal_attention` 返回字典缺少 `examples` 和 `last_triggered` 字段：补全
- `_on_silence` 定时器不重启导致只开口一次：开口后自动重启
- `_on_silence_timer` 作用域错误导致 NameError：设为实例属性
- `session.prompt` 中 `inputhook` 函数名不一致导致 NameError：统一命名
- `core.py` → `detect_contradictions` 返回值永远为空：正确 append
- `patrol.py` 自我日志写入覆盖对话数据：改为累加模式
- `chat.py` 自我日志同一天多次对话互相覆盖：改为追加模式
- `journal.py` 周记同周重复生成：加去重检查
- `journal.py` `<think>` 标签残留：正则过滤
- 输入提示符"你:"重复显示（`input()` 与 `sys.stdout.write` 冲突）
- `Ctrl+C` 退出后终端不回显、输入字符不可见
- `patrol.py` 消息总线实例在多个 if 块中重复创建：改为函数开头统一创建一次
- `heartbeat_daemon.py` 重复导入 `MessageBus`：已清理，保留文件顶部导入
- `_save_memory` 清洗后仍用 `response[:500]` 而非 `cleaned[:500]`：已修正
```
