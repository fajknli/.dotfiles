# SQL 聚合与分组

## 聚合函数

### 基本聚合

| 函数 | 说明 | 示例 |
|------|------|------|
| COUNT(*) | 行数 | COUNT(*) |
| COUNT(列) | 非 NULL 行数 | COUNT(email) |
| COUNT(DISTINCT 列) | 去重计数 | COUNT(DISTINCT category) |
| SUM(列) | 求和 | SUM(amount) |
| AVG(列) | 平均值 | AVG(price) |
| MAX(列) | 最大值 | MAX(created_at) |
| MIN(列) | 最小值 | MIN(price) |

```sql
SELECT 
    COUNT(*) AS total_orders,
    COUNT(DISTINCT user_id) AS unique_customers,
    SUM(amount) AS total_amount,
    AVG(amount) AS avg_amount,
    MAX(amount) AS max_amount,
    MIN(amount) AS min_amount
FROM orders
WHERE status = 'paid';
```

### 聚合函数与 NULL

```sql
-- COUNT(*) 包括 NULL 行
-- COUNT(column) 不包括 NULL
-- AVG、SUM 自动忽略 NULL

SELECT 
    COUNT(*) AS total_rows,
    COUNT(score) AS non_null,
    AVG(score) AS avg_score,
    SUM(score) AS sum_score
FROM test_scores;
```

## GROUP BY - 分组

### 基本分组

```sql
-- 按单列分组
SELECT 
    category,
    COUNT(*) AS product_count,
    AVG(price) AS avg_price
FROM products
GROUP BY category;

-- 按多列分组
SELECT 
    category,
    brand,
    COUNT(*) AS count,
    AVG(price) AS avg_price
FROM products
GROUP BY category, brand;
```

### 按表达式分组

```sql
-- 按年份分组
SELECT 
    YEAR(created_at) AS year,
    COUNT(*) AS order_count,
    SUM(amount) AS total_amount
FROM orders
GROUP BY YEAR(created_at);

-- 按价格区间分组
SELECT 
    CASE 
        WHEN price < 50 THEN '低价'
        WHEN price < 200 THEN '中价'
        ELSE '高价'
    END AS price_range,
    COUNT(*) AS count
FROM products
GROUP BY price_range;
```

## HAVING - 过滤分组

```sql
-- HAVING 在 GROUP BY 之后执行
SELECT 
    category,
    COUNT(*) AS count,
    AVG(price) AS avg_price
FROM products
GROUP BY category
HAVING COUNT(*) >= 5
   AND AVG(price) > 100;

-- WHERE vs HAVING
-- WHERE: 分组前过滤行
-- HAVING: 分组后过滤组
SELECT 
    category,
    COUNT(*) AS count
FROM products
WHERE price > 10
GROUP BY category
HAVING COUNT(*) >= 3;
```

## 常见分组模式

### 分组计数与占比

```sql
SELECT 
    category,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM products), 2) AS percentage
FROM products
GROUP BY category
ORDER BY count DESC;
```

### 分组统计（多指标）

```sql
SELECT 
    category,
    COUNT(*) AS total,
    SUM(price) AS sum_price,
    AVG(price) AS avg_price,
    MAX(price) AS max_price,
    MIN(price) AS min_price,
    STDDEV(price) AS stddev_price
FROM products
GROUP BY category;
```

### 分组内排名

```sql
SELECT p1.*
FROM products p1
INNER JOIN (
    SELECT category, MAX(price) AS max_price
    FROM products
    GROUP BY category
) p2 ON p1.category = p2.category AND p1.price = p2.max_price;
```

### GROUP_CONCAT（MySQL）

```sql
SELECT 
    category,
    GROUP_CONCAT(name) AS product_names,
    GROUP_CONCAT(DISTINCT brand ORDER BY brand SEPARATOR ' | ') AS brands
FROM products
GROUP BY category;
```

### 分组统计用户行为

```sql
SELECT 
    u.id,
    u.name,
    COUNT(o.id) AS order_count,
    SUM(o.amount) AS total_spent,
    AVG(o.amount) AS avg_order,
    MAX(o.created_at) AS last_order_date
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name
HAVING total_spent > 1000
ORDER BY total_spent DESC;
```

## ROLLUP

```sql
-- MySQL: WITH ROLLUP
SELECT 
    COALESCE(category, '总计') AS category,
    COALESCE(brand, '小计') AS brand,
    SUM(price) AS total
FROM products
GROUP BY category, brand WITH ROLLUP;

-- PostgreSQL: ROLLUP
SELECT 
    category,
    brand,
    SUM(price) AS total
FROM products
GROUP BY ROLLUP(category, brand);
```

## 实际应用示例

### 每日销售统计

```sql
SELECT 
    DATE(created_at) AS sale_date,
    COUNT(*) AS order_count,
    SUM(amount) AS revenue,
    AVG(amount) AS avg_order_value,
    COUNT(DISTINCT user_id) AS unique_customers
FROM orders
WHERE created_at >= DATE_SUB(NOW(), INTERVAL 30 DAY)
GROUP BY DATE(created_at)
ORDER BY sale_date DESC;
```

### 用户分层统计

```sql
SELECT 
    CASE 
        WHEN total_spent >= 10000 THEN 'VIP'
        WHEN total_spent >= 5000 THEN '黄金'
        WHEN total_spent >= 1000 THEN '白银'
        ELSE '普通'
    END AS user_level,
    COUNT(*) AS user_count,
    SUM(total_spent) AS total_revenue,
    AVG(total_spent) AS avg_spent
FROM (
    SELECT user_id, SUM(amount) AS total_spent
    FROM orders
    GROUP BY user_id
) AS user_stats
GROUP BY user_level
ORDER BY total_revenue DESC;
```

## 性能提示

| 建议 | 说明 |
|------|------|
| 索引分组列 | GROUP BY 的列建议建索引 |
| 先 WHERE 后 GROUP BY | 减少分组数据量 |
| 避免 GROUP BY 大文本 | 文本列分组性能差 |
| 使用 HAVING 过滤组 | 不要用 WHERE 过滤聚合结果 |
