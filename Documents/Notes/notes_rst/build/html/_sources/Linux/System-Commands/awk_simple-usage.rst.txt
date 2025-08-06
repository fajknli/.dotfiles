awk 数据处理
##############################

**awk 语法格式**

::

    awk [参数] [处理内容] [操作对象]

用法案例:

1.在Linux/Unix中交换文件的第一列和第二列

::

    这会交换前两列的位置，并保留原始分隔符（通常是空格或制表符）。
    awk '{print $2, $1}' input.txt > output.txt

    如果列之间有特定分隔符（如逗号），可以这样处理
    awk -F',' '{print $2 "," $1}' input.csv > output.csv

    使用sed（适用于简单情况）
    sed -E 's/^([^ ]+) +([^ ]+)/\2 \1/' input.txt > output.txt

    使用cut和paste组合
    paste <(cut -d' ' -f2 input.txt) <(cut -d' ' -f1 input.txt) > output.txt

2.使用awk合并两个文件的第一列到一个文件的两列

::

    使用paste和awk组合
    paste file1 file2 | awk '{print $1, $NF}'

    直接使用awk处理两个文件
    awk 'NR==FNR{a[NR]=$1; next} {print a[FNR], $1}' file1 file2 > output.txt

    使用join命令（如果文件行数相同）
    join -1 1 -2 1 -o 1.1,2.1 file1 file2 > output.txt
