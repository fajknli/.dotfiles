Python Standard Library
#######################


    os：提供了与操作系统交互的接口，用于文件和目录操作。

    sys：提供对Python解释器使用或维护的一些变量以及与解释器强烈交互的操作。

    math：包含数学函数。

    random：生成随机数的模块。

    datetime：处理日期和时间的类。

    json：处理JSON数据的编码和解码。

    collections：提供额外的数据类型，如deque、namedtuple等。

    re：支持正则表达式。

    threading：支持多线程编程。

    multiprocessing：支持多进程编程。

    subprocess：用于生成新的进程，连接到它们的输入/输出/错误管道，并获取它们的返回码。

    io：处理流（如文件操作）的基础库。

    pickle：对象的序列化和反序列化。

    time：提供时间相关的函数。

    warnings：警告的触发、控制和过滤。

    itertools：创建有效循环的函数。

    logging：配置日志记录的功能。

    argparse：编写命令行接口的程序。

    gettext：国际化和本地化的应用程序。

    unittest：测试发现和丰富的断言方法。

--------------------------------------------

1. OS
======

os：提供了与操作系统交互的接口，用于文件和目录操作。


::

    import os
    print(dir(os))

    dir(os) 会返回一个包含 os 模块所有属性和方法的列表。

1. 系统相关
-------------------------------------------------

- os.name                                         系统名字
- os.environ                                      系统的坏境变量
- os.sep                                          系统分隔符号
- os.pathsep                                      系统路径分隔符号
- os.linesep                                      系统行分隔符号
- os.getgid                                       来获取当前进程的真实组ID
- os.getpid                                       返回当前进程的进程 ID
- os.getuid                                       返回当前进程的用户 ID。它也被称为 UID

2. 文件和目录相关
-------------------------------------------------

- os.getcwd                                       函数输入当前工作目录
- os.chdir                                        函数可更改当前工作目录
- os.listdir                                      函数返回当前工作目录中所有文件和文件夹的名称列表
- os.walk                                         输出目标路径,目录,文件
- os.mkdir                                        函数创建一个新目录(不能已经存在),不能递归创建
- os.makedirs                                     创建一个目录，可以递归，不像mkdir,没那么严格
- os.removedirs                                   删除包括所有子目录在内的现有目录(必须存在此目录)
- os.rmdir                                        删除现有目录(必须存在此目录),不会删除子目录
- with open(filename,'w/r') as file
- os.renames                                      该函数用于重命名文件或目录。它需要文件的当前名称和文件的新名称。
- os.remove                                       永久删除现有文件，但对目录不起作用
- os.unlink                                       删除文件
- os.path.exists                                  判断目录或者文件是否存在
- os.path.isdir                                   判断目标是否是目录
- os.path.isfile                                  判断目标是否是文件
- os.path.isabs                                   判断是否是绝对路径(就是从根目录开始的)
- os.path.split                                   将路径和文件名分开，存放在二元组里
- os.path.getatime                                表示文件最后一次被读取的时间
- os.path.getctime                                最后一次更改的时间，或者内容最后一次更改的时间
- os.path.getmtime                                表示文件内容最后一次被写入的时间
- os.path.getsize                                 获取目标字节大小
- os.access('path',os.F_OK)                       F/R/W/X_OK 模式验证路径是否存在/可读/可写/可执行
- os.stat                                         输出目标路径信息

3. 执行目录,管理进程
-------------------------------------------------

- os.system                                       函数允许我们在 Python 环境中运行 shell 命令



with...as...加open()写入目标文件

::

    file_name = "apple.txt"

    # 写入文件
    with open(file_name, 'w') as file:
        file.write("Apples are healthy")

    # 读取并打印文件内容
    with open(file_name, 'r') as file:
        print(file.read())

    使用 with ... as ... 结构的好处是，当代码块执行完毕后，它会确保资源被正确关闭或释放，即使在代码块中发生了异常。这样可以简化代码，避免因为忘记关闭资源而导致的问题
    这不是属于os库的，但是和打开文件有关，os.popen()函数，这个函数在Python 3中已经被移除了。我们可以使用open()函数来替代它。



输出目标路径信息

::

    import os
    print(os.stat("path"))

    该函数对传递的路径执行 stat 系统调用，并返回路径的以下信息。

    st_mode = 保护位
    st_ino = 节点编号
    st_dev = 设备 ID
    st_nlink = 硬连接数
    st_uid = 用户 ID
    st_gid = 组 ID
    st_size = 以字节为单位的文件大小
    st_atime = 最近一次访问的时间
    st_mtime = 最近一次修改的时间
    st_ctime = 最近一次元数据更改的时间


--------------------------------------------

2. sys
=============

1. 命令行参数处理： 
-----------------------

- sys.argv                  一个显示命令行执行的参数的列表

2. 系统相关操作： 
--------------------------------------------

- sys.exit([arg])           退出Python程序。如果提供了arg，它会显示一个错误消息并退出；如果没有提供arg，程序将正常退出
- sys.version               返回当前Python解释器的版本信息
- sys.platform              返回当前操作系统的名称

3. 文件IO操作： 
--------------------------------------------

- sys.stdin                    标准输入
- sys.stdout                   标准输出
- sys.stderr                   标准错误

4. 内存和性能管理： 
--------------------------------------------

- sys.getsizeof(object)              返回指定对象的内存大小（以字节为单位）。
- sys.setrecursionlimit(limit)       设置Python递归调用的最大深度。

5. 模块和引用管理： 
--------------------------------------------

- sys.path       一个字符串列表，包含了系统查找模块的路径集合。
- sys.modules    一个字典，键为模块名，值为模块对象，包含了所有已导入的模块。

6. 其他
--------------------------------------------



- sys.getrefcount(object)      返回指定对象的引用计数。

--------------------------------------------

3. math
=========

1. 数学常量：
--------------------------------------------


- math.pi：圆周率π的值。
- math.e：自然对数的底数e的值。
- math.tau：tau（2π）的值。
- math.inf：表示正无穷大的浮点数。
- math.nan：表示非数字（Not a Number）的特殊浮点数。

2. 三角函数和双曲函数： 
-------------------------------------------------------


- math.sin(x)：返回x的正弦值。
- math.cos(x)：返回x的余弦值。
- math.tan(x)：返回x的正切值。
- math.asin(x)：返回x的反正弦值。
- math.acos(x)：返回x的反余弦值。
- math.atan(x)：返回x的反正切值。
- math.acosh(x)：返回x的反双曲余弦值。

3. 指数和对数函数： 
-------------------------------------------------------


- math.exp(x)：返回E的x次方。
- math.log(x[, base])：返回x的自然对数，base参数可选，默认为e。
- math.log10(x)：返回x的以10为底的对数。


4. 幂函数和根号函数： 
-------------------------------------------------------

- math.pow(x, y)：返回x的y次方。
- math.sqrt(x)：返回x的平方根。



5. 取整和取余函数： 
-------------------------------------------------------


- math.ceil(x)：返回大于或等于x的最小整数。
- math.floor(x)：返回小于或等于x的最大整数。
- math.comb(n, k)：返回n个元素中取k个元素的组合数。

6. 其他有用的数学函数： 
-------------------------------------------------------


- math.copysign(x, y)：返回一个数值，其绝对值为x，符号与y相同。
- math.fabs(x)：返回x的绝对值。
- math.factorial(x)：返回x的阶乘。
- math.fmod(x, y)：返回x除以y后的余数。
- math.frexp(x)：返回x的尾数和指数。


--------------------------------------------

4. random
==========



1. 生成随机数：
----------------------

- random.random(): 返回一个 0 到 1 之间的随机浮点数。
- random.randint(a, b): 返回一个 a 到 b 之间的随机整数，包括 a 和 b。
- random.uniform(a, b): 返回一个 a 到 b 之间的随机浮点数。
- random.gauss(mu, sigma): 返回一个服从正态分布的随机数，其中 mu 是均值，sigma 是标准差。

2. 生成随机序列：
----------------------

- random.choice(seq): 从序列 seq 中随机选择一个元素。
- random.shuffle(seq): 将序列 seq 中的元素随机打乱顺序。
- random.sample(population, k): 从总体 population 中随机选择 k 个不重复的样本。

3. 种子和状态控制：
----------------------

- random.seed(a=None): 初始化随机数生成器的种子，可用于控制随机数生成的结果。
- random.getstate(), random.setstate(state): 获取和设置随机数生成器的状态，用于保存和恢复生成器的状态。

4. 其他函数：
----------------------

- random.randrange(start, stop[, step]): 返回一个指定范围内的随机整数，可指定起始值、结束值和步长。
- random.random(): 返回一个 0 到 1 之间的随机浮点数。
- random.seed(a=None): 初始化随机数生成器的种子。


--------------------------------------------

5. datetime
============

datetime 模块是 Python 标准库中用于处理日期和时间的模块，主要负责日期时间的表示、计算和格式化。下面是 datetime 模块中的一些主要功能分类和函数：

1. 日期时间对象：
--------------------------------------------

- datetime.datetime(year, month, day, hour, minute, second, microsecond): 创建一个表示特定日期时间的对象。
- datetime.date(year, month, day): 创建一个表示日期的对象。
- datetime.time(hour, minute, second, microsecond): 创建一个表示时间的对象。
- datetime.timedelta(days, seconds, microseconds, milliseconds, minutes, hours, weeks): 表示时间间隔或持续时间的对象。

2. 日期时间操作：
--------------------------------------------

- datetime.datetime.now(): 返回当前日期时间。
- datetime.datetime.combine(date, time): 合并日期和时间对象。
- datetime.datetime.strptime(date_string, format): 将日期时间字符串转换为 datetime 对象。
- datetime.datetime.strftime(format): 将 datetime 对象格式化为字符串。

3. 日期时间比较和计算：
--------------------------------------------

- datetime.datetime1 < datetime.datetime2: 比较两个日期时间对象的大小。
- datetime.datetime1 + timedelta: 对日期时间对象进行加法操作。
- datetime.datetime1 - datetime.datetime2: 计算两个日期时间对象之间的时间间隔。
 
4. 时区处理：
--------------------------------------------

- datetime.timezone(offset, name): 表示时区的对象。
- datetime.datetime.astimezone(tz): 将日期时间对象转换为指定时区的时间。

5. 其他函数：
--------------------------------------------

- datetime.datetime.today(): 返回当前日期时间，不包含时区信息。
- datetime.datetime.fromtimestamp(timestamp): 将时间戳转换为 datetime 对象。
- datetime.datetime.utcfromtimestamp(timestamp): 将 UTC 时间戳转换为 datetime 对象。

--------------------------------------------

6. json
========

json 模块在 Python 中主要负责 JSON 数据的编码和解码。JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，常用于前后端数据传输和存储。

下面是 json 模块中的主要分类和函数：

JSON 编码（序列化）：
--------------------------------------------

- json.dumps(obj, indent=None, separators=None, default=None): 将 Python 对象编码为 JSON 字符串。可以指定缩进、分隔符等参数。
- json.dump(obj, fp, indent=None, separators=None, default=None): 将 Python 对象编码为 JSON 字符串，并将结果写入文件对象。

JSON 解码（反序列化）：
--------------------------------------------


- json.loads(s): 将 JSON 字符串解码为 Python 对象。
- json.load(fp): 从文件对象中读取 JSON 数据并解码为 Python 对象。

其他函数：
--------------------------------------------

- json.dump(obj, fp, kwargs): 将 Python 对象编码为 JSON 格式并写入文件，支持更多参数设置。
- json.dumps(obj, kwargs): 将 Python 对象编码为 JSON 格式的字符串，支持更多参数设置。
- json.load(fp, kwargs): 从文件对象中读取 JSON 数据并解码为 Python 对象，支持更多参数设置。
- json.loads(s, kwargs): 将 JSON 字符串解码为 Python 对象，支持更多参数设置。
- json.JSONEncoder.default(o): JSON 编码器的默认方法，用于处理不可序列化的对象。
- json.JSONDecoder.object_hook(d): JSON 解码器的默认方法，用于处理 JSON 字符串中的对象。

json 模块提供了方便的方法来处理 JSON 数据，实现了 Python 对象与 JSON 数据之间的相互转换。通过这些函数，可以轻松地将 Python 数据结构转换为 JSON 格式进行传输和存储，也可以将 JSON 数据解析为 Python 对象进行处理。这使得在 Python 中与其他系统进行数据交换变得更加简单和高效。

7. collections
===================

collections 模块在 Python 中主要提供了一些额外的数据结构，这些数据结构不同于内置的基本数据结构（如列表、字典、集合等），可以帮助我们更高效地解决一些特定的问题。

下面是 collections 模块中的主要分类和函数：

容器数据类型：
--------------------------------------------

- namedtuple(typename, field_names, \*, rename=False, defaults=None, module=None): 创建一个具有命名字段的元组子类。
- deque([iterable[, maxlen]]): 双向队列，支持在两端快速添加和删除元素。
- ChainMap(\*maps): 将多个字典或映射合并为一个视图。
- Counter([iterable-or-mapping]): 字典的子类，用于计数可哈希对象。
- OrderedDict: 有序字典，可以记住元素的添加顺序。
- defaultdict(default_factory): 字典的子类，提供默认值以避免键错误。

抽象基类：
--------------------------------------------

- abc: 提供了抽象基类，如 Iterable, Container, Sized 等，用于定义集合类的接口规范。

其他函数：
--------------------------------------------

- ChainMap.new_child(m=None): 创建一个新的 ChainMap 对象，继承原始的 ChainMap 对象。
- Counter.most_common([n]): 返回计数器中出现次数最多的元素及其计数。
- OrderedDict.popitem(last=True): 弹出并返回有序字典中的一个键值对。
- defaultdict.default_factory: 返回 defaultdict 对象的默认工厂函数。

collections 模块为 Python 提供了一些有用的数据结构，可以帮助我们更方便地处理特定类型的数据。这些数据结构在实际编程中经常被用到，能够提高代码的可读性和性能。例如，Counter 可用于统计元素出现的次数，deque 可以用于实现队列和栈等数据结构，namedtuple 则可以方便地创建具有命名字段的元组，提高代码的可读性。

--------------------------------------------

8. re
=======

re 模块在 Python 中主要负责处理正则表达式（regular expressions）。正则表达式是一种强大的字符串匹配工具，可以用来搜索、替换和解析字符串。

下面是 re 模块中的主要分类和函数：

1. 函数：
--------------------------------------------

- re.compile(pattern, flags=0): 编译正则表达式模式，返回一个正则表达式对象。
- re.match(pattern, string, flags=0): 尝试从字符串的起始位置匹配一个模式。
- re.search(pattern, string, flags=0): 在字符串中搜索匹配模式的位置。
- re.findall(pattern, string, flags=0): 返回字符串中所有与模式匹配的字符串。
- re.finditer(pattern, string, flags=0): 返回一个迭代器，包含所有与模式匹配的匹配对象。
- re.sub(pattern, repl, string, count=0, flags=0): 使用替换字符串替换匹配到的模式。
- re.split(pattern, string, maxsplit=0, flags=0): 根据模式分割字符串。
- re.fullmatch(pattern, string, flags=0): 尝试完全匹配字符串与模式。

2. 标志（flags）：
--------------------------------------------

- re.IGNORECASE: 忽略大小写。
- re.MULTILINE: 多行模式，改变 ^ 和 $ 的行为。
- re.DOTALL: 使 . 匹配包括换行符在内的任意字符。

等等其他标志。

3. 正则表达式模式语法：
--------------------------------------------

- .: 匹配任意字符。
- ^: 匹配字符串的开头。
- $: 匹配字符串的结尾。
- \*: 匹配前一个字符的零个或多个。
- +: 匹配前一个字符的一个或多个。
- ?: 匹配前一个字符的零个或一个。
- \\\: 转义特殊字符。
- []: 匹配括号内的任意一个字符。
- \|: 或操作符。
- (): 分组。

re 模块提供了丰富的功能来处理正则表达式，可以用于字符串的模式匹配、查找和替换等操作。正则表达式在文本处理和数据提取中非常有用，能够帮助我们快速有效地处理各种复杂的字符串匹配问题。


--------------------------------------------


9. time
=========

time 模块在 Python 中主要用于处理时间相关的操作，包括获取时间戳、日期时间的转换、暂停程序执行等功能。

下面是 time 模块中的主要分类和函数：

时间获取：
--------------------------------------------

- time(): 返回当前时间的时间戳（从1970年1月1日开始的秒数）。
- gmtime([secs]): 将时间戳转换为 UTC 时间的 struct_time 对象。
- localtime([secs]): 将时间戳转换为本地时间的 struct_time 对象。
- asctime([t]): 将 struct_time 对象转换为可读的时间字符串。
- ctime([secs]): 将时间戳转换为可读的时间字符串。

时间格式化：
--------------------------------------------

- strftime(format[, t]): 将 struct_time 对象根据指定格式转换为字符串。
- strptime(string, format): 将字符串解析为 struct_time 对象。

时间延迟：
--------------------------------------------

- sleep(secs): 暂停程序执行指定秒数。
 
性能计时：
--------------------------------------------

- perf_counter(): 返回一个性能计数器的值，用于测量短时间间隔的性能。
- process_time(): 返回当前进程的用户CPU时间和系统CPU时间的总和。

其他函数：
--------------------------------------------

- time_ns(): 返回当前时间的纳秒级别精确时间戳。
- monotonic(): 返回一个单调递增的时间值，用于测量时间间隔。

time 模块提供了丰富的时间处理功能，可以帮助我们获取、转换和操作时间相关的信息。这些函数在编写需要处理时间的程序时非常有用，可以用于实现定时任务、性能测试、日志记录等功能。

--------------------------------------------

9. argparse
=============

argparse 模块在 Python 中主要用于解析命令行参数，帮助我们编写命令行工具时能够接收用户输入的参数，并进行相应的处理。

下面是 argparse 模块中的主要分类和函数：

1. 创建解析器：
--------------------------------------------

- ArgumentParser(): 创建一个参数解析器对象，用于管理命令行参数的定义和解析。

2. 添加参数：
--------------------------------------------

- add_argument(): 向解析器中添加命令行参数的定义，包括参数名、参数类型、帮助信息等。

参数类型包括：位置参数、可选参数、布尔参数等。

3. 解析参数：
--------------------------------------------

- parse_args(args=None, namespace=None): 解析命令行参数，并返回一个包含用户输入值的命名空间对象。

4. 参数定义：
--------------------------------------------

- nargs: 指定参数接受的值的个数。
- choices: 指定参数接受的值的范围。
- default: 指定参数的默认值。
- help: 参数的帮助信息。
- type: 参数的类型，如 int、float、str 等。
- action: 参数的行为，如存储值、计数等。

5. 子命令：
--------------------------------------------

- add_subparsers(): 添加子命令解析器，用于支持多个子命令的情况。

6. 参数组：
--------------------------------------------

- add_argument_group(): 添加参数组，用于将参数分组显示在帮助信息中。

7. 帮助信息：
--------------------------------------------

- print_help(): 打印程序的帮助信息。
- print_usage(): 打印程序的用法信息。

argparse 模块提供了强大的功能，使得我们可以轻松地处理命令行参数，定义参数的类型、默认值和帮助信息，并且支持子命令和参数分组，让我们的命令行工具更加灵活和易用。通过使用 argparse 模块，我们可以快速构建出功能完善的命令行工具。


--------------------------------------------

10. pickie
===========

pickle 模块是 Python 中用于序列化（serialization）和反序列化（deserialization）对象的标准模块。序列化是指将对象转换为字节流的过程，以便于存储到文件或在网络上传输；而反序列化则是将字节流转换回对象的过程。pickle 模块提供了一种将 Python 对象转换为字节流，以及将字节流转换回 Python 对象的机制。

pickle 模块中主要包含以下几个类别的函数：

1. 序列化和反序列化函数：
--------------------------------------------

- pickle.dump(obj, file)：将对象序列化并写入文件对象。
- pickle.dumps(obj)：将对象序列化为字节流。
- pickle.load(file)：从文件对象中读取字节流并反序列化为对象。
- pickle.loads(bytes_object)：从字节流中反序列化为对象。

2. 高级接口函数：
--------------------------------------------

- pickle.dump(obj, file, protocol)：指定序列化协议版本。
- pickle.dumps(obj, protocol)：指定序列化协议版本。
- pickle.load(file, \*, fix_imports=True, encoding="ASCII", errors="strict")：控制导入行为和编码。
- pickle.loads(bytes_object, \*, fix_imports=True, encoding="ASCII", errors="strict")：控制导入行为和编码。

3. 辅助函数：
--------------------------------------------

- pickle.HIGHEST_PROTOCOL：返回支持的最高协议版本。
- pickle.DEFAULT_PROTOCOL：返回默认的序列化协议版本。
- pickle.Pickler(file, protocol)：用于自定义序列化行为的 Pickler 类。
- pickle.Unpickler(file)：用于自定义反序列化行为的 Unpickler 类。

除了上述函数外，pickle 模块还提供了一些其他功能，如处理循环引用、支持自定义对象的序列化和反序列化，以及支持压缩等。总的来说，pickle 模块是 Python 中用于对象序列化和反序列化的核心模块，能够方便地将 Python 对象转换为可存储或传输的格式，以及将其还原为原始对象。

