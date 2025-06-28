HTML
######

1. 标记语言HTML介绍
===================

    HTML(Hyper Test Markup Language),超文本标记语言。其文件扩展名为.htm或者.html

2. 主要结构
============

:<!doctype html>: 文档声明
:<html> </html>: html文档标签 
:<head> </head>: 文件头标签 
:<title> </title>: 标题标签 
:<body> </body>: 主体标签 

文档声明用于浏览器正确显示网页

HTML文件只有一个<html></html>标签，其他部分都是html的元素体

1. meta标记符号
------------------

用于定义文件信息，对网页文件进行说明，便于搜索引擎查找，放置在<head> </head>之间

1. 设置关键字
   
::

    <meta name = "keywords" content="value">

2. 设置描述

::

    <meta name = "description" content="value">

    例如：

    设置作者：

    <meta name = "author" content="作者名字">

3. 设置字符集

::

    设置UTF-8
    <meta charset="UTF-8">

    停留2秒自动刷新并且指向新页面
    <meta http-equiv = "refresh" content="2;URL = http://www.baidu.com">

2. <title> </title> 文件标题标签
--------------------------------

title元素是文件头里唯一一个必须出现在<head></head>里

长度一般在64字符内

::

    <title> 标签页名字 </title>

3. <body></body>文件体标签
----------------------------------

网页文档的正文部分，包含许多网页设定元素


2. 文本格式标记符号
=====================

1. 标题标记符
-------------

::

    <Hn align="对齐方式"> 标题文字 </Hn>

    n 可以为1-6的数字，从(H1)最大的标题到(H6)最小的标题

    例如：

    <H1 align="对齐方式"> 标题文字 </H1>
    <H2 align="对齐方式"> 标题文字 </H2>

2. 特殊文本标记符
-----------------

1. 强调加粗标记符

::

    <b>...</b>

    <strong>...</strong>

2. 斜体文本标记符

::

    <i>...</i>

3. 上下标文本

::

    上标
    <sup>...</sup>

    下标
    <sub>...</sub>

4. 水平线标记符

::

    <HR size="5" color="red" width="300">

3. 文本编辑标记符号
====================

1. 换段标记符
-------------

1. <p></p>标签里设置段落标记

<p>...</p>里的文字超过屏幕大小会自动换行

<p align="left,center,right">...</p>

设置文本对齐方式，左，中间，右边

2. 强制换段标记符

<P> 大写P

::

    <body>

    春眠不觉晓，<P>处处闻嘀鸟。

    </body>

    输出：

    春眠不觉晓，

    处处闻嘀鸟。

3. 注释标记符

::

    <! --注释内容-->

4. 强制换行标记符<br>

放一行的末尾

::

   <p>关关雎鸠，在河之洲。窈窕淑女，君子好逑。<br>
   参差荇菜，左右流之。窈窕淑女，寤寐求之。<br>
   求之不得，寤寐思服。悠哉悠哉，辗转反侧。<br>
   参差荇菜，左右采之。窈窕淑女，琴瑟友之。<br>
   参差荇菜，左右芼之。窈窕淑女，钟鼓乐之。<br>
   </p>

4. HTML5排版标记符
==================

1.表格标记符
--------------

1. 基本结构

::

    <table>
    <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    </tr>

    <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    </tr>

    <tr>
    <td>...</td>
    <td>...</td>
    <td>...</td>
    </tr>
    </table>

<table>表示开始一个表格

<tr>表示表格的一行内容,每个<tr>就表示表格其中的一行

<td>表示在<tr>里的每个表格单元

2. 表格属性

==============   ===========================================    ======================
属性名              含义                                        常用属性值
==============   ===========================================    ======================
border              设置表格的边框(默认0,无边框)                像素值
cellspacing         设置单元格与单元格之间的空白间距            像素值(默认值为2px)
cellpadding         设置单元格内容与单元格边框之间的空白间距    像素值(默认为1px)
width               设置表格的宽度                              像素值
height              设置表格的高度                              像素值
align               设置表格在网页中的水平对其方式              left,center,right
==============   ===========================================    ======================

3. 表格实现跨行跨列

COLSPAN="n"表示跨多少列
rowspan="n"表示跨多少行

作用于单个单元格例如：

::

    <td colspan="2">...</td>
    <td rowspan="2">...</td>

    表示这个单元格跨多少行或者多少列，也就是这个单元格变大了

4. 表格的美化



:width: 设置表格宽度 px
:height: 设置表格高度 px
:border: 设置表格边框尺寸大小 px
:bordercolor: 设置表格边框颜色 rgb ("#ff0000")
:background: 设置表格背景图片 
:bgcolor: 设置表格、行、列的背景颜色 rgb
:align: 设置表格、行、列的对齐方式
:cellspacing: 表示表格内框宽度
:cellpadding: 表示表格内填充距离


2.列表标记符
-----------------

1.无序列表标记符

::

    <ul>
    <li>...</li>
    <li>...</li>
    <li>...</li>
    </ul>

<ul type="">

无序列表里的type有disc(实心圆点,默认),circle(空心圆环),square(空心正方形)


2.有序列表标记符

::

    <ol>
    <li>...</li>
    <li>...</li>
    <li>...</li>
    </ol>

有序列表里的type有5个属性值

======  =================
type    含义
======  =================
1       阿拉伯数字排序
a       小写英文字母排序
A       大小英文字母排序
i       小写罗马数字排序
I       大写罗马字母排序
======  =================

3.自定义列表

自定义列表用于对名词或者术语进行解释和描述，这种列表前面没有任何符号，没有点没有数字

::

    <dl>            自定义列表define list
    <dt>...</dt>    自定义列表标题difine title
    <dd>...</dd>    自定义列表描述difine description
    </dl>


4.图像标记符

::

    <img src="images/1.jpg" width="300" height="150" alt="1号图片">

    src     设置图像文件位置

    width/height    宽/高

    alt     光标放在图片上会有提示信息，为"1号图片"

5.HTML超链接
================

1.超链接标签
--------------

超链接格式：<a>...</a>

其中可有图片或者文字

1.href属性

href属性指向一个目标,是<a>标签不可缺少的，其值是一个网页或者资源地址，href="URL"

2.target属性

该属性用于定义该怎么打开链接

_blank:另起一个窗口打开新网页

_self:在当前窗口打开网页

_parent:在iframe框架里使用，平时等同于_self

_top:等同_self

2.指向不同类型的超链接
------------------------

1. href="file.tar.gz"           指向压缩文件
2. href="file.html"             指向html网页
3. href="file.jpg"              指向图片
4. href="file.doc"              指向doc文档
5. href="URL"                   指向网址
6. href="172.16.1.254"          指向ftp服务器
7. href="mailto:1234@qq.com"    指向邮箱
8. href="#name"                 建立书签
9. href="name"                  指向书签链接
10. href="javascript:"          创建javascript链接

3.创建图片热点区域
--------------------

HTML5中可创建3中类型的热点区域：1.矩形，2.圆形，3,多边形

使用 <map> 和 <area> 标记

::

<img src="URL" usemap="#name">
<map name="#name">
<area shape="rect" cord="10,10,100,100" href="#">
<area shape="circle" cord="120,120,50" href="#">
<area shape="poly" cord="10,20,30,40,50" href="#">
</map>

其中：1.rect(矩形),2.circle(圆形),3.poly(多边形)

矩形cord为：矩形左上角xy坐标和右下角xy坐标

圆形cord为: 圆心xy坐标和半径值

多边形cord为：矩形各个点的xy坐标

6. HTML5网页表单
=================

表单标签
---------

<form>...</form>

<form action="url" method="get|post" enctype="mime">...</form>

::

    action="url" 意思是处理提交表单的格式可以是url或者电子邮件地址
    method="get|post" 意思是提交表单的HTTP方法，默认是get
    enctype="mime" 意思是把表单提交给服务器时的互联网媒体形式

1.<input> 标签
---------------------------------

<input>是单标记，必须嵌套在<form></form>表单标签内，用于定义一个用户输入项

::

    <form>
    <input name="" type="">
    </form>

<input>标记主要有6个属性，type,name,size,value,maxlength,check.

其中type和name为必需项，name的值为相应程序中的变量名

1.1 type
''''''''''

以下表格为type主要的10中类型

============    ==========================
属性值          描述
============    ==========================
text            单行文本输入框
password        密码输入框
radio           单选按钮
checkbox        复选框
button          普通按钮
submit          提交按钮
reset           重置按钮
image           图像形式提交按钮
file            文件域
hidden          隐藏当前的input元素
============    ==========================


以下表格为<input>除type外其他属性

============    ===========================     =========================================================
属性            属性值                          描述
============    ===========================     =========================================================
name            用户自定义                      控件名称
value           用户自定义                      input控件中的默认文本值
size            正整数                          input控件在页面中显示的宽度
checked         checked                         定义选择控件默认被选中的项
maxlength       正整数                          控件允许输入的最多字符数
disabled        disabled                        当input元素加载时禁用此元素
readonly        readonly                        设置输入字段为只读
alt             text                            定义图像输入的代替文本
size            number_of_char                  定义输入的字段的宽度
src             url                             定义以提交按钮形式显示的图像url
accept          mime_type                       设置通过文件上传来提交的文件类型
============    ===========================     =========================================================

1.2 多行文本输入框<textarea>
''''''''''''''''''''''''''''''''''

结构：<textarea>...</textarea> 
属性：naem,rows,cols,wrap

name:用于指定输入框名字
rows:设置输入框初始行数，文本超过此行数会出现滚动条,(数字值)
cols:设置输入框的宽度大小,(数字值)
wrap:默认就是会自动换行，而此数据提交处理时不带有换行符的出现

1.3 下拉列表框<select>,<option>
''''''''''''''''''''''''''''''''''

<select>为下拉列表框主体，<option>为它的选项,单标记

::

    <form>
    <select name="" size="">
    <option value="">
    ...
    ...
    <option value="">
    </select>
    </form>

<select>的name,size,multiple属性

:name: 设置下拉列表的名字
:size: 可选，用于改变下拉框的大小，size值为数字,表示下拉列表显示的选项数目，默认为1,size值小于实际选项值时会添加滚动条
:multiple: 此属性可使用户多选选项

<option>的value,selected可选选项

:value: 选择后提交给服务器的值，默认为提交选项的内容
:selected: 指定选项的初始状态，表示该选项开始的时候就被选中

2.高级表单元素
---------------

1.url属性
''''''''''

<input type="url" name="userurl" max="50" min="30"/>

