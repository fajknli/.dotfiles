Set
#############################################

集合（set）是 Python 中无序、不重复元素的数据结构，提供了丰富的数学集合运算。

集合基础
=============================================

1. 创建集合
---------------------------------------------

::

    # 多种创建方式
    empty_set = set()  # 注意：不能使用 {} 创建空集合，{} 创建的是空字典
    numbers = {1, 2, 3, 4, 4, 4}  # 自动去重
    mixed = {1, "hello", 3.14, True}

    # 使用 set() 构造函数
    from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
    from_string = set("hello")           # {'h', 'e', 'l', 'o'}
    from_tuple = set((1, 2, 3, 2, 1))    # {1, 2, 3}
    from_range = set(range(5))           # {0, 1, 2, 3, 4}

    print("各种集合:", numbers, mixed, from_list, from_string)

2. 集合的基本特性
---------------------------------------------

::

    # 无序性
    s = {3, 1, 4, 1, 5, 9, 2}
    print("集合:", s)  # 每次输出的顺序可能不同

    # 唯一性（自动去重）
    duplicates = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4}
    print("去重后:", duplicates)  # {1, 2, 3, 4}

    # 可变性（可以添加删除元素）
    s.add(6)
    s.remove(1)
    print("修改后:", s)

    # 成员检查（非常高效 - O(1)）
    print("4在集合中:", 4 in s)  # True
    print("7在集合中:", 7 in s)  # False

    # 长度
    print("集合大小:", len(s))

集合运算
=============================================

1. 基本集合运算
---------------------------------------------

::

    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    print("集合A:", A)
    print("集合B:", B)

    # 并集
    print("A | B:", A | B)        # {1, 2, 3, 4, 5, 6, 7, 8}
    print("A.union(B):", A.union(B))

    # 交集
    print("A & B:", A & B)        # {4, 5}
    print("A.intersection(B):", A.intersection(B))

    # 差集
    print("A - B:", A - B)        # {1, 2, 3}
    print("A.difference(B):", A.difference(B))

    # 对称差集
    print("A ^ B:", A ^ B)        # {1, 2, 3, 6, 7, 8}
    print("A.symmetric_difference(B):", A.symmetric_difference(B))

2. 集合关系判断
---------------------------------------------

::

    X = {1, 2, 3}
    Y = {1, 2, 3, 4, 5}
    Z = {4, 5, 6}

    print("集合X:", X)
    print("集合Y:", Y)
    print("集合Z:", Z)

    # 子集检查
    print("X ⊆ Y:", X.issubset(Y))     # True
    print("X <= Y:", X <= Y)           # True
    print("X < Y:", X < Y)             # True (真子集)

    # 超集检查
    print("Y ⊇ X:", Y.issuperset(X))   # True
    print("Y >= X:", Y >= X)           # True
    print("Y > X:", Y > X)             # True

    # 不相交检查
    print("X 和 Z 不相交:", X.isdisjoint(Z))  # True
    print("Y 和 Z 不相交:", Y.isdisjoint(Z))  # False

集合方法详解
=============================================

1. 添加和删除元素
---------------------------------------------

::

    s = {1, 2, 3}

    # 添加元素
    s.add(4)
    print("add(4)后:", s)  # {1, 2, 3, 4}

    s.add(2)  # 添加已存在的元素，无变化
    print("重复add(2):", s)

    # 添加多个元素
    s.update([5, 6, 7])
    print("update后:", s)  # {1, 2, 3, 4, 5, 6, 7}

    s.update({8, 9}, (10, 11))
    print("多次update后:", s)

    # 删除元素
    s.remove(3)  # 删除存在的元素
    print("remove(3)后:", s)

    # s.remove(99)  # 删除不存在的元素会报错 KeyError

    s.discard(4)  # 删除元素，如果不存在也不报错
    s.discard(99)  # 安全删除
    print("discard后:", s)

    # 随机删除并返回一个元素
    popped = s.pop()
    print(f"pop()返回: {popped}, 剩余集合: {s}")

    # 清空集合
    s.clear()
    print("clear后:", s)  # set()

2. 集合运算方法
---------------------------------------------

::

    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    # 原地修改的方法
    A_copy = A.copy()

    # 交集更新
    A_copy.intersection_update(B)
    print("A ∩= B:", A_copy)  # {3, 4}

    A_copy = A.copy()
    # 差集更新
    A_copy.difference_update(B)
    print("A -= B:", A_copy)  # {1, 2}

    A_copy = A.copy()
    # 对称差集更新
    A_copy.symmetric_difference_update(B)
    print("A ^= B:", A_copy)  # {1, 2, 5, 6}

    A_copy = A.copy()
    # 并集更新
    A_copy.update(B)
    print("A |= B:", A_copy)  # {1, 2, 3, 4, 5, 6}

不可变集合 frozenset
---------------------------------------------

::

    # 创建不可变集合
    fs = frozenset([1, 2, 3, 3, 2, 1])
    print("frozenset:", fs)  # frozenset({1, 2, 3})

    # 支持集合运算，但不能修改
    fs2 = frozenset([3, 4, 5])
    print("并集:", fs | fs2)    # frozenset({1, 2, 3, 4, 5})
    print("交集:", fs & fs2)    # frozenset({3})

    # 以下操作会报错：
    # fs.add(4)      # AttributeError
    # fs.remove(1)   # AttributeError

    # 作为字典的键
    dict_with_frozenset = {
        frozenset([1, 2]): "集合A",
        frozenset([3, 4]): "集合B"
    }
    print("frozenset字典:", dict_with_frozenset)

实际应用场景
=============================================

1. 数据去重
---------------------------------------------

::

    def remove_duplicates(data):
        """快速去重"""
        return list(set(data))

    def remove_duplicates_preserve_order(data):
        """去重并保持顺序"""
        seen = set()
        result = []
        for item in data:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    # 测试
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    words = ["apple", "banana", "apple", "cherry", "banana"]

    print("简单去重:", remove_duplicates(numbers))
    print("保持顺序去重:", remove_duplicates_preserve_order(words))

2. 关系数据库操作模拟
---------------------------------------------

::

    class SimpleDatabase:
        def __init__(self):
            self.tables = {}
        
        def create_table(self, table_name, columns):
            self.tables[table_name] = {col: set() for col in columns}
        
        def insert(self, table_name, **data):
            for column, value in data.items():
                if column in self.tables[table_name]:
                    self.tables[table_name][column].add(value)
        
        def select_unique(self, table_name, column):
            return self.tables[table_name].get(column, set())
        
        def inner_join(self, table1, col1, table2, col2):
            """模拟内连接"""
            return self.tables[table1][col1] & self.tables[table2][col2]

    # 使用示例
    db = SimpleDatabase()
    db.create_table("users", ["name", "city"])
    db.create_table("products", ["name", "category"])

    db.insert("users", name="Alice", city="Beijing")
    db.insert("users", name="Bob", city="Shanghai")
    db.insert("users", name="Charlie", city="Beijing")

    db.insert("products", name="Laptop", category="Electronics")
    db.insert("products", name="Book", category="Education")

    print("所有城市:", db.select_unique("users", "city"))
    print("所有分类:", db.select_unique("products", "category"))

3. 权限管理系统
---------------------------------------------

::

    class PermissionSystem:
        def __init__(self):
            self.user_roles = {}  # 用户 -> 角色集合
            self.role_permissions = {}  # 角色 -> 权限集合
        
        def add_role(self, role, permissions):
            self.role_permissions[role] = set(permissions)
        
        def assign_role(self, user, role):
            if user not in self.user_roles:
                self.user_roles[user] = set()
            self.user_roles[user].add(role)
        
        def check_permission(self, user, permission):
            if user not in self.user_roles:
                return False
            
            user_permissions = set()
            for role in self.user_roles[user]:
                user_permissions.update(self.role_permissions.get(role, set()))
            
            return permission in user_permissions
        
        def get_user_permissions(self, user):
            if user not in self.user_roles:
                return set()
            
            permissions = set()
            for role in self.user_roles[user]:
                permissions.update(self.role_permissions.get(role, set()))
            return permissions

    # 使用示例
    perms = PermissionSystem()

    # 定义角色和权限
    perms.add_role("admin", ["read", "write", "delete", "manage_users"])
    perms.add_role("editor", ["read", "write"])
    perms.add_role("viewer", ["read"])

    # 分配角色
    perms.assign_role("alice", "admin")
    perms.assign_role("bob", "editor")
    perms.assign_role("charlie", "viewer")

    # 检查权限
    print("Alice可以删除:", perms.check_permission("alice", "delete"))  # True
    print("Bob可以删除:", perms.check_permission("bob", "delete"))      # False
    print("Charlie的权限:", perms.get_user_permissions("charlie"))      # {'read'}

4. 共同好友/兴趣发现
---------------------------------------------

::

    def find_common_interests(user_interests):
        """找出用户间的共同兴趣"""
        common_pairs = {}
        users = list(user_interests.keys())
        
        for i in range(len(users)):
            for j in range(i + 1, len(users)):
                user1, user2 = users[i], users[j]
                common = user_interests[user1] & user_interests[user2]
                if common:
                    common_pairs[(user1, user2)] = common
        
        return common_pairs

    def recommend_friends(user, user_interests, min_common=2):
        """基于共同兴趣推荐好友"""
        recommendations = []
        user_interest = user_interests[user]
        
        for other_user, interests in user_interests.items():
            if other_user != user:
                common = user_interest & interests
                if len(common) >= min_common:
                    recommendations.append((other_user, common))
        
        # 按共同兴趣数量排序
        recommendations.sort(key=lambda x: len(x[1]), reverse=True)
        return recommendations

    # 使用示例
    user_interests = {
        "Alice": {"python", "music", "travel", "reading"},
        "Bob": {"python", "gaming", "music", "sports"},
        "Charlie": {"travel", "photography", "reading"},
        "Diana": {"python", "data science", "machine learning"}
    }

    print("共同兴趣:")
    common = find_common_interests(user_interests)
    for pair, interests in common.items():
        print(f"{pair[0]} 和 {pair[1]} 的共同兴趣: {interests}")

    print("\n给Alice推荐好友:")
    recs = recommend_friends("Alice", user_interests)
    for user, common_interests in recs:
        print(f"{user}: 共同兴趣 {len(common_interests)} 个 - {common_interests}")

5. 数据验证和过滤
---------------------------------------------

::

    class DataValidator:
        def __init__(self):
            self.valid_countries = {"US", "UK", "CA", "AU", "DE", "FR", "JP"}
            self.valid_categories = {"electronics", "clothing", "books", "home", "sports"}
            self.blocked_words = {"spam", "fraud", "fake", "scam"}
        
        def validate_product(self, product_data):
            """验证产品数据"""
            errors = set()
            
            # 检查国家
            if product_data.get('country') not in self.valid_countries:
                errors.add("invalid_country")
            
            # 检查分类
            if product_data.get('category') not in self.valid_categories:
                errors.add("invalid_category")
            
            # 检查标题中的屏蔽词
            title = product_data.get('title', '').lower()
            found_blocked = self.blocked_words & set(title.split())
            if found_blocked:
                errors.add(f"contains_blocked_words: {found_blocked}")
            
            return errors
        
        def add_valid_country(self, country):
            self.valid_countries.add(country)
        
        def add_blocked_word(self, word):
            self.blocked_words.add(word.lower())

    # 使用示例
    validator = DataValidator()

    products = [
        {"title": "Genuine Laptop", "country": "US", "category": "electronics"},
        {"title": "Fake Rolex Watch", "country": "CN", "category": "clothing"},
        {"title": "Spam Email Software", "country": "US", "category": "invalid"}
    ]

    for i, product in enumerate(products):
        errors = validator.validate_product(product)
        if errors:
            print(f"产品 {i+1} 错误: {errors}")
        else:
            print(f"产品 {i+1} 验证通过")

集合推导式
=============================================

::

    # 基本集合推导式
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    even_squares = {x**2 for x in numbers if x % 2 == 0}
    print("偶数的平方:", even_squares)  # {16, 4, 36, 64, 100}

    # 字符串处理
    words = {"apple", "banana", "cherry", "date", "elderberry"}
    long_words = {word.upper() for word in words if len(word) > 5}
    print("长单词大写:", long_words)  # {'BANANA', 'CHERRY', 'ELDERBERRY'}

    # 复杂推导式
    sentence = "the quick brown fox jumps over the lazy dog"
    unique_vowels = {char for char in sentence if char in 'aeiou'}
    print("句子中的元音:", unique_vowels)  # {'e', 'u', 'i', 'o', 'a'}

性能特点
---------------------------------------------

::

    import time

    def performance_test():
        n = 10000
        
        # 列表和集合的成员检查性能对比
        list_data = list(range(n))
        set_data = set(range(n))
        
        # 测试在列表中的成员检查
        start = time.time()
        for i in range(n):
            _ = i in list_data
        list_time = time.time() - start
        
        # 测试在集合中的成员检查
        start = time.time()
        for i in range(n):
            _ = i in set_data
        set_time = time.time() - start
        
        print(f"列表成员检查: {list_time:.4f}s")
        print(f"集合成员检查: {set_time:.4f}s")
        print(f"集合比列表快 {list_time/set_time:.1f} 倍")

    performance_test()

最佳实践
=============================================

1. 何时使用集合
---------------------------------------------

::

    """
    使用集合的场景：
    - 需要快速成员检查
    - 需要去除重复元素
    - 需要数学集合运算（并集、交集等）
    - 数据顺序不重要
    - 元素需要是哈希化的

    不使用集合的场景：
    - 需要保持元素顺序
    - 需要重复元素
    - 元素是不可哈希的（如列表、字典）
    - 需要索引访问
    """

    # 示例选择
    def choose_data_structure():
        # 用户ID集合 - 快速检查用户是否存在
        user_ids = {123, 456, 789}
        
        # 标签系统 - 集合运算找到共同标签
        user_tags = {"python", "programming", "tech"}
        post_tags = {"python", "tutorial"}
        common_tags = user_tags & post_tags
        
        # 访问记录 - 列表保持顺序
        access_log = ["user1", "user2", "user1", "user3"]
        
        return user_ids, common_tags, access_log

2. 集合使用技巧
---------------------------------------------

::

    # 1. 使用集合推导式创建集合
    unique_chars = {char for char in "hello world" if char != ' '}

    # 2. 使用集合进行快速去重
    def get_unique_elements(sequence):
        return set(sequence)

    # 3. 使用集合运算简化逻辑
    def has_common_elements(list1, list2):
        return bool(set(list1) & set(list2))

    # 4. 使用frozenset作为字典键
    graph_edges = {
        frozenset(['A', 'B']): 5,
        frozenset(['B', 'C']): 3,
        frozenset(['A', 'C']): 7
    }

    # 5. 使用集合进行数据验证
    def validate_data(data, allowed_values):
        return set(data).issubset(allowed_values)

总结
=============================================

集合是 Python 中强大的数据结构：

无序唯一：自动去重，顺序不重要

高效操作：O(1) 的成员检查

数学运算：丰富的集合运算方法

实际应用：去重、关系运算、权限管理、推荐系统等

性能优势：在成员检查和大数据去重时表现优异

掌握集合的特性和应用场景，能够帮助你写出更高效、更简洁的 Python 代码！
