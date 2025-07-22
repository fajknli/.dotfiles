ColorScheme
#################

ANSI颜色(ANSI Color Codes) 控制终端的文本颜色、背景色、格式(粗体或者下划线)
的标准编码系统。它基于ANSI转义序列(ANSI Escape Sequences)。由美国国家标准协会
制定，最初用于控制早期计算机终端的显示效果

ANSI颜色代码以 ``\033[`` 开头， ``\033`` 是ASCII里的ESC字符，
``[`` 表示参数的开始，后面接颜色代码或者格式代码，用分号分隔，最后以m结尾。

例如：

::

    \033[1;32m # 粗体绿色文本

文本颜色（前景色）

==========  ==========  ================ ====================================================
前景色代码  背景色代码  颜色             色卡  
==========  ==========  ================ ====================================================
40          30          黑色 ``black``   .. image:: https://placehold.co/15x15/ffffff/fff.png
41          31          红色 ``red``     .. image:: https://placehold.co/15x15/ff0000/fff.png
42          32          绿色 ``green``   .. image:: https://placehold.co/15x15/00ff00/fff.png
43          33          黄色 ``yellow``  .. image:: https://placehold.co/15x15/ffff00/fff.png
44          34          蓝色 ``blue``    .. image:: https://placehold.co/15x15/0000ff/fff.png
45          35          洋红 ``magenta`` .. image:: https://placehold.co/15x15/ff00ff/fff.png
46          36          青色 ``cyan``    .. image:: https://placehold.co/15x15/00ffff/fff.png
47          37          白色 ``white``   .. image:: https://placehold.co/15x15/000000/fff.png
==========  ==========  ================ ====================================================

文本样式

==== ============
代码 效果        
==== ============
0    重置所有样式
1    粗体        
2    弱化        
3    斜体        
4    下划线      
5    闪烁        
7    反色        
9    删除线      
==== ============
