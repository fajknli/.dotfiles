Perl
#######

Install Perl

System may already Installed

1. Basic
==========

1. 交互式编程
---------------

::

    $ perl -e 'print "Hello World\n"'

    Output:

    Hello World

2. 脚本式编程
----------------

create hello.pl

::

    #!/usr/bin/perl

    # 输出 "Hello, World"
    print "Hello, world\n";


$ chmod 0755 hello.pl

$ ./hello.pl

Hello, world

文件名可以包含数字，符号和字母，但不能包含空格，可以使用下划线（_）来替代空格。

3. 注释
----------

One line comment

perl 注释的方法为在语句的开头用字符#

::

    # 这一行是 perl 中的注释

Multi-line comment

POD(Plain Old Documentations) 

::

    =pdo 注释
    这是一个多行注释
    这是一个多行注释
    这是一个多行注释
    这是一个多行注释
    =cut




Perl 解释器不会关心有多少个空白

所有类型的空白如：空格，tab ，空行等如果在引号外解释器会忽略它，如果在引号内会原样输出。

::

    print       "Hello, world\n";


    Hello, world


    print "Hello
                 world\n";


    Hello
          world

单引号和双引号
-----------------

perl 输出字符串可以使用单引号和双引号，如下所示：

::

    print "Hello, world\n";    # 双引号
    print 'Hello, world\n';    # 单引号

OutPut:

::

    Hello, world
    Hello, world\n

Like Shell

Perl双引号和单引号的区别: 双引号可以正常解析一些转义字符与变量，而单引号无法解析会原样输出。


heredoc
------------

Multi-line definition string

1.必须后接分号，否则编译通不过。

2.END可以用任意其它字符代替，只需保证结束标识与开始标识一致。

3.结束标识必须顶格独自占一行(即必须从行首开始，前后不能衔接任何空白和字符)。

4.开始标识可以不带引号号或带单双引号，不带引号与带双引号效果一致，解释内嵌的变量和转义符号，带单引号则不解释内嵌的变量和转义符号。

5.当内容需要内嵌引号（单引号或双引号）时，不需要加转义符

::

    #!/usr/bin/perl

    $a = 10;
    $var = <<"EOF";
    这是一个 Here 文档实例，使用双引号。
    可以在这输如字符串和变量。
    例如：a = $a
    EOF
    print "$var\n";

    $var = <<'EOF';
    这是一个 Here 文档实例，使用单引号。
    例如：a = $a
    EOF
    print "$var\n";

Output:

::

    这是一个 Here 文档实例，使用双引号。
    可以在这输如字符串和变量。
    例如：a = 10

    这是一个 Here 文档实例，使用单引号。
    例如：a = $a

转义字符
---------

In String, use backslash

双引号下的转义，单引号不能进行转义，会直接输出原来字符

::

    \\          反斜杠
    \'          单引号
    \"          双引号
    \b          退格
    \f           换页符(将其后面的字符串移动到下一行,保持之前的缩进)
    \n           换行
    \r           回车
    \u           强制其后一个字符变成大写
    \U           强制其后所有字符变成大写
    \l           强制其后一个字符变成小写
    \L           强制其后所有字符变成小写
    \Q           将到\E为止的非单词（non-word）字符加上反斜线
    \E           结束\L、\U、\Q

Perl 标识符 
------------

Perl 标识符是用户编程时使用的名字，在程序中使用的变量名，常量名，函数名，语句块名等统称为标识符

标识符组成单元：英文字母（a~z，A~Z），数字（0~9）和下划线（_）。

标识符由英文字母或下划线开头,No Number

标识符区分大小写

Perl 数据类型
---------------

在 Perl 中，my 是一个用于声明词法变量的关键字。它的作用范围仅限于当前代码块或表达式。

使用 my 声明的变量是私有变量，其值只能在定义它的代码块内部访问。当代码块执行完毕后，这些变量的值将不再存在。

::

    my $var = 22;


Perl 有三个基本的数据类型：标量、数组、哈希。以下是这三种数据类型的说明：

- 标量: $var=数字,字符串,浮点数....;

- 数组: @var=(1,2,3) The index starts from scratch(zero)

- 哈希: %var=('a'=>1,'b'=>2); Out-of-order key-value pairs

Perl 数字字面量
-----------------

Perl中的数字字面量可以是整数或浮点数。

在 Perl 中，浮点数是以十进制形式表示的，并且可以有小数部分。Perl 内部将所有的数值都存储为双精度浮点数，这意味着整数和浮点数在内部是相同的数据类型。

以下是一些关于 Perl 中浮点数的使用和操作的要点：

- 字面量：浮点数可以直接作为字面量使用，例如 3.14、-0.5 或 1.23e-4（科学记数法）。

- 数学运算：可以使用标准的算术运算符对浮点数进行加（+）、减（-）、乘（*）、除（/）和取余（%）操作。

- 函数：Perl 提供了一些内置函数来处理浮点数，例如 int 用于取整，sqrt 用于计算平方根，log 用于计算自然对数等。

- 格式化输出：使用 sprintf 或 printf 函数可以格式化浮点数的输出，例如设置小数点后的位数或使用科学记数法。

- 比较：由于浮点数的精度问题，直接比较两个浮点数是否相等通常是不安全的。应该使用近似值比较，例如判断两个浮点数之差的绝对值是否小于一个很小的阈值。

- 精度问题：由于浮点数的表示限制，某些浮点数可能无法精确表示，这可能导致舍入错误。在进行精确计算时，需要注意这一点。

- 大数：对于非常大的浮点数，Perl 可以自动处理，但仍然受限于双精度浮点数的表示范围。

- 复数：Perl 也支持复数，可以使用 Math::Complex 模块进行复数运算。

下面是一个简单的 Perl 代码示例，展示了如何对浮点数进行操作：

::

    #!/usr/bin/perl

    # 定义浮点数
    my $pi = 3.14159;

    # 加法
    my $sum = $pi + 1.23;
    print "Sum: $sum
    ";

    # 减法
    my $difference = $pi - 0.5;
    print "Difference: $difference
    ";

    # 乘法
    my $product = $pi * 2;
    print "Product: $product
    ";

    # 除法
    my $quotient = $pi / 3;
    print "Quotient: $quotient
    ";

    # 取整
    my $integer_part = int($pi);
    print "Integer part of pi: $integer_part
    ";

    # 格式化输出
    my $formatted_pi = sprintf("%.2f", $pi);
    print "Formatted pi: $formatted_pi
    ";

    # 比较浮点数（不推荐）
    if ($pi == 3.14) {
        print "Pi is exactly 3.14
    ";
    } else {
        print "Pi is not exactly 3.14
    ";
    }

    # 更安全的比较方法
    if (abs($pi - 3.14) < 1e-9) {
        print "Pi is approximately equal to 3.14
    ";
    } else {
        print "Pi is not approximately equal to 3.14
    ";
    }


在 Perl 语言中，数字字面量是基本的标量数据类型之一，它们可以表示为整数或浮点数。由于 Perl 是一种弱类型语言，变量不需要预先指定类型，解释器会根据上下文自动选择匹配的类型。这意味着你可以将一个数字字面量赋值给一个变量，而无需显式声明该变量是整型还是浮点型。

在Perl中，科学记数法通过使用字母'e'或'E'来表示10的幂次。

- 2.18e22 或 2.18E22：这表示2.18乘以10的22次方。

- 5.16e-10：这表示5.16乘以10的负10次方。

精度：由于Perl内部将所有的数值都存储为双精度浮点数，因此即使输入的是整数，也可能会被存储为浮点数。

在Perl中，你可以使用sprintf函数将科学记数法转换为普通计数法。

使用%f作为格式字符串中的占位符。这将把数字转换为普通的计数法表示,由于浮点数的精度问题，转换后的数值可能会包含小数部分。如果你需要去除小数部分，可以使用int()函数将其转换为整数

::

    my $number = 5.41e03;

    my $formatted_number = sprintf("%f", $number);
    print "$formatted_number\n"; # 输出 541000.000000

    my $formatted_number = int(sprintf("%f", $number));
    print "$formatted_number\n"; # 输出 541000

Perl 支持多种进制数操作，包括二进制、八进制、十进制和十六进制。以下是一些常见的 Perl 进制数操作：



1. 二进制数：使用前缀 "0b" 表示二进制数。例如，0b1010 等于十进制的 10。

2. 八进制数：使用前缀 "0" 表示八进制数。例如，017 等于十进制的 15。

3. 十进制数：没有前缀表示十进制数。例如，42 等于十进制的 42。

4. 十六进制数：使用前缀 "0x" 表示十六进制数。例如，0x1f 等于十进制的 31。

在 Perl 中，可以使用内置函数 hex、oct、bin 和 dec 分别将十六进制、八进制、二进制和十进制转换为其他进制。例如：

::

    my $hex = hex("1a"); # 将十六进制数 "1a" 转换为十进制数
    my $oct = oct("32"); # 将八进制数 "32" 转换为十进制数
    my $bin = bin("1010"); # 将二进制数 "1010" 转换为十进制数
    my $dec = dec("42"); # 将十进制数 "42" 转换为十进制数

此外，还可以使用字符串操作符 . 将不同进制数连接在一起

::

    my $num = "0x1a" . "032"; # 将十六进制数 "1a" 和八进制数 "32" 连接在一起，得到 "0x1a032"

操作符将不同进制数的字符串形式连接在一起时，你实际上是在进行字符串拼接，而不是在进行数学上的加法运算。

变量
=====

标量变量
---------

$var = 123;

$var = 123.123;

$var = "123";

数组变量
---------

创建数组
''''''''''

::

    @array = (1, 2, 'Hello');

    @array = qw/这是 一个 数组/;  # qw//将元素收集并变成字符串

    第二个数组使用 qw// 运算符，它返回字符串列表，数组元素以空格分隔。当然也可以使用多行来定义数组：

    @array = qw/这是
    一个
    数组/;

按索引来给数组赋值

::

    $var[1] = 123 给数组var第2个元素设置为123,可以添加元素进去，也可以修改目标元素

    $var[2]       访问var数组的第3个元素

    $var[-1]      反方向访问var数组的后一个元素

    $var[-2]      反方向访问var数组的后二个元素

数组序列号
''''''''''''''

::

    @var_10 = (1..10);
    @var_20 = (10..20);
    @var_abc = ('a'..'z');

    print "@var_10\n";   # 输出 1 到 10
    print "@var_20\n";   # 输出 10 到 20
    print "@var_abc\n";  # 输出 a 到 z

数组大小/长度
'''''''''''''''
数组大小，元素个数:

::

    @array = (1,2,3,4,5,6,9);
    print scalar @array."\n";

数组长度:

::

    @array = (1,2,3);
    $array[20] = 4;

    $size = @array;

    print ($size."\n");

    print ($#array);

    OUTPUT:

    21  # 但是数组里只有4个元素，但是从0号索引到20号，中间一共有21个
    20  # 最数组大索引号

添加和删除数组元素
''''''''''''''''''''''

::

    # 创建一个简单是数组
    @sites = ("google","runoob","taobao");
    $new_size = @sites ;
    print "1. \@sites  = @sites\n"."原数组长度 ：$new_size\n";

    # 在数组结尾添加一个元素
    $new_size = push(@sites, "baidu");
    print "2. \@sites  = @sites\n"."新数组长度 ：$new_size\n";

    # 在数组开头添加一个元素
    $new_size = unshift(@sites, "weibo");
    print "3. \@sites  = @sites\n"."新数组长度 ：$new_size\n";

    # 删除数组末尾的元素
    $new_byte = pop(@sites);
    print "4. \@sites  = @sites\n"."弹出元素为 ：$new_byte\n";

    # 移除数组开头的元素
    $new_byte = shift(@sites);
    print "5. \@sites  = @sites\n"."弹出元素为 ：$new_byte\n";


切割数组
'''''''''''

::

    @sites = qw/google taobao runoob weibo qq facebook 网易/;

    @sites2 = @sites[3,4,5];

    print "@sites2\n";

输出:

::

    weibo qq facebook

.. note::

    数组索引需要指定有效的索引值，可以是正数后负数，每个索引值使用逗号隔开。

    如果是连续的索引，可以使用 .. 来表示指定范围：

::

    @sites = qw/google taobao runoob weibo qq facebook 网易/;

    @sites2 = @sites[3..5];

    print "@sites2\n";

    OUTPUT:

    weibo qq facebook

替换数组元素
''''''''''''''''

Perl 中数组元素替换使用 splice() 函数，语法格式如下：

splice (@ARRAY, OFFSET , LENGTH , LIST)

- @ARRAY：要替换的数组。

- OFFSET：替换的起始位置，不包括此位置自身替换。

- LENGTH：替换的元素个数。

- LIST：替换元素列表,一般和替换的元素个数一样，把这里的内容替换掉那个起始位置开始后的内容。

::

    @nums = (1..20);
    print "替换前 - @nums\n";

    splice(@nums, 5, 5, 21..25);
    print "替换后 - @nums\n";

输出：

::

    替换前 - 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    替换后 - 1 2 3 4 5 21 22 23 24 25 11 12 13 14 15 16 17 18 19 20




哈希变量
--------

无序,直接输出%date的结果元素顺序可能不一样

%data = ('google', 45, 'runoob', 30, 'taobao', 40);

$data{'google'}\n 访问键，得到值

特殊字符
---------

_FILE__, __LINE__, 和 __PACKAGE__ 分别表示当前执行脚本的文件名，行号，包名。

注意： __ 是两条下划线，__FILE__ 前后各两条下划线。

这些特殊字符是单独的标记，不能写在字符串中，例如：

::

    print "文件名 ". __FILE__ . "\n";

    print "行号 " . __LINE__ ."\n";

    print "包名 " . __PACKAGE__ ."\n";


v 字符串
--------

一个以 v 开头,后面跟着一个或多个用句点分隔的整数,会被当作一个字串文本。

::

    $smile  = v9786;
    $foo    = v102.111.111;
    $martin = v77.97.114.116.105.110;


    output:

    smile = ☺
    foo = foo
    martin = Martin




