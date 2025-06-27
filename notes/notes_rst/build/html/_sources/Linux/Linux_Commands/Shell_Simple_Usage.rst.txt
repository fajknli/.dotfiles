Shell_Simple_Usage
###################

1. 提取ls命令输出中的文件和目录列

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

