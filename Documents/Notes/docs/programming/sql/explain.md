# SQL 执行计划与查询优化

## 什么是执行计划

执行计划是数据库如何执行查询的步骤说明，用于分析查询性能瓶颈。

```sql
-- MySQL
EXPLAIN SELECT * FROM users WHERE age > 18;

-- PostgreSQL（增加 ANALYZE 查看实际执行时间）
EXPLAIN ANALYZE SELECT * FROM users WHERE age > 18;
```

## EXPLAIN 输出解读

### MySQL EXPLAIN 列说明

| 列名 | 说明 | 重要程度 |
|------|------|----------|
| id | 查询执行顺序 | 中 |
| select_type | 查询类型（SIMPLE, PRIMARY, SUBQUERY, DERIVED, UNION） | 高 |
| table | 正在访问的表 | 低 |
| type | 访问类型（性能关键） | 最高 |
| possible_keys | 可能使用的索引 | 中 |
| key | 实际使用的索引 | 高 |
| key_len | 索引使用的长度 | 中 |
| ref | 索引比较的列 | 中 |
| rows | 估计扫描的行数 | 高 |
| filtered | 过滤后行数百分比 | 中 |
| Extra | 额外信息（Using index, Using where, Using filesort, Using temporary） | 高 |

### type 访问类型（性能从好到差）

| type | 说明 | 性能 |
|------|------|------|
| system | 系统表，只有一行 | 最好 |
| const | 主键或唯一索引常量查找 | 极好 |
| eq_ref | 唯一索引连接 | 很好 |
| ref | 非唯一索引查找 | 好 |
| range | 索引范围扫描（BETWEEN, >, <, IN） | 中等 |
| index | 全索引扫描 | 较差 |
| ALL | 全表扫描 | 最差 |

```sql
-- const 示例（最好）
EXPLAIN SELECT * FROM users WHERE id = 1;

-- range 示例（中等）
EXPLAIN SELECT * FROM products WHERE price BETWEEN 50 AND 100;

-- ALL 示例（最差，无索引）
EXPLAIN SELECT * FROM products WHERE price = 50;
```

### Extra 信息解读

| Extra | 含义 | 处理建议 |
|-------|------|----------|
| Using index | 覆盖索引，只查索引不查表 | 好，无需优化 |
| Using where | 需要回表过滤 | 可接受 |
| Using filesort | 需要额外排序 | 尽量添加索引 |
| Using temporary | 使用临时表（GROUP BY 无索引） | 需优化 |
| Using index condition | 索引下推 | 好 |

## 查询优化技巧

### 1. 索引优化

```sql
-- 为 WHERE 条件列创建索引
CREATE INDEX idx_age ON users(age);

-- 为 JOIN 连接列创建索引
CREATE INDEX idx_user_id ON orders(user_id);

-- 覆盖索引（查询列都在索引中）
CREATE INDEX idx_name_age ON users(name, age);
SELECT name, age FROM users WHERE name = '张三';
```

### 2. 避免 SELECT *

```sql
-- 不推荐
SELECT * FROM users;

-- 推荐（只选择需要的列）
SELECT id, name, email FROM users;
```

### 3. 避免在 WHERE 中使用函数

```sql
-- 不推荐（无法使用索引）
SELECT * FROM users WHERE YEAR(created_at) = 2024;

-- 推荐（可以使用索引）
SELECT * FROM users WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
```

### 4. 使用 EXISTS 替代 IN

```sql
-- IN 子查询（可能性能差）
SELECT * FROM users WHERE id IN (SELECT user_id FROM orders);

-- EXISTS（通常更好）
SELECT * FROM users u 
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

### 5. 避免 LIKE 以 % 开头

```sql
-- 不推荐（无法使用索引）
SELECT * FROM users WHERE name LIKE '%张';

-- 推荐（可以使用索引）
SELECT * FROM users WHERE name LIKE '张%';
```

### 6. 优化 LIMIT 分页

```sql
-- 大偏移量分页（慢）
SELECT * FROM users ORDER BY id LIMIT 100000, 10;

-- 使用游标分页（快）
SELECT * FROM users WHERE id > 100000 ORDER BY id LIMIT 10;
```

### 7. 避免 OR 使用 UNION

```sql
-- OR 可能导致不使用索引
SELECT * FROM users WHERE name = '张三' OR email = 'zhang@example.com';

-- 使用 UNION（各子查询可用独立索引）
SELECT * FROM users WHERE name = '张三'
UNION
SELECT * FROM users WHERE email = 'zhang@example.com';
```

### 8. 避免在 WHERE 中对列进行运算

```sql
-- 不推荐
SELECT * FROM products WHERE price * 0.9 > 100;

-- 推荐
SELECT * FROM products WHERE price > 100 / 0.9;
```

## 实际优化案例

### 案例一：慢查询分析

```sql
-- 慢查询
EXPLAIN SELECT o.order_id, u.name, p.product_name
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.status = 'paid'
ORDER BY o.created_at DESC
LIMIT 100;

-- 发现问题：type = ALL, Using filesort
-- 解决方案：添加索引
CREATE INDEX idx_orders_status_created ON orders(status, created_at);
```

### 案例二：GROUP BY 优化

```sql
-- 慢查询
EXPLAIN SELECT user_id, COUNT(*) FROM orders GROUP BY user_id;
-- type = ALL, Using temporary

-- 解决方案：添加索引
CREATE INDEX idx_orders_user_id ON orders(user_id);
-- 变为 type = index，Using index
```

### 案例三：COUNT 优化

```sql
-- 慢（全表扫描）
SELECT COUNT(*) FROM logs;

-- 使用二级索引统计（InnoDB）
SELECT COUNT(*) FROM logs USE INDEX (idx_created_at);
```

## 常用性能查询

### 查看慢查询日志

```sql
-- MySQL
SHOW VARIABLES LIKE 'slow_query_log%';
SET GLOBAL slow_query_log = ON;
SET GLOBAL long_query_time = 2;
```

### 查看当前连接

```sql
-- MySQL
SHOW PROCESSLIST;
SHOW FULL PROCESSLIST;

-- PostgreSQL
SELECT * FROM pg_stat_activity;
```

### 查看表大小

```sql
-- MySQL
SELECT 
    table_name,
    ROUND(((data_length + index_length) / 1024 / 1024), 2) AS size_mb
FROM information_schema.tables
WHERE table_schema = 'database_name'
ORDER BY size_mb DESC;
```

## 优化检查清单

| 检查项 | 操作 |
|--------|------|
| 是否使用索引 | EXPLAIN 查看 type |
| 是否全表扫描 | 避免 type = ALL |
| 是否使用临时表 | 避免 Extra = Using temporary |
| 是否使用文件排序 | 避免 Extra = Using filesort |
| WHERE 条件是否可优化 | 避免函数、运算 |
| JOIN 列是否有索引 | 连接列应建索引 |
| 是否 SELECT * | 只取需要的列 |
| 分页是否优化 | 大偏移量使用游标 |
