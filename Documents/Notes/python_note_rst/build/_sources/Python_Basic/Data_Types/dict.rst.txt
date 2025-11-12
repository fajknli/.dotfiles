Dict
############

字典（dict）是 Python 中最重要的数据结构之一，用于存储键值对映射关系。

字典基础
============================================

1. 创建字典
--------------------------------------------

::

    # 多种创建方式
    empty_dict = {}
    person1 = {"name": "Alice", "age": 22, "city": "Changsha"}
    person2 = dict(name="Bob", age=23, city="Luki")
    person3 = dict([("name", "Haili"), ("age", 24)])

    print("person1:", person1)
    print("person2:", person2)
    print("person3:", person3)

    # 使用字典推导式
    squares = {x: x**2 for x in range(5)}
    print("平方字典:", squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

    # 使用 fromkeys() 创建默认字典
    default_dict = dict.fromkeys(['name', 'age', 'city'], 'unknown')
    print("默认字典:", default_dict)  # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

2. 访问和修改
--------------------------------------------

::

    user = {"name": "Tom", "age": 25, "city": "Beijing"}

    # 访问元素
    print("姓名:", user["name"])  # Tom
    print("年龄:", user.get("age"))  # 25

    # 修改元素
    user["age"] = 26
    user["city"] = "Shanghai"
    print("修改后:", user)

    # 添加新元素
    user["email"] = "tom@example.com"
    print("添加后:", user)

    # 安全访问（避免 KeyError）
    print("身高:", user.get("height"))  # None
    print("身高:", user.get("height", "180cm"))  # 180cm

    # 使用 setdefault() - 如果键不存在则设置默认值
    user.setdefault("country", "China")
    user.setdefault("name", "Unknown")  # 已存在，不会修改
    print("setdefault后:", user)

字典方法详解
============================================

1. 键、值、键值对操作
--------------------------------------------

::

    student = {"name": "Alice", "age": 20, "major": "CS", "grade": "A"}

    # 获取所有键
    print("所有键:", list(student.keys()))  # ['name', 'age', 'major', 'grade']

    # 获取所有值
    print("所有值:", list(student.values()))  # ['Alice', 20, 'CS', 'A']

    # 获取所有键值对
    print("所有键值对:", list(student.items()))  # [('name', 'Alice'), ('age', 20), ...]

    # 遍历字典
    print("遍历键:")
    for key in student:
        print(f"  {key}: {student[key]}")

    print("遍历键值对:")
    for key, value in student.items():
        print(f"  {key}: {value}")

    # 检查键是否存在
    print("是否有age键:", "age" in student)  # True
    print("是否有height键:", "height" in student)  # False

2. 删除操作
--------------------------------------------

::

    user = {"name": "Tom", "age": 25, "city": "Beijing", "email": "tom@test.com"}

    # del 语句删除
    del user["email"]
    print("del删除后:", user)

    # pop() - 删除并返回值
    age = user.pop("age")
    print(f"pop返回: {age}, 剩余字典: {user}")

    # pop() 带默认值
    height = user.pop("height", "180cm")
    print(f"pop不存在的键: {height}")

    # popitem() - 删除并返回最后一个键值对（LIFO）
    last_item = user.popitem()
    print(f"popitem返回: {last_item}, 剩余字典: {user}")

    # clear() - 清空字典
    user.clear()
    print("clear后:", user)  # {}

3. 更新和合并
--------------------------------------------

::

    # update() - 合并字典
    base_info = {"name": "Alice", "age": 25}
    additional_info = {"city": "Beijing", "job": "Engineer"}

    base_info.update(additional_info)
    print("update后:", base_info)

    # 合并多个字典
    extra_info = {"hobby": "reading", "language": "Python"}
    base_info.update(extra_info)
    print("再次update后:", base_info)

    # 使用 | 运算符合并（Python 3.9+）
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    merged = dict1 | dict2  # 后者覆盖前者
    print("合并结果:", merged)  # {'a': 1, 'b': 3, 'c': 4}

字典推导式
--------------------------------------------

::

    # 基本推导式
    numbers = [1, 2, 3, 4, 5]
    squared_dict = {x: x**2 for x in numbers}
    print("平方字典:", squared_dict)

    # 带条件的推导式
    even_squares = {x: x**2 for x in numbers if x % 2 == 0}
    print("偶数的平方:", even_squares)

    # 处理字符串
    words = ["apple", "banana", "cherry"]
    word_lengths = {word: len(word) for word in words}
    print("单词长度:", word_lengths)

    # 键值转换
    original = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in original.items()}
    print("键值交换:", swapped)

    # 复杂推导式
    text = "hello world"
    char_count = {char: text.count(char) for char in set(text) if char != ' '}
    print("字符统计:", char_count)

嵌套字典
============================================

1. 多层嵌套
--------------------------------------------

::

    # 嵌套字典
    company = {
        "employee1": {
            "name": "Alice",
            "age": 30,
            "department": "Engineering",
            "skills": ["Python", "Java", "SQL"]
        },
        "employee2": {
            "name": "Bob", 
            "age": 25,
            "department": "Marketing",
            "skills": ["SEO", "Content Writing", "Analytics"]
        }
    }

    # 访问嵌套字典
    print("Alice的部门:", company["employee1"]["department"])
    print("Bob的技能:", company["employee2"]["skills"][0])

    # 修改嵌套字典
    company["employee1"]["age"] = 31
    company["employee2"]["skills"].append("Social Media")

    # 遍历嵌套字典
    print("\n公司员工信息:")
    for emp_id, emp_info in company.items():
        print(f"\n员工 {emp_id}:")
        for key, value in emp_info.items():
            print(f"  {key}: {value}")

2. 复杂数据结构
--------------------------------------------

::

    # 学校数据结构
    school = {
        "classes": {
            "class1": {
                "teacher": "Mr. Smith",
                "students": {
                    "stu1": {"name": "Alice", "grade": 85},
                    "stu2": {"name": "Bob", "grade": 92}
                }
            },
            "class2": {
                "teacher": "Ms. Johnson", 
                "students": {
                    "stu3": {"name": "Charlie", "grade": 78},
                    "stu4": {"name": "Diana", "grade": 88}
                }
            }
        }
    }

    # 访问深层数据
    class1_teacher = school["classes"]["class1"]["teacher"]
    alice_grade = school["classes"]["class1"]["students"]["stu1"]["grade"]
    print(f"Class1老师: {class1_teacher}, Alice成绩: {alice_grade}")

    # 添加新数据
    school["classes"]["class1"]["students"]["stu5"] = {"name": "Eve", "grade": 95}

实际应用场景
============================================

1. 配置管理系统
--------------------------------------------

::

    class ConfigManager:
        def __init__(self):
            self.config = {
                "database": {
                    "host": "localhost",
                    "port": 5432,
                    "name": "myapp",
                    "user": "admin"
                },
                "server": {
                    "host": "0.0.0.0",
                    "port": 8000,
                    "debug": True
                },
                "logging": {
                    "level": "INFO",
                    "file": "app.log"
                }
            }
        
        def get(self, path, default=None):
            """通过路径获取配置，如 'database.host'"""
            keys = path.split('.')
            current = self.config
            
            for key in keys:
                if isinstance(current, dict) and key in current:
                    current = current[key]
                else:
                    return default
            return current
        
        def set(self, path, value):
            """通过路径设置配置"""
            keys = path.split('.')
            current = self.config
            
            for key in keys[:-1]:
                if key not in current:
                    current[key] = {}
                current = current[key]
            
            current[keys[-1]] = value
        
        def show_all(self):
            """显示所有配置"""
            import json
            print(json.dumps(self.config, indent=2))

    # 使用示例
    config = ConfigManager()
    print("数据库主机:", config.get("database.host"))
    config.set("server.port", 8080)
    config.set("database.password", "secret")
    config.show_all()

2. 缓存系统
--------------------------------------------

::

    import time

    class SimpleCache:
        def __init__(self, max_size=100, ttl=3600):
            self.cache = {}
            self.max_size = max_size
            self.ttl = ttl  # 生存时间（秒）
        
        def get(self, key):
            """获取缓存值"""
            if key in self.cache:
                value, timestamp = self.cache[key]
                # 检查是否过期
                if time.time() - timestamp < self.ttl:
                    return value
                else:
                    # 过期删除
                    del self.cache[key]
            return None
        
        def set(self, key, value):
            """设置缓存值"""
            # 如果达到最大大小，删除最旧的一个
            if len(self.cache) >= self.max_size:
                oldest_key = next(iter(self.cache))
                del self.cache[oldest_key]
            
            self.cache[key] = (value, time.time())
        
        def clear_expired(self):
            """清理过期缓存"""
            current_time = time.time()
            expired_keys = [
                key for key, (_, timestamp) in self.cache.items()
                if current_time - timestamp >= self.ttl
            ]
            for key in expired_keys:
                del self.cache[key]
        
        def stats(self):
            """缓存统计"""
            return {
                "size": len(self.cache),
                "max_size": self.max_size,
                "usage": f"{len(self.cache) / self.max_size * 100:.1f}%"
            }

    # 使用示例
    cache = SimpleCache(max_size=5, ttl=10)

    # 模拟缓存数据
    for i in range(7):
        cache.set(f"key_{i}", f"value_{i}")

    print("缓存内容:", cache.cache)
    print("获取key_1:", cache.get("key_1"))
    print("缓存统计:", cache.stats())

    # 等待过期
    time.sleep(11)
    cache.clear_expired()
    print("过期清理后:", cache.cache)

3. 词频统计
--------------------------------------------

::

    def word_frequency_analysis(text):
        """文本词频分析"""
        # 清理文本并分割单词
        words = text.lower().replace(',', '').replace('.', '').split()
        
        # 统计词频
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        
        return frequency

    def get_top_words(frequency, n=10):
        """获取前n个最常用单词"""
        sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_words[:n])

    # 使用示例
    text = """
    Python is an interpreted high-level general-purpose programming language. 
    Python's design philosophy emphasizes code readability with its notable use of significant indentation.
    Python is dynamically-typed and garbage-collected.
    """

    freq = word_frequency_analysis(text)
    top_words = get_top_words(freq, 5)

    print("词频统计:")
    for word, count in freq.items():
        print(f"  {word}: {count}")

    print("\n前5个最常用单词:")
    for word, count in top_words.items():
        print(f"  {word}: {count}")

4. 数据转换和映射
--------------------------------------------

::

    class DataTransformer:
        def __init__(self):
            self.category_map = {
                "tech": ["python", "java", "javascript", "programming"],
                "science": ["physics", "chemistry", "biology", "math"],
                "arts": ["music", "painting", "literature", "dance"]
            }
            
            self.status_codes = {
                200: "OK",
                404: "Not Found", 
                500: "Internal Server Error",
                301: "Moved Permanently"
            }
        
        def categorize_content(self, keywords):
            """根据关键词分类内容"""
            categories = set()
            
            for keyword in keywords:
                for category, terms in self.category_map.items():
                    if keyword.lower() in terms:
                        categories.add(category)
            
            return list(categories) if categories else ["uncategorized"]
        
        def get_status_message(self, code):
            """获取状态码对应的消息"""
            return self.status_codes.get(code, "Unknown Status")
        
        def transform_user_data(self, raw_data):
            """转换用户数据格式"""
            field_mapping = {
                "user_name": "username",
                "user_age": "age", 
                "user_email": "email",
                "user_city": "city"
            }
            
            transformed = {}
            for old_field, new_field in field_mapping.items():
                if old_field in raw_data:
                    transformed[new_field] = raw_data[old_field]
            
            return transformed

    # 使用示例
    transformer = DataTransformer()

    # 分类测试
    keywords = ["python", "music", "physics"]
    categories = transformer.categorize_content(keywords)
    print("内容分类:", categories)

    # 状态码测试
    print("状态码200:", transformer.get_status_message(200))
    print("状态码999:", transformer.get_status_message(999))

    # 数据转换测试
    raw_user = {"user_name": "alice", "user_age": 25, "user_city": "Beijing"}
    clean_user = transformer.transform_user_data(raw_user)
    print("转换后的用户数据:", clean_user)

高级特性
============================================

1. defaultdict
--------------------------------------------

::

    from collections import defaultdict

    # 自动处理缺失键的字典
    word_count = defaultdict(int)  # 默认值为0
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

    for word in words:
        word_count[word] += 1

    print("单词计数:", dict(word_count))

    # 列表作为默认值
    student_grades = defaultdict(list)
    grades_data = [("Alice", 85), ("Bob", 92), ("Alice", 90), ("Charlie", 78)]

    for student, grade in grades_data:
        student_grades[student].append(grade)

    print("学生成绩:", dict(student_grades))

    # 自定义默认值
    def default_score():
        return {"math": 0, "english": 0, "science": 0}

    scores = defaultdict(default_score)
    scores["Alice"]["math"] = 95
    scores["Bob"]["english"] = 88

    print("科目分数:", dict(scores))

2. OrderedDict
--------------------------------------------

::

    from collections import OrderedDict

    # 保持插入顺序的字典
    ordered = OrderedDict()
    ordered["first"] = 1
    ordered["second"] = 2
    ordered["third"] = 3

    print("有序字典:", ordered)

    # 移动元素到末尾
    ordered.move_to_end("first")
    print("移动后:", ordered)

    # 弹出第一个元素
    first = ordered.popitem(last=False)
    print(f"弹出第一个: {first}, 剩余: {ordered}")
    3. ChainMap
    ::

    from collections import ChainMap

    # 合并多个字典的视图
    defaults = {"theme": "light", "language": "en", "font_size": 14}
    user_prefs = {"theme": "dark", "font_size": 16}
    system_settings = {"language": "zh", "timezone": "UTC+8"}

    # 创建链式映射（优先级从高到低）
    settings = ChainMap(user_prefs, system_settings, defaults)

    print("当前设置:")
    for key, value in settings.items():
        print(f"  {key}: {value}")

    # 修改会影响第一个字典
    settings["theme"] = "blue"
    print("修改后user_prefs:", user_prefs)

性能优化
============================================

1. 字典视图的高效使用
--------------------------------------------

::

    def efficient_dict_operations():
        large_dict = {f"key_{i}": f"value_{i}" for i in range(10000)}
        
        # 高效的键检查
        if "key_9999" in large_dict:  # O(1)
            print("键存在")
        
        # 使用字典视图进行集合运算
        dict1 = {"a": 1, "b": 2, "c": 3}
        dict2 = {"b": 2, "c": 4, "d": 5}
        
        common_keys = dict1.keys() & dict2.keys()  # 交集
        unique_to_dict1 = dict1.keys() - dict2.keys()  # 差集
        
        print("共同键:", common_keys)
        print("dict1独有键:", unique_to_dict1)

    efficient_dict_operations()

2. 内存优化
--------------------------------------------

::

    import sys

    def memory_usage_comparison():
        # 列表 vs 字典的内存使用
        n = 1000
        
        # 列表存储键值对
        list_pairs = [(f"key_{i}", f"value_{i}") for i in range(n)]
        
        # 字典存储
        dict_data = {f"key_{i}": f"value_{i}" for i in range(n)}
        
        print(f"列表内存: {sys.getsizeof(list_pairs)} bytes")
        print(f"字典内存: {sys.getsizeof(dict_data)} bytes")
        
        # 对于大量数据，考虑使用其他结构
        from array import array
        arr = array('i', range(n))  # 更紧凑的存储
        print(f"数组内存: {sys.getsizeof(arr)} bytes")

    memory_usage_comparison()

最佳实践
============================================

1. 字典使用指南
--------------------------------------------

::

    """
    字典最佳实践：

    1. 键的选择：
       - 使用不可变类型（字符串、数字、元组）
       - 避免使用可变类型（列表、字典）
       - 键应该具有唯一性

    2. 访问安全：
       - 使用 get() 方法避免 KeyError
       - 使用 setdefault() 设置默认值
       - 使用 in 检查键是否存在

    3. 性能考虑：
       - 字典查找是 O(1) 的
       - 对于大量数据，字典比列表查找更快
       - 使用字典视图进行集合运算

    4. 内存使用：
       - 字典比列表占用更多内存
       - 对于大量简单数据，考虑使用数组或其他结构
    """

    # 好的字典使用示例
    def good_practices():
        # 使用有意义的键名
        user_profile = {
            "username": "alice",
            "email": "alice@example.com",
            "preferences": {
                "theme": "dark",
                "language": "en"
            }
        }
        
        # 安全访问
        age = user_profile.get("age", 0)  # 提供默认值
        
        # 使用字典推导式
        config = {key: value.upper() for key, value in user_profile.items() 
                  if isinstance(value, str)}
        
        return config

2. 常见陷阱和解决方案
--------------------------------------------

::

    def common_pitfalls():
        # 陷阱1：可变对象作为键
        try:
            # bad_dict = {[1, 2]: "value"}  # TypeError
            pass
        except TypeError as e:
            print("陷阱1 - 可变键:", e)
        
        # 解决方案：使用元组
        good_dict = {(1, 2): "value"}  # OK
        
        # 陷阱2：在迭代时修改字典
        data = {"a": 1, "b": 2, "c": 3}
        try:
            # for key in data:
            #     if key == "b":
            #         del data[key]  # RuntimeError
            pass
        except RuntimeError as e:
            print("陷阱2 - 迭代时修改:", e)
        
        # 解决方案：创建副本或收集要删除的键
        keys_to_delete = [key for key in data if key == "b"]
        for key in keys_to_delete:
            del data[key]
        
        # 陷阱3：浅拷贝问题
        original = {"list": [1, 2, 3]}
        shallow_copy = original.copy()
        shallow_copy["list"].append(4)
        print("陷阱3 - 浅拷贝:", original["list"])  # [1, 2, 3, 4]
        
        # 解决方案：深拷贝
        import copy
        deep_copy = copy.deepcopy(original)
        deep_copy["list"].append(5)
        print("深拷贝解决方案:", original["list"])  # [1, 2, 3, 4]

    common_pitfalls()

总结
============================================

字典是 Python 中最强大的数据结构之一：

键值映射：高效的键值对存储和检索

灵活可变：动态添加、删除、修改元素

丰富方法：提供多种操作和转换方法

高性能：O(1) 的平均时间复杂度

广泛应用：配置管理、缓存、数据转换、统计等

掌握字典的特性和最佳实践，能够帮助你构建更高效、更健壮的 Python 应用程序！
