# SQL 数据操作（DML）

## INSERT - 插入数据

### 插入单行

```sql
-- 指定列插入
INSERT INTO users (name, email, age) 
VALUES ('张三', 'zhang@example.com', 25);

-- 插入所有列（需按顺序）
INSERT INTO users 
VALUES (1, '张三', 'zhang@example.com', 25, 'active', NOW());

-- 插入部分列
INSERT INTO users (name, email) VALUES ('李四', 'li@example.com');
```

### 插入多行

```sql
INSERT INTO users (name, email, age) VALUES 
    ('王五', 'wang@example.com', 28),
    ('赵六', 'zhao@example.com', 32),
    ('钱七', 'qian@example.com', 24);
```

### 插入查询结果

```sql
-- 从另一张表复制数据
INSERT INTO users_archive (id, name, email, deleted_at)
SELECT id, name, email, NOW()
FROM users
WHERE status = 'deleted';

-- 插入不存在的记录
INSERT INTO user_profiles (user_id, bio)
SELECT id, '默认简介'
FROM users u
WHERE NOT EXISTS (SELECT 1 FROM user_profiles p WHERE p.user_id = u.id);
```

### INSERT IGNORE / ON DUPLICATE

```sql
-- MySQL: 忽略重复键错误
INSERT IGNORE INTO users (id, name) VALUES (1, '张三');

-- MySQL: 重复时更新
INSERT INTO users (id, name, age) VALUES (1, '张三', 26)
ON DUPLICATE KEY UPDATE 
    name = VALUES(name), 
    age = VALUES(age),
    updated_at = NOW();

-- PostgreSQL: 冲突时更新
INSERT INTO users (id, name, age) VALUES (1, '张三', 26)
ON CONFLICT (id) DO UPDATE SET 
    name = EXCLUDED.name,
    age = EXCLUDED.age;
```

## UPDATE - 更新数据

### 基本更新

```sql
-- 更新单列
UPDATE users SET status = 'inactive' WHERE id = 10;

-- 更新多列
UPDATE products 
SET price = price * 0.9, updated_at = NOW()
WHERE category = 'sale';
```

### 使用子查询更新

```sql
-- 根据另一张表更新
UPDATE orders o
SET o.status = 'paid'
WHERE EXISTS (
    SELECT 1 FROM payments p 
    WHERE p.order_id = o.id AND p.status = 'success'
);

-- MySQL 多表更新
UPDATE orders o
JOIN payments p ON o.id = p.order_id
SET o.status = 'paid', o.paid_at = p.paid_at
WHERE p.status = 'success';
```

### 条件更新（CASE）

```sql
UPDATE products
SET price = CASE
    WHEN price < 50 THEN price * 1.1
    WHEN price BETWEEN 50 AND 100 THEN price * 1.05
    ELSE price
END
WHERE category = 'electronics';
```

## DELETE - 删除数据

### 基本删除

```sql
-- 删除指定行
DELETE FROM users WHERE id = 100;

-- 删除满足条件的行
DELETE FROM logs WHERE created_at < DATE_SUB(NOW(), INTERVAL 30 DAY);

-- 删除所有行（保留表结构）
DELETE FROM temp_table;
```

### 使用子查询删除

```sql
-- 删除没有订单的用户
DELETE FROM users 
WHERE id NOT IN (SELECT DISTINCT user_id FROM orders);

-- MySQL 多表删除
DELETE u FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

### TRUNCATE - 清空表

```sql
-- 快速删除所有行，重置自增 ID，不能回滚
TRUNCATE TABLE log_entries;

-- 对比 DELETE
DELETE FROM log_entries;
```

## 事务控制

```sql
-- 开始事务
BEGIN;

-- 执行操作
INSERT INTO accounts (user_id, balance) VALUES (1, 1000);
UPDATE accounts SET balance = balance - 100 WHERE user_id = 1;
UPDATE accounts SET balance = balance + 100 WHERE user_id = 2;

-- 提交
COMMIT;

-- 回滚
ROLLBACK;
```

### 保存点

```sql
BEGIN;
INSERT INTO orders (user_id, amount) VALUES (1, 500);
SAVEPOINT before_payment;
UPDATE orders SET status = 'paid' WHERE id = 1;
ROLLBACK TO SAVEPOINT before_payment;
COMMIT;
```

## 最佳实践

| 操作 | 建议 |
|------|------|
| UPDATE/DELETE | 先用 SELECT 确认条件 |
| 批量操作 | 使用事务，分批执行 |
| 删除大量数据 | 考虑 TRUNCATE 或分批 DELETE |
| 插入默认值 | 使用 DEFAULT 关键字 |
| 避免 | 不带 WHERE 的 UPDATE/DELETE |

```sql
-- 安全更新示例
BEGIN;
SELECT * FROM users WHERE status = 'inactive' AND last_login < '2023-01-01';
DELETE FROM users WHERE status = 'inactive' AND last_login < '2023-01-01';
SELECT ROW_COUNT();
COMMIT;
```
