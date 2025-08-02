Rust
###########

1. 安装
==============

1.1 Rustup
----------

1. Rustup 安装:

Debian下： ``sudo apt install rustup``

这样安装的在执行 ``rustc --version`` 可能会出现问题:

::

    error: rustup could not choose a version of rustc to run, because one wasn't specified explicitly, and no default is configured.
    help: run 'rustup default stable' to download the latest stable release of Rust and set it as your default toolchain.

所以执行再 ``rustup default stable`` 更新稳定版

更新时可使用镜像源加快下载速度:

::

    # for bash
    RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup rustup install stable # for stable
    # for fish
    env RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup rustup install stable # for stable
    # for bash
    RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup rustup install nightly # for nightly
    # for fish
    env RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup rustup install nightly # for nightly
    # for bash
    RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup rustup install nightly-YYYY-mm-dd
    # for fish
    env RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup rustup install nightly-YYYY-mm-dd

若要长期启用镜像源，执行：

::

    # for bash
    echo 'export RUSTUP_UPDATE_ROOT=https://mirrors.tuna.tsinghua.edu.cn/rustup/rustup' >> ~/.bash_profile
    echo 'export RUSTUP_DIST_SERVER=https://mirrors.tuna.tsinghua.edu.cn/rustup' >> ~/.bash_profile
    # for fish
    echo 'set -x RUSTUP_UPDATE_ROOT https://mirrors.tuna.tsinghua.edu.cn/rustup/rustup' >> ~/.config/fish/config.fish
    echo 'set -x RUSTUP_DIST_SERVER https://mirrors.tuna.tsinghua.edu.cn/rustup' >> ~/.config/fish/config.fish

`清华源 <https://mirrors.tuna.tsinghua.edu.cn/help/rustup/>`_



2. Rustup 更新:

::

    rustup updata

2. Cargo
==========

2.1. 用Cargo创建项目 
-------------------------------


::

    $ cargo new hello_cargo
    $ cd hello_cargo 

.. note::
   ``cargo new --vcs=git`` 可以指定version control system(版本控制系统)
   产生的 ``cargo.lock`` 不用修改啥，cargo会帮你自己控制它


2.2. cargo build
-------------------------------

使用cargo build来编译cargo/rust项目

::
    
    $ cargo build    
        Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
        Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs 

cargo build --release命令是Rust中构建Release版本非常重要的一个步骤。
使用cargo build --release可以启用优化来构建Release版本。主要的区别有:

- 执行文件会生成在target/release目录,而不是target/debug。
- 优化使代码运行更快,但编译时间会更长。
- debug版本用于开发,重建和编译频繁;release版本给最终用户,优化运行速度。

所以使用步骤是:

- 开发时使用cargo build构建debug版本
- 准备发布时使用cargo build --release构建release版本
- 测试运行速度时,使用target/release下的可执行文件

总结起来,利用cargo build --release可以得到优化的release版本用于发布,是Rust开发到部署的关键一步。

2.3. cargo run
-------------------------------

使用cargo run 来运行已经编译好的rust程序

::

    $ cargo run
        Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs 
        Running `target/debug/hello_cargo` Hello, world! 

.. note::
   这样就不必手动 ``$ ./target/debug/hello_cargo`` 运行了，更方便

如果再次执行 ``cargo run`` 不会输出编译信息而是会直接执行输出，不会再次编译，如果你修改了源码，执行 ``cargo run`` 才会输出编译信息

::

    $ cargo run  
        Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)   
        Finished dev [unoptimized + debuginfo] target(s) in 0.33 secs  
        Running `target/debug/hello_cargo` Hello, world! 


2.4. cargo check:
-------------------------------

使用cargo命令,执行check子命令。
check子命令会对当前Rust项目进行检查,分析代码,确保可以正确编译通过。但不会产生实际的二进制可执行文件。

::

    $ cargo check  
        Checking hello_cargo v0.1.0 (file:///projects/hello_cargo)   
        Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs

2.5. 总结
-------------------------------

- cargo new 创建项目
- cargo build 构建项目
- cargo run 构建并运行项目
- cargo check 检查错误,不产生二进制
- 构建结果存放在target/debug目录

另一个优点是Cargo的命令在不同操作系统下是一致的,所以使用Cargo可以避免不同系统间的差异。

利用Cargo和它的子命令可以标准化Rust项目的构建和管理。主要要记住:

- cargo new 创建项目
- cargo build/run 构建和运行
- cargo check 检查错误
- Cargo把构建结果放在target目录

通过Cargo可以统一管理Rust项目的整个生命周期。

对于简单的项目,与直接使用rustc相比,Cargo并不能提供太多价值。但是随着程序变得越来越复杂,Cargo的优势就会体现出来。一旦程序增长到多个文件或需要依赖其他库,让Cargo来协调构建过程会方便很多。虽然hello_cargo这个项目很简单,但它已经使用了您之后在Rust编程中会大量用到的真正工具。事实上,要开发任何已存在的项目,您可以使用下面的命令检查代码、切换到项目目录并构建:

::

    git checkout <someproject>
    cd <someproject>
    cargo build

简而言之,Cargo的优势在大型复杂项目中更为明显。它可以很好地协调构建过程。即使在简单项目中使用Cargo也是Rust编程的最佳实践。掌握Cargo可以大大提高工作效率。



3. 实现一个经典的入门问题:猜数游戏
===================================

3.1 Setting Up a New Project
------------------------------------------

::

    $ cargo new guessing_game
    $ cd guessing_game

3.2 查看src/main.rs
------------------------------------------

::

    fn main() {
        println!("Hello, world!");
    }

这个文件是主程序源码，主要的编译执行输出。

将其改为：

::

    use std::io;

    fn main() {
        println!("Guess the number!");

        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        println!("You guessed: {guess}");
    }

这段代码包含许多信息,我们一行行来看。为了获取用户输入并打印输出结果,我们需要引入io输入/输出库到作用域中。io库来自标准库std:

3.2.1 分析
^^^^^^^^^^^^^^^^

这行指令把std库中的io模块引入到当前作用域。


::

    use std::io;


然后是主函数:

::

    fn main() {

    }

``println!`` 是一个宏,用于打印字符串到屏幕:

::

    println!("Guess the number!");

    println!("Please input your guess.");


在 Rust 语言中，:: 是作用域解析运算符（scope resolution operator），它用于指定一个项（如函数、结构体、枚举、模块、常量等）属于哪个模块或命名空间。这个运算符有助于 Rust 的模块系统，允许你访问模块中的项，尤其是当存在命名冲突时。

以下是 :: 在 Rust 中几种常见用法的示例：

1. 访问模块中的项：
   如果有一个模块 my_module，它包含一个函数 my_function，你可以使用 :: 来指定 my_function 属于 my_module：

::

   mod my_module {
       pub fn my_function() {
           // 函数体
       }
   }

   // 调用 my_module 中的 my_function
   my_module::my_function();

2. 访问枚举的变体：
   对于枚举类型，:: 用于指定枚举的哪个变体：

::

   enum Status {
       Active,
       Inactive,
   }

   // 创建一个 Status::Inactive 枚举的实例
   let status = Status::Inactive;

3. 访问类型的关联函数：
   :: 也用于调用一个类型的关联函数（即静态方法）：

::

   struct Point {
       x: i32,
       y: i32,
   }

   impl Point {
       fn origin() -> Point {
           Point { x: 0, y: 0 }
       }
   }

   // 使用 :: 调用 Point 的关联函数 origin
   let p = Point::origin();

4. 指定类型或函数的完全限定名：
   当你需要完全限定一个名称以避免冲突时，可以使用 `::` 来指定一个类型或函数的完整路径：

::

   use some_crate::MyType;
   use another_crate::MyType;

   // 明确指定使用哪个 crate 中的 MyType
   let instance = some_crate::MyType;

在你之前的代码示例中，`Ordering::Less` 中的 `::` 就是用来指定 `Less` 是 `Ordering` 枚举的一个变体。这样的语法确保了你访问的是 `Ordering` 枚举中的 `Less` 成员，而不是可能存在的同名的其他项。





存值到变量里
^^^^^^^^^^^^^^^^

::

    let mut guess = String::new();

这个语句做了以下几件事:

1. 使用`let`关键字声明了一个叫`guess`的变量
2. 用`mut`指定这个变量是可变的
3. 变量类型是`String`字符串
4. 使用`String::new()`创建一个空的`String`实例并赋值给`guess`

所以这行代码声明了一个名为`guess`、类型为`String`、初始值为空串的可变变量。
之后可以通过`guess`来获取用户输入并存储。使用`mut`是因为每轮游戏时需要修改`guess`的值。

总结一下,这行代码展示了:

- 使用`let`声明变量
- 变量可变性`mut`
- 变量类型注解
- 为变量赋初始值

1. 使用 ``let`` 关键字声明变量,如 ``let apples = 5;``
2. 默认情况下,Rust中的变量是不可变的(immutable),一旦绑定了一个值,就不能再改变
3. 使用`mut`关键字可以声明一个可变变量(mutable),如 ``let mut bananas = 5;``
4. 通过 ``//`` 可以写注释,注释内容会被Rust编译器忽略
5. 默认不可变可以防止意外地修改变量,是Rust安全性的重要组成。但有时需要可变性,就可以用 ``mut``
6. 第3章会更深入地讨论变量、可变性等概念

::语法和associated function的含义。让我来概括一下:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. ::表示new是String类型的associated function,也就是说new函数是在String类型上实现的。
2. associated function是在某个类型上实现的函数,这里的new函数可以创建一个新的空字符串。
3. 许多类型上都有new函数,因为这是“创建某种新值”这一常见功能的常用命名。
4. let mut guess = String::new();这一行,创建了一个可变变量guess,当前绑定到一个新的空字符串上。

通过这个示例,我对Rust中::语法调用associated function的用法有了更深的理解。associated function是Rust的一个非常好的设计,可以在类型上实现相关的功能。


3.2.2 接受用户输入
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    io::stdin()
        .read_line(&mut guess)

1. 通过use std::io在程序开头导入io库。(如果我们没有在程序开头通过use std::io导入io库,我们仍可以通过写成std::io::stdin来使用这个函数)
2. 调用io模块的stdin()函数来获取标准输入的句柄。
3. stdin()返回一个Stdin实例,它代表终端标准输入的句柄。
4. 在Stdin上调用read_line方法获取用户输入。
5. 传入&mut guess作为参数,来告诉read_line将用户输入存储在guess字符串中。
6. read_line会将用户输入追加到字符串中,所以需要传入一个可变字符串。(mut)
7. &表示这个参数是引用,可以安全地在代码中共享数据。
8. 引用默认是不可变的,所以需要&mut guess来使其可变。
9. 引用是Rust的重要优势之一,可以安全地在代码中共享数据。


3.2.3 处理程序可能出现的错误
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    .expect("Failed to read line");

它其实可以和上面一部分连在一起

::

    io::stdin().read_line(&mut guess).expect("Failed to read line");

代码示例很好地解释了Result和expect的用法。让我来概括一下:

1. 从逻辑上这是同一行代码,只是为了阅读方便分成多行。
2. read_line后调用expect方法处理可能的错误。
3. expect的字符串参数是读取失败时的错误信息。
4. 可以把这一行写成一行,但会难以阅读,所以最好分成多行。
5. 当用.method_name()语法调用方法时,使用换行和空白来分割长行会更易读。
6. expect方法来自Result类型,可以处理read_line可能返回的错误。

Rust 会警告你没有使用 read_line 返回的 Result 值,这表示程序没有处理可能的错误。

需要使用 Result 值的原因是:

read_line 这个函数在读取用户输入时,有可能会 occur 错误,比如文件结束或读取超时等。为了体现这个不确定性,它不会直接返回字符串,而是返回一个 Result。

Result 是一个枚举,它有两个变体:Ok 和 Err。当成功读取到用户输入时,它会是 Ok 变体,并包含字符串;如果发生错误,它会是 Err 变体,并包含错误信息。

所以 read_line 的返回值就是一个代表可能成功也可能失败的 Result。如果不去处理这个 Result,就相当于忽略了可能的错误情况。

Rust 做了这个设计是为了鼓励开发者去显式处理错误,这样可以编写出更加健壮的程序。

所以调用 read_line 后需要对其 Result 返回值进行处理:

- 要么使用`match`去处理`Ok`和`Err`两种情况
- 要么使用`unwrap`或`expect`来获取`Ok`中的值,如果是`Err`就panic
- 要么使用`?`操作符在函数中简洁的处理错误

总之,需要处理`Result`是Rust非常重要的错误处理机制,可以避免很多错误被忽略。

.. warning::
    您提到的使用expect来压制警告的方法虽然可以使程序快速crash掉,但并不是处理错误的正确方式。
    压制警告的正确方式是编写错误处理代码,在第9章中将会学习错误恢复。
    虽然在我们的例子中,可能只是想在出现问题时让程序快速crash,可以使用expect。
    但是在实际项目中,我们还是应该适当处理错误,而不是简单的崩溃程序。
    正确处理错误的方法有:

    - 使用match语句针对Ok和Err情况进行处理
    - 将错误传播给上层调用者处理
    - 提供默认的失败处理,让程序可以优雅的处理错误
    - 记录错误信息,以便debug
    - 显示错误信息给用户
    - 重试操作

3.2.4 用 println! 打印占位符
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    println!("You guessed: {guess}");

{}, 调用之前的变量

例如：

::

    let x = 5;
    let y = 10;

    println!("x = {x} and y + 2 = {}", y + 2);

输出:

::

    x = 5 and y + 2 = 12

使用外来模块，Rand
^^^^^^^^^^^^^^^^^^^^^^

在cargo创建的工作区里，如果程序要求使用不是标准库里的库时，也就是crate,直接在main.rc里调用会出问题

但是可以在Cargo.toml,文件里的[dependencies]区域下面设置需要的模块，例如

::

    [dependencies]
    rand = "0.8.5" // 或者是 rand = "^0.8.5" ,意思是0.8.5到0.9.0版本之间

cargo 会从registry,也就是Crates.io下载rand,同时还会下载rand依赖的其他crates

Crates.io 是 Rust 生态系统中的人们发布开源 Rust 项目供他人使用的地方。

Cargo.lock文件
^^^^^^^^^^^^^^^^

用于控制crates的版本，移植项目的时候，就不会出问题

cargo update
^^^^^^^^^^^^^

用于更新crates,使用这个命令会忽略cargo.lock文件的内容，进行更新

前提是要修改Cargo.toml里的版本，然后再进行更新

3.3 rng生成随机数
----------------------

::

    use rand::Rng;

    let secret_number = rand::thread_rng().gen_range(1..=100);

第一行，将 Rng 特性引入作用域

use rand::Rng;：这行代码引入了 rand crate（一个生成随机数的库）中的 Rng trait。这个 trait 提供了生成随机数的方法。


第二行，调用了 rand::thread_rng 函数,调用 gen_range 方法,range范围为1-100,(1..=100)

源码：

::

    use std::io;
    use rand::Rng;

    fn main() {
        println!("Guess the number!");

        let secret_number = rand::thread_rng().gen_range(1..=100);

        println!("The secret number is: {secret_number}");

        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        println!("You guessed: {guess}");
    }

Cargo 查看项目内的crates的描述
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

进入项目文件目录后，输入以下命令将创建个html文件，然后打开浏览器

::

    cargo doc --open

3.4 将猜测与秘密数字进行比较
--------------------------------


从标准库中引入名为 std::cmp::Ordering 的类型,Ordering 类型是一个枚举,具有 Less、Greater 和 Equal 变体,也就是可以来比较数字

use std::cmp::Ordering;：这行代码引入了 std（标准库）中的 cmp 模块的 Ordering 类型。Ordering 是一个枚举，表示比较的结果，它有三个变体：Less、Greater 和 Equal。

::

    use rand::Rng;
    use std::cmp::Ordering;
    use std::io;

    fn main() {
        // --snip--

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => println!("You win!"),
        }
    }


cmp 方法比较两个值，可以在任何可以比较的对象上调用。它需要一个指向你想要比较的任何值的引用：这里是将 guess 与 secret_number 进行比较

match 语句是比较用户猜测的数字（guess）和秘数字（secret_number）的值，并根据比较结果输出相应的信息。


.. note::

    在 Rust 中，=> 符号用于定义 match 表达式中的分支。match 表达式是一种强大的控制流结构，类似于其他编程语言中的 switch 语句。它允许你将一个值与多个模式进行比较，并执行与第一个匹配模式相对应的代码块

这里的 guess.cmp(&secret_number) 调用是一个比较操作，它比较变量 guess 和 secret_number 的值。cmp 方法返回一个 Ordering 枚举的实例，具体取决于 guess 是小于、等于还是大于 secret_number。

如果 guess 小于 secret_number，cmp 方法将返回 Ordering::Less，然后 match 表达式将匹配到第一个分支，并执行 println!("Too small!")，打印出 "Too small!"。

match 表达式会找到第一个匹配的分支，并执行该分支后面的代码，然后退出 match 表达式。如果没有一个分支匹配成功，那么 match 表达式将是一个错误，因为 Rust 要求所有的可能情况都要被覆盖到。

源码:

::

    use rand::Rng;
    use std::cmp::Ordering;
    use std::io;

    fn main() {
        // --snip--

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => println!("You win!"),
        }
    }



但是这个会出现错误，出现错误的原因是 Rust 无法比较字符串和数字类型


基本数值,有符号（signed）和无符号（unsigned）两大类
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 Rust 中，基本数值类型分为有符号（signed）和无符号（unsigned）两大类，并且提供了不同位数（bit width）的选择。这些类型用于确保程序中变量的存储大小和它们能够表示的数值范围。以下是一些基本数值类型的说明：

1. ** i32 ** ：这是 32 位大小的有符号整数类型。"i" 代表 "integer"（整数），而 "32" 表示它占用 32 位的存储空间。有符号整数意味着它可以表示正数、负数以及零。

2. ** u32 ** ：这是 32 位大小的无符号整数类型。"u" 代表 "unsigned"（无符号），意味着它只能表示非负整数，即从 0 到其最大值（2^32 - 1）。

3. ** i64 ** ：这是 64 位大小的有符号整数类型，可以存储更大的整数范围，从 -2^63 到 2^63-1。

Rust 提供了其他位数的整数类型，如 `i8`、`u8`（8 位）、`i16`、`u16`（16 位）、`i128`、`u128`（128 位），以及 `isize` 和 `usize`，它们的大小取决于目标平台的指针宽度（32 位或 64 位）。

当提到 "除非另有说明，否则 Rust 默认使用 i32"，这通常是指在没有明确指定类型的情况下，Rust 会使用 `i32` 作为整数字面量（literal）的类型。例如：

::

    let x = 42; // x 的类型是 i32

在这个例子中，没有指定 `x` 的类型，Rust 编译器根据上下文推断出 `x` 是一个 `i32` 类型的值。

选择正确的整数类型对于性能和内存使用都是重要的。例如，如果你知道一个变量永远不会是负数，使用无符号整数类型（如 `u32`）可以节省内存，并可能提高性能，因为无符号整数的运算在某些情况下会更简单。

此外，选择合适大小的整数类型也很重要。对于只需要表示较小数值的变量，使用 `i8` 或 `i16` 可以减少内存的使用。然而，对于可能表示非常大范围数值的变量，使用 `i64` 或 `i128` 可能更合适。在处理指针或数组索引时，`isize` 和 `usize` 是常用的，因为它们的大小与平台的指针大小相匹配。


修改整数类型
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

在 Rust 中，你可以通过以下几种方式改变默认的整数类型：

1. ** 显式类型声明 ** ：你可以在变量声明时明确指定其类型。

::

    let x: u32 = 42; // 显式声明 x 为 u32 类型

2. ** 类型推断 ** ：在某些情况下，即使没有显式指定类型，编译器也可以根据变量的上下文来推断其类型。

::

    let y = SomeU32Value; // 如果 SomeU32Value 是 u32 类型，y 也会被推断为 u32

3. ** 类型转换 ** ：你可以使用类型转换函数，如 `to_i32`、`to_u32`、`to_i64` 等，将一个数值转换为特定的类型。

::

    let a: i32 = 42;
    let b: u32 = a as u32; // 将 i32 类型的 a 转换为 u32 类型的 b

4. ** 字面量后缀 ** ：在字面量后面添加后缀可以指定其类型。

::

    let x = 42_i32;  // 使用 _i32 后缀明确表示 x 是 i32 类型
    let y = 42_u32;  // 使用 _u32 后缀明确表示 y 是 u32 类型

5. ** 表达式类型推断 ** ：在表达式中，编译器会根据表达式的上下文来推断类型。

::

    let z = (42 + 2) * 3; // z 的类型由表达式的结果推断得出

6. ** 函数参数和返回类型 ** ：在定义函数时，可以指定参数和返回值的类型。

::

    fn add(a: i32, b: i32) -> i32 {
        a + b
    }

7. ** 宏使用 ** ：在使用宏时，可以指定参数的类型。

::

    let arr: [i32; 10] = [0; 10]; // 使用宏定义一个 i32 类型的数组

8. ** trait 约束 ** ：在使用 trait 时，可以指定类型参数的类型。

::

    fn foo<T: std::fmt::Display>(x: T) {
        println!("{}", x);
    }

9. ** 结构体和枚举定义 ** ：在定义结构体或枚举时，可以为其中的字段指定类型。

::

    struct Point {
        x: i32,
        y: i32,
    }

通过这些方法，你可以控制变量、参数、返回类型等的类型，而不是依赖 Rust 的默认类型推断。这在编写明确、可读性高的代码时非常重要，尤其是在涉及到多种不同类型或跨模块交互时。


将字符串转换为数字
^^^^^^^^^^^^^^^^^^^^^

源码:

::

    // --snip--

    let mut guess = String::new();

    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    let guess: u32 = guess.trim().parse().expect("Please type a number!"); // 加入这条

    println!("You guessed: {guess}");

    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }

将之前的guess的值转换为无符号32位数字

trim() 方法移除字符串两端的空白字符（包括空格、制表符、换行符等）

parse() 方法尝试将字符串解析为指定的类型，这里就是 u32,如果字符串能够成功解析为一个 u32，那么 parse() 将返回 Ok(value)，其中 value 是解析后的 u32 值；如果字符串包含非数字字符或为空，则返回 Err。

expect() 方法用于处理 Result 类型，它接受一个参数，这个参数是一个字符串，当 Result 是 Err 时将被用作错误信息,Ok,就返回原来的数值

::

    let guess: u32 = guess.trim().parse().expect("Please type a number!");

在这里，我们用它将字符串转换为数字。我们需要使用 let guess: u32 告诉 Rust 我们想要的确切数字类型。guess 后面的冒号（:）告诉 Rust 我们将注解变量的类型

3.5 通过循环允许多次猜测
--------------------------

::

    loop {

    }

源码:

::

        // --snip--

        println!("The secret number is: {secret_number}");

        loop {
            println!("Please input your guess.");

            // --snip--

            match guess.cmp(&secret_number) {
                Ordering::Less => println!("Too small!"),
                Ordering::Greater => println!("Too big!"),
                Ordering::Equal => println!("You win!"),
            }
        }
    }

把loop{}放在合适的位置





3.6 猜对后退出
--------------------------

源码：

::

            // --snip--

            match guess.cmp(&secret_number) {
                Ordering::Less => println!("Too small!"),
                Ordering::Greater => println!("Too big!"),
                Ordering::Equal => {
                    println!("You win!");
                    break;
                }
            }
        }
    }


match 语法可以这样使用

3.7 处理无效输入
------------------

如果没有这个处理，当问你要个数字时，你输入个'k'或者其他的不是数字的，这个程序就自己退出了，所以要这个处理

源码:

::

        // --snip--

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");

        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        // --snip--

使用 match 表达式处理 Result 类型,就是把.expect("ERROR"),变成match ... {Ok(num) => num, Err(_) => continue},更好控制错误输出

** 解释 **

由于 parse() 方法返回一个 Result<u32, ParseIntError> 类型，它可能是 Ok(num)（如果解析成功）或 Err(e)（如果解析失败）。使用 match 表达式来匹配这两种情况：

- Ok(num) => num：如果 parse() 成功，Ok(num) 将与第一个模式匹配，match 表达式将返回 num，这是解析后的数字，它将被用来更新 guess 变量的值。

- Err(_) => continue：如果 parse() 失败，Err(_) 将与第二个模式匹配。这里使用下划线 _ 作为通配符模式，表示匹配所有错误情况，而不考虑错误的具体内容。在这种情况下，执行 continue 语句，这会导致程序跳过当前循环的剩余部分，并开始下一次循环迭代，从而请求用户再次输入。

** Ok(num) => num; 解释 **

num 是在模式中定义的变量名，它只在 match 表达式的当前分支中有效。如果你想要在 Ok 分支中使用不同的变量名，你完全可以这样做，只是你需要在模式中以及使用该变量时保持一致：

::

    Ok(Fuck) => Fuck;

完整源代码
------------

::

    use rand::Rng;
    use std::cmp::Ordering;
    use std::io;

    fn main() {
        println!("Guess the number!");

        let secret_number = rand::thread_rng().gen_range(1..=100);

        loop {
            println!("Please input your guess.");

            let mut guess = String::new();

            io::stdin()
                .read_line(&mut guess)
                .expect("Failed to read line");

            let guess: u32 = match guess.trim().parse() {
                Ok(num) => num,
                Err(_) => continue,
            };

            println!("You guessed: {guess}");

            match guess.cmp(&secret_number) {
                Ordering::Less => println!("Too small!"),
                Ordering::Greater => println!("Too big!"),
                Ordering::Equal => {
                    println!("You win!");
                    break;
                }
            }
        }
    }

Rust 关键字
=============

- as：用于类型转换，也可以用来消除歧义，即当有多个可能的 trait 包含同名项时，指定使用哪一个。
- async：将一个函数或闭包标记为异步操作，它将返回一个 Future 对象，而不是阻塞当前线程。
- await：用于暂停当前 async 函数的执行，直到某个 Future 对象准备就绪。
- break：立即退出最近的 loop（循环）。
- const：定义一个常量，常量的值在编译时就已经确定。
- continue：跳过当前循环的剩余部分，并开始下一次循环迭代。
- crate：在模块路径中，指向当前项目的根模块。
- dyn：用于创建动态分派的 trait 对象。
- else：在 if 或 if let 控制流结构中，作为备选分支。
- enum：定义枚举类型，枚举是一种特殊的类型，可以是多种预设值之一。
- extern：声明外部函数或变量，通常用于与 C 语言交互。
- false：布尔假值字面量。
- fn：定义一个函数或函数指针类型。
- for：遍历迭代器中的项，实现 trait，或指定一个高等级生命周期。
- if：根据条件表达式的结果进行分支选择。
- impl：实现特定类型的固有方法或 trait 方法。
- in：是 for 循环语法的一部分。
- let：绑定一个变量。
- loop：无条件地无限循环。
- match：将一个值与多个模式进行匹配。
- mod：定义一个模块。
- move：使闭包获取它所有捕获的值的所有权。
- mut：表示可变性，用于引用、裸指针或模式绑定。
- pub：表示公共可见性，用于结构体字段、实现块或模块。
- ref：通过引用进行绑定。
- return：从函数返回。
- Self：在定义或实现中，表示当前类型。
- self：方法的主体或当前模块。
- static：定义一个全局变量或一个持续整个程序执行的生命周期。
- struct：定义一个结构体。
- super：当前模块的父模块。
- trait：定义一个 trait，trait 是一种特殊的类型，用于为其他类型定义能力。
- true：布尔真值字面量。
- type：定义一个类型别名或关联类型。
- union：定义一个联合体，它是一种特殊的类型，其中所有字段共享相同的内存位置。
- unsafe：表示不安全的代码、函数、特性或实现。
- use：将符号引入当前作用域。
- where：用于指定类型约束的子句。
- while：根据表达式的结果有条件地进行循环。


变量和可变性
==============

不可变变量,定义变量时，默认变量

::

    let x = 1;

    x = 2;

    // ERROR,不能修改不可变变量

可变变量,变量名前加mut

::

    let mut x = 1;

    x = 2;

    // 可以修改x 为 2

常量
--------

Rust 的常量命名规则是使用全大写字母，字与字之间使用下划线

::

    const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;


常量不能修改，不能加mut

常量在程序运行的整个过程中都在其声明的范围内有效

变量遮蔽
----------

在Rust中，变量遮蔽（Shadowing）是一种特性，允许你使用相同的变量名来声明一个新的变量，这个新变量会遮蔽（shadow）之前声明的同名变量。这意味着在当前作用域内，同名的新变量会覆盖旧的变量。

在你的示例代码中：

::

    fn main() {
        let x = 5; // 第一个x的声明

        let x = x + 1; // 使用let关键字重新声明x，这会遮蔽第一个x，新的x的值是第一个x的值加1

        {
            let x = x * 2; // 在这个新的作用域内，再次使用let关键字声明x，这个x会遮蔽外层的x
            println!("The value of x in the inner scope is: {}", x); // 这里的x是内层作用域的x，值为 (5 + 1) * 2 = 12
        }

        println!("The value of x is: {}", x); // 这里的x是外层作用域的x，其值是5 + 1 = 6
    }

这段代码的输出将会是：

::

    The value of x in the inner scope is: 12
    The value of x is: 6

这里的关键点是：

- 第一个let x = 5;声明了一个变量x。
- 第二个let x = x + 1;声明了一个新的变量x，它遮蔽了第一个x。这个新的x的值是第一个x的值加1。
- 在花括号{}内的作用域中，第三个let x = x * 2;声明了另一个新的变量x，它遮蔽了外层作用域中的x。这个新的x的值是外层作用域中x的值乘以2。
- 当内层作用域结束时，内层的x不再存在，外层的x仍然有效，其值为6。

实际上，第二个变量会覆盖第一个变量，将变量名的任何使用都带到自己身上，直到它自己被阴影覆盖或作用域结束

这种遮蔽机制在Rust中是完全合法的，并且经常被用于需要重新使用变量名以简化代码的情况。然而，它与变量的可变性（mutability）是两个不同的概念。可变性指的是变量的值是否可以改变，而遮蔽则是在相同作用域内使用相同的变量名来创建一个新的变量。

例子:

::

    let spaces = "   ";
    let spaces = spaces.len();

例如，我们的程序要求用户通过输入空格字符来显示他们希望在某些文本之间输入多少个空格，然后我们希望将输入值存储为一个数字：

这样就只要一个变量名就ok了，不用什么spaces_num或者spaces_str

::

    let mut spaces = "   ";
    spaces = spaces.len();

不能用mut这种方法

数据类型
==========

Rust 中的每个值都有特定的数据类型

标量
-----

标量类型表示单个值。Rust 有四种主要的标量类型：整数、浮点数、布尔型和字符型

整数类型
^^^^^^^^^^

整数是没有小数成分的数字

Rust 默认定义整数类型是 *i32*

使用.parse(),结合以下的整数类型

(显式定义)

- 8-bit	    i8	    u8
- 16-bit	i16	    u16
- 32-bit	i32	    u32
- 64-bit	i64	    u64
- 128-bit	i128	u128
- arch	    isize	usize

::

    let guess: u32 = "42".parse().expect("Not a number!");

isize 和 usize 类型取决于程序运行的计算机体系结构，表中用 "arch "表示：如果是 64 位架构，则为 64 位；如果是 32 位架构，则为 32 位。

可以使用以下所示的任何形式编写整数字面量。需要注意的是，可以是多种数字类型的数字字面量允许使用类型后缀（如 57u8）来指定类型。数字字面量还可以使用 _ 作为视觉分隔符，使数字更容易读取，例如 1_000，其值与指定的 1000 相同。

(隐式定义）

- Decimal           98_222
- Hex               0xff
- Octal             0o77
- Binary            0b1111_0000
- Byte (u8 only)	b'A'


浮点类型
---------

Rust 的浮点类型:

- 32-bit      f32
- 64-bit      f64

默认类型是 f64，因为在现代 CPU 上，它的速度与 f32 大致相同，但精度更高。所有浮点类型都是带符号的。

::

    fn main() {
        let x = 2.0; // f64

        let y: f32 = 3.0; // f32
    }

f32 类型是单精度浮点数，f64 是双精度浮点数。

数字运算
----------

Rust 支持所有数字类型的基本数学运算：加法、减法、乘法、除法和余数

在定义变量时,可以进行数学运算

::

    fn main() {
        // addition
        let sum = 5 + 10;

        // subtraction
        let difference = 95.5 - 4.3;

        // multiplication
        let product = 4 * 30;

        // division
        let quotient = 56.7 / 32.2;
        let truncated = -5 / 3; // Results in -1

        // remainder
        let remainder = 43 % 5;
    }

逻辑运算符
^^^^^^^^^^^^^^^^^^^^

-     !：逻辑非，用于取反一个布尔值。
-     &&：逻辑与，用于短路逻辑与操作。
-     ||：逻辑或，用于短路逻辑或操作。

比较运算符
^^^^^^^^^^^^^^^^^^^^

-     ==：等于，用于比较两个值是否相等。
-     !=：不等于，用于比较两个值是否不相等。
-     <：小于，用于比较两个值的大小。
-     <=：小于或等于，用于比较两个值的大小。
-     >：大于，用于比较两个值的大小。
-     >=：大于或等于，用于比较两个值的大小。

位运算符
^^^^^^^^^^^^^^^^^^^^

-     &：按位与，用于对两个数的位进行逻辑与操作。
-     \|：按位或，用于对两个数的位进行逻辑或操作。
-     ^：按位异或，用于对两个数的位进行逻辑异或操作。
-     !：按位非，用于对一个数的位进行逻辑非操作（注意：与逻辑非运算符 ! 的使用场合不同）。
-     <<：左移，将一个数的位向左移动指定的位数。
-     >>：右移，将一个数的位向右移动指定的位数。

算术运算符
^^^^^^^^^^^^^^^^^^^^

-     +：加法，用于计算两个数值的和。
-     -：减法，用于计算两个数值的差。
-     \*：乘法，用于计算两个数值的乘积。
-     /：除法，用于计算两个数值的商。
-     %：取模，用于计算两个数值相除后的余数。

赋值运算符
^^^^^^^^^^^^^^^^^^^^

-     =：赋值，将右侧的值赋给左侧的变量。
-     +=：加法赋值，将左侧变量与右侧表达式相加的结果赋给左侧变量。
-     -=：减法赋值，将左侧变量与右侧表达式相减的结果赋给左侧变量。
-     \*=：乘法赋值，将左侧变量与右侧表达式相乘的结果赋给左侧变量。
-     /=：除法赋值，将左侧变量与右侧表达式相除的结果赋给左侧变量。
-     %=：取模赋值，将左侧变量与右侧表达式取模的结果赋给左侧变量。
-     &=：按位与赋值。
-     \|=：按位或赋值。
-     ^=：按位异或赋值。
-     <<=：左移赋值。
-     >>=：右移赋值。

其他运算符
^^^^^^^^^^^^^^^^^^^^

-     .：点，用于访问结构体或枚举的成员。
-     ->：箭头，用于指定函数或闭包的返回类型，或者用于解引用智能指针访问其内部的值。
-     :：冒号，用于类型约束、结构体字段初始化或循环标签。
-     ;：分号，用于终止语句或项。
-     ,：逗号，用于分隔函数参数或元组中的元素。
-     ?：错误传播，用于将错误传递到上一层代码。

布尔类型
---------

Rust 中的布尔类型有两种可能的值：true 和 false。

布尔值的大小为一个字节。

Rust 中的布尔类型使用 bool 指定

::

    fn main() {
        let t = true;

        let f: bool = false; // 具有显式类型注释with explicit type annotation
    }

字符类型
----------

Rust 的 char 类型是该语言最原始的字母类型

::

    fn main() {
        let c = 'z';
        let z: char = 'ℤ'; // with explicit type annotation
        let heart_eyed_cat = '😻';
    }


