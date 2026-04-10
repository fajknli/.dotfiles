# reStructuredText (reST) 速查表

## 一句话理解

reStructuredText 是一种轻量级标记语言，用于编写文档，Sphinx 默认使用。

```rst
标题
====

这是正文。*斜体* **粗体** ``行内代码``。
```

## 标题

```rst
一级标题（上划线可选）
########################

二级标题
========

三级标题
--------

四级标题
~~~~~~~~

五级标题
^^^^^^^^
```

## 段落和换行

```rst
这是一个段落。段落之间用空行分隔。

这是另一个段落。

一行结尾加两个空格  
可以实现换行。
```

## 文本修饰

| 语法 | 效果 |
|------|------|
| `*斜体*` | *斜体* |
| `**粗体**` | **粗体** |
| ```行内代码```` | `行内代码` |
| `\*转义\*` | *转义*（显示为文字） |

## 列表

### 无序列表

```rst
* 项目 1
* 项目 2
  * 子项目 2.1
  * 子项目 2.2
* 项目 3

- 用短横也可以
- 效果相同
```

### 有序列表

```rst
1. 第一项
2. 第二项
#. 自动编号（延续上一个数字）
#. 继续自动编号

(一) 中文编号
(二) 第二项
```

### 定义列表

```rst
术语
    定义内容，可以有多行。
    缩进表示继续。

另一个术语
    另一个定义。
```

## 代码块

```rst
.. code-block:: bash

    # 这是代码
    echo "hello"

使用 `::` 简化：
::

    # 简化写法
    echo "hello"
```

支持的语言：bash、python、yaml、json、markdown 等。

## 链接

### 外部链接

```rst
`显示文字 <https://example.com>`_

直接写 URL：https://example.com

匿名链接：`Google <https://google.com>`__
```

### 内部链接（文档内）

```rst
:doc:`/path/to/doc`

:doc:`显示文字 </path/to/doc>`
```

### 内部链接（标题）

```rst
.. _我的标签:

标题
====

跳转到 :ref:`我的标签`
```

## 图片

```rst
.. image:: /path/to/image.png
   :alt: 替代文字
   :width: 400px
   :align: center
```

## 表格

### 简单表格

```rst
=====  =====  =====
列1    列2    列3
=====  =====  =====
A      B      C
D      E      F
=====  =====  =====
```

### 网格表格

```rst
+-----+-----+-----+
| A   | B   | C   |
+=====+=====+=====+
| 1   | 2   | 3   |
+-----+-----+-----+
| 4   | 5   | 6   |
+-----+-----+-----+
```

### 列表表格

```rst
.. list-table:: 表格标题
   :header-rows: 1
   :widths: 20 30 50

   * - 列1
     - 列2
     - 列3
   * - 值1
     - 值2
     - 值3
```

## 注释和提示

```rst
.. note:: 这是一个提示。

.. warning:: 这是一个警告。

.. tip:: 这是一个小技巧。

.. important:: 这是重要信息。

.. caution:: 这是注意事项。

.. seealso:: 另请参阅相关文档。
```

## 分隔线

```rst
----
```

四个或更多短横。

## 脚注

```rst
这是带脚注的文字 [1]_。

.. [1] 脚注内容。
```

## 引用和提示框

```rst
.. admonition:: 自定义标题
   :class: custom

   自定义提示框内容。
```

## 行内修饰

| 语法 | 效果 |
|------|------|
| `:guilabel:` | GUI 标签 |
| `:kbd:` | 键盘按键 |
| `:menuselection:` | 菜单选择 |
| `:file:` | 文件名 |
| `:command:` | 命令名 |

```rst
按 :kbd:`Ctrl+C` 退出。

选择 :menuselection:`文件 --> 打开`。

运行 :command:`ls -la`。
```

## 目录树

```rst
.. toctree::
   :maxdepth: 2
   :caption: 目录标题

   page1
   page2
   subdir/index
```

| 选项 | 说明 |
|------|------|
| `:maxdepth:` | 最大深度 |
| `:caption:` | 目录标题 |
| `:glob:` | 支持通配符 |
| `:hidden:` | 隐藏目录树 |
| `:titlesonly:` | 只显示标题 |

## 包含文件

```rst
.. include:: /path/to/file.rst

.. literalinclude:: /path/to/code.py
   :language: python
   :lines: 1-10
```

## 替换

```rst
|版本| 是最新版本。

.. |版本| replace:: 2.0
```

## 条件标记

```rst
.. only:: html

   只在 HTML 输出中显示。

.. only:: latex

   只在 LaTeX 输出中显示。
```

## 常用指令速查

| 指令 | 用途 |
|------|------|
| `.. code-block::` | 代码块 |
| `.. note::` | 提示 |
| `.. warning::` | 警告 |
| `.. image::` | 图片 |
| `.. figure::` | 带标题的图片 |
| `.. table::` | 表格 |
| `.. list-table::` | 列表表格 |
| `.. toctree::` | 目录树 |
| `.. include::` | 包含文件 |
| `.. literalinclude::` | 包含代码文件 |
| `.. raw::` | 原始输出（HTML/LaTeX） |

## 一句话总结

reST 核心：`=` 划线标题，`*斜体*` `**粗体**` ``` ``行内代码`` ```，代码块用 `.. code-block:: lang`，链接用 `` `文字 <url>`_``，图片用 `.. image::`，提示用 `.. note::`，目录用 `.. toctree::`。Sphinx 文档首选格式。
