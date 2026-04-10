# SQL 基础查询

## SELECT 语句

### 查询所有列

```sql
-- 查询表中所有数据
SELECT * FROM users;

-- 查询指定列
SELECT id, name, email FROM users;

-- 查询并计算
SELECT name, price, price * 0.9 AS discounted_price FROM products;
```

### 去重查询

```sql
-- DISTINCT 去除重复值
SELECT DISTINCT category FROM products;
SELECT DISTINCT category, brand FROM products;
```

## WHERE 条件筛选

### 比较运算符

```sql
-- 等于、不等于
SELECT * FROM users WHERE age = 25;
SELECT * FROM users WHERE status != 'deleted';

-- 大于、小于
SELECT * FROM products WHERE price > 100;
SELECT * FROM orders WHERE amount >= 1000;

-- 范围查询
SELECT * FROM products WHERE price BETWEEN 50 AND 200;
SELECT * FROM users WHERE created_at BETWEEN '2024-01-01' AND '2024-12-31';
```

### 逻辑运算符

```sql
-- AND
SELECT * FROM products 
WHERE category = 'electronics' AND price < 500;

-- OR
SELECT * FROM users 
WHERE city = '北京' OR city = '上海';

-- NOT
SELECT * FROM users WHERE NOT status = 'inactive';

-- 组合使用
SELECT * FROM orders 
WHERE status = 'paid' 
  AND (amount > 1000 OR discount > 0);
```

### IN 和 NOT IN

```sql
-- IN：匹配列表中的值
SELECT * FROM users WHERE city IN ('北京', '上海', '广州');
SELECT * FROM orders WHERE status IN ('paid', 'shipped');

-- NOT IN：排除列表中的值
SELECT * FROM products WHERE category NOT IN ('discontinued', 'out_of_stock');
```

### LIKE 模糊匹配

```sql
-- % 代表任意多个字符
SELECT * FROM users WHERE name LIKE '张%';
SELECT * FROM users WHERE email LIKE '%@gmail.com';

-- _ 代表单个字符
SELECT * FROM users WHERE phone LIKE '138________';

-- 转义特殊字符
SELECT * FROM products WHERE name LIKE '%\%%' ESCAPE '\\';
```

### NULL 值处理

```sql
-- NULL 不能用 = 判断
SELECT * FROM users WHERE email IS NULL;
SELECT * FROM users WHERE email IS NOT NULL;

-- COALESCE 处理 NULL
SELECT name, COALESCE(phone, '无电话') AS contact FROM users;
```

## ORDER BY 排序

```sql
-- 单列排序
SELECT * FROM products ORDER BY price ASC;
SELECT * FROM products ORDER BY price DESC;

-- 多列排序
SELECT * FROM products 
ORDER BY category ASC, price DESC;

-- 按表达式排序
SELECT name, price * quantity AS total 
FROM order_items 
ORDER BY total DESC;
```

## LIMIT 分页

```sql
-- MySQL / PostgreSQL / SQLite
SELECT * FROM users LIMIT 10;
SELECT * FROM users LIMIT 10 OFFSET 20;
SELECT * FROM users LIMIT 20, 10;

-- SQL Server / Oracle
SELECT TOP 10 * FROM users;
```

## 子查询

### WHERE 子句中的子查询

```sql
-- 标量子查询（返回单个值）
SELECT * FROM products 
WHERE price > (SELECT AVG(price) FROM products);

-- 列子查询（返回一列）
SELECT * FROM users 
WHERE id IN (SELECT user_id FROM orders WHERE amount > 1000);

-- EXISTS 子查询
SELECT * FROM users u
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.user_id = u.id);
```

### FROM 子句中的子查询

```sql
SELECT category, avg_price
FROM (
    SELECT category, AVG(price) AS avg_price
    FROM products
    GROUP BY category
) AS category_stats
WHERE avg_price > 100;
```

### SELECT 子句中的子查询

```sql
SELECT 
    name,
    price,
    (SELECT AVG(price) FROM products) AS avg_price,
    price - (SELECT AVG(price) FROM products) AS diff
FROM products;
```

## UNION 合并结果

```sql
-- UNION：去重合并
SELECT name, email FROM customers
UNION
SELECT name, email FROM suppliers;

-- UNION ALL：保留重复
SELECT city FROM customers
UNION ALL
SELECT city FROM suppliers;
```

## 常见模式

### 查询第 N 高的值

```sql
-- 第2高的工资
SELECT DISTINCT salary 
FROM employees 
ORDER BY salary DESC 
LIMIT 1 OFFSET 1;

-- 使用子查询
SELECT MAX(salary) FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees);
```

### 查找重复记录

```sql
SELECT email, COUNT(*) 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;
```

### 条件计数

```sql
SELECT 
    COUNT(*) AS total,
    SUM(CASE WHEN status = 'active' THEN 1 ELSE 0 END) AS active_count,
    SUM(CASE WHEN status = 'inactive' THEN 1 ELSE 0 END) AS inactive_count
FROM users;
```
