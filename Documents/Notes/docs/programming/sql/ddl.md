# SQL 数据定义（DDL）

## 数据类型

### 常用数据类型

| 类型 | MySQL | PostgreSQL | 说明 |
|------|-------|------------|------|
| 整数 | INT, BIGINT | INTEGER, BIGINT | 整数类型 |
| 小数 | DECIMAL(10,2) | NUMERIC(10,2) | 精确小数 |
| 浮点 | FLOAT, DOUBLE | REAL, DOUBLE | 近似小数 |
| 字符串 | VARCHAR(255) | VARCHAR(255) | 变长字符串 |
| 定长 | CHAR(10) | CHAR(10) | 定长字符串 |
| 文本 | TEXT | TEXT | 长文本 |
| 日期 | DATE | DATE | 日期 |
| 时间 | DATETIME, TIMESTAMP | TIMESTAMP | 日期时间 |
| 布尔 | BOOLEAN, TINYINT(1) | BOOLEAN | 布尔值 |
| JSON | JSON | JSONB | JSON 数据 |

```sql
CREATE TABLE products (
    id INT,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    description TEXT,
    created_at DATETIME,
    is_active BOOLEAN,
    attributes JSON
);
```

## CREATE TABLE - 创建表

### 基本语法

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    age INT CHECK (age >= 0 AND age <= 150),
    status VARCHAR(20) DEFAULT 'active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 带约束的完整示例

```sql
CREATE TABLE orders (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    order_number VARCHAR(50) NOT NULL UNIQUE,
    amount DECIMAL(10, 2) NOT NULL CHECK (amount > 0),
    status ENUM('pending', 'paid', 'shipped', 'delivered') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE KEY uk_order_number (order_number),
    INDEX idx_user_id (user_id),
    INDEX idx_status (status)
);
```

## 约束

### 约束类型

| 约束 | 说明 | 示例 |
|------|------|------|
| PRIMARY KEY | 主键，唯一且非空 | `id INT PRIMARY KEY` |
| FOREIGN KEY | 外键，引用其他表 | `user_id INT REFERENCES users(id)` |
| UNIQUE | 唯一值 | `email VARCHAR(100) UNIQUE` |
| NOT NULL | 不能为空 | `name VARCHAR(50) NOT NULL` |
| CHECK | 条件检查 | `age INT CHECK (age >= 0)` |
| DEFAULT | 默认值 | `status VARCHAR(20) DEFAULT 'active'` |

```sql
-- 添加约束
ALTER TABLE users ADD UNIQUE (email);
ALTER TABLE users ADD CHECK (age >= 0);
ALTER TABLE orders ADD FOREIGN KEY (user_id) REFERENCES users(id);

-- 删除约束
ALTER TABLE users DROP INDEX email;
ALTER TABLE orders DROP FOREIGN KEY orders_ibfk_1;
```

## ALTER TABLE - 修改表

### 列操作

```sql
-- 添加列
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users ADD COLUMN age INT AFTER email;
ALTER TABLE users ADD COLUMN bio TEXT FIRST;

-- 修改列（MySQL）
ALTER TABLE users MODIFY COLUMN phone VARCHAR(30);
ALTER TABLE users CHANGE COLUMN phone mobile VARCHAR(20);

-- 修改列（PostgreSQL）
ALTER TABLE users ALTER COLUMN age SET NOT NULL;
ALTER TABLE users ALTER COLUMN age TYPE VARCHAR(10);

-- 重命名列
ALTER TABLE users RENAME COLUMN phone TO mobile;

-- 删除列
ALTER TABLE users DROP COLUMN bio;
```

### 表操作

```sql
-- 重命名表
ALTER TABLE users RENAME TO customers;
RENAME TABLE users TO customers;

-- 修改表注释
ALTER TABLE users COMMENT = '用户信息表';

-- 设置自增起始值（MySQL）
ALTER TABLE users AUTO_INCREMENT = 1000;
```

## DROP - 删除

```sql
-- 删除表
DROP TABLE temp_table;
DROP TABLE IF EXISTS temp_table;

-- 删除数据库
DROP DATABASE old_database;

-- 删除视图
DROP VIEW user_orders_view;
```

## 索引

### 创建索引

```sql
-- 普通索引
CREATE INDEX idx_email ON users(email);

-- 唯一索引
CREATE UNIQUE INDEX idx_username ON users(username);

-- 复合索引
CREATE INDEX idx_name_age ON users(last_name, first_name, age);

-- 全文索引（MySQL）
CREATE FULLTEXT INDEX idx_content ON articles(title, content);

-- 删除索引
DROP INDEX idx_email ON users;
```

### 索引使用建议

```sql
-- 适合建索引的列
-- WHERE 条件中的列
-- JOIN 连接的列
-- ORDER BY 的列
-- GROUP BY 的列

-- 不适合建索引的列
-- 重复值多的列（如性别）
-- 频繁更新的列
-- 很少使用的列
```

## 视图

```sql
-- 创建视图
CREATE VIEW active_users AS
SELECT id, name, email, created_at
FROM users
WHERE status = 'active';

-- 使用视图
SELECT * FROM active_users WHERE created_at > '2024-01-01';

-- 更新视图
CREATE OR REPLACE VIEW user_orders AS
SELECT u.name, o.order_number, o.amount
FROM users u
JOIN orders o ON u.id = o.user_id;

-- 删除视图
DROP VIEW active_users;
```

## 临时表

```sql
-- MySQL
CREATE TEMPORARY TABLE temp_sales AS
SELECT category, SUM(amount) AS total
FROM sales
GROUP BY category;

SELECT * FROM temp_sales;
```

## 常用模式

### 创建带自增主键的表

```sql
-- MySQL
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

-- PostgreSQL
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

-- SQLite
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
```

### 创建带时间戳的表

```sql
CREATE TABLE logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    action VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```
