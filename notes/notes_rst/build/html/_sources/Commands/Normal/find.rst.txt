find
##################

::

    find [路径] [选项] [表达式]

基本查找
---------

::

    find /home -name "*.txt"      # 在/home目录下查找所有.txt文件
    find . -name "file*"          # 当前目录下查找以"file"开头的文件
    find / -type d -name "docs"   # 查找所有名为"docs"的目录

基本选项	
''''''''''

.. seealso::

    \-name       "pattern"	    按文件名匹配（支持通配符 \*, ?, []）

    \-iname      "pattern"	    不区分大小写的 -name

    \-path       "pattern"	    按路径匹配（支持通配符）

    \-ipath      "pattern"	    不区分大小写的 -path

    \-regex      "pattern"	    使用正则表达式匹配完整路径

    \-iregex     "pattern"	    不区分大小写的 -regex

按类型查找
-----------

::

    find / -type f                # 查找所有普通文件
    find / -type d                # 查找所有目录
    find / -type l                # 查找所有符号链接

文件类型	
''''''''''

.. seealso::

    \-type f	查找普通文件

    \-type d	查找目录

    \-type l	查找符号链接

    \-type b	查找块设备文件

    \-type c	查找字符设备文件

    \-type p	查找命名管道（FIFO）

    \-type s	查找套接字文件

按时间查找
--------------

::

    find / -mtime -7             # 查找7天内修改过的文件
    find / -mtime +30            # 查找30天前修改过的文件
    find / -atime -1             # 查找24小时内访问过的文件
    find / -newer file.txt       # 查找比file.txt更新的文件

时间相关	
''''''''''

.. seealso::

    \-mtime n	查找 n 天前修改的文件（+n=超过n天，-n=n天内）

    \-atime n	查找 n 天前访问的文件

    \-ctime n	查找 n 天前状态（权限/所有者）变化的文件

    \-mmin n	查找 n 分钟前修改的文件

    \-amin n	查找 n 分钟前访问的文件

    \-cmin n	查找 n 分钟前状态变化的文件

    \-newer file	查找比 file 更新的文件

    \-anewer file	查找比 file 更晚访问的文件

    \-cnewer file	查找比 file 更晚状态变化的文件


按大小查找
----------

::

    find / -size +10M            # 查找大于10MB的文件
    find / -size -1G             # 查找小于1GB的文件
    find / -size +100k -size -1M # 查找大于100KB小于1MB的文件

大小相关	
''''''''

.. seealso::

    \-size n[cwbkMG]	查找大小为 n 的文件（c=字节，w=字，b=块，k=KB，M=MB，G=GB）

    \-size +n	查找大于 n 的文件

    \-size -n	查找小于 n 的文件

按权限查找
-----------

::

    find / -perm 644             # 查找权限为644的文件
    find / -perm -u=r            # 查找用户可读的文件
    find / -perm /a+x            # 查找任何人有执行权限的文件

权限相关	
'''''''''

.. seealso::

    \-perm mode	查找权限 完全匹配 mode 的文件（如 -perm 644）

    \-perm -mode	查找权限 包含所有 mode 位的文件（如 -perm -u=rw）

    \-perm /mode	查找权限 包含任意 mode 位的文件（如 -perm /a+x）

    \-user name	查找属于用户 name 的文件

    \-group name	查找属于组 name 的文件

    \-nouser	查找没有所属用户的文件（用户被删除）

    \-nogroup	查找没有所属组的文件（组被删除）


组合条件
----------

::

    find / -name "*.log" -and -mtime +30  # 查找30天前的.log文件
    find / -name "*.tmp" -or -name "*.temp" # 查找.tmp或.temp文件
    find / ! -name "*.txt"                # 查找不是.txt结尾的文件

逻辑操作	
''''''''

.. seealso::

    \-a / -and	逻辑与（默认）

    \-o / -or	逻辑或

    \! / -not	逻辑非

对查找结果执行操作
---------------------

::

    find . -name "*.bak" -delete          # 删除所有.bak文件
    find /tmp -type f -exec rm {} \;      # 删除/tmp下所有文件
    find . -name "*.jpg" -exec chmod 644 {} \; # 修改权限
    find . -name "*.old" -ok rm {} \;     # 交互式删除(询问确认)
    
执行操作	
'''''''''

.. seealso::

    \-exec command {} \;	对匹配的文件执行 command（{} 替换为文件名，\; 结束）

    \-exec command {} +	类似 -exec，但更高效（一次性传递多个文件）

    \-ok command {} \;	交互式 -exec（每次执行前询问确认）

    \-delete	删除匹配的文件

    \-print	打印匹配的文件（默认）

    \-print0	以 \0 分隔文件名（适合处理含空格的文件）


其他有用选项
--------------

::

    find / -maxdepth 3 -name "file"      # 最多搜索3层子目录
    find / -user root                    # 查找root用户的文件
    find / -group dev                    # 查找dev组的文件
    find / -empty                        # 查找空文件或目录

其他选项	
'''''''''

.. seealso::

    \-maxdepth n	最大搜索深度（目录层级）

    \-mindepth n	最小搜索深度（目录层级）

    \-follow	跟随符号链接（已弃用，推荐用 -L）

    \-L	跟随符号链接（解析链接指向的真实文件）

    \-P	不跟随符号链接（默认）

    \-D debugopts	启用调试输出（如 -D tree 显示搜索树）

    \-O n	优化级别（1=文件名优先，3=深度优先）

-----------

在 Linux/Unix 中，文件名可能包含空格或特殊字符（如换行符），直接使用 find + xargs 可能会导致错误解析。-print0 和 xargs -0 可以安全处理这类文件名

为什么要用 -print0 和 xargs -0？
********************************

默认情况下：

* find 用 换行符 \n 分隔文件名。

* xargs 用 空格/制表符/换行符 分隔输入。

* 如果文件名包含空格或换行符，xargs 会错误地拆分成多个参数：

::

    # ❌ 错误示例：如果文件名是 "hello world.txt"，会被拆分成 "hello" 和 "world.txt"
    find . -name "*.txt" | xargs rm

解决方案：

* find -print0：用 \0（NULL 字符） 分隔文件名（\0 是唯一不能出现在文件名中的字符）。

* xargs -0：从输入中读取 \0 分隔的内容。
 
------------

使用方法
********

::

    find [路径] [条件] -print0 | xargs -0 [命令]

示例

删除所有 .txt 文件（安全处理空格）

::

    find . -name "*.txt" -print0 | xargs -0 rm -v

* -print0：find 输出以 \0 分隔的文件名。

* xargs -0：读取 \0 分隔的输入并传递给 rm。

查找并复制文件到目标目录

::

    find /source -name "*.pdf" -print0 | xargs -0 cp -t /target/

* cp -t：指定目标目录（避免 xargs 参数位置问题）。

**查找并统计文件行数**

::

    find . -type f -name "*.sh" -print0 | xargs -0 wc -l

**结合 grep 搜索内容**

::

    find . -type f -name "*.conf" -print0 | xargs -0 grep -l "error"

* grep -l：只显示包含匹配内容的文件名。

-------------

更安全的替代方案：-exec
*************************

如果不想用 xargs，可以直接用 find -exec，它原生支持 \0 安全处理：

::

    # 删除所有 .tmp 文件（无需 xargs）
    find . -name "*.tmp" -exec rm {} +

* {} +：类似 xargs，高效传递多个参数。

-------------

特殊情况处理
************

文件名包含引号或特殊字符

-print0 + xargs -0 仍然安全：

::

    # 文件名是 "file'name.txt" 或 "file\nname.txt"
    find . -name "*.txt" -print0 | xargs -0 rm

**调试 xargs 命令**

用 -t 显示实际执行的命令：

::

    find . -name "*.log" -print0 | xargs -0 -t rm
    # 输出：rm ./a.log ./b log.txt ...

