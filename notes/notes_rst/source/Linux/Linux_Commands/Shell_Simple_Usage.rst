Shell_Simple_Usage
###################

1. 提取ls命令输出中的文件和目录列
==================================================

::

    find . -maxdepth 1 -type f -printf "%f\n"  # 仅文件
    find . -maxdepth 1 -type d -printf "%f\n"  # 仅目录（不包括当前目录.）

    在 find 命令的 -printf 选项中，%f 和 \n 是格式控制符，它们的含义如下：

    %f 表示仅显示文件名（不包括路径）
    \n 表示换行符，确保每个文件名单独占一行
    %p 完整路径
    %P 去掉路径里包括 find 指定的部分 

::

    ls -1A | sort -f

    -1：每行显示一个文件/目录
    -A：显示所有文件（包括 . 开头的隐藏文件，但不包括 . 和 ..）

    -f：忽略大小写排序

2. 随机数生成
==================================================

::

    shuf -i 20-59 -n 1

    awk 'BEGIN { srand(); print int(20 + rand() * 40) }'

----

3. 独立进程
==================================================

setsid 守护进程，比nohup, disown 更彻底

::

    (
        setsid sh -c '
            <commands>...
            <commands>...
        ' "$variet" &

        echo $! > /tmp/PID_FILE
    )


setsid command & 的 $! 返回的是 setsid 的子 shell PID，而非 command 的 PID。

.. note::

   ( 括号内命令将视为子进程而创建 ) &       # 后跟 & 来被 $! 捕获 进行后续控制


----

4. 标准输入</dev/null
==================================================

- 写入 /dev/null 的数据会被直接丢弃（像黑洞一样）

- 从 /dev/null 读取数据会立即返回 EOF（文件结束符）

2. 为什么 </dev/null 能让进程立即返回 EOF？

(1) 标准输入（stdin）的工作原理 标准输入就是 < , 标准输出就是 >

当进程尝试从 stdin 读取输入时（比如 read 或 scanf）：

- 如果 stdin 是终端（TTY），进程会阻塞，等待用户输入。
 
- 如果 stdin 是普通文件，进程会读取文件内容，读完时返回 EOF。
 
- 如果 stdin 是 /dev/null，内核会直接返回 EOF，而不是等待/堵塞(程序有读取动作时跳过)。

/dev/null 读取时立即返回 EOF，而不是阻塞。

</dev/null 是关闭 stdin 的标准方法，比单纯 & 更可靠。

----

5. 终止进程
==================================================

1. 简单命令

命令: kill,pkill,killall

kill -<信号> <PID>
kill -l     查看信号列表 1 挂起 9 强制终止(SIGKILL不可捕获) 15 优雅退出(SIGTERM)

pkill -<信号> <进程名>      # 终止其名称进程
killall -<信号> <进程名>    # 终止其名称相同的所有的进程

kill -- -<PGID>             # 终止进程组里的所有进程
ps -o pgid= <PID> | tr -d ' '       # 通过其中进程的ID获取进程组ID 配合上述终止命令进行控制

pkill -u <用户名>          # 终止某用户的所有进程
killall -u <用户名>        # 替代方案

kill $(ps -eo pid,etimes --sort=start_time | awk '$2 > 3600{print $1}') # 终止运行超过1小时的进程,命令还可进行查看使用

kill $(ps -eo pid,%mem --sort=-%mem | awk '$2 > 50{print $1}')          # 终止内存超过1GB的进程

2. 进程关系

- PPID：父进程ID（ps -o ppid= <PID>）
 
- PGID：进程组ID（ps -o pgid= <PID>）
 
- SID：会话ID（ps -o sid= <PID>）

每个进程对应 /proc/<PID>/ 目录

::

    cat /proc/<PID>/status   # 进程状态（内存、线程数等）
    cat /proc/<PID>/cmdline  # 完整启动命令
    ls -l /proc/<PID>/fd     # 查看进程打开的文件描述符

.. caution::

    普通用户只能查看自己的进程

    Root用户可查看所有进程（sudo ps aux）

    内核线程通常以[]括起（如[kthreadd]）

    恶意进程可能隐藏，需用unhide工具检测

查看进程: 
--------------------------------------------------

ps aux                 # 查看所有用户的所有进程（BSD风格）
ps -ef                 # 查看所有进程（标准UNIX风格）

1. 按名称

::

    pgrep -l "nginx"       # 查找nginx进程并显示PID和名称
    pidof python           # 返回所有python进程的PID

2. 按资源占用

::

    ps aux --sort=-%cpu | head -n 10   # 显示CPU占用前10的进程
    ps aux --sort=-%mem | head -n 5    # 显示内存占用前5的进程

3. 按用户/时间过滤

::

    ps -u root              # 查看root用户的进程
    ps -eo pid,lstart,cmd  # 显示进程启动时间

4. 查看进程树关系

::

    pstree -p              # 树形显示进程父子关系
    ps -ef --forest        # 类似效果（适合脚本解析）

查看进程详细信息
--------------------------------------------------

1. 查看进程打开的文件

::

    lsof -p <PID>          # 列出进程打开的所有文件
    lsof -i :80            # 查看占用80端口的进程

2. 查看进程环境变量

::

    cat /proc/<PID>/environ | tr '\0' '\n'  # 解析为可读格式

3. 查看进程资源限制

::

    cat /proc/<PID>/limits # 查看进程资源限制（如最大文件数）

4. 实时统计进程IO

::

    iotop -o               # 查看磁盘IO高的进程（需root）

实例脚本片段
-------------------------------------------------------

1. 监控<PID>进程

::

    while true; do
        if ! ps -p <PID> > /dev/null; then
            echo "进程已退出！"
            break
        fi
        sleep 5
    done

2. 记录进程资源变化

::

    watch -n 1 'ps -p <PID> -o %cpu,%mem,cmd >> log.txt'

3. PID锁 控制进程

将(<command>)子进程的$!输出到文件(.pid约定俗成),通过外置或者放在文件开头用来检查并对目标PID/PGID进行控制

::

    PID_FILE="/tmp/example.pid"

    if [ -s "$PID_FILE" ]; then
        mpv_pid="$(cat "$PID_FILE")"
        kill -- -"$(ps -o pgid= $mpv_pid | tr -d ' ')"
        rm -f "$PID_FILE"
    fi

expressions
=======================================================

::

    -b file             True if file exists and is a block special file.

    -c file             True if file exists and is a character special file.

    -d file             True if file exists and is a directory.

    -e file             True if file exists (regardless of type).

    -f file             True if file exists and is a regular file.

    -g file             True if file exists and its set group ID flag is set.

    -h file             True if file exists and is a symbolic link.

    -k file             True if file exists and its sticky bit is set.

    -n string           True if the length of string is nonzero.

    -p file             True if file is a named pipe (FIFO).

    -r file             True if file exists and is readable.
    -s file             True if file exists and has a size greater than zero.

    -t file_descriptor  True if the file whose file descriptor number is file_descriptor is open and is associated with a terminal.

    -u file             True if file exists and its set user ID flag is set.

    -w file             True  if  file  exists  and  is  writable.  True indicates only that the write flag is on.  The file is not
                        writable on a read-only file system even if this test indicates true.

    -x file             True if file exists and is executable.  True indicates only that the execute flag is on.  If file is a  di‐
                        rectory, true indicates that file can be searched.

    -z string           True if the length of string is zero.

    -L file             True if file exists and is a symbolic link.  This operator is retained for compatibility with previous ver‐
                        sions of this program.  Do not rely on its existence; use -h instead.

    -O file             True if file exists and its owner matches the effective user id of this process.

    -G file             True if file exists and its group matches the effective group id of this process.

    -S file             True if file exists and is a socket.

    file1 -nt file2     True if file1 and file2 exist and file1 is newer than file2.

    file1 -ot file2     True if file1 and file2 exist and file1 is older than file2.

    file1 -ef file2     True if file1 and file2 exist and refer to the same file.

    string              True if string is not the null string.

    s1 = s2             True if the strings s1 and s2 are identical.

    s1 != s2            True if the strings s1 and s2 are not identical.

    s1 < s2             True if string s1 comes before s2 based on the ASCII value of their characters.

    s1 > s2             True if string s1 comes after s2 based on the ASCII value of their characters.

    n1 -eq n2           True if the integers n1 and n2 are algebraically equal.

    n1 -ne n2           True if the integers n1 and n2 are not algebraically equal.

    n1 -gt n2           True if the integer n1 is algebraically greater than the integer n2.

    n1 -ge n2           True if the integer n1 is algebraically greater than or equal to the integer n2.

    n1 -lt n2           True if the integer n1 is algebraically less than the integer n2.

    n1 -le n2           True if the integer n1 is algebraically less than or equal to the integer n2.

    These primaries can be combined with the following operators:

    ! expression  True if expression is false.

    expression1 -a expression2      True if both expression1 and expression2 are true.

    expression1 -o expression2      True if either expression1 or expression2 are true.

    (expression)  True if expression is true.
    The -a operator has higher precedence than the -o operator.
 

Interesting Field Codes
=======================================================

1. 需要 先尝试推送，失败后重试

::

    max_retries=3
    count=0

    while [ $count -lt $max_retries ]; do
        if git push origin main; then
            echo "推送成功"
            break
        else
            ((count++))
            echo "尝试第 $count 次重试..."
            sleep 2
        fi
    done

    if [ $count -eq $max_retries ]; then
        echo "推送失败，已达最大重试次数"
        exit 1
    fi

2. check if the standard output is terminal or not
=======================================================

::

    if [ -t 1 ]; then
        echo "Output is going to a terminal (color supported)"
    else
        echo "Output is being piped/redirected (avoid colors)"
    fi
