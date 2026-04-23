**PalaceLite 可执行 ToDo 列表（终版 v2）**

---

**设计哲学**

不是在造工具，是在造一个随时间生长的自己的镜子。工具是表面，镜子是终点。地基不稳后面全得重来，所以第零阶段必须在一切之前完成。数据质量永远优先于功能数量。

---

**第零阶段：换地基**

目标是在动任何新功能之前，把存储层换干净。这一步做完，后面所有阶段都踩得稳。

**1. 替换ChromaDB为sqlite-vec** `palacelite/storage.py`

- [ ] `requirements.txt`和`pyproject.toml`删掉`chromadb>=1.5.0`，新增`sqlite-vec>=0.1.0`
- [ ] `_init_db()`里用sqlite-vec初始化向量表，和现有SQLite同一个文件：
```sql
CREATE VIRTUAL TABLE IF NOT EXISTS vec_drawers USING vec0(
    drawer_id TEXT PRIMARY KEY,
    embedding FLOAT[384]  -- bge-small-zh-v1.5 维度是384
)
```
- [ ] 新增三个私有方法，封装所有向量操作，外部不得直接碰向量层：
  - `_vector_add(drawer_id: str, embedding: List[float]) -> None`
  - `_vector_get(drawer_ids: List[str]) -> Dict[str, List[float]]`
  - `_vector_delete(drawer_ids: List[str]) -> None`
- [ ] 用`_vector_add`重写`add_drawer`的向量写入部分，删掉ChromaDB的`collection.add`
- [ ] 用`_vector_delete`重写`delete_archived_memories`的向量删除部分，删掉ChromaDB的`collection.delete`
- [ ] 删掉`self.chroma_path`、`self.chroma_client`、`ensure_directory(chroma_path)`
- [ ] 删掉`import chromadb`

**2. 修复retrieval.py** `palacelite/retrieval.py`

- [ ] `_get_drawer_embeddings_batch`改为调用`self.storage._vector_get()`，删掉所有直接访问`chroma_client`的代码
- [ ] 确认Retriever里没有任何`chroma`字样残留

**3. encoder改实例变量** `palacelite/storage.py`

- [ ] 删掉`Storage._encoder = None`类变量
- [ ] `__init__`签名改为`Storage(workspace, offline, encoder_model=EMBEDDING_MODEL)`，模型名可从外部传入
- [ ] `__init__`里改为`self.encoder = SentenceTransformer(encoder_model, ...)`实例变量
- [ ] 为将来四模型pipeline里不同模型用不同encoder留好接口，不强耦合

**4. 数据迁移** 新建`scripts/migrate_chroma_to_sqlite.py`

- [ ] 从现有ChromaDB读出所有向量（按room分组，参考现有`_get_drawer_embeddings_batch`的读取逻辑）
- [ ] 用`_vector_add`逐条写入sqlite-vec
- [ ] 打印迁移进度和成功/失败数量
- [ ] 迁移完成后提示可以手动删除`~/.palacelite/chroma/`目录

**5. 更新gitignore和rebuild脚本**

- [ ] `.gitignore`删掉`chroma/`，新增`*.db-shm`、`*.db-wal`
- [ ] `scripts/rebuild_embeddings.py`里删掉`chromadb`相关代码，改用`_vector_add`批量写入

**6. 验证**

- [ ] 跑`scripts/test_models.py`全部通过
- [ ] 跑`python palacelite/core.py`验证增删查搜索全部正常
- [ ] 跑`scripts/rebuild_embeddings.py --dry-run`确认不报错
- [ ] 确认`~/.palacelite/`目录下只有`palace.db`，没有`chroma/`

---

**第一阶段：地基**

第零阶段全部验证通过后再动这里。目标是把骨架搭对，schema一次设计到位。

**1. Schema升级** `palacelite/storage.py`

- [ ] `drawers`表新增`superseded_by TEXT DEFAULT NULL`，外键指向`drawers(id)`
- [ ] `drawers`表新增`raw_content TEXT DEFAULT NULL`，存提炼前的原文备份，提炼出问题时有原文可重跑
- [ ] 现有`content`字段语义改为存提炼后的结构化文本，注释里写清楚
- [ ] 新增`relations`表：
```sql
CREATE TABLE IF NOT EXISTS relations (
    id TEXT PRIMARY KEY,
    drawer_id_a TEXT NOT NULL,
    drawer_id_b TEXT NOT NULL,
    relation_type TEXT NOT NULL,  -- 现在只有 contradicts
    confidence REAL NOT NULL,
    created_at REAL NOT NULL,
    FOREIGN KEY(drawer_id_a) REFERENCES drawers(id) ON DELETE CASCADE,
    FOREIGN KEY(drawer_id_b) REFERENCES drawers(id) ON DELETE CASCADE
)
```
- [ ] `relations`表给`drawer_id_a`和`drawer_id_b`各加索引
- [ ] 新增`patrol_queue`表：
```sql
CREATE TABLE IF NOT EXISTS patrol_queue (
    id TEXT PRIMARY KEY,
    target_id TEXT NOT NULL,
    target_type TEXT NOT NULL,  -- 'drawer' 或 'relation'
    issue_type TEXT NOT NULL,   -- 'low_confidence' 或 'orphan'
    created_at REAL NOT NULL,
    resolved INTEGER DEFAULT 0
)
```
- [ ] 所有新增字段和表在`_init_db()`里套`try/except ALTER TABLE`兼容旧库，参考现有`archived`做法
- [ ] 新增`add_relation(drawer_id_a, drawer_id_b, relation_type, confidence)`方法
- [ ] 新增`get_relations(drawer_id)`方法，返回该记忆的所有关系边
- [ ] 新增`supersede_drawer(old_id, new_id)`方法，填写`superseded_by`字段
- [ ] 新增`add_to_patrol_queue(target_id, target_type, issue_type)`方法
- [ ] 新增`list_patrol_queue(resolved=False)`方法
- [ ] 新增`resolve_patrol_item(item_id, keep: bool)`方法，keep=False时删除target，keep=True时只标记resolved
- [ ] 写`scripts/test_schema.py`，手动插数据验证外键、级联删除、索引都正常，再动后面的

**2. 提炼模型接入** 新建`palacelite/distiller.py`

- [ ] 写`Distiller`类，接收原始对话文本，调用本地小模型提炼
- [ ] prompt里严格要求只返回JSON，不带任何多余内容：
```
你是记忆提炼助手。将以下对话提炼为一条结构化记忆。
只返回JSON，不要任何其他文字：
{"content": "简洁的核心内容", "tags": ["标签1", "标签2"], "importance": 1到10的整数}
```
- [ ] JSON解析失败时降级处理：`raw_content`存原文，`content`填`"[提炼失败，见raw_content]"`，不丢数据
- [ ] 异步队列用`threading.Thread`跑，不阻塞主对话
- [ ] `session_history`保持不动，短期缓冲继续由它承担，对话内检索不受影响

**3. 管理员模型接入** 新建`palacelite/manager.py`

- [ ] 写`MemoryManager`类，接收`Distiller`输出的结构化记忆
- [ ] 实现分类判断：prompt里给定约束顶层分类列表，输出Wing/Room，找不到的一律进杂项，不让模型自由发挥防止分类崩塌：
```
从以下分类中选择最合适的，找不到就返回"杂项"：
[分类列表在这里]
只返回Wing名和Room名，格式：wing/room
```
- [ ] 实现极简关系提取，严格两步走：
  - 第一步：只对tags有重叠的候选记忆才继续，无重叠直接跳过，省掉90%检索量
  - 第二步：对有tag重叠的候选调用`_vector_get`算相似度，超过0.85再检查否定词列表（不是、错了、其实、并非、不对、应该是、之前说的）
  - 两个条件都满足才调用`add_relation`写入`contradicts`关系，confidence暂时写死0.7
  - 宁漏勿错，漏掉比连错代价小
- [ ] 实现`supersede`判断：新记忆和旧记忆语义高度重叠且性质是修正，调用`supersede_drawer()`
- [ ] `relation_type`枚举集中定义在`models.py`，不散落硬编码：
```python
class RelationType:
    CONTRADICTS = "contradicts"
    # 后期扩展：SUPPORTS = "supports" / EXTENDS = "extends"
```

**4. 检索模型接入** 修改`palacelite/retrieval.py`

- [ ] `search()`入口前加查询改写，调用本地小模型把口语化query规范化
- [ ] 改写失败时降级走原始query，不能因改写出错卡住检索
- [ ] `list_drawers()`和`search()`的SQL里加`superseded_by IS NULL`过滤，废弃记忆默认不参与检索
- [ ] 新增`search_including_superseded()`方法供历史查询用，不污染主检索逻辑

**5. pipeline串联** 修改`examples/chat.py`

- [ ] 对话结束后异步触发：原文 → `Distiller` → `MemoryManager` → 存库
- [ ] 替换现有直接`add_memory()`调用，改走pipeline
- [ ] 检索时同时查`session_history`（内存）和`storage`（磁盘），合并结果去重，`session_history`结果优先

**6. 顶层分类策略**

- [ ] 现在不定，全进杂项，跑几周看实际数据自然冒出什么
- [ ] 从真实积累里归纳，不要定你以为自己会想什么

---

**第二阶段：密度**

第一阶段全部跑稳后再动。

**7. 废弃机制完善** `palacelite/storage.py`

- [ ] `list_drawers()`默认过滤`superseded_by IS NOT NULL`，已废弃记忆不出现在常规列表
- [ ] `search()`评分里废弃记忆不参与，SQL层直接过滤，不拉到内存再算
- [ ] CLI新增`palacelite superseded`命令，列出所有已废弃记忆及其替代者，方便人工审查

**8. 关系类型扩展** `palacelite/manager.py`

- [ ] 等本地模型能力到位，在`MemoryManager`里新增`supports`、`extends`识别
- [ ] 在`models.py`的`RelationType`里补充新类型
- [ ] 新增类型的confidence阈值单独配置，不和`contradicts`混用
- [ ] 门槛依然高，乱麻图比没有图更糟糕

**9. 杂项清理工具** 新建`scripts/review_misc.py`

- [ ] 扫描杂项Wing下所有记忆
- [ ] 按内容聚类，输出"这些记忆可能属于同一类别"的建议
- [ ] 人工确认后批量移动到新Wing/Room
- [ ] 这一步做完后可以开始定顶层分类

---

**第三阶段：夜间巡逻**

**10. 巡逻机制** 新建`palacelite/patrol.py`

- [ ] 写`NightPatrol`类，实现定期扫描
- [ ] 关系边处理（记忆本身的遗忘交给时间衰减，两件事逻辑分开不混用）：
  - confidence < 0.3：直接删除，不打扰你
  - confidence 0.3–0.6：调用`add_to_patrol_queue`，target_type填`relation`
  - confidence > 0.6：不动
- [ ] 孤立记忆检测：无任何relation且`last_accessed`超过阈值且importance衰减接近1.0，调用`add_to_patrol_queue`，target_type填`drawer`
- [ ] CLI新增`palacelite patrol`命令，展示`patrol_queue`待审列表，逐条确认留或删
- [ ] 每次处理控制在五分钟内，列表太长就分批，不强迫你一次清完
- [ ] 系统不替你做价值判断，只替你做体力活，最终决定权在你

---

**第四阶段：飞轮**

**11. 微调数据管道完善** `scripts/clean_memories.py`（已有，补充）

- [ ] 过滤掉`superseded_by IS NOT NULL`的废弃记忆，不进训练集
- [ ] 过滤掉低confidence关系边涉及的噪音记忆
- [ ] 过滤掉`raw_content`不为空但`content`是`[提炼失败]`的记录
- [ ] 确认输出格式和目标LoRA训练框架对齐
- [ ] **用LoRA，不要全量微调**，全量微调会导致灾难性遗忘，模型学会你的说话方式但推理能力退化，LoRA把性格做成插件不重写大脑

---

**始终要做的事**

- [ ] 每隔几周扫一次杂项，看能不能归纳出新的顶层分类
- [ ] 定期跑`palacelite patrol`，处理待审列表，控制在每次五分钟以内
- [ ] 换嵌入模型前跑`scripts/rebuild_embeddings.py`，不要忘
- [ ] 关系图越稠密越要警惕噪音，宁缺毋滥，保持图谱干净比丰满更重要

---

**开工顺序**

第零阶段 → 验证通过 → 第一阶段第1条建表 → 跑`test_schema.py` → 表没问题再动Python代码。骨架歪了后面全得重来。
