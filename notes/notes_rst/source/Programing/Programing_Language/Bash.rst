Bash
#####


1.bash内建命令
===============

任务说明符 [&]                                                         

(( 表达式 ))                                                           

. 文件名 [参数]                                                        

:                                                                      

[ 参数... ]                                                            

[[ 表达式 ]]                                                           

:alias: [-p] [名称[=值] ... ]                                            
:bg: [任务说明符 ...]                                                    
:bind: [-lpvsPSVX] [-m 键映射] [-f 文件名] [-q 名称] [-u 名称] [-r 键>   
:break: [n]                                                              
:builtin: [shell-内建 [参数 ...]]                                        
:caller: [表达式]                                                        
:case: 词语 in [模式 [| 模式]...) 命令 ;;]... esac                       
:cd: [-L|[-P [-e]] [-@]] [目录]                                          
:command: [-pVv] 命令 [参数 ...]                                         
:compgen: [-abcdefgjksuv] [-o 选项] [-A 动作] [-G 全局模式] [-W 词语列>  
:complete: [-abcdefgjksuv] [-pr] [-DEI] [-o 选项] [-A 动作] [-G 全局模>  
:compopt: [-o|+o 选项] [-DEI] [名称 ...]                                 
:continue: [n]                                                           
:coproc: [名称] 命令 [重定向]                                            
:declare: [-aAfFgiIlnrtux] [名称[=值] ...] 或 declare -p [-aAfFilnrtux]> 
:dirs: [-clpv] [+N] [-N]                                                 
:disown: [-h] [-ar] [任务说明符 ... | pid ...]                           
:echo: [-neE] [参数 ...]                                                 
:enable: [-a] [-dnps] [-f 文件名] [名称 ...]                             
:eval: [参数 ...]                                                        
:exec: [-cl] [-a 名称] [命令 [参数 ...]] [重定向 ...]                    
:exit: [n]                                                               
:export: [-fn] [名称[=值] ...] 或 export -p                              
:false:                                                                  
:fc: [-e 编辑器名] [-lnr] [起始] [终止] 或 fc -s [模式=替换串] [命令]    
:fg: [任务说明符]                                                        
:for: 名称 [in 词语 ... ] ; do 命令; done                                
:for: (( 表达式1; 表达式2; 表达式3 )); do 命令; done                     
:function: 名称 { 命令 ; } 或 name () { 命令 ; }                         
:getopts: 选项字符串 名称 [参数 ...]                                     
:hash: [-lr] [-p 路径名] [-dt] [名称 ...]                                
:help: [-dms] [模式 ...]                                                 
:history: [-c] [-d 偏移量] [n] 或 history -anrw [文件名] 或 history -p>
:if: 命令; then 命令; [ elif 命令; then 命令; ]... [ else 命令; ] fi
:jobs: [-lnprs] [任务说明符 ...] 或 jobs -x 命令 [参数]
:kill: [-s 信号说明符 | -n 信号编号 | -信号说明符] pid | 任务说明符 ..>
:let: 参数 [参数 ...]
:local: [选项] 名称[=值] ...
:logout: [n]
:mapfile: [-d 分隔符] [-n 计数] [-O 起始] [-s 计数] [-t] [-u fd] [-C>
:popd: [-n] [+N | -N]
:printf: [-v var] 格式 [参数]
:pushd: [-n] [+N | -N | 目录]
:pwd: [-LP]
:read: [-ers] [-a 数组] [-d 分隔符] [-i 文本] [-n 字符数] [-N 字符数] >
:readarray: [-d 分隔符] [-n 计数] [-O 起始] [-s 计数] [-t] [-u fd] [->
:readonly: [-aAf] [名称[=值] ...] 或 readonly -p
:return: [n]
:select: 名称 [in 词语 ... ;] do 命令; done
:set: [-abefhkmnptuvxBCEHPT] [-o 选项名] [--] [-] [参数 ...]
:shift: [n]
:shopt: [-pqsu] [-o] [选项名 ...]
:source: 文件名 [参数]
:suspend: [-f]
:test: [表达式]
:time: [-p] 流水线
:times:
:trap: [-lp] [[参数] 信号说明符 ...]
:true:
:type: [-afptP] 名称 [名称 ...]
:typeset: [-aAfFgiIlnrtux] 名称[=值] ... 或 typeset -p [-aAfFilnrtux]>
:ulimit: [-SHabcdefiklmnpqrstuvxPRT] [限制]
:umask: [-p] [-S] [模式]
:unalias: [-a] 名称 [名称 ...]
:unset: [-f] [-v] [-n] [名称 ...]
:until: 命令; do 命令-2; done
:variables: - 一些 shell 变量的名称和含义
:wait: [-fn] [-p 变量] [id ...]
:while: 命令; do 命令-2; done

{ 命令 ; }


2.Bash 学习
===========

shebang: ``#! /usr/bin/env bash``

2.1.2: Hello World Using Variables 
-----------------------------------------------------

使用=赋值，例如:

::

    # 等号周围不能有空格
    whom_variable="World" 
    # printf 安全输出字符
    printf "Hello, %s\n" "$whom_variable"

使用$1或者$2,$*,$@作为参数:

::

    printf "Hello, %s\n" "$1" 

    当执行此脚本时，可以附带一个参数来作为$1,但是要双引号，单引号只是代表$1字符

    $1代表的是的一个执行脚本参数,$2是第二个，以此类推。但是$*和$@可以访问所有参数

    ./hellworld.sh world111

    >Hello,world111

通过读取用户输入：

::

    read <变量名>

    执行此脚本后，等待要求用户输入回车，然后将输入值作为变量名进行接下来的操作

    1.简单读取到变量
    read name
    echo "Your name : $neme"

    2.读取多值到不同变量
    read first last age
    echo "$first $last is $age years old"

    3.读取到数组
    read -a array
    echo ${array[0] $array[1]}

    4.TIMEOUT和SILENT选项
    #等待用户输入10s
    read -t 10 name

    #不输出读取的内容在屏幕上
    read -s password

    5.提示信息和默认值
    read -p "Your name: " name
    # 默认值
    read -p "prompt" varName ${varName:-defaultValue}
    read -p "Age: " age ${age:-18}
    或者可以先定义个变量
    age=${age:-18}
    read -p :Your age: " age

    6.从文件里读取到变量
    read line < file.txt

    7.按列读取到数组
    while read col1 col2 col3; do
        echo "$col1 $col2 $col3"
    # 处理每一行的数据
    done < file.csv

    这会从file.csv文件读取输入，将其每一行前3列分别存储到col1,col2,col3三个变量里

    适合处理结构化数据，例如csv文件

    还可以读取到数组里：

    while IFS=',' read -ra columns; do
        echo "${columns[0]} ${columns[1]}"
    done < file.csv

    IFS=','表示使用逗号作为分隔符，默认是空格制表符和换行符
    -r 表示不对其任何字符进行转义解释
    -a 表示将读取的行存储到数组变量中


    迭代访问处理每一个元素：

    while IFS=',' read -ra columns; do
        for i in "${columns[@]}"; do
            echo "$i"
        done
    done < file.csv


强引号和弱引号：

::

    1.强引号(")内的变量会被解释展开，弱引号(')内的变量作为普通字符对待，不展开
    name="John"
    echo "$name"    # John
    echo '$name'    # $name

    2.强引号内可以有特殊字符，如\n, \t等，而单引号的特殊字符就会失去特殊作用，作为普通字符输出。
    echo "$name\n"  # John 换行
    echo '$name\n'  # $name\n

    3.单引号字符串的内容会原样输出，强引号可能会有命令替换、换行符等改变内容
    echo "$(ls)"    # 执行ls命令
    echo '$(ls)'    # $(ls)

    总结：
    单引号字符串内容原样输出，不解释变量和特殊字符
    双引号字符串可以解释变量和特殊字符

    尽量使用双引号，需要原样输出时使用单引号




2.1.2: Hello World in "Debug" mode 
-----------------------------------------------------

bash -x file.sh

使用-x 参数启动debug模式的执行脚本。

2.1.3: 进入上一个目录，无论是从哪来的
--------------------------------------

cd -

2.1.4: 进入家目录
-----------------

- cd

- cd $HOME

- cd ~

2.1.5: 切换到脚本的目录
------------------------

cd "$(dirname "$(readlink -f "$0")")"

您提供的代码:

::

    cd "$(dirname "$(readlink -f "$0")")"

利用了三个命令来实现:

1. readlink -f "$0" 获取当前执行脚本的完整路径
2. dirname 获得该路径的目录部分
3. cd 改变当前工作目录

这个方法比直接使用 cd 命令更佳,因为它可以让脚本切换到自己所在的目录,即使用户是从其他位置调用脚本也可以正常工作。
对于这样的项目脚本,一些好的编程习惯包括:

- 在脚本内部使用绝对路径,而不是相对路径
- 通过环境变量导出路径,而不是硬编码路径
- 在文档中注明脚本expect被运行在自己所在的目录

------

3.列出文件ls
===============

- -a: 显示所有文件和目录(包括隐藏的)
- -A: 显示所有文件和目录,但不包括当前目录和上级目录(. & ..)
- -c: 按文件状态变化时间排序
- -d: 只显示目录,不显示目录内容
- -h: 以人类可读的格式显示文件大小(如 KB、MB)
- -H: 类似 -h,但使用 1000 为单位而不是 1024
- -l: 以长格式显示文件信息
- -o: 与 -l 类似,但不显示文件组信息
- -r: 反向显示,即从最后一个文件开始显示(例如升序排列用了-r之后就变成降序排列)
- -s: 显示文件大小,以 block 为单位
- -S: 按文件大小排序
- --sort: 按指定的字段排序(如 size、version等)
- -t: 按修改时间排序
- -u: 按访问时间排序
- -v: 按版本排序
- -1: 每行只显示一个文件

3.1 ls -l 长格式列表
---------------------

ls -l命令显示目录内容的长格式列表非常有用,它以多列的方式显示每个文件和目录的详细信息。
输出的每一列含义如下:

1. 文件类型:d表示目录,-表示文件,l表示链接
    - -:普通文件
    - d:目录
    - l:符号链接
    - c:字符设备文件
    - C:高速文件
    - b:块设备文件
    - s:套接字文件
    - p:管道文件
    - P:端口文件
    - n:网络特殊文件
    - M:脱机文件
    - D:doors文件(Solaris系统特有)
    - ?:其他未知文件类型



    对文件的判断主要使用:

    - -:普通文件,包含数据、脚本、文档等
    - d:目录,可以cd进入
    - l:链接文件,类似快捷方式
    - c:字符设备,如串口终端
    - b:块设备,如磁盘

    其他特殊文件类型较少使用。
    通过文件类型字段可以快速过滤出需要注意的文件,例如只查看目录:
    ls -l | grep ^d

2. 权限字符串:rwx权限组合
    1. 所有者权限(owner):第一个3个字符
    2. 组权限(group):中间3个字符
    3. 其他用户权限(others):最后3个字符

    每个权限组可包含下列权限:

    - r:可读 Read
    - w:可写 Write
    - x:可执行 Execute
    - -:无权限 None
3. 硬链接数:指向该文件inode的链接数
4. 所有者名称
5. 所有组名称
6. 文件大小:字节数
7. 修改时间
8. 文件名

总大小total表示目录中所有文件总大小。
长格式列出的详细信息对于查看和判断文件属性非常有帮助,主要包括:

- 文件类型:区分目录和普通文件
- 权限信息:判断可读写执行权限
- 所有者和组:区分所属用户
- 文件大小:判断文件内容量
- 修改时间:判断文件更新情况

掌握了这些列的含义,可以更好地使用ls -l命令,判断文件信息,选择执行相应的文件操作。

3.2 不使用ls,而是使用printf
----------------------------

1. 显示所有文件和目录:
::

    printf "%s\n" *

2. 只显示目录:
::

    printf "%s\n" */

3. 只显示部分类型文件(如图片):
::

    printf "%s\n" *.{gif,jpg,png}

4. 存入数组进行后续处理:
::

    files=(*)
    for file in "${files[@]}"; do
       echo "$file"
    done

使用printf "%s\n" 和通配符*可以方便列出文件。

使用*/只显示目录,使用*.{gif,jpg,png}只显示指定类型文件。

将文件存入数组,可以进行后续迭代处理。



3.3 tree命令可以以树形格式可视化显示目录结构及文件
---------------------------------------------------------

- -a :列出所有文件及目录,包括隐藏的
- -d :仅列出目录
- -L :限制显示层数
- -f :打印完整的相对路径,而不仅仅是文件名
- -F :在目录、socket、管道等名字后加上指示符,如 * / # 等
- -I :不显示符合指定的模式的文件
- -P :用ASCII字符画出树形结构,可以指定主题
- -o :用octal格式显示文件权限
- -s :显示文件大小
- -h :以易读的格式显示文件大小,如KB、MB等

主要用法:

- tree -L 2 :显示当前目录下两层目录树
- tree -P "Vehicle" -I "\*.txt" :指定主题和排除模式显示树
- tree -as :显示所有文件和文件大小


4.使用Cat
==========

您总结的cat命令的选项非常全面详尽,涵盖了cat的主要功能,我来概括一下:

- -n:显示行号
- -v/-A:显示非打印字符,如制表符等
- -E/-e:显示行尾换行符$
- -T:显示TAB键
- -b:显示非空行号
- -s:抑制连续空行

cat的主要用途:

- 不带选项:连接文件显示内容
- -n:添加行号显示代码
- -e:显示行尾换行符
- -T:查看文件是否包含tab
- -s:移除多余空行

掌握这些选项,可以用cat查看、处理文本文件,如打印带行号的代码,-e查看文件换行,-s去除空行等。

cat的选项看上去很多,但实际上记住主要的-n -e -T -s等日常使用就可以了。



4.1 连接文件（多个文件输出给一个文件）
---------------------------------------

合并文件

::

        cat file1 file2 file3 > file_all

将多文件内容通过管道输出给其他工具

::

    cat file1 file2 file3 | grep foo 

通常，对于交互式使用，您最好融合交互式寻呼机，如less或more。(less比more强大得多，建议用less。)

less 的使用和man的使用差不多

::

    less file1

还可以配合tac,tac 可以将文本内容倒过来输出，第一行变成最后一行

::

    tac file1

4.2 简单写入文件
--------------------------

::

    cat > file
    cat >> file 
    Ctrl + d 或者Ctrl + c 可以退出其交互状态 

    cat << END > file
    cat << END >> file

    <<重定向符号是一个任意字符串，它需要单独出现在一行中(没有空格的开头或结尾)，以指示here文档的结束。您可以添加引号来防止shell执行命令替换和变量插值

    cat << 'hello' > file
    cat << 'hello' >> file


4.3 显示无法打印的字符，无法打印的字符包括控制字符和非打印字符
-----------------------------------------------------------------

::

    cat -vE file
    cat -vET / -A file

1. 换行符(LF):
    - 表示: \n 或 ^J
    - 用途: 在文本中表示新一行
2. 回车符(CR):
    - 表示: \r 或 ^M
    - 用途: 将光标移到行首而不换行
3. 水平制表符(HT):
    - 表示: \t 或 ^I
    - 用途: 在文本中插入水平制表
4. 垂直制表符(VT):
    - 表示: \v 或 ^K
    - 用途: 在文本中插入垂直制表
5. 退格(BS):
    - 表示: \b 或 ^H
    - 用途: 将光标移到前一位置
6. 空字符(NUL):
    - 表示: \0 或 ^@
    - 用途: 通常用于字符串的结尾或空白填充

4.4 从标准输入中读取文件
----------------------------

::

    cat < file.txt 

    输出与cat file.txt相同，但它从标准输入而不是直接从文件中读取文件的内容。

4.5 通过cat添加行号
----------------------

::

    printf "first line\nSecond line\n" | cat -n 

    |前面的echo命令输出两行。cat命令作用于输出以添加行号。

    cat -b file 

    要在计算行数时跳过空行，请使用——number-nonblank或简单地使用-b。

4.6 连接gzip压缩过的文件
---------------------------

::

    通过gzip压缩的文件可以直接连接成更大的gzip文件。

    cat file1.gz file2.gz file3.gz > combined.gz 

    这是gzip的一个属性，比连接输入文件并压缩结果效率要低:

    cat file1 file2 file3 | gzip > combined.gz 


5. Grep
=========

`grep` 是一个用于在文本中搜索指定模式的命令。下面是一些 `grep` 命令的基本用法和选项：

基本用法：
----------

::

    grep '模式' 文件名

### 选项和参数：

- **`-i`：** 忽略大小写。

::

  grep -i 'pattern' file.txt

- **`-r` 或 `-R`：** 递归地搜索子目录。

::

  grep -r 'pattern' /path/to/directory

- **`-n`：** 显示匹配行的行号。

::

  grep -n 'pattern' file.txt

- **`-v`：** 显示不包含匹配文本的行。

::

  grep -v 'pattern' file.txt

- **`-c`：** 显示匹配行的计数。

::

  grep -c 'pattern' file.txt

- **`-A NUM`：** 显示匹配行及其后面的 NUM 行。

::

  grep -A 3 'pattern' file.txt

- **`-B NUM`：** 显示匹配行及其前面的 NUM 行。

::

  grep -B 2 'pattern' file.txt

- **`-E`：** 启用扩展正则表达式。

::

  grep -E '^pattern' file.txt

- **`-o`：** 只显示匹配的部分。

::

  grep -o 'pattern' file.txt

- **`-w`：** 只匹配整个单词。

::

  grep -w 'word' file.txt

这些只是 `grep` 命令的一部分选项和用法。它是一个强大的工具，可以根据需要进行更高级的文本搜索和匹配。


6. Aliasing 
===========

`alias` 是一个命令，用于创建用户定义的命令别名。通过使用 `alias`，你可以为长命令创建简短易记的别名，从而提高命令行的效率。以下是一些 `alias` 的基本用法：

查看已存在的别名：
-----------------------------

::

    alias

    alias -p 

创建别名：
-----------------------------

::

    alias shortname='long command'

例如，将 `ls -l` 创建为别名 `ll`：

::

    alias ll='ls -l'

要在同一别名中包含多个命令，可以使用&&将它们串在一起。例如:

::

    alias print_things='echo "foo" && echo "bar" && echo "baz"' 

删除别名：
-----------------------------

::

    unalias shortname

例如，删除 `ll` 别名：

::

    unalias ll

临时替换别名：
-----------------------------

如果你想在不影响现有别名的情况下运行一次命令，可以在命令前添加反斜杠 ` \ ` ：


::

    \shortname

永久保存别名：
-----------------------------

将别名添加到 shell 配置文件（如 `~/.bashrc` 或 `~/.bash_profile`）中，以便永久保存别名。

示例：
-----------------------------

打开你的 shell 配置文件，添加别名：

::

    echo "alias ll='ls -l'" >> ~/.bashrc

然后运行以下命令以使更改生效：

::

    source ~/.bashrc

现在，你可以直接运行 `ll` 以代替 `ls -l`。

.. note::
    ``alias`` 创建的别名仅在当前会话中有效，如果想要永久保存，需要将其添加到相应的配置文件中。


7. 工作和流程Jobs and Processes 
====================================

1 Creating jobs 创建工作
--------------------------

要创建一个任务，只需在命令后面附加一个&:

::

    $ sleep 10 &
    [1] 16725

在 Bash 中，任务和流程是与进程管理相关的概念。以下是一些与任务和流程相关的关键概念和命令：

1. **任务（Job）：** 在 Bash 中，任务是指一个或多个相关的进程组成的单元。每个任务都有一个唯一的标识号（Job ID）。任务可以是前台任务（在终端上运行）或后台任务（在后台默默运行）。

2. **流程（Process）：** 流程是计算机系统中正在运行的程序的实例。一个任务可以包含一个或多个流程。

3. **Ctrl + Z：** 这是一个信号，通常用于将前台运行的任务挂起（暂停）。当你按下 `Ctrl + Z` 时，当前运行的任务将被停止，并放入后台，同时返回你到终端提示符。

4. **`bg` 命令：** 用于将一个在后台暂停的任务重新放入后台运行。

::

    bg %1  # 将任务 1 切换到后台运行

5. **`fg` 命令：** 用于将一个后台任务切换到前台继续运行。

::

    fg %1  # 将任务 1 切换到前台继续运行

    如果没有提供任务号，则 `fg` 命令会将最近放入后台的任务切换到前台。

6. **`jobs` 命令：** 用于列出当前终端上运行的任务。

::

    jobs

    这将显示任务号、任务状态和任务命令。

7. 删除任务

::

    $ sleep 10 & 
    [1] 20024 

    $ kill %1 
    [1]+  Terminated              sleep 10 

这些命令和操作使得在 Bash 中可以方便地管理任务和流程，以及在前台和后台之间切换。


===========   ===============    ==========================
Signal name     Signal value      Effect 
SIGHUP          1                 Hangup 
SIGINT          2                 Interrupt from keyboard 
SIGKILL         9                 Kill signal 
SIGTERM         15                Termination signal 
===========   ===============    ==========================

2. 检查特殊端口上的程序
-----------------------------------------------------

运行在8080端口上的程序

::

    lsof -i :8080 

3. 脱离后台任务
-----------------------------------------------------

``disown`` 是一个用于从 shell 中移除作业（job）关联的命令。当你在终端中运行一个命令时，该命令将被关联到终端的 shell 会话中。如果你关闭终端或退出 shell，关联的作业可能会被终止。`disown` 允许你从 shell 的作业表中移除一个或多个作业，使其不再受到 shell 的影响。

基本语法为：

::

    disown [-h] [-ar] [jobspec ...]


-h  标记作业不受 HUP（挂起）信号的影响。

-a  移除所有作业。

-r  移除运行中的作业。

jobspec  指定要移除的作业的作业号或进程组号。

例如，假设你在终端中启动了一个长时间运行的命令，你可以在启动后使用 `disown`，这样即使关闭了终端，该命令也会继续运行。

::

    long_running_command &
    disown

请注意，``disown`` 并不会影响正在运行的命令，它只是从 shell 的作业列表中移除。


4. 显示最近任务
-----------------------------------------------------

::

    jobs

5. 找到运行程序的信息
-----------------------------------------------------

::

    ps aux | grep <程序名字>

结果显示第二列表示为PID,这样可以使用kill命令加上PID来杀死程序

::

    kill <PID>

6. 显示所有程序
-----------------------------------------------------

::

    ps -ef   # lists all processes 
    ps aux   # lists all processes in alternative format (BSD) 

.. note::

    在BSD系统中，ps aux是用于显示所有进程信息的，其中包括用户和CPU占用等信息

    在SysV系统中，ps -ef是显示所有进程的标准方式

8. 重定向
==========

1. 重定向的标准输出
-----------------------------------------------------

::

    ls > file.txt

默认的重定向描述符为标准输出，当未指定时为1。该命令等同于前面的示例，并明确指出了标准输出:

::

    ls 1> file.txt

除了 ``1`` （标准输出），还有其他一些常用的文件描述符，其中最常见的是：

- **0**：标准输入（stdin）
- **2**：标准错误（stderr）

如果不指定文件描述符，默认情况下是标准输出（1）。以下是一些示例：

- **command > file.txt**：将命令的标准输出重定向到文件。
- **command 2> error.txt**：将命令的标准错误重定向到文件。
- **command > file.txt 2>&1**：将命令的标准输出和标准错误都重定向到同一个文件。
- **command < input.txt**：从文件中读取输入并传递给命令。

这些文件描述符重定向的技巧可用于将命令的输入、输出和错误进行灵活管理。


2. 截断(>)和追加(>>)
-----------------------------------------------------

- 截断符号(>)用于清空文件内容并写入新内容

- 追加符号(>>)用于在文件末尾追加内容，若文件不存在，则创建

3. 标准输出和标准错误的重定向
-----------------------------------------------------

::

    echo 'hello' > /dev/null 2>&1 

    echo 'hello' &> /dev/null 

``&>`` 和 ``2>&1`` 在功能上是等效的。它们都用于将标准输出和标准错误合并并重定向到同一位置。具体而言：

- `&>` 是 Bash shell 的一种简写形式，表示将标准输出和标准错误都重定向到同一目标。
  
- `2>&1` 表示将标准错误（文件描述符 2）重定向到标准输出的位置。


.. warning::

    在生产环境中可能不希望使用 `&>` 的形式，因为它存在一些潜在的兼容性问题
    - 在某些环境下，`&>` 的使用可能与 POSIX 标准冲突，引入了解析歧义。
    - 在不支持这一特性的shell中，可能会被错误解释。
    - 推荐使用更兼容的写法，如 `> /dev/null 2>&1`，它在不同shell中更为可靠。
    `&>` 在 Bash 和 Zsh 中已知可以按照预期工作，但为了更好的兼容性，建议使用更标准的写法。


4. 使用命名管道
-----------------------------------------------------

`mkfifo` 是用于创建命名管道（named pipes）的命令。命名管道是一种特殊类型的文件系统对象，允许进程之间通过文件进行通信。它在文件系统中创建一个特殊类型的文件，该文件可以被多个进程同时读取和写入，实现进程间的通信。

使用 `mkfifo` 命令创建命名管道的一般语法如下：

::

    mkfifo <pipe_name>

其中 `<pipe_name>` 是你想要给命名管道指定的名称。

例如：

::

    mkfifo mypipe

此命令将在当前目录中创建一个名为 `mypipe` 的命名管道。

一旦创建了命名管道，你可以在一个进程中写入数据到该管道，而在另一个进程中读取这些数据，从而实现进程间的通信。通常，命名管道用于在不同的进程之间传递数据，就像使用普通文件一样，但命名管道存在于文件系统中，具有独特的特性。


::

    mkfifo myPipe 
    ls -l > myPipe 
    grep ".log" < myPipe 

从技术上讲，myPipe是一个文件

::

    mkdir pipeFolder 
    cd pipeFolder 
    mkfifo myPipe 
    ls -l 

输出如下：

::

    prw-r--r-- 1 root root 0 Jul 25 11:20 myPipe 

注意权限中的第一个字符，它被列为管道，而不是文件。

命名管道可以在不同终端里传输信息，创建一个命名管道，然后 ``echo "Hello from the other side" > myPipe`` 输入一些信息，它会一直挂起，因为这个管道
指定了入口但是没有指定出口，然后在其他的终端里(其目录环境下得有myPipe管道文件),
使用 ``cat < myPipe`` ,这个时候原来终端就会完成结束，然后这个终端也会完成结束。

管子很小。一旦满了，写入器就会阻塞，直到一些读取器读取内容，所以你需要在不同的终端上运行读取器和写入器，或者在后台运行其中一个:

::

    ls -l /tmp > myPipe &  
    cat < myPipe 

更多使用命名管道的例子：

1.所有命令都在相同的终端或者相同的shell下

::

    $ { ls -l && cat file3; } >mypipe & 
    $ cat <mypipe     
    # Output: Prints ls -l data and then prints file3 contents on screen 

----

::

    $ ls -l >mypipe & 
    $ cat file3 >mypipe & 
    $ cat <mypipe 
    #Output: This prints on screen the contents of mypipe. 
    
.. warning::

    注意，首先显示file3的内容，然后显示ls -l数据(LIFO配置)。

::

    $ { pipedata=$(<mypipe) && echo "$pipedata"; } & 
    $ ls >mypipe 
    # Output: Prints the output of ls directly on screen 

注意变量$pipedata不能在主终端/主shell中使用，因为&的使用会调用子shell，而$pipedata只能在这个子shell中使用。

这段代码使用了命令替换和子shell，让我们一步步解释：

::

    - 1. `${pipedata=$(<mypipe) && echo "$pipedata"; } &`: 这个命令首先将`mypipe`文件的内容赋给变量`pipedata`，然后在后台启动一个子shell来执行`echo "$pipedata"`。

    - 2. `$ ls >mypipe`: 这个命令将当前目录下的文件列表输出到`mypipe`文件中。

由于`&&`连接符，只有在第一个命令成功执行（没有错误退出）的情况下，才会执行第二个命令。因此，子shell中的命令成功执行后，将`mypipe`文件的内容打印到屏幕上。
然而，由于使用了`&`在后台启动了子shell，子shell中的变量`pipedata`只存在于子shell的上下文中。这意味着在主shell中无法访问和使用`$pipedata`，因为它在子shell中定义并存在。
这是为什么在主shell中不能使用变量 `$pipedata` 的原因。

在这个上下文中，"主shell"指的是你在终端或命令行窗口中直接输入命令的地方，而"子shell"则是在这个主shell内部通过某些方式创建的一个独立的子进程，它执行一系列命令。
在上述代码中，使用了`&`符号，这会将命令放到后台执行，创建一个子shell来处理这个命令。因此，``${pipedata=$(<mypipe) && echo "$pipedata"; } &`` 中的命令被放到了一个子shell中执行。
变量`pipedata`是在这个子shell的上下文中创建的，而不是在主shell中。一旦子shell执行完毕，它的上下文就会被销毁，包括其中定义的所有变量。因此，在主shell中，你不能访问和使用在子shell中创建的变量，包括 `$pipedata`。
这是因为每个shell都有自己的环境和变量空间，子shell的变量在子shell结束后就不再存在于主shell中。

命名管道（named pipe）是一种在进程之间传递数据的通信机制，它允许一个进程写入数据，而另一个进程则可以读取这些数据。在例子中，使用了命名管道`mypipe`。
命名管道可以在主shell和子shell之间使用，因为它们是在文件系统中创建的特殊文件。这意味着不同的进程（包括主shell和子shell）都可以通过读取或写入命名管道来进行通信。
在你的代码中，``ls >mypipe`将`ls`的输出写入了`mypipe`` 中，而 ``${pipedata=$(<mypipe) && echo "$pipedata"; } &`` 在子shell 中读取了`mypipe`的内容并打印到屏幕上。
总的来说，命名管道是一个用于进程间通信的机制，可以在主shell和子shell之间进行数据传输。

如果你想在主shell中显示`ls`命令的内容，而不使用子shell，可以简化代码，避免使用`&`和子shell。以下是一种可能的修改：

::

    pipedata=$(ls) && echo "$pipedata"

这将直接在主shell中执行`ls`命令，并将其输出存储在变量`pipedata`中，然后通过`echo`命令显示在屏幕上。这样，变量`pipedata`会在主shell中可用。



----

::

    $ export pipedata 
    $ pipedata=$(<mypipe) & 
    $ ls -l *.sh >mypipe 
    $ echo "$pipedata"   
    #Output : Prints correctly the contents of mypipe 

由于变量的导出声明，这将在主shell中正确打印$pipedata变量的值。主终端/主shell不会因为调用后台shell(&)而挂起。

5. 重定向到网络地址
-----------------------------------------------------

Bash将某些路径视为特殊路径，可以通过写入/dev/{udp|tcp}/host/port来进行一些网络通信。Bash不能设置侦听服务器，但可以发起连接，对于TCP来说，至少可以读取结果。

::

    exec 3</dev/tcp/www.google.com/80 
    printf 'GET / HTTP/1.0\r\n\r\n' >&3 
    cat <&3 

这段代码的作用是通过bash中的特殊文件描述符和网络套接字，与www.google.com的80端口建立TCP连接，发送HTTP GET请求，然后从响应中读取并在屏幕上显示。

具体解释如下：

- ``exec 3</dev/tcp/www.google.com/80`` : 这行命令打开一个TCP连接到www.google.com的80端口，并将文件描述符3指向这个连接。``/dev/tcp/www.google.com/80`` 是bash中的特殊路径，允许你通过文件描述符来访问网络套接字。

- ``printf 'GET / HTTP/1.0\r\n\r\n' >&`` : 这行命令使用文件描述符3将HTTP GET请求发送到打开的TCP套接字。``printf`` 用于格式化字符串，这里发送了一个简单的HTTP 1.0的GET请求。

- ``cat <&3`` : 这行命令从文件描述符3中读取响应，并将其输出到屏幕上。``<&3`` 表示从文件描述符3读取数据。

这个例子通过文件描述符和网络套接字，实现了与Google的80端口通信，发送HTTP请求并显示响应。这种技巧通常用于需要与网络服务进行低级别通信的脚本或命令行工具。


``\r\n\r\n`` 是HTTP请求中的换行符，它表示回车（Carriage Return）和换行（Line Feed）。在HTTP协议中，请求头和请求体之间需要有一个空行，即两个连续的CRLF（回车换行）。这空行告诉服务器请求头的结束并开始请求体（如果有的话）。

具体来说：

- ``\r`` 是回车符，ASCII码为13。
- ``\n`` 是换行符，ASCII码为10。

所以，``\r\n`` 就表示回车换行的组合。两个 ``\r\n`` 连在一起（ `\r\n\r\n` ）表示两个空行，标志着请求头的结束。

在HTTP 1.0中，请求头和请求体之间需要一个空行，而在HTTP 1.1中，这个规定变得更加严格，要求使用 `\r\n` 作为换行符。这样的格式规定有助于确保不同操作系统和设备之间的一致性，因为不同系统使用不同的换行符。

----

在HTTP协议中，GET请求是一种用于从服务器获取资源的方法。GET请求通常用于请求服务器发送某个特定资源的内容。在HTTP请求中，GET请求的目标资源由URL中的路径部分指定。

例如，在 ``GET / HTTP/1.0\r\n\r\n`` 中，`/` 表示服务器应该返回根目录的内容。这是因为路径部分指定了所请求资源的位置，而 `/` 表示根目录。

如果你将 `/` 替换为其他路径，例如 ``/example`` ，那么服务器将尝试返回位于该路径下的资源。这是一种用于指定所请求资源的通用方式，允许客户端从服务器检索不同的内容。

需要注意的是，GET请求的格式是 ``GET 请求路径 HTTP版本\r\n\r\n`` ，而路径部分指定了请求的资源。

.. note::

    在HTTP协议中，除了HTTP/1.0之外，还有其他版本的HTTP。主要的HTTP版本包括：

    1. **HTTP/0.9**: 最早的版本，只支持GET请求，并没有完整的HTTP头部。它在每个请求之间使用一个空行作为分隔符，非常简单。

    2. **HTTP/1.0**: 引入了更多的请求方法，如POST，支持更多的头部字段，还引入了状态码和更复杂的连接管理。

    3. **HTTP/1.1**: 引入了持久连接（Persistent Connections），管道化（Pipeline），增加了缓存管理、范围请求等特性，以提高性能。HTTP/1.1是目前最为广泛使用的版本。

    4. **HTTP/2**: 引入了二进制协议，多路复用（Multiplexing），头部压缩，服务器推送等特性，以提升性能。HTTP/2的目标是减少页面加载时间。

    5. **HTTP/3**: 使用QUIC协议，通过UDP传输数据，以取代TCP，旨在进一步提高性能和安全性。

    每个HTTP版本都有其独特的特性和改进，而且随着时间的推移，新的版本可能会被引入以满足不断变化的网络需求。


6. 将错误信息打印到错误输出
-----------------------------------------------------

::

    cmd || echo 'cmd failed' 
    可能对简单的情况有用，但不是通常的方法。在本例中，错误消息将在标准输出中混合错误和成功输出，从而污染脚本的实际输出。简而言之，错误消息应该转到stderr而不是stdout。这很简单:

::

    cmd || echo 'cmd failed' >/dev/stderr 

    or

    if cmd; then 
        echo 'success' 
    else 
        echo 'cmd failed' >/dev/stderr 
    fi

    在上面的示例中，成功消息将在标准输出上打印，而错误消息将在标准输出上打印。

打印错误信息的更好方法是定义一个函数:

::

    err(){ 
        echo "E: $*" >>/dev/stderr 
    } 

现在，当你必须打印一个错误时:

::

    err "My error message" 

7. 将多个命令重定向到同一文件
-----------------------------------------------------

::

    { 
        echo "contents of home directory" 
        ls ~ 
    } > output.txt 

8. 标准输入重定向
-----------------------------------------------------

::

    echo "b" > file.txt
    echo "c" >> file.txt
    echo "a" >> file.txt
    sort 0< file.txt

符号0< 为标准输入

9. 标准错误重定向
-----------------------------------------------------

符号2>为标准错误重定向

::

    echo_to_stderr () { 
        echo stderr >&2 
    }

    $ echo_to_stderr 
    stderr 

    $ echo_to_stderr 2>/dev/null # echos nothing 

9. 控制结构
===========

:文件操作: 细节
:-e "$file": 如果文件存在则返回true。 
:-d "$file": 如果文件存在并且是一个目录，则返回true
:-f "$file": 如果文件存在并且是一个常规文件，则返回true
:-h "$file": 如果文件存在并且是一个符号链接，则返回true

:字符串比较器: 细节
:-z "$str": 如果字符串的长度为零，则为True
:-n "$str: 如果字符串长度非零，则为True
:"$str" = "$str2": 如果string $str等于string $str2，则为True。不适合整数。它可能会起作用，但会不一致
:"$str" != "$str2": 如果字符串不相等，则为True

:整数比较器: 细节
:"$int1" -eq "$int2": 如果整数相等，则为True
:"$int1" -ne "$int2": 如果整数不相等，则为True 
:"$int1" -gt "$int2": 如果int1大于int2，则为True 
:"$int1" -ge "$int2": 当int1大于或等于int2时为真 
:"$int1" -lt "$int2": 当int1小于int2时为True
:"$int1" -le "$int2": 当int1小于或等于int2时为真 

1. 命令列表的条件执行
-----------------------------------------------------

任何内置命令、表达式或函数，以及任何外部命令或脚本都可以使用&&(and)和||(or)操作符有条件地执行。


::

    ╔[Wed Jan 03]═[~]
    ╚$ cd void && sjdf || echo "No such directory"
    bash: sjdf: command not found
    No such directory

    ╔[Wed Jan 03]═[~/void]
    ╚$
    
可以看见cd命令是成功的，然后执行sjdf是失败的，进而执行了后面的 echo "No such directory"

所以，执行||或运算的条件是前面的一个结果为错误

条件执行比它快多了……但是它的主要优点是允许函数和脚本提前退出，或者“短路”。

与许多语言(如C语言)不同，在C语言中，内存被显式地分配给结构体和变量等(因此必须被释放)，bash在幕后处理这个问题。在大多数情况下，我们不需要在离开函数之前清理任何东西。返回语句将释放函数的所有本地内存，并在堆栈上的返回地址处获取执行。


因此，尽快从函数或退出脚本返回可以通过避免不必要的代码执行来显著提高性能并减少系统负载。例如……

::

    my_function () { 
        ### ALWAYS CHECK THE RETURN CODE 

        # 检查参数是否为空，如果为空则立即返回1
        [[ "$1" ]]             || return 1 

        # 处理参数，如果处理失败则立即返回1
        do_something_with "$1" || return 1 
        # 进行另一项操作，如果失败则立即返回1 
        do_something_else      || return 1 

        # 成功执行，没有检测到错误，返回0
        return 0 
    } 
    
- **成功返回值：** 在脚本中，通常使用 `return 0` 来表示函数执行成功。这是一种标准的做法，因为在 Unix 系统中，程序约定使用0表示成功，非零表示错误。在你的例子中，函数成功执行时，返回值为0。

- **错误返回值：** 如果在函数执行过程中发生了错误，使用 **return**  **非零值**来表示错误。在你的例子中，**return 1** 表示发生了错误，因为在脚本中非零值通常被认为是错误的标志。

调用函数时，你可以通过检查函数的返回值来确定函数是否成功执行。在 Bash 中，你可以使用 `$?` 来获取上一个命令的退出状态。例如：

::

    my_function "some_argument"

    if [ $? -eq 0 ]; then
        echo "Function executed successfully."
    else
        echo "Function encountered an error."
    fi

这个例子中，如果 `my_function` 成功执行，将输出 "Function executed successfully."，否则输出 "Function encountered an error."。

2. If语句
-----------------------------------------------------

结束的fi是必要的，但是elif和/或else子句可以省略。

::

    if [[ $1 -eq 1 ]]; then 
        echo "1 was passed in the first parameter" 
    elif [[ $1 -gt 2 ]]; then 
        echo "2 was not passed in the first parameter" 
    else 
        echo "The first parameter was not 1 and is not more than 2." 
    fi

分号之前的分号是将两个命令合并在一行上的标准语法;只有当它们移动到下一行时，它们才能被省略。

重要的是要理解括号[[不是语法的一部分，而是被视为命令;正在测试的是该命令的退出代码。因此，必须始终在括号周围包含空格。

这也意味着可以测试任何命令的结果。如果命令的退出代码为零，则认为该语句为真。

::

    if grep "foo" bar.txt; then 
        echo "foo was found" 
    else 
        echo "foo was not found" 
    fi

数学表达式，当放在双括号内时，也以同样的方式返回0或1，并且也可以进行测试:

::

    if (( $1 + 5 > 91 )); then 
        echo "$1 is greater than 86" 
    fi 

您还可能遇到带有单括号的if语句。这些是在POSIX标准中定义的，并保证在所有POSIX兼容的shell(包括Bash)中工作。语法与Bash非常相似:

::

    if [ "$1" -eq 1 ]; then 
        echo "1 was passed in the first parameter" 
    elif [ "$1" -gt 2 ]; then 
        echo "2 was not passed in the first parameter" 
    else 
        echo "The first parameter was not 1 and is not more than 2." 
    fi

在 Bash 脚本中，`if` 语句可以使用单括号 ``[ ]`` 或双括号 ``[[ ]]``，它们有一些区别：

1. **单括号 `[ ]`:**
   - 传统的测试结构，适用于基本的条件测试。
   - 使用标准的字符串比较和文件测试。
   - 必须在两侧添加空格，例如：`[ "$var" == "value" ]`。
   - 需要使用转义或引号来处理某些特殊字符。

   示例：

::

   if [ "$var" == "value" ]; then
       echo "Condition is true."
   fi

2. **双括号 `[[ ]]`:**
   - 引入了高级的条件测试，提供更多的功能和灵活性。
   - 不需要在两侧添加空格，例如：`[[ $var == value ]]`。
   - 支持高级的字符串操作和模式匹配。
   - 不需要转义某些特殊字符。

   示例：

::

   if [[ $var == value ]]; then
       echo "Condition is true."
   fi

总体而言，使用双括号 `[[ ]]` 更为灵活，特别适合在 Bash 
脚本中进行复杂的条件测试和字符串操作。如果你只需要进行基本的条件测试，单括号 `[ ]` 也是有效的，而且在一些旧的脚本中可能更为常见。

3. 循环遍历数组
-----------------------------------------------------

for 循环

::

    arr=(a b c d e f) 
    for i in "${arr[@]}";do 
        echo "$i" 
    done 

或者

::

    for ((i=0;i<${#arr[@]};i++));do 
        echo "${arr[$i]}" 
    done 

while 循环

::

    i=0 
    while [ $i -lt ${#arr[@]} ];do 
        echo "${arr[$i]}" 
        i=$(expr $i + 1) 
    done

或者

::

    i=0
    while (( $i < ${#arr[@]} ));do 
        echo "${arr[$i]}" 
        ((i++)) 
    done

4. 使用For循环对数字进行列表迭代
----------------------------------------------

::

    for i in {1..10}; do # {1..10} expands to "1 2 3 4 5 6 7 8 9 10" 
        echo $i 
    done

输出：

::

    1
    2
    3
    4
    5
    6
    7
    8
    9
    10

5. 继续循环和打破循环

继续循环的例子

::

    for i in [series] 
    do
        command 1 
        command 2
        if (condition) 
            continue 
        fi
        command 3 
    done

打破循环的例子

::

    for i in [series] 
    do
        command 4
        if (condition)
        then
            command 5
            break
        fi
        command 6
    done

6. 循环打破
-------------

打破多层循环

::

    arr=(a b c d e f) 
    for i in "${arr[@]}";do 
        echo "$i" 
        for j in "${arr[@]}";do 
            echo "$j" 
            break 2 
        done
    done

输出：

::

    a
    a

里面的break 2 让2层循环退出

打破单层循环

::

    arr=(a b c d e f) 
    for i in "${arr[@]}";do 
        echo "$i" 
        for j in "${arr[@]}";do 
            echo "$j" 
            break
        done 
    done

输出:

::

    a
    a
    b
    a
    c
    a
    d
    a
    e
    a
    f
    a
    

while 循环

::

    i=0 
    while [ $i -lt 5 ] #While i is less than 5 
    do
        echo "i is currently $i" 
        i=$[$i+1]  # 括号周围没有空格。这使得它不是一个测试表达式
    done

注意在测试期间(while语句之后)括号周围有空格。这些空间是必要的。

循环的输出

::

    i is currently 0 
    i is currently 1
    i is currently 2
    i is currently 3
    i is currently 4

8. C语法风格的for循环
----------------------------------


C语法风格的for循环基本格式

::

    for (( variable assignment; condition; iteration process )) 

- 在c风格的for循环中，变量的赋值可以包含空格，这与通常的赋值不同

- c风格的for循环中的变量前面没有$。

::

    for (( i = 0; i < 10; i++ )) 
    do
        echo "The iteration number is $i" 
    done

我们还可以在c风格的for循环中处理多个变量:

::

    for (( i = 0, j = 0; i < 10; i++, j = i * i )) 
    do
        echo "The square of $i is equal to $j" 
    done

9. Until 循环
----------------------------------

直到condition为真才执行Until循环

::

    i=5
    until [[ i -eq 10 ]]; do # 检查i是否等于10
        echo "i=$i" # 打印i值
        i=$((i+1)) # 增长i1

输出:

::

    i=5 
    i=6 
    i=7 
    i=8 
    i=9 

当i达到10时，until循环中的条件变为真，循环结束。


10. 带case的Switch语句
--------------------------------

使用case语句，您可以针对一个变量匹配值。

传递给case的参数被展开，并尝试匹配每个模式。

如果找到匹配项，则命令将到执行到;;。

::

    case "$BASH_VERSION" in 
    [34]*) 
        echo {1..4} 
        ;;
        *)
        seq -s" " 1 4 
    esac

模式不是正则表达式，而是shell模式匹配(又名globs)。

11. 没有list-of-words参数的For循环

::

    for arg; do 
        echo arg=$arg
    done

不带单词参数列表的for循环将迭代位置参数。换句话说，上面的例子等价于下面的代码:

::

    for arg in "$@"; do 
        echo arg=$arg 
    done 

就是相当于去掉in "$@"的部分

10. True、false和:命令
===========================

1. 无限循环
----------------------

::

    while true; do 
        echo ok
    done

或者

::

    while :; do 
        echo ok
    done

或者

::

    until false; do
        echo ok
    done


2. 函数返回
--------------------------

::


    # 积极的
    function positive() { 
        return 0 
    }

    # 消极的
    function negative() { 
        return 1
    }

3. 一直或者永不执行的代码
-----------------------------

::

    if true; then 
        echo Always executed 
    fi
    if false; then 
        echo Never executed 
    fi 

11. 数组
===============

1. 数组赋值
--------------

任务列表

如果您熟悉Perl、C或Java，您可能会认为Bash会使用逗号来分隔数组元素，但事实并非如此;相反，Bash使用空格:

::

    # Array in Perl 
    my @array = (1, 2, 3, 4); 

    # Array in Bash 
    array=(1 2 3 4) 

创建一个包含新元素的数组:

::

    array=('first element' 'second element' 'third element') 

下标赋值

创建一个具有显式元素索引的数组:

::

    array=([3]='fourth element' [4]='fifth element') 

按索引赋值

::

    array[0]='first element' 
    array[1]='second element' 

按名称赋值(关联数组)

::
    
    declare -A array 
    array[first]='First element' 
    array[second]='Second element' 

动态分配

从其他命令的输出创建一个数组，例如使用seq获取1到10的范围:

::

    array=(`seq 1 10`) 

从脚本的输入参数赋值:

::

    array=("$@") 

循环内赋值:

::

    while read -r; do 
        #array+=("$REPLY")     # Array append
        array[$i]="$REPLY"     # Assignment by index 
        let i++                # Increment index 
    done < <(seq 1 10)  # command substitution 
    echo ${array[@]}    # output: 1 2 3 4 5 6 7 8 9 10 
    
其中$REPLY总是当前输入

2. 访问数组元素
------------------

打印在索引0上的元素

::

    echo "${array[0]}" 

    Version < 4.3 

使用子字符串展开语法打印最后一个元素

::

    echo "${arr[@]: -1 }" 

    Version ≥ 4.3 

使用下标语法打印最后一个元素

::

    echo "${array[-1]}" 


打印所有元素，每个元素单独引用

::

    echo "${array[@]}" 

将所有元素打印为单个引号字符串

::

    echo "${array[*]}" 

打印索引1中的所有元素，每个元素单独引用

::

    echo "${array[@]:1}" 

从索引1中打印3个元素，每个元素单独引用

::

    echo "${array[@]:1:3}" 

字符串操作

如果引用单个元素，则允许进行字符串操作:

::

    array=(zero one two) 
    echo "${array[0]:0:3}" # gives out zer (chars at position 0, 1 and 2 in the string zero) 
    echo "${array[0]:1:3}" # gives out ero (chars at position 1, 2 and 3 in the string zero) 

因此${array[$i]:N:M}给出一个字符串，从字符串${array[$i]}的第N个位置(从0开始)开始，后面有M个字符。

3. 数组修改
-------------

改变索引

初始化或更新数组中的特定元素

::

    array[10]="elevenths element"    # because it's starting with 0 

    Version ≥ 3.1 

附加

修改数组，如果没有指定下标，则将元素添加到末尾。

::

    array+=('fourth element' 'fifth element') 

用新的参数列表替换整个数组。

::

    array=("${array[@]}" "fourth element" "fifth element") 

在开头添加一个元素:

::

    array=("new element" "${array[@]}") 

插入

在给定的索引位置插入一个元素:

::

    arr=(a b c d) 
    # insert an element at index 2 
    i=2 
    arr=("${arr[@]:0:$i}" 'new' "${arr[@]:$i}") 
    echo "${arr[2]}" #output: new 

删除

使用内置的unset命令删除数组索引:

::

    arr=(a b c) 
    echo "${arr[@]}"   # outputs: a b c 
    echo "${!arr[@]}"  # outputs: 0 1 2 
    unset -v 'arr[1]' 
    echo "${arr[@]}"   # outputs: a c 
    echo "${!arr[@]}"  # outputs: 0 2 

合并

这也适用于稀疏数组。

::

    array3=("${array1[@]}" "${array2[@]}") 

重新索引数组

如果元素已从数组中删除，或者您不确定数组中是否存在空白，则此功能非常有用。要重新创建没有间隙的索引:

::

    array=("${array[@]}") 

4. 数组的迭代
--------------------

数组迭代有两种方式，foreach和经典的for循环:

::

    a=(1 2 3 4) 
    # foreach loop 
    for y in "${a[@]}"; do 
        # act on $y 
        echo "$y" 
    done

    # classic for-loop 
    for ((idx=0; idx < ${#a[@]}; ++idx)); do 
        # act on ${a[$idx]} 
        echo "${a[$idx]}" 
    done

你也可以遍历命令的输出:

::

    a=($(tr ',' ' ' <<<"a,b,c,d")) # tr can transform one character to another 
    for y in "${a[@]}"; do 
        echo "$y" 
    done

5. 数组长度
--------------------

${#array[@]}给出了数组的长度${array[@]}:

::

    array=('first element' 'second element' 'third element') 
    echo "${#array[@]}" # gives out a length of 3 

这也适用于单个元素中的字符串:

::

    echo "${#array[0]}"    # gives out the lenght of the string at element 0: 13 ---> "first element" 13 lenght

6. 关联数组
--------------

Version ≥ 4.0 

声明一个关联数组

::

    declare -A aa 

在初始化或使用之前声明关联数组是强制性的

----

初始化元素

你可以一次初始化一个元素，如下所示:

::

    aa[hello]=world 
    aa[ab]=cd 
    aa["key with space"]="hello world" 

你也可以在一条语句中初始化整个关联数组:

::

    aa=([hello]=world [ab]=cd ["key with space"]="hello world") 

访问关联数组元素

::

    echo ${aa[hello]} 
    # Out: world 

列出关联数组键

::

    echo "${!aa[@]}" 
    #Out: hello ab key with space 

列出关联数组值

::

    echo "${aa[@]}" 
    #Out: world cd hello world 

迭代关联数组的键和值

::

    for key in "${!aa[@]}"; do 
        echo "Key:   ${key}" 
        echo "Value: ${array[$key]}" 
    done

    # Out: 
    # Key:   hello 
    # Value: world 
    # Key:   ab 
    # Value: cd 
    # Key:   key with space 
    # Value: hello world 

计数关联数组元素

::

    echo "${#aa[@]}" 
    # Out: 3 

7. 循环遍历数组
-------------------

例子数组：

::

    arr=(a b c d e f) 

使用for..in loop: 

::

    for i in "${arr[@]}"; do 
        echo "$i" 
    done

    Version ≥ 2.04 

使用C-style for loop: 

::

    for ((i=0;i<${#arr[@]};i++)); do 
        echo "${arr[$i]}" 
    done

使用 while loop: 

::

    i=0 
    while [ $i -lt ${#arr[@]} ]; do 
        echo "${arr[$i]}" 
        i=$((i + 1)) 
    done

    Version ≥ 2.04 

使用带有数值条件的while循环:

::

    i=0 
    while (( $i < ${#arr[@]} )); do 
        echo "${arr[$i]}" 
        ((i++)) 
    done

使用until循环:

::

    i=0 
    until [ $i -ge ${#arr[@]} ]; do 
        echo "${arr[$i]}" 
        i=$((i + 1)) 
    done

    Version ≥ 2.04 

使用带有数值条件的until循环:

::

    i=0 
    until (( $i >= ${#arr[@]} )); do 
        echo "${arr[$i]}" 
        ((i++)) 
    done 

8. 销毁、删除或取消设置Array
-----------------------------

销毁、删除或取消设置一个数组:

::

    unset array 

销毁、删除或取消设置单个数组元素:

::

    unset array[10] 

9. 来自字符串的数组
--------------------

::

    stringVar="Apple Orange Banana Mango" 
    arrayVar=(${stringVar// / }) 

字符串中的每个空格表示结果数组中的一个新项。

::

    echo ${arrayVar[0]} # will print Apple 
    echo ${arrayVar[3]} # will print Mango 

类似地，其他字符也可以用作分隔符。

::

    stringVar="Apple+Orange+Banana+Mango" 
    arrayVar=(${stringVar//+/ }) 
    echo ${arrayVar[0]} # will print Apple 
    echo ${arrayVar[2]} # will print Banana 

10. 初始化索引列表
--------------------

在数组里获得初始化索引列表：

::

    $ arr[2]='second' 
    $ arr[10]='tenth' 
    $ arr[25]='twenty five' 
    $ echo ${!arr[@]} 

    2 10 25     


11. 将整个文件读入数组
--------------------------

一步读取：

::

    IFS=$'\n' read -r -a arr < file 

循环中读取:

::

    arr=() 
    while IFS= read -r line; do 
        arr+=("$line") 
    done

    Version ≥ 4.0 

使用mapfile或readarray(它们是同义词):

::

    mapfile -t arr < file 
    readarray -t arr < file 

12. 数组插入函数
-----------------

这个函数将一个元素插入到给定索引处的数组中:

::

    insert(){ 
        h=' 
    ################## insert ######################## 
    # Usage: 
    #   insert arr_name index element 
    # 
    #   Parameters: 
    #       arr_name    : Name of the array variable 
    #       index       : Index to insert at 
    #       element     : Element to insert 
    ################################################## 
        ' 
        [[ $1 = -h ]] && { echo "$h" >/dev/stderr; return 1; } 
        declare -n __arr__=$1   # reference to the array variable
        i=$2                    # index to insert at 
        el="$3"                 # element to insert 
        # handle errors 
        [[ ! "$i" =~ ^[0-9]+$ ]] && { echo "E: insert: index must be a valid integer" >/dev/stderr; return 1; } 
        (( $1 < 0 )) && { echo "E: insert: index can not be negative" >/dev/stderr; return 1; } 
        # Now insert $el at $i 
        __arr__=("${__arr__[@]:0:$i}" "$el" "${__arr__[@]:$i}") 
        }



.. note::

    [[ $1 = -h ]] && { echo "$h" >/dev/stderr; return 1; } 解释

    检查传递给脚本或函数的第一个参数是否等于 `-h`。让我解释一下：
    1. `[[ $1 = -h ]]`: 这是一个条件测试，它检查脚本或函数的第一个参数是否等于 `-h`。

    2. `&&`: 这是逻辑 AND 运算符，表示在前一个条件（`[[ $1 = -h ]]`）为真的情况下，执行后面的命令。

    3. ``{ echo "$h" >/dev/stderr; return 1; }`` : 如果前面的条件为真，这段代码块会执行两个命令：
    -            - ``echo "$h" >/dev/stderr`` 将帮助文档 `$h` 输出到标准错误流（stderr）。
    - ``return 1``: 返回一个非零的退出码（1），表示发生了错误或提供了帮助文档。
    所以，整体来说，这行代码的作用是：如果脚本或函数的第一个参数是 ``-h`` ，则将帮助文档输出到标准错误流，并返回一个非零的退出码。这通常用于显示帮助信息并通知用户有关正确使用脚本或函数的方式

.. note::

   declare -n __arr__=$1   # reference to the array variable 解释

    这行代码使用 `declare` 命令创建了一个变量 `__arr__`，并将其设置为对传递给脚本或函数的数组参数的引用。让我详细解释：

    - `declare -n __arr__=$1`: 这行代码使用 `-n` 选项声明了一个名称引用。它将变量 `__arr__` 设置为对 `$1` 的引用，其中 `$1` 是传递给脚本或函数的第一个参数，通常是一个数组的名称。

    - 简单来说，`__arr__` 现在是一个别名，它指向传递给脚本或函数的数组。这样，对 `__arr__` 的任何操作都将直接影响到原始数组。

    这通常用于在函数内部处理数组，而无需拷贝整个数组内容，从而提高效率。

    名称引用（name reference）是 Bash 中的一个特性，允许你创建一个变量，它的值是另一个变量的引用，而不是值的拷贝。在这里，`declare -n` 命令创建了一个名称引用 `__arr__`，该引用指向传递给函数的数组。

    使用名称引用的好处在于，它避免了在内存中创建原始数组的副本。当你传递一个数组给函数并在函数内部对其进行修改时，如果使用传值方式（拷贝数组内容），可能会导致内存占用较大，特别是当数组很大时。

    通过使用名称引用，函数实际上在处理原始数组，而不是创建一个数组副本。这样，对数组的修改直接反映在原始数组上，而不需要额外的内存开销。这可以提高程序的性能和效率，尤其是在处理大型数组时。

    在这个特定的代码中，`declare -n __arr__=$1` 的作用是在函数中创建一个名为 `__arr__` 的引用，该引用指向传递给函数的数组。这样，函数中对 `__arr__` 的任何修改都将影响到原始数组。


.. note::

   在 Bash 中，`=~`、`^`、和`$` 是用于字符串匹配的模式匹配操作符。
    1. **`=~`：正则表达式匹配**
            - 使用 `=~` 来进行正则表达式匹配。例如，`[[ $i =~ ^[0-9]+$ ]]` 检查变量 `$i` 是否匹配一个以数字开头并以数字结尾的字符串。
    2. **`^`：锚点 - 匹配字符串的开头**
              - 在正则表达式中，`^` 用作锚点，匹配字符串的开头。例如，`^abc` 匹配以 "abc" 开头的字符串。
    3. **`$`：锚点 - 匹配字符串的结尾**
              - 在正则表达式中，`$` 用作锚点，匹配字符串的结尾。例如，`xyz$` 匹配以 "xyz" 结尾的字符串。

    在你的代码片段中，`[[ ! "$i" =~ ^[0-9]+$ ]]` 的含义是：检查变量 `$i` 是否不匹配一个以数字开头并以数字结尾的字符串。如果不匹配，执行相应的错误处理。

.. note::

    那以数字结尾不就是直接在0-9方括号后面加上$不就可以了吗，为什么还需要一个+号
    
    正确，你的理解是对的。在正则表达式中，`[0-9]+$` 表示匹配以一个或多个数字结尾的字符串。这是因为 `+` 是一个量词，表示匹配前面的元素（这里是 `[0-9]`）至少一次或更多次。

    如果只是 `[0-9]$`，它将匹配以单个数字结尾的字符串。添加 `+` 表示匹配一个或多个数字。

    所以，`[0-9]+$` 表示匹配以一个或多个数字结尾的字符串，而 `^[0-9]+$` 则表示整个字符串必须由一个或多个数字组成。


当涉及到正则表达式时，有许多符号和模式可用于灵活地匹配和处理字符串。以下是一些基本的正则表达式元字符和用法：

1. **`.`：匹配任意单个字符**
      - 例如，`a.c` 可以匹配 "abc"、"adc"、"aec" 等。
2. **`*`：匹配前一个元素零次或多次**
      - 例如，`ab*c` 可以匹配 "ac"、"abc"、"abbc" 等。
3. **`?`：匹配前一个元素零次或一次**
      - 例如，`ab?c` 可以匹配 "ac"、"abc" 等。
4. **`[...]`：字符类，匹配方括号中的任意一个字符**
      - 例如，`[aeiou]` 匹配任何一个元音字母。
5. **`[^...]`：否定字符类，匹配不在方括号中的任意字符**
      - 例如，`[^0-9]` 匹配任何非数字字符。
6. **`()`：捕获组，用于捕获匹配的子字符串**
      - 例如，`(ab)+` 可以匹配 "ab"、"abab" 等。
7. **`\\`：转义字符**
      - 例如，`\\.` 可以匹配实际的点字符，而不是任意字符。
8. **`|`：或操作符**
      - 例如，`cat|dog` 可以匹配 "cat" 或 "dog"。

这只是正则表达式的基础，正则表达式语法非常灵活，允许你进行更复杂的模式匹配。在 Bash 中，`[[ ... =~ ... ]]` 构造提供了对正则表达式的支持。如果你有具体的问题或用例，我可以提供更详细的帮助。

----
    
在 Bash 中，圆括号 `(( ... ))` 通常用于进行算术运算，而不是正则表达式。以下是圆括号在算术上的一些常见用法：

1. **基本算术运算**：

   - `(( a + b ))`: 执行加法。

   - `(( a - b ))`: 执行减法。

   - `(( a * b ))`: 执行乘法。

   - `(( a / b ))`: 执行除法。

2. **比较运算**：

   - `(( a == b ))`: 检查是否相等。

   - `(( a != b ))`: 检查是否不相等。

   - `(( a > b ))`: 检查是否大于。

   - `(( a < b ))`: 检查是否小于。

   - `(( a >= b ))`: 检查是否大于等于。

   - `(( a <= b ))`: 检查是否小于等于。

3. **逻辑运算**：

   - `(( a && b ))`: 逻辑 AND。

   - `(( a || b ))`: 逻辑 OR。

   - `(( !a ))`: 逻辑 NOT。

4. **自增和自减**：

   - `(( a++ ))`: 将 `a` 增加 1。

   - `(( a-- ))`: 将 `a` 减少 1。

这些圆括号用于执行整数算术运算，并且在条件判断中也很常见。例如，`if (( a > b )); then ... fi` 可以在 Bash 脚本中使用这种形式进行条件判断。圆括号中的变量和运算符不需要使用 `$` 符号。

 
----

sh 中，双方括号 `[[ ... ]]` 主要用于条件测试，提供了一些额外的功能和安全性比单方括号 `[ ... ]` 更强大的条件测试。以下是双方括号的一些常见用法：

1. **字符串比较**：

   - `[[ "$string1" == "$string2" ]]`: 检查两个字符串是否相等。

   - `[[ "$string1" != "$string2" ]]`: 检查两个字符串是否不相等。

2. **正则表达式匹配**：

   - `[[ "$string" =~ pattern ]]`: 检查字符串是否匹配正则表达式模式。

3. **文件测试**：
   
   - `[[ -e "$file" ]]`: 检查文件是否存在。

   - `[[ -f "$file" ]]`: 检查文件是否为普通文件。

   - `[[ -d "$directory" ]]`: 检查路径是否为目录。

4. **逻辑运算**：
   - `[[ condition1 && condition2 ]]`: 逻辑 AND。

   - `[[ condition1 || condition2 ]]`: 逻辑 OR。

   - `[[ !condition ]]`: 逻辑 NOT。

5. **变量存在性检查**：

   - `[[ -n "$variable" ]]`: 检查变量是否存在且非空。

   - `[[ -z "$variable" ]]`: 检查变量是否存在且为空。

6. **数组测试**：

   - `[[ ${#array[@]} -gt 0 ]]`: 检查数组是否非空。

7. **模式匹配**：

   - `[[ "$string" == pattern* ]]`: 检查字符串是否以指定模式开头。

双方括号支持更丰富的条件测试，同时在字符串和变量处理上更加灵活，因此在 Bash 脚本中，通常推荐使用 `[[ ... ]]` 进行条件测试，而不是 `[ ... ]`。






使用:

::

    insert array_variable_name index element 

例子:

::

    arr=(a b c d) 
    echo "${arr[2]}" # output: c 
    # Now call the insert function and pass the array variable name, 
    # index to insert at 
    # and the element to insert 
    insert arr 2 'New Element' 
    # 'New Element' was inserted at index 2 in arr, now print them 
    echo "${arr[2]}" # output: New Element 
    echo "${arr[3]}" # output: c 

12. 关联数组
=============

1. 检查关联数组
-----------------

下面的代码片段显示了所有需要的用法:

declare: usage: declare [-aAfFgiIlnrtux] [name[=value] ...] or declare -p [-aAfFilnrtux] [name ...]


.. note::

    -a：申明数组变量
    -A：申明关联数组，可以使用字符串作为数组索引
    -f：仅显示已定义的函数
    -F：不显示函数定义
    -g：指定变量为全局变量，即使在函数内定义变量
    -i：声明整型变量
    -l：将变量值的小写字母变为小写
    -r：设置只读属性
    -t：设置变量跟踪属性，用于跟踪函数进行调试，对于变量没有特殊意义
    -u：变量值的大写字母变为大写
    -x：将指定的Shell变量换成环境变量
    -p：显示变量定义的方式和值+：取消变量属性，但是 +a 和 +r 无效，无法删除数组和只读属性，可以使用unset删除数组，但是 unset 不能删除只读变量




::

	#!/usr/bin/env bash

	declare -A assoc_array=([key_string]=value \
				[one]="something" \
				[two]="another thing" \
				[ three ]='mind the blanks!' \
				[ " four" ]='count the blanks of this key later!' \
				[IMPORTANT]='SPACES DO ADD UP!!!' \
				[1]='there are no integers!' \
				[info]="to avoid history expansion " \
				[info2]="quote exclamation mark with single quotes" \
				)
	echo # just a blank line
	echo now here are the values of assoc_array:
	echo ${assoc_array[@]}
	echo not that useful,
	echo # just a blank line
	echo this is better:

	declare -p assoc_array # -p == print

	echo have a close look at the spaces above\!\!\!
	echo # just a blank line

	echo accessing the keys
	echo the keys in assoc_array are ${!assoc_array[*]}
	echo mind the use of indirection operator \!
	echo # just a blank line

	echo now we loop over the assoc_array line by line
	echo note the \! indirection operator which works differently,
	echo if used with assoc_array.
	echo # just a blank line

	for key in "${!assoc_array[@]}"; do # accessing keys using ! indirection!!!!
		printf "key: \"%s\"\nvalue: \"%s\"\n\n" "$key" "${assoc_array[$key]}"
	done

	echo have a close look at the spaces in entries with keys two, three and four above\!\!\!
	echo # just a blank line
	echo # just another blank line

	echo there is a difference using integers as keys\!\!\!
	i=1
	echo declaring an integer var i=1
	echo # just a blank line
	echo Within an integer_array bash recognizes artithmetic context.
	echo Within an assoc_array bash DOES NOT recognize artithmetic context.
	echo # just a blank line
	echo this works: \${assoc_array[\$i]}: ${assoc_array[$i]}
	echo this NOT!!: \${assoc_array[i]}: ${assoc_array[i]}
	echo # just a blank line
	echo # just a blank line
	echo an \${assoc_array[i]} has a string context within braces in contrast to an integer_array
	declare -i integer_array=( one two three )
	echo "doing a: declare -i integer_array=( one two three )"
	echo # just a blank line

	echo both forms do work: \${integer_array[i]} : ${integer_array[i]}
	echo and this too: \${integer_array[\$i]} : ${integer_array[$i]}
	
    
13. 函数
========

1. 带参数的函数
---------------

::

	#!/bin/bash
	greet() {
	local name="$1"
	echo "Hello, $name"
	}
	greet "John Doe"
	# running above script
	$ bash helloJohn.sh
	Hello, John Doe

1. 如果不以任何方式修改参数，则不需要将其复制到局部变量—只需echo即可 “Hello, $1“。

2. 你可以使用$1，$2，$3等等来访问函数内部的参数。

.. note::

    对于大于9的参数$10不起作用(bash会将其读取为$10)，您需要执行${10}， ${11}等等。
    就是给数字加个花括号

3. $@表示函数的所有参数:

::

	#!/bin/bash
	foo() {
	echo "$@"
	}
	foo 1 2 3 # output => 1 2 3    

.. note::

    你实际上应该总是在"$@"周围使用双引号，就像这里一样。

省略引号将导致shell扩展通配符，通常会引入不受欢迎的行为，甚至潜在的安全问题。

::

    "string with spaces;" '$HOME' "*"
    # output => string with spaces; $HOME *

4. 对于默认参数，使用${1:-default_val}。例如:

::

    #!/bin/bash
    foo() {
    local val=${1:-25}
    echo "$val"
    }
    foo
    foo 30
    # output => 25
    # output => 30 

5. 需要一个参数使用${var:?error message}

::

	foo() {
	local val=${1:?Must provide an argument}
	echo "$val"
	}

2. 简单函数
--------------

::

	#!/bin/bash
	# Define a function greet
	greet ()
	{
	echo "Hello World!"
	}
	# Call the function greet
	greet	

在运行脚本时，我们看到了我们的消息

::

	$ bash helloWorld.sh
	Hello World!

请注意，使用函数源文件可以使它们在当前的bash会话中可用。

::

	$ source helloWorld.sh
	$ greet
	Hello World!

您可以在某些shell中export(导出)函数，以便将其公开给子进程。

::

	bash -c 'greet' # fails
	export -f greet # export function; note -f
	bash -c 'greet' # success

3. 处理标志和可选参数
----------------------

内置的getopts可以在函数内部使用，以编写容纳标志和可选的函数 参数。这没有特别的困难，但是必须适当地处理getopts所触及的值。 例如，我们定义了一个failwith函数，它在stderr上写一条消息，并以代码1或任意代码退出 作为参数提供给-x选项的代码:

::

	# failwith [-x STATUS] PRINTF-LIKE-ARGV
	# Fail with the given diagnostic message
	#
	# The -x flag can be used to convey a custom exit status, instead of
	# the value 1. A newline is automatically added to the output.
	failwith()
	{
		# 声明几个局部变量，用于处理命令行参数
		local OPTIND OPTION OPTARG status

		status=1 # 初始化一个变量status并设值为1
		OPTIND=1 # 初始化命令行选项的索引

		while getopts 'x:' OPTION; do # while 循环，使用getopts命令解析命令行选项
			case ${OPTION} in # 开始case语句，根据不同选项执行相应操作
				x)	status="${OPTARG}";;
				*)	1>&2 printf 'failwith: %s: Unsupported option.\n' "${OPTION}";; # 输出错误信息
			esac
		done

		shift $(( OPTIND - 1 )) # 将处理过的选项移除，以便后续处理剩余的命令行参数
		{
			printf 'Failure: '
			printf "$@"
			printf '\n'
		} 1>&2 # 将输出定向到标准错误流
		exit "${status}" # 以status的值退出脚本
	}


4. 打印函数定义
----------------

::

	getfunc() {
		declare -f "$@"
	}
	function func(){
		echo "I am a sample function"
	}
	funcd="$(getfunc func)"
	getfunc func # or echo "$funcd"

输出：

::

	func ()
	{
		echo "I am a sample function"
	}

5. 接受命名参数的函数
----------------------

::

	foo() {
		while [[ "$#" -gt 0 ]]
	do
		case $1 in
			-f|--follow)
			local FOLLOW="following"
			;;
			-t|--tail)
			local TAIL="tail=$2"
			;;
		esac
		shift
	done

	echo "FOLLOW: $FOLLOW"
	echo "TAIL: $TAIL"
	}

使用例子：

::

	foo -f
	foo -t 10
	foo -f --tail 10
	foo --follow --tail 10

6. 函数的返回值
-----------------

Bash中的return语句不像c函数那样返回一个值，而是用返回值退出函数 的地位。你可以把它想象成那个函数的退出状态。

如果你想从函数中返回一个值，然后像这样将值发送到stdout:

::

	fun() {
		local var="Sample value to be returned"
		echo "$var"
		#printf "%s\n" "$var"
	}

如果你这样执行：

::

	var="$(fun)"

fun的输出将会储存在$var变量里

7. 函数的退出码就是它的 最后一个命令
--------------------------------------

考虑这个示例函数来检查主机是否已启动:

::

	is_alive() {
		ping -c1 "$1" &> /dev/null
	}

该函数向第一个函数参数指定的主机发送单个ping。输出和错误输出 的ping都被重定向到/dev/null，所以这个函数永远不会输出任何东西。但是ping命令可以 成功时退出代码为0，失败时退出代码为非0。因为这是最后一个(在本例中也是唯一的)命令 这个函数，ping的退出码将被重用为函数本身的退出码。

这个事实在条件语句中非常有用。 例如，如果主机graucho已启动，那么使用ssh连接到它:

::

	if is_alive graucho; then
		ssh graucho
	fi

另一个例子:反复检查，直到graucho主机启动，然后用ssh连接到它:

::

	while ! is_alive graucho; do
		sleep 5
	done
	ssh graucho

14. Bash参数扩展
=================

$字符引入了参数扩展、命令替换或算术扩展。参数要扩展的名称或符号可以括在大括号中，大括号是可选的，但用于保护变量从紧跟其后的字符扩展，这些字符可以解释为名称的一部分。在 Bash 用户手册中阅读更多内容。

1. 修改字母的大小写
---------------------

Version ≥ 4.0

变成大写

::

	$ v="hello"
	# Just the first character
	$ printf '%s\n' "${v^}"
	Hello
	# All characters
	$ printf '%s\n' "${v^^}"
	HELLO
	# Alternative
	$ v="hello world"
	$ declare -u string="$v"
	$ echo "$string"
	HELLO WORLD

变成小写

::

	$ v="BYE"
	# Just the first character
	$ printf '%s\n' "${v,}"
	bYE
	# All characters
	$ printf '%s\n' "${v,,}"
	bye
	# Alternative
	$ v="HELLO WORLD"
	$ declare -l string="$v"
	$ echo "$string"
	hello world

切换大小写

::

	$ v="Hello World"
	# All chars
	$ echo "${v~~}"
	hELLO wORLD
	$ echo "${v~}"
	# Just the first char
	hello World

2. 参数长度
---------------

::

	# Length of a string
	$ var='12345'
	$ echo "${#var}"
	5

请注意，它是以字符数为单位的长度，不一定与字节数相同(如in UTF-8，其中大多数字符编码在一个字节以上)，也不是字形/字素的数量(其中一些 这是字符的组合)，也不一定与显示宽度相同。

::

	# Number of array elements
	$ myarr=(1 2 3)
	$ echo "${#myarr[@]}"
	3
	# Works for positional parameters as well
	$ set -- 1 2 3 4
	$ echo "${#@}"
	4
	# But more commonly (and portably to other shells), one would use
	$ echo "$#"
	4

3. 替换字符串中的模式
-----------------------

第一次匹配

::

	$ a='I am a string'
	$ echo "${a/a/A}"
	I Am a string

所有匹配	

::

	$ echo "${a//a/A}"
	I Am A string

匹配开头

::

	$ echo "${a/#I/y}"
	y am a string

匹配结尾

::

	$ echo "${a/%g/N}"
	I am a strinN

用空替换一个模式:

::

	$ echo "${a/g/}"
	I am a strin

添加前缀到数组本身

::

	$ A=(hello world)
	$ echo "${A[@]/#/R}"
	Rhello Rworld

4. 子字符串和子数组
---------------------

::

	var='0123456789abcdef'

	# Define a zero-based offset
	$ printf '%s\n' "${var:3}"
	3456789abcdef

	# Offset and length of substring
	$ printf '%s\n' "${var:3:4}"
	3456

::

	# Negative length counts from the end of the string
	$ printf '%s\n' "${var:3:-5}"
	3456789a

	# Negative offset counts from the end
	# Needs a space to avoid confusion with ${var:-6}
	$ printf '%s\n' "${var: -6}"
	abcdef

	# Alternative: parentheses
	$ printf '%s\n' "${var:(-6)}"
	abcdef

	# Negative offset and negative length
	$ printf '%s\n' "${var: -6:-5}"
	a

如果形参是位置形参或下标数组的元素，则适用相同的展开:

::

	# Set positional parameter $1
	set -- 0123456789abcdef

	# Define offset
	$ printf '%s\n' "${1:5}"
	56789abcdef

	# Assign to array element
	myarr[0]='0123456789abcdef'

	# Define offset and length
	$ printf '%s\n' "${myarr[0]:7:3}"
	789

类似的展开适用于位置参数，其中偏移量是基于1的:

::

	# Set positional parameters $1, $2, ...
	$ set -- 1 2 3 4 5 6 7 8 9 0 a b c d e f
	# Define an offset (beware $0 (not a positional parameter)
	# is being considered here as well)
	$ printf '%s\n' "${@:10}"
	0
	a
	b
	c
	d
	e
	f

	# Define an offset and a length
	$ printf '%s\n' "${@:10:3}"
	0
	a
	b

	# No negative lengths allowed for positional parameters
	$ printf '%s\n' "${@:10:-2}"
	bash: -2: substring expression < 0

	# Negative offset counts from the end
	# Needs a space to avoid confusion with ${@:-10:2}
	$ printf '%s\n' "${@: -10:2}"
	7
	8

	# ${@:0} is $0 which is not otherwise a positional parameters or part
	# of $@
	$ printf '%s\n' "${@:0:2}"
	/usr/bin/bash
	1


子字符串扩展可用于索引数组:

::

	# Create array (zero-based indices)
	$ myarr=(0 1 2 3 4 5 6 7 8 9 a b c d e f)
	# Elements with index 5 and higher
	$ printf '%s\n' "${myarr[@]:12}"
	c
	d
	e
	f

	# 3 elements, starting with index 5
	$ printf '%s\n' "${myarr[@]:5:3}"
	5
	6
	7

	# The last element of the array
	$ printf '%s\n' "${myarr[@]: -1}"
	f

5. 从字符串的开头删除一个模式
-------------------------------

最短匹配:

::

	$ a='I am a string'
	$ echo "${a#*a}"
	m a string

最长的匹配:

::

	$ echo "${a##*a}"
	string

6. 参数间接
------------

Bash间接允许获取包含在另一个变量中的变量的值,通过另外一个变量的名称。变量 例子:

::

	$ red="the color red"
	$ green="the color green"
	$ color=red
	$ echo "${!color}"
	the color red

	$ color=green
	$ echo "${!color}"
	the color green

下面是一些间接展开用法的例子:

::

	$ foo=10
	$ x=foo
	$ echo ${x}
	foo				# 经典打印变量

	$ foo=10
	$ x=foo
	$ echo ${!x}
	10				# 间接的扩张

也就是调用参数时在参数名字前面加个叹号"!"

另一个例子：

::

	$ argtester () { for (( i=1; i<="$#"; i++ )); do echo "${i}";done; }; argtester -ab -cd -ef
	1	#i expanded to 1
	2	#i expanded to 2
	3	#i expanded to 3

	$ argtester () { for (( i=1; i<="$#"; i++ )); do echo "${!i}";done; }; argtester -ab -cd -ef
	-ab	# i=1 --> expanded to $1 ---> expanded to first argument sent to function
	-cd	# i=2 --> expanded to $2 ---> expanded to second argument sent to function
	-ef	# i=3 --> expanded to $3 ---> expanded to third argument sent to function

7. 参数展开和文件名
--------------------

您可以使用Bash参数扩展来模拟常见的文件名处理操作，如basename和 目录名。

我们将使用这个作为我们的示例路径:

::

    FILENAME="/tmp/example/myfile.txt"

模拟dirname并返回文件路径的目录名:

::

    echo "${FILENAME%/*}"
    #Out: /tmp/example

要模拟basename $FILENAME并返回文件路径的文件名:

::

    echo "${FILENAME##*/}"
    #Out: myfile.tx

模拟basename $FILENAME .txt并返回不带.txt的文件名。扩展:

::

    BASENAME="${FILENAME##*/}"
    echo "${BASENAME%%.txt}"
    #Out: myfile

8. 默认值替换

.. note::

    ${parameter:-word}

    如果parameter未设置或为空，则替换word的展开部分。否则，parameter的值为设置值代替。

::

    $ unset var
    $ echo "${var:-XX}"
    XX

    $ var=""
    $ echo "${var:-XX}"
    XX

    $ var=23
    $ echo "${var:-XX}"
    23

.. note::

    ${parameter:=word}

    如果parameter未设置或为null，则将word的展开值赋给parameter。parameter的值为 然后替换。位置参数和特殊参数不能这样分配。

::

	$ unset var
	$ echo "${var:=XX}"
	XX
	$ echo "$var"
	XX
	$ var=""
	$ echo "${var:=XX}"
	XX
	$ echo "$var"
	XX
	$ var=23
	$ echo "${var:=XX}"
	23
	$ echo "$var"
	23


9. 从字符串末尾删除一个模式
---------------------------------

最短匹配：

::

    $ a='I am a string'
    $ echo "${a%a*}"
    I am

最长的匹配：

::

    $ echo "${a%%a*}"
    I

这里展示了在 Bash（一种Unix shell和编程语言）中如何从字符串末尾删除特定模式的方法，使用的是`${}`结构中的`%`和`%%`操作符。

1. **${a%a*}** ：
   - 这是最短匹配的例子。它会从变量 `$a` 的末尾开始，删除第一个匹配模式`a*` （即以字母 `a` 开头的任何内容），直到找到的第一个匹配为止。
   - 所以对于`$a='I am a string'` ，匹配的模式是从最后一个 `a` 开始，直到末尾的所有内容。
   - 结果是 `I am` ，因为它删除了字符串中从最后一个 `a` 开始到末尾的部分。

2. **${a%%a*}** ：
   - 这是最长匹配的例子。它会从变量 `$a` 的末尾开始，删除所有匹配模式 `a*` （即以字母 `a` 开头的任何内容），直到找到的最后一个匹配为止。
   - 所以对于 `$a='I am a string'` ，匹配的模式是从最后一个 `a` 开始，直到字符串的开头。
   - 结果是 `I` ，因为它删除了字符串中从最后一个 `a` 开始一直到开头的部分。

这些操作符非常有用，可以用来快速地在脚本中处理字符串。


10. 参数扩展 
-----------------------

变量不一定要扩展到其值--在扩展过程中可以提取子串，这对提取文件扩展名或部分路径非常有用。
这对于提取文件扩展名或路径的部分内容非常有用。全局变换字符保留其通常的含义，因此 .*
指的是一个字面意义上的点，后跟任意字符序列；它不是正则表达式。

::

    $ v=foo-bar-baz
    $ echo ${v%%-*}
    foo
    $ echo ${v%-*}
    foo-bar
    $ echo ${v##*-}
    baz
    $ echo ${v#*-}
    bar-baz

    例子中，v 是一个变量，它的值是 foo-bar-baz。你用了 #，##，%，%% 这四种符号，来从变量的值中删除一些子串。具体的结果如下：

    ${v%%-*} 表示从 v 的值的结尾删除最长的匹配 -* 的子串，也就是 -bar-baz。所以结果是 foo。
    ${v%-*} 表示从 v 的值的结尾删除最短的匹配 -* 的子串，也就是 -baz。所以结果是 foo-bar。
    ${v##*-} 表示从 v 的值的开头删除最长的匹配 *- 的子串，也就是 foo-bar-。所以结果是 baz。
    ${v#*-} 表示从 v 的值的开头删除最短的匹配 *- 的子串，也就是 foo-。所以结果是 bar-baz。

参数扩展是一种在命令行中对变量或参数进行替换或修改的方法1。你可以用大括号（{}）来包围参数的名字或符号，这样可以避免后面的字符被误认为参数的一部分2。你还可以在参数名字后面加上一些特殊的符号，来实现不同的功能3。例如：

`:-` 表示如果参数为空或未设置，就用后面的单词代替。否则就用参数的值。

`-`  表示如果参数为未设置，才使用后面的默认值

`:=` 表示如果参数为空或未设置，就把后面的单词赋值给参数。然后用参数的值。

`:?` 表示如果参数为空或未设置，就把后面的单词（或者一个默认的错误信息）输出到标准错误，并且退出 shell。

`#` 表示从参数的开头删除最短的匹配后面的模式的子串。

`##` 表示从参数的开头删除最长的匹配后面的模式的子串。

`%` 表示从参数的结尾删除最短的匹配后面的模式的子串。

`%%` 表示从参数的结尾删除最长的匹配后面的模式的子串。

`:+` 与默认值类似，也可以给出替代值；如果某个变量不可用，则使用默认值，如果变量可用，则使用替代值。
如果变量可用，则使用替代变量。

::

    $ a="set"
    $ b=""
    $ echo ${a:+alternative_a} ${b:+alternative_b}
    alternative_a

注意到这些扩展可以嵌套，在提供
参数时尤其有用；

::

    $ output_file=/tmp/foo
    $ wget ${output_file:+"-o ${output_file}"} www.stackexchange.com 可以看见这里的嵌套,提供了参数
    # expands to wget -o /tmp/foo www.stackexchange.com

    $ unset output_file
    $ wget ${output_file:+"-o ${output_file}"} www.stackexchange.com
    # expands to wget www.stackexchange.com

11. 变量为空或未设置时出错
-----------------------------

它的语义类似于默认值替换，但是它不是替换默认值，而是替换默认值
错误与提供的错误消息。 

形式是${VARNAME？ERRMSG}和${VARNAME：？ERRMSG}。 

表格如果变量未设置或为空，则会出错，而没有的表单只会在变量为空时出错
未设置。 如果抛出错误，则输出ERRMSG并将退出代码设置为1

::

    #!/bin/bash
    FOO=
    # ./script.sh: line 4: FOO: EMPTY
    echo "FOO is ${FOO:?EMPTY}"
    # FOO is
    echo "FOO is ${FOO?UNSET}"
    # ./script.sh: line 8: BAR: EMPTY
    echo "BAR is ${BAR:?EMPTY}"
    # ./script.sh: line 10: BAR: UNSET
    echo "BAR is ${BAR?UNSET}"

错误扩展。它的作用是检查一个变量是否为空或未设置，如果是的话，就输出一个错误信息，并退出脚本。它的语法是 VARNAME?ERRMSG或 {VARNAME:?ERRMSG}。其中，VARNAME 是要检查的变量名，ERRMSG 是要输出的错误信息。

**如果在 VARNAME 前面加上一个冒号 (:)，那么它会检查变量是否为空或未设置；如果不加冒号，那么它只会检查变量是否未设置。**

你的例子中，你定义了一个变量 FOO，但没有给它赋值，所以它是空的。然后你用 echo 命令输出 FOO 的值，但是在 FOO 的名字前面加了一个错误扩展。这样，如果 FOO 是空或未设置，就会输出你指定的错误信息，并退出脚本。你的例子中，你分别用了两种错误扩展的形式，一种是 FOO:?EMPTY，一种是 {FOO?UNSET}。前者会检查 FOO 是否为空或未设置，后者只会检查 FOO 是否未设置。因为 FOO 是空的，所以前者会触发错误扩展，输出 FOO:EMPTY，并退出脚本。后者不会触发错误扩展，因为 FOO 虽然是空的，但是已经设置了。所以后者会正常输出 FOO 的值，即空。

你的例子中，你还用了一个未定义的变量 BAR。你也用了两种错误扩展的形式，一种是 BAR:?EMPTY，一种是 {BAR?UNSET}。因为 BAR 是未设置的，所以两种形式都会触发错误扩展，分别输出 BAR: EMPTY 和 BAR: UNSET，并退出脚本


15. Copying (cp)
====================

====================    ======================================================
选项                    描述
====================    ======================================================
-a,-archive             结合了 d、p 和 r 选项 Combines the d, p and r options
-b, -backupBefore       在删除之前，进行备份 removal, makes a backup
-d, --no-deference      保存链接 Preserves links
-f, --force             无需提示用户即可删除现有目的地 Remove existing destinations without prompting user
-i, --interactive       覆盖前显示提示 Show prompt before overwriting
-l, --link              链接文件而不是复制文件 Instead of copying, link ﬁles instead
-p, --preserve          尽可能保留文件属性 Preserve file attributes when possible
-R, --recursive         递归复制目录 Recursively copy directories
====================    ======================================================

1. 复制单个文件
-----------------

Copy foo.txt from /path/to/source/ to /path/to/target/folder/

``cp /path/to/source/foo.txt /path/to/target/folder/``

Copy foo.txt from /path/to/source/ to /path/to/target/folder/ into a ﬁle called bar.txt

``cp /path/to/source/foo.txt /path/to/target/folder/bar.txt``

2. 复制文件夹
---------------

将 foo 文件夹复制到 bar 文件夹中

::

    cp -r /path/to/foo /path/to/bar

如果在发出命令前存在文件夹 bar，那么 foo 及其内容将被复制到文件夹 bar 中。
但是，如果在发出命令前 bar 不存在，那么将创建文件夹 bar，并将 foo 的内容放入 bar 中。
foo 的内容将被放入 bar

16. Find
========

find 是一条命令，用于递归搜索目录中符合条件的文件（或目录），然后对所选文件执行某些操作。
操作。

1. 按名称或扩展名搜索文件
---------------------------------

::

    查找与 pwd 相对的、具有特定名称的文件/目录：
    $ find . -name "myFile.txt"

    要查找具有特定扩展名的文件/目录，请使用通配符：
    $ find . -name "*.txt"

    # 要查找与多个扩展名之一匹配的文件/目录，请使用or标志:
    $ find . -name "*.txt" -o -name "*.sh"  

    查找名称以 abc 开头并以一个字母和一个数字结尾的文件/目录：
    $ find . -name "abc[a-z][0-9]"

    查找指定目录中的所有文件/目录
    $ find /opt

    要只搜索文件（而不是目录），请使用 -type f：
    $ find /opt -type f

    要只搜索目录（而不是普通文件），请使用 -type d：
    $ find /opt -type d


2. 对找到的文件执行命令
--------------------------------------------

有时，我们需要针对大量文件运行命令。这可以使用 xargs 来完成。

::

    find . -type d -print | xargs -r chmod 770

    上面的命令将递归地查找相对于 的所有目录（-type d）。（这是您当前的工作
    目录），并在其上执行 chmod 770。-r 选项指定 xargs 在未找到 find 时不运行 chmod
    任何文件。

如果您的文件名或目录中有空格符号，该命令可能会卡住；解决方法是使用以下命令
如下

::

    find . -type d -print0 | xargs -r -0 chmod 770


    在上例中，-print0 和 -0 标志指定文件名使用空字节分隔，并允许在文件名中使用特殊字符（如空格）。
    允许在文件名中使用空格等特殊字符。这是 GNU 扩展，可能无法在
    其他版本的 find 和 xargs 中可能无法使用。


首选方法是跳过 xargs 命令，让 find 自己调用子进程：

::

    find . -type d -exec chmod 770 {} \;

    在此，{} 是一个占位符，表示您希望在此时使用文件名。
    对每个文件执行 chmod 命令。


您也可以在调用 chmod 时传递所有文件名，方法是使用

::

    find . -type d -exec chmod 770 {} +

    这也是上述 xargs 片段的行为。(要单独调用每个文件，可以使用 xargs -n1）。)

第三种方法是让 bash 在 ﬁlenames 列表中循环查找输出：

::

    find . -type d | while read -r d; do chmod 770 "$d"; done

这在语法上是最笨拙的，但当你想在每个找到的文件上运行多个命令时却很方便。
不过，面对名称奇特的文件名，这种方法并不安全。

::

    find . -type f | while read -r d; do mv "$d" "${d// /_}"; done

    会用下划线替换文件名中的所有空格。如果目录名前有空格，此示例也将失效。


上面的问题是，虽然 read -r 希望每行只有一个条目，但文件名可以包含换行符。
(而且，read -r 会丢失任何尾部空白）。你可以通过回转来解决这个问题：

::

    find . -type d -exec bash -c 'for f; do mv "$f" "${f// /_}"; done' _ {} +

会以完全正确和可移植的形式接收文件名；而 bash -c 会以若干参数的形式接收文件名。
参数，这些参数将在 $@ 中找到，并正确地加上引号等。
当然，脚本需要正确处理这些名称；每个包含文件名的变量都需要使用双引号）。

神秘的 "_" 是必要的，因为 bash -c 的第一个参数 "脚本 "是用来填充 $0。

3. 按访问/修改时间查找文件
--------------------------------------------

在 ext 文件系统上，每个文件都有一个存储的 Access、Modification 和 （Status） Change time 与之关联 - 到
查看此信息，您可以使用

::

    stat myFile.txt;

使用 find 中的标志，我们可以搜索在一定时间范围内修改。

::

    查找最近 2 小时内修改过的文件：
    $ find . -mmin -120

    查找最近 2 小时内未被修改的文件：
    $ find . -mmin +120

    上述示例仅搜索修改后的时间，若要搜索访问时间或更改后的时间，请使用 a 或
    c 进行搜索。
    $ find . -amin -120
    $ find . -cmin +120

    一般格式：
    -mmin n : File was modiﬁed n minutes ago
    -mmin -n : File was modiﬁed less than n minutes ago
    -mmin +n : File was modiﬁed more than n minutes ago

    查找最近 2 天内修改过的文件：
    find . -mtime -2

    查找最近 2 天内未修改的文件
    find . -mtime +2

    使用 -atime 和 -ctime 分别表示访问时间和状态更改时间。
    一般格式：
    -mtime n : File was modiﬁed nx24 hours ago
    -mtime -n : File was modiﬁed less than nx24 hours ago
    -mtime +n : File was modiﬁed more than nx24 hours ago

    查找在 2007-06-07 到 2007-06-08 期间修改的文件：
    find . -type f -newermt 2007-06-07 ! -newermt 2007-06-08

    查找从 1 小时前到 10 分钟前在一定时间范围内访问过的文件（使用文件作为时间戳）：
    touch -t $(date -d '1 HOUR AGO' +%Y%m%d%H%M.%S) start_date
    touch -t $(date -d '10 MINUTE AGO' +%Y%m%d%H%M.%S) end_date
    timeout 10 find "$LOCAL_FOLDER" -newerat "start_date" ! -newerat "end_date" -print

    一般格式：
    -newerXY reference：将当前文件的时间戳与参照进行比较。XY 可以是以下值之一
    at（访问时间）、mt（修改时间）、ct（更改时间）等等。
    或描述绝对时间的字符串。
    时间。

4. 根据大小查找文件
--------------------------------------------

::

    查找大于 15MB 的文件：
    find -type f -size +15M

    查找小于 12KB 的文件：
    find -type f -size -12k

    查找大小正好为 12KB 的文件：
    find -type f -size 12k
    find -type f -size 12288c
    find -type f -size 24b
    find -type f -size 24

    一般格式：

::

    find [options] -size n[cwbkMG]

.. note::

    查找 n 块大小的图框，其中 +n 表示大于 n 块，-n 表示小于 n 块，n（不带任何符号）表示正好是 n 块。表示正好是 n 块

Block size:

1. c: bytes
2. w: 2 bytes
3. b: 512 bytes (default)
4. k: 1 KB
5. M: 1 MB
6. G: 1 GB

5. 过滤路径
-------------------------------------------------------

路径参数允许指定一个模式来匹配结果的路径。该模式也可以匹配
名称本身。

::

    只查找路径（文件夹或名称）中包含日志的文件：
    find . -type f -path '*log*'

    只查找名为日志的文件夹内的文件（任何级别）：
    find . -type f -path '*/log/*'

    只查找名为 **log** 或 **data** 的文件夹中的文件：
    find . -type f -path '*/log/*' -o -path '*/data/*'

    要查找除名为bin的文件夹中包含的文件之外的所有文件:
    find . -type f -not -path '*/bin/*'

    要查找所有文件，但 bin 或 log 文件夹中的文件除外：
    find . -type f -not -path '*log' -not -path '*/bin/*'

6. 按类型查找文件
--------------------------------------------

::

    要查找文件，请使用 -type f flag
    $ find . -type f

    要查找目录，请使用 -type d flag
    $ find . -type d

    要查找块设备，请使用 -type b flag
    $ find /dev -type b

    要查找符号链接，请使用 -type l flag
    $ find . -type l

7. 通过特定扩展查找文件
------------------------

要查找当前路径下某个扩展名的所有文件，可以使用以下查找语法。它的工作原理是
使用 bash 内置的 glob 结构来匹配所有带有 .扩展名的文件名。

::

    find /directory/to/search -maxdepth 1 -type f -name "*.extension"

要从当前目录中查找所有 .txt 类型的文件，请执行以下操作

::

    find . -maxdepth 1 -type f -name "*.txt"


17. sort
=============

sort命令在默认情况下，会按照字母顺序对文本进行排序

sort命令用于对文本文件的行进行排序，默认情况下按照ASCII码的次序排列。具体如下：

基本语法：sort [选项]... [文件]...

默认行为：sort命令会读取指定文件的内容，按行进行排序，并将结果输出到标准输出（屏幕）。如果没有指定文件，则接受标准输入。

排序方式：默认情况下，sort命令按照字符串的ASCII码值进行升序排序。这意味着它会从每行的首字符开始比较，依次向后，直到决定出顺序。

常用参数：

    -n：按照数值升序进行排序。

    -r：进行降序排序。

    -u：去除输出中的重复行。

    -k：指定排序的列，例如-k 2表示按照第二列排序。

    -t：指定列的分隔符，例如-t ','表示列之间由逗号分隔。

举个例子:

::

    sort -u -k 2 -t , example.txt 


    输出:

    Alice,20,female
    Bob,22,male
    Charlie,25,male
    Alice,28,female
    David,30,male


将对example.txt内容进行去重排序，"-k 2"决定了以行第二个字段为标准来对整个文件进行排序,"-t ,"是设置以什么来作为分段的分隔符

18. source/.
=============

source命令的详细使用说明：

1. 刷新当前的shell环境

2. 从脚本中导入环境中的Shell函数

3. 读取并执行命令和"."命令一样，./bash.sh

19. Here documents"和"here strings"
====================================

Here documents"和"here strings"是Shell脚本中用于输入多行文本到命令的机制

1. Here Documents (<<EOF):
----------------------------


- Here documents使用<<操作符后面跟随一个分隔符（如EOF），然后是你想要提供的文本，最后是同样的分隔符结束。
- 文本可以跨越多行，直到遇到结束分隔符为止。
- 可以在here document中使用变量，并且可以选择是否让Shell对其进行解析。
- 有两种类型的here documents:
    - 无限制的here documents：在<<之后直接放置分隔符，如<<EOF。这种类型的here document会进行变量替换和命令替换。
    - 有限制的here documents：在<<之后放置一个连字符和分隔符，如<<-EOF。这种类型的here document不会进行变量替换和命令替换。

2. Here Strings (<<<word):
----------------------------

- Here strings类似于here documents，但它们使用<<<操作符，并且只接受一个字符串作为输入，而不是多行文本。
- Here strings总是在双引号中进行解释，这意味着变量会被替换，但是命令不会。
- Here strings适用于只需要单行输入的情况。

19. Quoting,引号
=================



双引号和单引号的区别：

单引号:Cannot accept variables,Only show original special symbols,No backslash can escaping except '\',

双引号:Can receive the variables,can use $,\,and other special symbols,can directly use escaping backslash


20. Conditional Expressions
==============================

::

    if [[ -e $filename ]]; then
        echo "$filename exists"
    fi

-e Determine whether the file exists

-f Determine whether the file is a regular file

-d Determine whether the file is a directory

-p Determine whether the file is a pipe file

-S Determine whether the file is a Socket file

-b Determine whether the file is block device

-c Determine whether the file is a character device

-L Determine whether the file is s symbolic link

"||" 表示逻辑或（OR），当左侧的命令执行失败（返回非零值）时，才会执行右侧的命令。如果左侧的命令执行成功（返回零值），则整个表达式的结果为真。

"&&" 表示逻辑与（AND），只有当左侧的命令执行成功（返回零值）时，才会执行右侧的命令。如果左侧的命令执行失败（返回非零值），则整个表达式的结果为假。 

! not

For String
-----------

== Determine whether both are identical

!= Determine whether both are not identical

-n Determine whether the String is non-empty

-z Determine whether the String is empty/unset


Fot File
------------

-ef Determine whether both file are the same file

if u want compare a file byte by byte ,use "cmp" command

if u want a human-readable difference ,use "diff" utility command

-r Determine whether the file is readable file

-w Determine whether the file is writable file

-x Determine whether the file is executable file

For Numberical
-------------------

-eq Determine whether both number equal

-le Determine whether the number less than or equal to the other

-eq equal

-ne not equal

-le less or equal

-lt less than

-ge greater or equal

-gt greater than


if u want use >,<,==,<=,>=,The two sides must be numbers written in decimal (or in octal with a leading zero), Alternatively,use ((...)),The arithmetic expression syntax

Scripting with Parameters
==========================

In a Bash script, $# is a special variable that holds the number of positional parameters (arguments) passed to the script. It represents the count of arguments provided to the script when it was executed.

::

    #!/bin/bash

    # Load the user defined parameters
    while [[ $# > 0 ]]
    do
        case "$1" in
            -a|--valueA)
            valA="$2"
            shift
            ;;

            -b|--valueB)
            valB="$2"
            shift
            ;;

            --help|*)
            echo "Usage:"
            echo "
            --valueA \"value\""
            echo "
            --valueB \"value\""
            echo "
            --help"
            exit 1
            ;;
        esac
        shift
    done

    echo "A: $valA"
    echo "B: $valB"


"shift" command to move all parameters to the left. This effectively removes the first parameter from the list, so on the next iteration of the loop, $1 will be the second parameter, $2 will be the third parameter, and so on. The loop ends when there are no more positional parameters left.


$#: Represents the count of arguments provided to the script when it was executed. It is an integer value.

$@: Represents all of the positional parameters passed to the script as an array-like structure. It allows you to access each argument within a loop or other constructs.


Split string into an array in Bash
-----------------------------------
