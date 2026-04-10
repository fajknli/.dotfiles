# SQL 表连接

## 连接类型概览

```
INNER JOIN  - 只返回匹配的行
LEFT JOIN   - 返回左表所有行，右表无匹配为 NULL
RIGHT JOIN  - 返回右表所有行，左表无匹配为 NULL
FULL JOIN   - 返回两表所有行，无匹配为 NULL
CROSS JOIN  - 笛卡尔积
SELF JOIN   - 表自身连接
```

## INNER JOIN

### 基本语法

```sql
-- 标准写法
SELECT *
FROM table1
INNER JOIN table2 ON table1.key = table2.key;

-- 简写（INNER 可省略）
SELECT *
FROM table1
JOIN table2 ON table1.key = table2.key;
```

### 实际示例

```sql
-- 查询订单及其对应的用户信息
SELECT 
    o.order_id,
    o.amount,
    u.name,
    u.email
FROM orders o
INNER JOIN users u ON o.user_id = u.id;

-- 多表连接
SELECT 
    o.order_id,
    u.name,
    p.product_name,
    oi.quantity
FROM orders o
INNER JOIN users u ON o.user_id = u.id
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id;
```

## LEFT JOIN

### 基本语法

```sql
-- 左表所有行都会返回
SELECT *
FROM table1
LEFT JOIN table2 ON table1.key = table2.key;
```

### 实际示例

```sql
-- 查询所有用户及其订单（包括没有订单的用户）
SELECT 
    u.id,
    u.name,
    o.order_id,
    o.amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id;

-- 查找没有订单的用户
SELECT 
    u.id,
    u.name
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;
```

## RIGHT JOIN

```sql
-- 右表所有行都会返回
SELECT *
FROM table1
RIGHT JOIN table2 ON table1.key = table2.key;

-- 实际示例
SELECT 
    u.name,
    o.order_id,
    o.amount
FROM users u
RIGHT JOIN orders o ON u.id = o.user_id;
```

## FULL JOIN

```sql
-- MySQL 不直接支持 FULL JOIN，使用 UNION 模拟
SELECT * FROM table1
LEFT JOIN table2 ON table1.key = table2.key
UNION
SELECT * FROM table1
RIGHT JOIN table2 ON table1.key = table2.key;

-- PostgreSQL 直接支持
SELECT *
FROM table1
FULL JOIN table2 ON table1.key = table2.key;
```

## CROSS JOIN

```sql
-- 笛卡尔积：左表每行 × 右表每行
SELECT *
FROM colors
CROSS JOIN sizes;

-- 结果示例
-- red, S
-- red, M
-- red, L
-- blue, S
-- blue, M
-- blue, L
```

## SELF JOIN

```sql
-- 表自身连接，需要别名
SELECT 
    e.name AS employee,
    m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- 查找重复的电子邮件
SELECT DISTINCT a.email
FROM users a
JOIN users b ON a.email = b.email AND a.id != b.id;
```

## 多表连接

```sql
-- 三表连接
SELECT 
    o.order_id,
    u.name,
    p.product_name,
    oi.quantity
FROM orders o
JOIN users u ON o.user_id = u.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.status = 'paid';

-- 连接顺序不影响结果，但影响性能
```

## 连接条件

### ON vs WHERE

```sql
-- ON: 在连接时过滤
SELECT *
FROM users u
LEFT JOIN orders o ON u.id = o.user_id AND o.amount > 100;

-- WHERE: 在连接后过滤
SELECT *
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.amount > 100;  -- 实际变成了 INNER JOIN
```

### 复合连接条件

```sql
-- 使用多个条件连接
SELECT *
FROM table1 t1
JOIN table2 t2 ON t1.key1 = t2.key1 AND t1.key2 = t2.key2;

-- 使用 BETWEEN 连接
SELECT *
FROM employees e
JOIN salary_grades s ON e.salary BETWEEN s.min_salary AND s.max_salary;
```

## 实际应用示例

### 统计每个用户的订单数

```sql
SELECT 
    u.id,
    u.name,
    COUNT(o.id) AS order_count,
    COALESCE(SUM(o.amount), 0) AS total_amount
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
ORDER BY total_amount DESC;
```

### 查找共同购买的商品

```sql
-- 购买了商品 A 也购买了商品 B 的用户
SELECT DISTINCT o1.user_id
FROM order_items oi1
JOIN orders o1 ON oi1.order_id = o1.id
JOIN order_items oi2 ON o1.id = oi2.order_id
JOIN orders o2 ON oi2.order_id = o2.id
WHERE oi1.product_id = 1 AND oi2.product_id = 2;
```

### 环比计算

```sql
SELECT 
    t1.month,
    t1.revenue,
    t2.revenue AS prev_month_revenue,
    ROUND((t1.revenue - t2.revenue) / t2.revenue * 100, 2) AS growth_rate
FROM monthly_sales t1
LEFT JOIN monthly_sales t2 ON t1.month = t2.month + INTERVAL 1 MONTH;
```

## 连接性能对比

| 连接类型 | 性能 | 适用场景 |
|----------|------|----------|
| INNER JOIN | 最快 | 只需要匹配的数据 |
| LEFT JOIN | 较快 | 需要左表全部数据 |
| CROSS JOIN | 慢（数据量大时） | 需要生成所有组合 |
| 多表连接 | 取决于顺序 | 复杂查询 |

### 性能优化建议

```sql
-- 1. 先过滤再连接
SELECT *
FROM (SELECT * FROM orders WHERE status = 'paid') o
JOIN users u ON o.user_id = u.id;

-- 2. 使用合适的索引
-- 在连接的列上创建索引
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- 3. 避免连接不必要的表
-- 只 SELECT 需要的列
```
