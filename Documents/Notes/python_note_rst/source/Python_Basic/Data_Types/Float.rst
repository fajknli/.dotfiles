Float
#########

浮点数（float）是 Python 中用于表示实数的数据类型，可以表示小数和科学计数法。

基本概念
===================================

1. 浮点数定义
-----------------------------------

::

    # 基本浮点数
    a = 3.14
    b = -2.5
    c = 0.0
    d = .5  # 等同于 0.5
    e = 5.  # 等同于 5.0

    print(type(a))  # <class 'float'>

2. 科学计数法
-----------------------------------

::

    # 科学计数法表示
    large = 1.23e6    # 1.23 × 10^6 = 1230000.0
    small = 1.23e-6   # 1.23 × 10^-6 = 0.00000123

    print(large)  # 1230000.0
    print(small)  # 1.23e-06

    # 自动科学计数法
    very_large = 1000000000000.0
    print(very_large)  # 1e+12

浮点数运算
===================================

1. 基本算术运算
-----------------------------------

::

    # 四则运算
    a = 5.5
    b = 2.2

    print(a + b)   # 7.7
    print(a - b)   # 3.3
    print(a * b)   # 12.1
    print(a / b)   # 2.5

    # 幂运算
    print(2.0 ** 3.0)  # 8.0
    print(4.0 ** 0.5)  # 2.0 (平方根)

2. 混合类型运算
-----------------------------------

::

    # 浮点数与整数运算
    result1 = 3 + 2.5    # 整数 + 浮点数 = 浮点数
    result2 = 4.0 * 2    # 浮点数 * 整数 = 浮点数
    result3 = 7 / 2      # 整数 / 整数 = 浮点数 (Python 3)

    print(result1, type(result1))  # 5.5 <class 'float'>
    print(result2, type(result2))  # 8.0 <class 'float'>
    print(result3, type(result3))  # 3.5 <class 'float'>

3. 除法运算
-----------------------------------

::

    # 三种除法
    a = 7.0
    b = 2.0

    print(a / b)    # 3.5 (真除法)
    print(a // b)   # 3.0 (向下取整除法)
    print(a % b)    # 1.0 (取模)

    # 整数除法
    print(7 // 2)   # 3 (整数结果)
    print(7.0 // 2) # 3.0 (浮点数结果)

浮点数精度问题
===================================

1. 精度问题的原因
-----------------------------------

::

    # 经典的浮点数精度问题
    result = 0.1 + 0.2
    print(result)        # 0.30000000000000004
    print(result == 0.3) # False

    # 为什么会这样？
    # 计算机使用二进制表示浮点数，有些十进制小数无法精确表示为二进制

2. 处理精度问题的方法
-----------------------------------

::

    # 方法1：使用 round() 函数
    result = 0.1 + 0.2
    rounded = round(result, 2)
    print(rounded)           # 0.3
    print(rounded == 0.3)    # True

    # 方法2：使用 math.isclose()
    import math
    result = 0.1 + 0.2
    print(math.isclose(result, 0.3))  # True

    # 方法3：使用 decimal 模块（高精度计算）
    from decimal import Decimal
    a = Decimal('0.1')
    b = Decimal('0.2')
    result = a + b
    print(result)           # 0.3
    print(float(result))    # 0.3

浮点数特殊值
===================================

1. 无穷大和 NaN
-----------------------------------

::

    import math

    # 无穷大
    positive_inf = float('inf')
    negative_inf = float('-inf')

    print(positive_inf)                    # inf
    print(negative_inf)                    # -inf
    print(math.isinf(positive_inf))        # True

    # 非数字 (NaN)
    not_a_number = float('nan')
    print(not_a_number)                    # nan
    print(math.isnan(not_a_number))        # True

    # 产生无穷大的运算
    print(1.0 / 0.0)       # ZeroDivisionError
    print(float('inf') + 100)  # inf
    print(float('inf') * 0)    # nan

2. 检查特殊值
-----------------------------------

::

    import math

    def check_float(value):
        if math.isinf(value):
            return "无穷大"
        elif math.isnan(value):
            return "非数字"
        else:
            return f"正常数字: {value}"

    print(check_float(3.14))           # 正常数字: 3.14
    print(check_float(float('inf')))   # 无穷大
    print(check_float(float('nan')))   # 非数字

常用数学函数
===================================

1. 内置函数
-----------------------------------

::

    # 绝对值
    print(abs(-3.14))      # 3.14

    # 四舍五入
    print(round(3.14159, 2))   # 3.14
    print(round(3.14159, 3))   # 3.142

    # 最大值和最小值
    print(max(1.5, 2.3, 0.8))  # 2.3
    print(min(1.5, 2.3, 0.8))  # 0.8
    2. math 模块函数
       ::

    import math

    # 基本数学函数
    print(math.sqrt(16.0))     # 4.0 (平方根)
    print(math.pow(2.0, 3.0))  # 8.0 (幂运算)
    print(math.exp(1.0))       # 2.718... (e^x)
    print(math.log(10.0))      # 2.302... (自然对数)

    # 三角函数
    print(math.sin(math.pi/2)) # 1.0
    print(math.cos(math.pi))   # -1.0

    # 上下取整
    print(math.ceil(3.2))      # 4 (向上取整)
    print(math.floor(3.8))     # 3 (向下取整)
    print(math.trunc(3.8))     # 3 (截断小数部分)

类型转换
===================================

1. 转换为浮点数
-----------------------------------

::

    # 从整数转换
    print(float(5))        # 5.0
    print(float(-3))       # -3.0

    # 从字符串转换
    print(float("3.14"))   # 3.14
    print(float("1e-3"))   # 0.001
    print(float("  -2.5 ")) # -2.5 (自动去除空格)

    # 从布尔值转换
    print(float(True))     # 1.0
    print(float(False))    # 0.0

2. 浮点数转换为其他类型
-----------------------------------

::

    x = 3.75

    # 转换为整数（截断小数部分）
    print(int(x))          # 3

    # 转换为字符串
    print(str(x))          # "3.75"

    # 转换为布尔值
    print(bool(x))         # True
    print(bool(0.0))       # False

实际应用场景
===================================

1. 科学计算
-----------------------------------

::

    # 物理计算 - 计算圆的面积和周长
    import math

    def circle_calculations(radius):
        area = math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        return area, circumference

    area, circ = circle_calculations(5.0)
    print(f"面积: {area:.2f}")          # 面积: 78.54
    print(f"周长: {circ:.2f}")          # 周长: 31.42

2. 金融计算
-----------------------------------

::

    # 复利计算
    def compound_interest(principal, rate, years):
        amount = principal * (1 + rate/100) ** years
        return round(amount, 2)

    investment = 1000.0  # 初始投资
    annual_rate = 5.0    # 年利率 5%
    years = 10           # 投资年限

    final_amount = compound_interest(investment, annual_rate, years)
    print(f"最终金额: ${final_amount}")  # 最终金额: $1628.89

3. 数据分析
-----------------------------------

::

    # 计算平均值
    def calculate_average(numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)

    scores = [85.5, 92.0, 78.5, 96.0, 88.5]
    average = calculate_average(scores)
    print(f"平均分: {average:.1f}")  # 平均分: 88.1

4. 游戏开发
-----------------------------------

::

    # 物理引擎中的速度计算
    def calculate_position(initial_pos, velocity, time, acceleration=0.0):
        """计算物体位置"""
        return initial_pos + velocity * time + 0.5 * acceleration * time ** 2

    # 示例：计算抛射体位置
    initial_height = 10.0    # 初始高度
    initial_velocity = 15.0  # 初始速度
    gravity = -9.8           # 重力加速度
    time_elapsed = 2.0       # 经过时间

    height = calculate_position(initial_height, initial_velocity, time_elapsed, gravity)
    print(f"当前高度: {height:.2f} 米")  # 当前高度: 10.40 米

格式化输出
===================================

1. 基本格式化
-----------------------------------

::

    pi = 3.141592653589793

    # 保留小数位数
    print(f"π ≈ {pi:.2f}")      # π ≈ 3.14
    print(f"π ≈ {pi:.4f}")      # π ≈ 3.1416

    # 科学计数法格式化
    large_num = 1234567.89
    print(f"{large_num:.2e}")   # 1.23e+06

    # 百分比格式化
    completion = 0.8567
    print(f"完成度: {completion:.1%}")  # 完成度: 85.7%

2. 高级格式化
-----------------------------------

::

    # 对齐和填充
    number = 123.456
    print(f"{number:10.2f}")    # '    123.46' (宽度10，右对齐)
    print(f"{number:<10.2f}")   # '123.46    ' (左对齐)
    print(f"{number:^10.2f}")   # '  123.46  ' (居中对齐)

    # 千位分隔符
    large_number = 1234567.89
    print(f"{large_number:,.2f}")  # 1,234,567.89

常见陷阱和最佳实践
===================================

1. 避免直接比较浮点数
-----------------------------------

::

    # 错误做法
    a = 0.1 + 0.2
    b = 0.3
    print(a == b)  # False

    # 正确做法
    import math
    print(math.isclose(a, b))                    # True
    print(abs(a - b) < 1e-9)                    # True (自定义容差)

2. 注意整数除法的变化
-----------------------------------

::

    # Python 2 vs Python 3
    # Python 3 中整数除法得到浮点数
    print(7 / 2)    # 3.5

    # 如果需要整数结果，使用 //
    print(7 // 2)   # 3

3. 处理大数和小数
-----------------------------------

::

    # 大数可能失去精度
    very_large = 1e20
    very_small = 1e-20

    result = very_large + very_small
    print(result == very_large)  # True (小数被忽略了)

    # 解决方法：调整计算顺序或使用高精度库

总结
===================================

浮点数是 Python 中重要的数值类型：

表示范围广：从小数到很大的科学计数法数字

运算灵活：支持各种数学运算

精度问题：需要注意二进制表示的局限性

特殊值：inf、-inf、nan

丰富工具：math 模块提供各种数学函数

掌握浮点数的特性和使用方法，对于科学计算、数据分析、游戏开发等领域都至关重要！
