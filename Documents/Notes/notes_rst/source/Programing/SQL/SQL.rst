SQL
#######

SQL 的执行逻辑

F-W-G-H-O-L

FROM

WHERE

GROUP BY

HAVING

ORDER BY

LIMIT

::

    SELECT * FROM students           -- 1. 从学生表取数据
    ORDER BY age DESC                -- 2. 按年龄降序排列
    LIMIT 2;                         -- 3. 取前2条记录

    -- 1. 查询所有学生的所有信息
    SELECT * FROM students;

    -- 2. 只查询学生的姓名和年龄
    SELECT name, age FROM students;

    -- 3. 给列起别名（更友好的显示）
    SELECT 
        name AS 姓名, 
        age AS 年龄 
    FROM students;

    -- 4. 查询年龄大于20岁的学生
    SELECT * FROM students WHERE age > 20;

    -- 5. 查询年龄在19到22岁之间的学生
    SELECT * FROM students WHERE age BETWEEN 19 AND 22;

    -- 6. 查询姓名为"张三"的学生
    SELECT * FROM students WHERE name = '张三';

    -- 7. 按年龄排序（从小到大）
    SELECT * FROM students ORDER BY age ASC;

    -- 8. 按年龄排序（从大到小）
    SELECT * FROM students ORDER BY age DESC;

    -- 9. 只显示前2条记录
    SELECT * FROM students LIMIT 2;

    -- 10. 跳过第1条，显示后面的2条记录
    SELECT * FROM students LIMIT 2 OFFSET 1;

高级查询技巧

::

    -- 11. 模糊查询：查询名字中包含"三"的学生
    SELECT * FROM students WHERE name LIKE '%三%';

    -- 12. 模糊查询：查询姓"王"的学生
    SELECT * FROM students WHERE name LIKE '王%';

    -- 13. 查询年龄最大的学生
    SELECT * FROM students 
    ORDER BY age DESC 
    LIMIT 1;

    -- 14. 计算学生的平均年龄
    SELECT AVG(age) AS 平均年龄 FROM students;

    -- 15. 统计学生总数
    SELECT COUNT(*) AS 学生总数 FROM students;

    -- 16. 找出最小年龄和最大年龄
    SELECT 
        MIN(age) AS 最小年龄,
        MAX(age) AS 最大年龄 
    FROM students;

    -- 17. 按年龄段分组统计
    SELECT 
        CASE 
            WHEN age < 20 THEN '20岁以下'
            WHEN age BETWEEN 20 AND 21 THEN '20-21岁'
            ELSE '22岁以上'
        END AS 年龄段,
        COUNT(*) AS 人数
    FROM students
    GROUP BY 年龄段;

数据更新操作

::

    -- 18. 更新数据：将李四的年龄改为23岁
    UPDATE students SET age = 23 WHERE name = '李四';

    -- 验证更新结果
    SELECT * FROM students WHERE name = '李四';

    -- 19. 同时更新多个字段（添加邮箱字段后使用）
    ALTER TABLE students ADD COLUMN email TEXT;

    -- 更新多个学生的邮箱
    UPDATE students SET 
        email = CASE 
            WHEN name = '张三' THEN 'zhangsan@email.com'
            WHEN name = '李四' THEN 'lisi@email.com'
            WHEN name = '王五' THEN 'wangwu@email.com'
        END;

    -- 查看更新结果
    SELECT * FROM students;

1. ALTER 是一个多功能命令
ALTER命令用于修改各种数据库对象的结构，而不仅仅是表。在不同的数据库系统中，它可以修改的对象包括：

::

    TABLE（表）：最常用的，修改表结构

    INDEX（索引）：修改索引

    VIEW（视图）：修改视图

    SEQUENCE（序列）：修改序列

    DATABASE（数据库）：修改数据库属性

    PROCEDURE/FUNCTION（存储过程/函数）：修改存储过程或函数

创建关联表和复杂查询

::

    -- 20. 创建选课表（学生和课程的关联表）
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        course_id INTEGER,
        score REAL,
        enrollment_date DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );

    -- 21. 插入选课数据
    INSERT INTO enrollments (student_id, course_id, score) VALUES
    (1, 1, 85.5),  -- 张三选数学
    (1, 2, 92.0),  -- 张三选英语
    (2, 1, 78.0),  -- 李四选数学
    (2, 3, 88.5),  -- 李四选计算机科学
    (3, 2, 95.0),  -- 王五选英语
    (3, 3, 82.5);  -- 王五选计算机科学

    -- 22. 查看选课表数据
    SELECT * FROM enrollments;

多表连接查询

::

    -- 23. 内连接：查看每个学生选了哪些课程
    SELECT 
        s.name AS 学生姓名,
        c.name AS 课程名称,
        e.score AS 成绩
    FROM students s
    JOIN enrollments e ON s.id = e.student_id
    JOIN courses c ON e.course_id = c.id;

    -- 24. 左连接：查看所有学生及其选课情况（包括没选课的学生）
    SELECT 
        s.name AS 学生姓名,
        c.name AS 课程名称,
        e.score AS 成绩
    FROM students s
    LEFT JOIN enrollments e ON s.id = e.student_id
    LEFT JOIN courses c ON e.course_id = c.id;

    -- 25. 统计每个学生选了多少门课
    SELECT 
        s.name AS 学生姓名,
        COUNT(e.course_id) AS 选课数量
    FROM students s
    LEFT JOIN enrollments e ON s.id = e.student_id
    GROUP BY s.id, s.name;

    -- 26. 查询每门课程的平均分
    SELECT 
        c.name AS 课程名称,
        ROUND(AVG(e.score), 2) AS 平均分
    FROM courses c
    LEFT JOIN enrollments e ON c.id = e.course_id
    GROUP BY c.id, c.name;

子查询和复杂条件

::

    -- 27. 子查询：查询成绩高于平均分的学生选课记录
    SELECT 
        s.name AS 学生姓名,
        c.name AS 课程名称,
        e.score AS 成绩
    FROM students s
    JOIN enrollments e ON s.id = e.student_id
    JOIN courses c ON e.course_id = c.id
    WHERE e.score > (SELECT AVG(score) FROM enrollments);

    -- 28. 查询选了"计算机科学"课程的学生
    SELECT 
        s.name AS 学生姓名,
        e.score AS 成绩
    FROM students s
    JOIN enrollments e ON s.id = e.student_id
    WHERE e.course_id = (SELECT id FROM courses WHERE name = '计算机科学');

    -- 29. 查询选了超过1门课的学生
    SELECT 
        s.name AS 学生姓名,
        COUNT(e.course_id) AS 选课数量
    FROM students s
    JOIN enrollments e ON s.id = e.student_id
    GROUP BY s.id, s.name
    HAVING COUNT(e.course_id) > 1;

数据删除操作

::

    -- 30. 删除特定记录（谨慎操作！）
    -- 先查询要删除的数据
    SELECT * FROM enrollments WHERE score < 80;

    -- 确认无误后删除
    DELETE FROM enrollments WHERE score < 80;

    -- 验证删除结果
    SELECT * FROM enrollments;

    -- 31. 使用事务确保数据安全（重要！）
    BEGIN TRANSACTION;

    -- 在这里执行一系列操作
    UPDATE students SET age = age + 1 WHERE name = '张三';

    -- 如果一切正常，提交更改
    COMMIT;

    -- 如果出现问题，可以回滚
    -- ROLLBACK;

实用技巧

::

    -- 设置更好的显示格式
    .mode column
    .headers on
    .nullvalue NULL

    -- 查看表结构
    .schema students
    .schema courses
    .schema enrollments

    -- 查看所有数据
    SELECT '学生表' AS 表名; SELECT * FROM students;
    SELECT '课程表' AS 表名; SELECT * FROM courses;
    SELECT '选课表' AS 表名; SELECT * FROM enrollments;
