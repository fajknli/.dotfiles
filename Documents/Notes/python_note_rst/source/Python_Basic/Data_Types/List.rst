List
#####

列表是 Python 中最重要、最常用的数据结构之一。让我们系统地学习列表的各种操作和应用。

列表基础操作
=====================================================

1. 创建列表
-----------------------------------------------------

::

    # 多种创建方式
    empty_list = []
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, "hello", 3.14, True]
    nested = [[1, 2], [3, 4], [5, 6]]

    # 使用 list() 构造函数
    from_string = list("Python")  # ['P', 'y', 't', 'h', 'o', 'n']
    from_range = list(range(5))   # [0, 1, 2, 3, 4]
    from_tuple = list((1, 2, 3))  # [1, 2, 3]

    print("各种列表:", numbers, mixed, nested)

2. 列表推导式
-----------------------------------------------------

::

    # 基本推导式
    squares = [x**2 for x in range(10)]
    print("平方数:", squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # 带条件的推导式
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    print("偶数的平方:", even_squares)  # [0, 4, 16, 36, 64]

    # 嵌套推导式
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print("扁平化矩阵:", flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

列表方法详解
=====================================================

1. 添加元素
-----------------------------------------------------

::

    # append() - 末尾添加单个元素
    fruits = ['apple', 'banana']
    fruits.append('orange')
    print("append后:", fruits)  # ['apple', 'banana', 'orange']

    # extend() - 合并另一个可迭代对象
    fruits.extend(['grape', 'mango'])
    print("extend后:", fruits)  # ['apple', 'banana', 'orange', 'grape', 'mango']

    # insert() - 指定位置插入
    fruits.insert(1, 'pear')
    print("insert后:", fruits)  # ['apple', 'pear', 'banana', 'orange', 'grape', 'mango']

2. 删除元素
-----------------------------------------------------

::

    print("remove():")
    # remove() - 删除第一个匹配的元素
    fruits = ['apple', 'banana', 'orange', 'banana']
    fruits.remove('banana')
    print("remove后:", fruits)  # ['apple', 'orange', 'banana']

    # pop() - 删除并返回指定位置的元素
    last_fruit = fruits.pop()
    print(f"pop()返回: {last_fruit}, 列表: {fruits}")  # banana, ['apple', 'orange']

    second_fruit = fruits.pop(1)
    print(f"pop(1)返回: {second_fruit}, 列表: {fruits}")  # orange, ['apple']

    # clear() - 清空列表
    fruits.clear()
    print("clear后:", fruits)  # []

    # del 语句 - 删除指定位置或切片
    numbers = [0, 1, 2, 3, 4, 5]
    del numbers[2]  # 删除索引2的元素
    print("del后:", numbers)  # [0, 1, 3, 4, 5]

    del numbers[1:3]  # 删除切片
    print("del切片后:", numbers)  # [0, 4, 5]

3. 查找和统计
-----------------------------------------------------

::

    numbers = [1, 2, 3, 2, 4, 2, 5]

    # index() - 返回元素第一次出现的索引
    print("3的索引:", numbers.index(3))  # 2
    print("2的索引:", numbers.index(2))  # 1

    # 指定范围查找
    print("从索引2开始找2:", numbers.index(2, 2))  # 3

    # count() - 统计元素出现次数
    print("2的出现次数:", numbers.count(2))  # 3
    print("6的出现次数:", numbers.count(6))  # 0

    # in 运算符 - 检查元素是否存在
    print("4在列表中:", 4 in numbers)  # True
    print("6在列表中:", 6 in numbers)  # False

4. 排序和反转
-----------------------------------------------------

::

    # sort() - 原地排序
    numbers = [3, 1, 4, 1, 5, 9, 2]
    numbers.sort()
    print("升序排序:", numbers)  # [1, 1, 2, 3, 4, 5, 9]

    numbers.sort(reverse=True)
    print("降序排序:", numbers)  # [9, 5, 4, 3, 2, 1, 1]

    # 自定义排序
    words = ['apple', 'banana', 'cherry', 'date']
    words.sort(key=len)  # 按长度排序
    print("按长度排序:", words)  # ['date', 'apple', 'banana', 'cherry']

    # sorted() - 返回新排序列表（不改变原列表）
    numbers = [3, 1, 4, 1, 5]
    sorted_numbers = sorted(numbers)
    print("原列表:", numbers)  # [3, 1, 4, 1, 5]
    print("排序后:", sorted_numbers)  # [1, 1, 3, 4, 5]

    # reverse() - 原地反转
    numbers.reverse()
    print("反转后:", numbers)  # [5, 1, 4, 1, 3]

    # reversed() - 返回反转迭代器
    reversed_numbers = list(reversed(numbers))
    print("reversed:", reversed_numbers)  # [3, 1, 4, 1, 5]

5. 复制列表
-----------------------------------------------------

::

    original = [1, 2, [3, 4]]

    # 浅拷贝 - copy() 或切片
    shallow_copy = original.copy()
    slice_copy = original[:]

    # 修改浅拷贝会影响嵌套的原始对象
    shallow_copy[2][0] = 99
    print("原列表:", original)  # [1, 2, [99, 4]]
    print("浅拷贝:", shallow_copy)  # [1, 2, [99, 4]]

    # 深拷贝
    import copy
    original = [1, 2, [3, 4]]
    deep_copy = copy.deepcopy(original)
    deep_copy[2][0] = 99
    print("原列表:", original)  # [1, 2, [3, 4]]
    print("深拷贝:", deep_copy)  # [1, 2, [99, 4]]

高级列表操作
=====================================================

1. 列表切片技巧
-----------------------------------------------------

::

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 基本切片
    print("前5个:", numbers[:5])    # [0, 1, 2, 3, 4]
    print("后3个:", numbers[-3:])   # [7, 8, 9]
    print("索引2到6:", numbers[2:7]) # [2, 3, 4, 5, 6]

    # 步长切片
    print("每隔2个:", numbers[::2])     # [0, 2, 4, 6, 8]
    print("反转:", numbers[::-1])       # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print("从后往前每隔2个:", numbers[::-2]) # [9, 7, 5, 3, 1]

    # 切片赋值（修改原列表）
    numbers[2:5] = [20, 30, 40]
    print("切片赋值后:", numbers)  # [0, 1, 20, 30, 40, 5, 6, 7, 8, 9]

    # 切片删除
    numbers[2:5] = []
    print("切片删除后:", numbers)  # [0, 1, 5, 6, 7, 8, 9]

2. 列表解包
-----------------------------------------------------

::

    # 基本解包
    first, second, *rest = [1, 2, 3, 4, 5]
    print(f"first: {first}, second: {second}, rest: {rest}")  # first: 1, second: 2, rest: [3, 4, 5]

    # 各种解包模式
    a, *b, c = [1, 2, 3, 4, 5]
    print(f"a: {a}, b: {b}, c: {c}")  # a: 1, b: [2, 3, 4], c: 5

    *x, y, z = [1, 2, 3, 4, 5]
    print(f"x: {x}, y: {y}, z: {z}")  # x: [1, 2, 3], y: {4}, z: 5

    # 合并列表
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merged = [*list1, *list2]
    print("合并列表:", merged)  # [1, 2, 3, 4, 5, 6]

3. 列表与函数
-----------------------------------------------------

::

    # 可变参数
    def sum_numbers(*args):
        return sum(args)

    print("求和:", sum_numbers(1, 2, 3, 4, 5))  # 15

    # 列表作为参数传递
    def process_list(lst):
        # 注意：这会修改原列表！
        lst.append(100)
        return lst

    numbers = [1, 2, 3]
    result = process_list(numbers)
    print("原列表:", numbers)  # [1, 2, 3, 100] - 被修改了！
    print("返回值:", result)   # [1, 2, 3, 100]

    # 避免修改原列表的方法
    def safe_process_list(lst):
        new_lst = lst.copy()  # 创建副本
        new_lst.append(100)
        return new_lst

    numbers = [1, 2, 3]
    result = safe_process_list(numbers)
    print("原列表:", numbers)  # [1, 2, 3] - 未被修改
    print("返回值:", result)   # [1, 2, 3, 100]

实际应用场景
=====================================================

1. 数据分组
-----------------------------------------------------

::

    def chunk_list(lst, chunk_size):
        """将列表分割成指定大小的块"""
        return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

    numbers = list(range(10))
    chunks = chunk_list(numbers, 3)
    print("分块结果:", chunks)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]

2. 列表去重
-----------------------------------------------------

::

    # 方法1: 使用set（不保持顺序）
    def remove_duplicates_set(lst):
        return list(set(lst))

    # 方法2: 保持顺序
    def remove_duplicates_ordered(lst):
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    # 方法3: 使用dict（Python 3.7+ 保持插入顺序）
    def remove_duplicates_dict(lst):
        return list(dict.fromkeys(lst))

    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("set去重:", remove_duplicates_set(numbers))
    print("有序去重:", remove_duplicates_ordered(numbers))
    print("dict去重:", remove_duplicates_dict(numbers))

3. 列表过滤
-----------------------------------------------------

::

    # 使用列表推导式
    numbers = [1, -2, 3, -4, 5, -6]
    positive = [x for x in numbers if x > 0]
    print("正数:", positive)  # [1, 3, 5]

    # 使用filter函数
    def is_even(x):
        return x % 2 == 0

    even_numbers = list(filter(is_even, numbers))
    print("偶数:", even_numbers)  # [-2, -4, -6]

    # 使用lambda表达式
    negative = list(filter(lambda x: x < 0, numbers))
    print("负数:", negative)  # [-2, -4, -6]

4. 列表映射
-----------------------------------------------------

::

    # 使用列表推导式
    numbers = [1, 2, 3, 4, 5]
    squared = [x**2 for x in numbers]
    print("平方:", squared)  # [1, 4, 9, 16, 25]

    # 使用map函数
    cubed = list(map(lambda x: x**3, numbers))
    print("立方:", cubed)  # [1, 8, 27, 64, 125]

    # 复杂映射
    def process_number(x):
        if x % 2 == 0:
            return x * 2
        else:
            return x + 1

    processed = [process_number(x) for x in numbers]
    print("处理后的数:", processed)  # [2, 4, 4, 8, 6]

性能考虑
=====================================================

1. 时间复杂度
-----------------------------------------------------

::

    # 常见操作的时间复杂度
    """
    操作        时间复杂度
    索引访问    O(1)
    追加append  O(1)
    插入insert  O(n)
    删除remove  O(n)
    查找in      O(n)
    切片        O(k) - k是切片大小
    排序sort    O(n log n)
    """

    # 性能对比示例
    import time

    def test_append_vs_insert():
        n = 10000
        
        # append - O(1)
        start = time.time()
        lst = []
        for i in range(n):
            lst.append(i)
        append_time = time.time() - start
        
        # insert(0) - O(n)
        start = time.time()
        lst = []
        for i in range(n):
            lst.insert(0, i)
        insert_time = time.time() - start
        
        print(f"append 时间: {append_time:.4f}s")
        print(f"insert(0) 时间: {insert_time:.4f}s")

    test_append_vs_insert()

2. 内存使用优化
-----------------------------------------------------

::

    # 使用生成器表达式处理大数据
    def process_large_data():
        # 列表推导式 - 占用大量内存
        # squares = [x**2 for x in range(1000000)]
        
        # 生成器表达式 - 节省内存
        squares_gen = (x**2 for x in range(1000000))
        
        total = 0
        for square in squares_gen:
            total += square
            if total > 1000000:
                break
        
        return total

    result = process_large_data()
    print(f"处理结果: {result}")

总结
=====================================================

列表是 Python 中最灵活的数据结构：

创建方式多样：字面量、构造函数、推导式

操作丰富：增删改查、排序、反转、切片

性能考虑：了解不同操作的时间复杂度

实际应用：数据处理、算法实现、业务逻辑


