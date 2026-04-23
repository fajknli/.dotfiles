好。基于你已有的 `0.8.0` 记录，我整理一份 **0.8.1** 的 Changelog，只写从 `0.8.0` 到现在的改动，不重复已有内容。

---

## [0.8.1] - 2026-04-23

### Added
- **演化路径命令** (`evolution`)：追踪关键词的观点变化历程，支持 `--strict` 过滤问句和纯态度词
- **事件队列**：`events` 表存储巡逻发现的事件，支持 `/events` 和 `/events_read` 命令
- **重要性自动调整**：矛盾点 +0.5，重复点 -0.3（写入关系表时自动执行）
- **自动否定检测**：`has_opposite_tendency` 支持“不X”与“X”的自动识别（正则匹配）
- **自动巡逻脚本** (`patrol.py`)：每日检测矛盾 + 归档旧忆 + 生成报告，支持 cron 定时
- **对话矛盾提醒**：查询 `relations` 表，在 system prompt 中注入矛盾信息
- **三类关系分类**：`duplicate`（相似度 ≥0.95 且关键词重叠 ≥0.6）、`similar`（≥0.7 且不矛盾）、`contradicts`（观点相反）
- **CLI 关系查看命令**：
  - `list-relations`：支持按类型（`--type`）、龛 ID（`--drawer-id`）过滤
  - `show-relation`：支持关系 ID（`--rel-id`）或龛 ID（`--drawer-id`）查看具体内容
  - 两者均支持短 ID 前缀匹配

### Changed
- 矛盾检测相似度阈值：`0.6` → `0.7`（CLI 默认值同步更新）
- 关键词重叠阈值：`0.2` → `0.3`
- `duplicate` 判定阈值：`0.9` → `0.95`
- `evolution --strict` 增强：过滤问句（`?`、`？`、`吗`），要求同时包含关键词和态度词
- 关闭 `detect_contradictions` 中的 DEBUG 打印
- `list-relations` 表格增加“缘印”列（关系 ID 前 8 位）
- `/list` 命令支持指定数量（如 `/list 20`）

### Fixed
- `list-relations --drawer-id` 前缀匹配失效 → 已修复
- `show-relation --rel-id` 前缀匹配失效 → 已修复
- `_check_contradiction` 关闭共享数据库连接导致后续 `add_memory` 崩溃 → 已修复（不再关闭连接）
- `cli.py` 重复导入 `datetime` → 已删除重复行
- `storage.py` `_init_db` 缺少 `events` 表索引 → 已添加 `idx_events_unread`

### Removed
- `detect_contradictions` 中的 `print(f"DEBUG: ...")` 调试输出

### Known Issues
- 无

---

要我把这个写入 `CHANGELOG.md` 吗？
