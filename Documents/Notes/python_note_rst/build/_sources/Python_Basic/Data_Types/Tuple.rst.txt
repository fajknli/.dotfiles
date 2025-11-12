Tuple
######

元组（tuple）是 Python 中不可变的序列类型，与列表相似但具有重要的区别和特性。

元组基础
==========================================

1. 创建元组
------------------------------------------

::

    # 多种创建方式
    empty_tuple = ()
    single_tuple = (42,)  # 注意逗号！没有逗号就是整数42
    numbers = (1, 2, 3, 4, 5)
    mixed = (1, "hello", 3.14, True)
    nested = ((1, 2), (3, 4), [5, 6])  # 可以嵌套其他可变对象

    # 不使用括号（元组打包）
    packed = 1, 2, 3, 4, 5
    print("打包元组:", packed)  # (1, 2, 3, 4, 5)

    # 使用 tuple() 构造函数
    from_list = tuple([1, 2, 3])
    from_string = tuple("Python")
    from_range = tuple(range(5))

    print("从列表创建:", from_list)    # (1, 2, 3)
    print("从字符串创建:", from_string) # ('P', 'y', 't', 'h', 'o', 'n')
    print("从range创建:", from_range)  # (0, 1, 2, 3, 4)

2. 元组的基本特性
------------------------------------------

::

    # 不可变性测试
    t = (1, 2, 3)
    print("原元组:", t)

    # 以下操作都会报错：
    # t[0] = 10        # TypeError
    # t.append(4)      # AttributeError
    # t.remove(2)      # AttributeError

    # 但可以访问元素
    print("第一个元素:", t[0])    # 1
    print("最后一个元素:", t[-1])  # 3
    print("切片:", t[1:])        # (2, 3)

    # 元组长度和成员检查
    print("长度:", len(t))           # 3
    print("包含2:", 2 in t)         # True
    print("不包含5:", 5 not in t)    # True

元组操作和方法
==========================================

1. 元组方法（有限的几个）
------------------------------------------

::

    t = (1, 2, 2, 3, 4, 2)

    # count() - 统计元素出现次数
    print("2的出现次数:", t.count(2))  # 3
    print("5的出现次数:", t.count(5))  # 0

    # index() - 查找元素第一次出现的索引
    print("3的索引:", t.index(3))      # 3
    print("从索引2开始找2:", t.index(2, 2))  # 2

    # 注意：没有 append, extend, insert, remove, pop, sort, reverse 等方法

2. 元组运算
------------------------------------------

::

    # 连接运算
    t1 = (1, 2, 3)
    t2 = (4, 5, 6)
    combined = t1 + t2
    print("连接后:", combined)  # (1, 2, 3, 4, 5, 6)

    # 重复运算
    repeated = t1 * 3
    print("重复3次:", repeated)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

    # 比较运算
    print("(1,2) < (1,3):", (1, 2) < (1, 3))  # True
    print("(1,2) == (1,2):", (1, 2) == (1, 2))  # True
    print("(1,2,3) > (1,2):", (1, 2, 3) > (1, 2))  # True

元组的不可变性深入理解
==========================================

1. 浅不可变 vs 深不可变
------------------------------------------

::

    # 元组本身不可变，但包含的可变对象可以改变
    mixed_tuple = (1, 2, [3, 4])
    print("原元组:", mixed_tuple)  # (1, 2, [3, 4])

    # 可以修改元组中的列表
    mixed_tuple[2].append(5)
    mixed_tuple[2][0] = 30
    print("修改后:", mixed_tuple)  # (1, 2, [30, 4, 5])

    # 但不能替换整个列表
    # mixed_tuple[2] = [6, 7]  # TypeError

    # 真正的不可变元组应该只包含不可变元素
    immutable_tuple = (1, 2, (3, 4))
    print("真正的不可变元组:", immutable_tuple)

2. 不可变性的优势
------------------------------------------

::

    # 1. 作为字典的键
    coordinates = {(1, 2): "点A", (3, 4): "点B"}
    print("坐标字典:", coordinates)  # {(1, 2): '点A', (3, 4): '点B'}

    # 列表不能作为字典键
    # invalid_dict = {[1, 2]: "错误"}  # TypeError

    # 2. 线程安全
    def process_data(data_tuple):
        # 由于元组不可变，多线程环境下是安全的
        return sum(data_tuple)

    # 3. 哈希支持
    print("元组的哈希值:", hash((1, 2, 3)))
    # print("列表的哈希值:", hash([1, 2, 3]))  # TypeError

元组解包（Tuple Unpacking）
------------------------------------------

1. 基本解包
------------------------------------------

::

    # 简单解包
    point = (10, 20)
    x, y = point
    print(f"x: {x}, y: {y}")  # x: 10, y: 20

    # 交换变量（不需要临时变量）
    a, b = 1, 2
    a, b = b, a
    print(f"a: {a}, b: {b}")  # a: 2, b: 1

    # 函数返回多个值
    def get_stats(numbers):
        return min(numbers), max(numbers), sum(numbers) / len(numbers)

    min_val, max_val, avg_val = get_stats([1, 2, 3, 4, 5])
    print(f"最小值: {min_val}, 最大值: {max_val}, 平均值: {avg_val}")

2. 高级解包技巧
------------------------------------------

::

    # 使用 * 操作符解包
    numbers = (1, 2, 3, 4, 5)
    first, *middle, last = numbers
    print(f"第一个: {first}, 中间: {middle}, 最后: {last}")  
    # 第一个: 1, 中间: [2, 3, 4], 最后: 5

    # 嵌套解包
    nested = (1, (2, 3), 4)
    a, (b, c), d = nested
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")  # a: 1, b: 2, c: 3, d: 4

    # 解包在循环中
    points = [(1, 2), (3, 4), (5, 6)]
    for x, y in points:
        print(f"处理点 ({x}, {y})")

    # 解包函数参数
    def connect_to_database(host, port, username, password):
        print(f"连接到 {host}:{port} 用户: {username}")

    db_config = ('localhost', 5432, 'admin', 'secret')
    connect_to_database(*db_config)

元组与函数的配合
==========================================

1. 函数返回多个值
------------------------------------------

::

    def analyze_numbers(data):
        """返回统计信息"""
        if not data:
            return None
        
        count = len(data)
        total = sum(data)
        mean = total / count
        variance = sum((x - mean) ** 2 for x in data) / count
        
        return count, total, mean, variance

    stats = analyze_numbers([1, 2, 3, 4, 5])
    print(f"统计结果: {stats}")
    # 或者解包
    count, total, mean, variance = analyze_numbers([1, 2, 3, 4, 5])
    print(f"数量: {count}, 总和: {total}, 均值: {mean:.2f}, 方差: {variance:.2f}")

2. \\*args 参数
------------------------------------------

::

    def print_details(name, *scores, **kwargs):
        """演示 *args 的使用"""
        print(f"姓名: {name}")
        print(f"分数: {scores} (类型: {type(scores)})")
        
        if kwargs:
            print("其他信息:")
            for key, value in kwargs.items():
                print(f"  {key}: {value}")

    # 调用
    print_details("Alice", 85, 92, 78, age=20, city="Beijing")
    # 姓名: Alice
    # 分数: (85, 92, 78) (类型: <class 'tuple'>)
    # 其他信息:
    #   age: 20
    #   city: Beijing

实际应用场景
==========================================

1. 数据库记录
------------------------------------------

::

    # 模拟数据库查询结果
    def get_user_profile(user_id):
        """模拟从数据库获取用户信息"""
        # 返回不可变的用户信息元组
        return (user_id, "Alice", 25, "alice@example.com", "Engineer")

    user_id, name, age, email, job = get_user_profile(1)
    print(f"用户 {name} (ID: {user_id}), 年龄: {age}, 职业: {job}")

    # 多个用户
    users = [
        (1, "Alice", 25, "Engineer"),
        (2, "Bob", 30, "Designer"),
        (3, "Charlie", 35, "Manager")
    ]

    for user_id, name, age, job in users:
        print(f"{name} - {job}")

2. 坐标和几何计算
------------------------------------------

::

    def calculate_distance(point1, point2):
        """计算两点间距离"""
        x1, y1 = point1
        x2, y2 = point2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def get_rectangle_corners(top_left, width, height):
        """根据左上角坐标计算矩形四个角"""
        x, y = top_left
        return (
            (x, y),                    # 左上
            (x + width, y),            # 右上
            (x + width, y + height),   # 右下
            (x, y + height)            # 左下
        )

    # 使用
    point_a = (0, 0)
    point_b = (3, 4)
    distance = calculate_distance(point_a, point_b)
    print(f"两点距离: {distance}")  # 5.0

    corners = get_rectangle_corners((10, 10), 5, 3)
    print("矩形角点:", corners)

3. 配置信息
------------------------------------------

::

    # 不可变的配置信息
    DATABASE_CONFIG = (
        "localhost",    # host
        5432,           # port
        "myapp_db",     # database
        "admin",        # username
        "password"      # password
    )

    # 颜色配置
    COLORS = (
        ("RED", (255, 0, 0)),
        ("GREEN", (0, 255, 0)),
        ("BLUE", (0, 0, 255))
    )

    def get_color_rgb(color_name):
        """根据颜色名获取RGB值"""
        for name, rgb in COLORS:
            if name == color_name:
                return rgb
        return None

    print("红色RGB:", get_color_rgb("RED"))  # (255, 0, 0)

4. 枚举替代方案
------------------------------------------

::

    # 在没有enum模块时使用元组作为枚举
    STATUS = (
        ("PENDING", "等待中"),
        ("PROCESSING", "处理中"),
        ("COMPLETED", "已完成"),
        ("FAILED", "失败")
    )

    def get_status_display(status_code):
        """获取状态显示文本"""
        for code, display in STATUS:
            if code == status_code:
                return display
        return "未知状态"

    print("处理中:", get_status_display("PROCESSING"))  # 处理中

性能比较
------------------------------------------

1. 创建和访问性能
------------------------------------------

::

    import time
    import sys

    def performance_comparison():
        n = 1000000
        
        # 创建性能
        start = time.time()
        list_data = [i for i in range(n)]
        list_creation = time.time() - start
        
        start = time.time()
        tuple_data = tuple(i for i in range(n))
        tuple_creation = time.time() - start
        
        # 内存使用
        list_memory = sys.getsizeof(list_data)
        tuple_memory = sys.getsizeof(tuple_data)
        
        # 访问性能
        start = time.time()
        for i in range(n):
            _ = list_data[i]
        list_access = time.time() - start
        
        start = time.time()
        for i in range(n):
            _ = tuple_data[i]
        tuple_access = time.time() - start
        
        print(f"创建时间 - 列表: {list_creation:.4f}s, 元组: {tuple_creation:.4f}s")
        print(f"内存使用 - 列表: {list_memory} bytes, 元组: {tuple_memory} bytes")
        print(f"访问时间 - 列表: {list_access:.4f}s, 元组: {tuple_access:.4f}s")

    performance_comparison()

最佳实践
------------------------------------------

1. 何时使用元组
------------------------------------------

::

    # 适合使用元组的场景：

    # 1. 数据记录 - 不可变的属性集合
    person = ("Alice", 25, "Engineer")

    # 2. 函数返回多个值
    def get_coordinates():
        return 10.5, 20.3

    # 3. 字典键
    locations = {
        (40.7128, -74.0060): "New York",
        (51.5074, -0.1278): "London"
    }

    # 4. 保护数据不被修改
    CONSTANTS = (3.14159, 2.71828, 1.41421)

    # 5. 性能敏感的场景
    def process_chunk(data_tuple):
        # 元组的处理通常比列表快
        return sum(data_tuple)

2. 元组与列表的选择指南
------------------------------------------

::

    """
    选择元组的情况：
    - 数据不应该被修改
    - 需要作为字典键使用
    - 需要哈希支持
    - 性能是关键因素
    - 数据是天然不可变的（如坐标、配置）

    选择列表的情况：
    - 数据需要频繁修改
    - 需要动态添加/删除元素
    - 需要使用列表特有的方法
    - 数据顺序可能改变
    """

    # 示例：坐标系统使用元组，待办事项使用列表
    coordinates = [(1, 2), (3, 4), (5, 6)]  # 列表包含元组
    todo_list = ["买菜", "做饭", "打扫"]     # 列表，内容会变化

总结
==========================================

元组是 Python 中重要的不可变序列：

不可变性：数据安全、线程安全、可哈希

性能优势：创建和访问通常比列表快

解包特性：方便的多变量赋值和函数返回

适用场景：配置数据、坐标、字典键、函数多返回值

理解元组的特性和适用场景，能够帮助你在合适的场合选择最合适的数据结构，写出更高效、更安全的代码
