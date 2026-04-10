# SQL 公用表表达式（CTE）

## CTE 基础

### 什么是 CTE

CTE（Common Table Expression）是一个临时的结果集，可以在单个 SQL 语句中多次引用。使用 WITH 关键字定义。

```sql
-- 基本语法
WITH cte_name AS (
    SELECT 查询
)
SELECT * FROM cte_name;
```

### 简单示例

```sql
-- 查询价格高于平均值的产品
WITH avg_price AS (
    SELECT AVG(price) AS avg_price FROM products
)
SELECT p.name, p.price
FROM products p, avg_price
WHERE p.price > avg_price.avg_price;
```

## 多个 CTE

```sql
-- 定义多个 CTE，用逗号分隔
WITH 
    category_stats AS (
        SELECT category, AVG(price) AS avg_price
        FROM products
        GROUP BY category
    ),
    brand_stats AS (
        SELECT brand, COUNT(*) AS product_count
        FROM products
        GROUP BY brand
    )
SELECT * FROM category_stats
UNION ALL
SELECT * FROM brand_stats;
```

## CTE 在复杂查询中的应用

### 替代子查询

```sql
-- 使用子查询（可读性差）
SELECT *
FROM orders
WHERE user_id IN (
    SELECT id FROM users WHERE status = 'active'
)
AND amount > (
    SELECT AVG(amount) FROM orders
);

-- 使用 CTE（可读性好）
WITH active_users AS (
    SELECT id FROM users WHERE status = 'active'
),
avg_order_amount AS (
    SELECT AVG(amount) AS avg_amount FROM orders
)
SELECT o.*
FROM orders o
JOIN active_users au ON o.user_id = au.id
CROSS JOIN avg_order_amount aoa
WHERE o.amount > aoa.avg_amount;
```

### 多表连接中的 CTE

```sql
-- 先聚合再连接
WITH user_order_stats AS (
    SELECT 
        user_id,
        COUNT(*) AS order_count,
        SUM(amount) AS total_amount
    FROM orders
    GROUP BY user_id
)
SELECT 
    u.id,
    u.name,
    uos.order_count,
    uos.total_amount
FROM users u
LEFT JOIN user_order_stats uos ON u.id = uos.user_id;
```

### 避免重复计算

```sql
-- 同一 CTE 被多次引用
WITH expensive_products AS (
    SELECT * FROM products WHERE price > 500
)
SELECT 
    (SELECT COUNT(*) FROM expensive_products) AS count,
    (SELECT AVG(price) FROM expensive_products) AS avg_price,
    (SELECT MAX(price) FROM expensive_products) AS max_price;
```

## 递归 CTE

### 递归语法

```sql
WITH RECURSIVE cte_name AS (
    -- 锚点成员：初始查询
    SELECT initial_query
    UNION ALL
    -- 递归成员：引用 CTE 自身
    SELECT recursive_query
    WHERE condition
)
SELECT * FROM cte_name;
```

### 生成数字序列

```sql
-- MySQL / PostgreSQL
WITH RECURSIVE numbers AS (
    SELECT 1 AS n
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 10
)
SELECT * FROM numbers;
```

### 日期序列

```sql
-- MySQL
WITH RECURSIVE date_series AS (
    SELECT CURDATE() AS date
    UNION ALL
    SELECT date - INTERVAL 1 DAY
    FROM date_series
    WHERE date - INTERVAL 1 DAY >= CURDATE() - INTERVAL 6 DAY
)
SELECT * FROM date_series ORDER BY date;
```

### 组织结构递归查询

```sql
-- 查询员工及所有下属（树形结构）
WITH RECURSIVE org_tree AS (
    -- 锚点：从 CEO 开始
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- 递归：查找下属
    SELECT e.id, e.name, e.manager_id, ot.level + 1
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.id
)
SELECT * FROM org_tree ORDER BY level, name;
```

### 计算阶乘

```sql
WITH RECURSIVE factorial AS (
    SELECT 1 AS n, 1 AS result
    UNION ALL
    SELECT n + 1, result * (n + 1)
    FROM factorial
    WHERE n < 5
)
SELECT * FROM factorial;
```

## CTE vs 子查询 vs 临时表

| 特性 | CTE | 子查询 | 临时表 |
|------|-----|--------|--------|
| 可读性 | 高 | 低（嵌套时） | 中 |
| 可重复引用 | 是（同语句内） | 否 | 是 |
| 递归支持 | 是 | 否 | 否 |
| 性能 | 中 | 中 | 高（有索引） |
| 作用域 | 单条语句 | 单条语句 | 当前会话 |

## 实际应用示例

### 销售排名

```sql
WITH ranked_products AS (
    SELECT 
        category,
        name,
        sales,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY sales DESC) AS rank
    FROM products
)
SELECT * FROM ranked_products WHERE rank <= 3;
```

### 连续日期补全

```sql
WITH RECURSIVE calendar AS (
    SELECT MIN(sale_date) AS date FROM sales
    UNION ALL
    SELECT date + INTERVAL 1 DAY
    FROM calendar
    WHERE date < (SELECT MAX(sale_date) FROM sales)
)
SELECT 
    c.date,
    COALESCE(SUM(s.amount), 0) AS daily_sales
FROM calendar c
LEFT JOIN sales s ON c.date = s.sale_date
GROUP BY c.date
ORDER BY c.date;
```

### 环比计算

```sql
WITH monthly_revenue AS (
    SELECT 
        DATE_FORMAT(created_at, '%Y-%m') AS month,
        SUM(amount) AS revenue
    FROM orders
    GROUP BY DATE_FORMAT(created_at, '%Y-%m')
)
SELECT 
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_revenue,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY month)) / 
          LAG(revenue) OVER (ORDER BY month) * 100, 2) AS growth_rate
FROM monthly_revenue;
```

## 注意事项

| 注意点 | 说明 |
|--------|------|
| 递归深度限制 | MySQL 默认 1000，可调 |
| 性能 | 递归 CTE 可能比循环慢 |
| 语法差异 | MySQL 需要 RECURSIVE 关键字 |
| 无限递归 | 确保递归有条件终止 |

```sql
-- MySQL 设置递归深度
SET SESSION cte_max_recursion_depth = 10000;
```
