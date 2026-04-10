# SQL 函数

## 字符串函数

### 常用函数

| 函数 | 说明 | 示例 |
|------|------|------|
| CONCAT(a, b) | 字符串连接 | CONCAT('Hello', ' ', 'World') -> 'Hello World' |
| LENGTH(s) | 字符串长度 | LENGTH('Hello') -> 5 |
| UPPER(s) | 转大写 | UPPER('hello') -> 'HELLO' |
| LOWER(s) | 转小写 | LOWER('HELLO') -> 'hello' |
| SUBSTRING(s, start, len) | 截取子串 | SUBSTRING('Hello', 2, 3) -> 'ell' |
| TRIM(s) | 去除两端空格 | TRIM('  hi  ') -> 'hi' |
| REPLACE(s, from, to) | 替换 | REPLACE('abca', 'a', 'x') -> 'xbcx' |
| INSTR(s, sub) | 查找位置 | INSTR('Hello', 'e') -> 2 |
| LEFT(s, n) | 左边 n 个字符 | LEFT('Hello', 2) -> 'He' |
| RIGHT(s, n) | 右边 n 个字符 | RIGHT('Hello', 2) -> 'lo' |

```sql
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name,
    UPPER(email) AS email_upper,
    SUBSTRING(phone, 1, 3) AS area_code,
    REPLACE(description, 'old', 'new') AS updated_desc
FROM users;
```

## 数值函数

### 常用函数

| 函数 | 说明 | 示例 |
|------|------|------|
| ROUND(x, d) | 四舍五入 | ROUND(3.14159, 2) -> 3.14 |
| FLOOR(x) | 向下取整 | FLOOR(3.9) -> 3 |
| CEIL(x) | 向上取整 | CEIL(3.1) -> 4 |
| ABS(x) | 绝对值 | ABS(-5) -> 5 |
| MOD(x, y) | 取余 | MOD(10, 3) -> 1 |
| POWER(x, y) | 幂运算 | POWER(2, 3) -> 8 |
| SQRT(x) | 平方根 | SQRT(16) -> 4 |
| RAND() | 随机数 | RAND() -> 0.12345 |

```sql
SELECT 
    price,
    ROUND(price * 0.9, 2) AS discounted_price,
    FLOOR(price / 100) * 100 AS price_tier,
    CEIL(price * 1.1) AS price_with_tax,
    MOD(id, 2) AS is_even
FROM products;
```

## 日期时间函数

### 获取当前时间

```sql
-- MySQL
SELECT 
    NOW(),
    CURDATE(),
    CURTIME(),
    SYSDATE();

-- PostgreSQL
SELECT 
    NOW(),
    CURRENT_DATE,
    CURRENT_TIME,
    CURRENT_TIMESTAMP;
```

### 日期提取

```sql
-- MySQL
SELECT 
    YEAR(created_at) AS year,
    MONTH(created_at) AS month,
    DAY(created_at) AS day,
    HOUR(created_at) AS hour,
    WEEKDAY(created_at) AS weekday,
    DAYOFWEEK(created_at) AS dow
FROM orders;

-- PostgreSQL
SELECT 
    EXTRACT(YEAR FROM created_at) AS year,
    EXTRACT(MONTH FROM created_at) AS month,
    EXTRACT(DOW FROM created_at) AS day_of_week
FROM orders;
```

### 日期计算

```sql
-- MySQL
SELECT 
    DATE_ADD(NOW(), INTERVAL 7 DAY) AS next_week,
    DATE_SUB(NOW(), INTERVAL 1 MONTH) AS last_month,
    DATEDIFF('2024-12-31', '2024-01-01') AS days_diff,
    TIMESTAMPDIFF(YEAR, birth_date, NOW()) AS age;

-- PostgreSQL
SELECT 
    NOW() + INTERVAL '7 days' AS next_week,
    NOW() - INTERVAL '1 month' AS last_month,
    AGE('2024-12-31', '2024-01-01') AS age_interval,
    EXTRACT(YEAR FROM AGE(NOW(), birth_date)) AS age;
```

### 日期格式化

```sql
-- MySQL
SELECT 
    DATE_FORMAT(created_at, '%Y-%m-%d') AS date_only,
    DATE_FORMAT(created_at, '%Y年%m月%d日') AS chinese_date,
    DATE_FORMAT(created_at, '%W') AS weekday_name;

-- 常用格式符
-- %Y: 四位年份  %y: 两位年份
-- %m: 月份(01-12) %M: 月份名
-- %d: 日(01-31)  %W: 星期名
-- %H: 24小时      %h: 12小时
-- %i: 分钟        %s: 秒
```

## 条件函数

### CASE WHEN

```sql
SELECT 
    name,
    price,
    CASE 
        WHEN price < 50 THEN '低价'
        WHEN price BETWEEN 50 AND 200 THEN '中价'
        WHEN price > 200 THEN '高价'
        ELSE '未知'
    END AS price_level
FROM products;
```

### IF / IIF

```sql
-- MySQL
SELECT 
    name,
    IF(price > 100, '贵', '便宜') AS price_tag,
    IFNULL(discount, 0) AS discount_value,
    NULLIF(price, 0) AS safe_price
FROM products;

-- SQL Server / SQLite
SELECT 
    name,
    IIF(price > 100, '贵', '便宜') AS price_tag
FROM products;
```

### COALESCE

```sql
SELECT 
    name,
    COALESCE(phone, mobile, '无联系方式') AS contact
FROM users;
```

## 类型转换

```sql
-- MySQL
SELECT 
    CAST('123' AS SIGNED) AS int_val,
    CAST('123.45' AS DECIMAL(10,2)) AS decimal_val,
    CONVERT('2024-01-15', DATE) AS date_val;

-- PostgreSQL
SELECT 
    '123'::INTEGER AS int_val,
    '123.45'::NUMERIC(10,2) AS decimal_val,
    '2024-01-15'::DATE AS date_val;
```

## 窗口函数

```sql
-- ROW_NUMBER：排名（不并列）
SELECT 
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- RANK：排名（并列跳过）
SELECT 
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- DENSE_RANK：排名（并列不跳过）
SELECT 
    name,
    salary,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
FROM employees;

-- 分组排名
SELECT 
    department,
    name,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank
FROM employees;

-- 累计求和
SELECT 
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) AS running_total
FROM sales;
```
