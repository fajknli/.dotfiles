Python_Libraries
###################


Top Python Libraries in 2024
=============================

====================    ===============================================================================================
库名                    主要优势
====================    ===============================================================================================
1. Requests             简化 HTTP 请求，在 Python 中实现简单高效的网络通信。
2. FastAPI              基于标准 Python 类型提示，为使用 Python 构建 API 提供现代、快速（高性能）的网络框架
3. Asyncio              增强 Python 中的异步编程功能，让编写并发代码变得更容易
4. aiohttp              在 Python 中启用异步 HTTP 客户端/服务器功能
5. Tkinter              提供用 Python 创建图形用户界面应用程序的简单方法
6. Pygame               促进用 Python 开发视频游戏和多媒体应用程序
7. Pillow               功能强大、用户友好的 Python 图像处理库
8. OpenCV               在 Python 中为各种应用提供强大的图像处理和计算机视觉任务
9. Kivy                 可为各种设备创建创新的多点触控应用程序
10. NumPy               为 Python 提供强大的数组操作和数值计算功能
11. Pandas              提供快速灵活的数据结构，可轻松直观地处理结构化数据和时间序列数据
12. SciPy               用 Python 提供高级数学函数和算法，增强科学计算能力
13. Matplotlib          为在 Python 中创建静态、动画和交互式可视化效果提供了一个综合库
14. Seaborn             利用高级界面绘制美观、翔实的统计图形，增强 Python 的数据可视化功能
15. Bokeh               用 Python 创建交互式、视觉效果好的数据可视化工具
16. Sci-Kit Learn       为使用 Python 进行数据挖掘和数据分析提供多种简单高效的工具
17. TensorFlow          促进机器学习模型（尤其是深度学习）的构建和训练，重点关注可扩展性和性能
18. PyTorch             为深度学习和张量计算提供动态、直观的框架，并提供强大的 GPU 加速支持
19. Keras               通过高级、用户友好的应用程序接口，简化深度学习模型的创建和训练
20. Theano              优化并高效评估数学表达式，尤其是多维数组的数学表达式
21. LightGBM            为大规模机器学习提供快速、分布式和高性能梯度提升框架
22. PyCaret             简化机器学习工作流程，通过自动化方法使其更易用、更高效
23. Scrapy              用 Python 简化网络搜索和数据提取流程
24. BeautifulSoup       简化从网页中抓取信息的过程，使解析和浏览 HTML 和 XML 文档变得更容易
====================    ===============================================================================================

1. Pillow
==============

Pillow 是 Python 中较为基础的图像处理库，主要用于图像的基本处理，比如裁剪图像、调整图像大小和图像颜色处理等。

1.1 pip包管理器安装
---------------------

创建虚拟环境安装:

::

    # 创建一个<virtenv_dirname>名字的虚拟目录环境:
    python -m venv <virtenv_dirname>

    # 激活虚拟环境：
    source <virtenv_dirname>/bin/activate

    # 在虚拟环境中安装Pillow：
    pip install pillow

    # 验证是否已经安装
    在Python的REPL(交互模式)下，输入"import pillow",若无报错，说明成功安装



1.2 打开和保存图片 
----------------------

::

    from PIL import Image

    # 打开一个jpg图像文件
    im = Image.open('test.jpg')

    # 显示图片
    im.show()

    # 保存图片
    im.save('new_test.jpg')

1.3 图片的剪裁和缩放
--------------------------

::

    from PIL import Image

    # 打开一个jpg图像文件
    im = Image.open('test.jpg')

    # 图片剪裁，参数为一个四元组，分别表示被裁剪矩形区域的左上角 x、y 坐标和右下角 x，y 坐标,原点为右上角(0,0)
    im_cropped = im.crop((50, 50, 150, 150))

    # 保存剪裁后的图片
    im_cropped.save('new_test_cropped.jpg')

    # 图片缩放，参数为一个二元组，表示新的图片大小
    im_resized = im.resize((200, 200))

    # 保存缩放后的图片
    im_resized.save('new_test_resized.jpg')

1.4 图像拷贝和粘贴操作 
--------------------------

::

    from PIL import Image

    # 打开一个jpg图像文件
    img1 = Image.open('test.jpg')

    # Image 类提供了 copy() 和 paste() 方法来实现图像的复制和粘贴
    # 创建img1的副本
    img2 = img1.copy()

    # 将img2粘贴到img1上，指定目标区域为(0, 0, 100, 100)
    img1.paste(img2, (0, 0, 100, 100))

    # 保存结果图像
    img1.save('new_test.jpg')

1.5 图片的旋转和翻转
--------------------------------------------

::

    from PIL import Image

    # 打开一个jpg图像文件
    im = Image.open('test.jpg')

    # # 顺时针旋转45度，参数为旋转的角度
    im_rotated = im.rotate(45)

    # im.rotate(angle, resample=PIL.Image.NEAREST, expand=None, center=None, translate=None, fillcolor=None)
    # angle：表示任意旋转的角度；
    # resample：重采样滤波器，默认为 PIL.Image.NEAREST 最近邻插值方法；
    # expand：可选参数，表示是否对图像进行扩展， False 或者省略，则表示按原图像大小输出；
    # center：可选参数，指定旋转中心，参数值是长度为 2 的元组，默认以图像中心进行旋转；
    # translate：参数值为二元组，表示对旋转后的图像进行平移，以左上角为原点；
    # fillcolor：可选参数，填充颜色，图像旋转后，对图像之外的区域进行填充。

    # 保存旋转后的图片
    im_rotated.save('new_test_rotated.jpg')

    # Image.FLIP_LEFT_RIGHT：左右水平翻转；
    # Image.FLIP_TOP_BOTTOM：上下垂直翻转；
    # Image.ROTATE_90：图像顺时针旋转 90 度；
    # Image.ROTATE_180：图像顺时针旋转 180 度；
    # Image.ROTATE_270：图像顺时针旋转 270 度；
    # Image.TRANSPOSE：图像转置；
    # Image.TRANSVERSE：图像横向翻转。
    im_flipped = im.transpose(Image.FLIP_LEFT_RIGHT)

    # 保存翻转后的图片
    im_flipped.save('new_test_flipped.jpg')

1.6 图像降噪处理
------------------

::

    from PIL import Image, ImageFilter

    # 打开图像文件
    image = Image.open("example.jpg")

    # 应用模糊滤镜
    blurred_image = image.filter(ImageFilter.BLUR)

    # 保存模糊后的图像
    blurred_image.save("blurred_example.jpg")


==============================  ======================================================================================
滤波器名称                      说明
==============================  ======================================================================================
ImageFilter.BLUR 	            模糊滤波，即均值滤波
ImageFilter.CONTOUR 	        轮廓滤波，寻找图像轮廓信息,素描一样
ImageFilter.DETAIL 	            细节滤波，使得图像显示更加精细
ImageFilter.FIND_EDGES 	        寻找边界滤波（找寻图像的边界信息）
ImageFilter.EMBOSS 	            浮雕滤波，以浮雕图的形式显示图像
ImageFilter.EDGE_ENHANCE 	    边界增强滤波
ImageFilter.EDGE_ENHANCE_MORE 	深度边缘增强滤波
ImageFilter.SMOOTH 	            平滑滤波
ImageFilter.SMOOTH_MORE 	    深度平滑滤波
ImageFilter.SHARPEN 	        锐化滤波
ImageFilter.GaussianBlur() 	    高斯模糊
ImageFilter.UnsharpMask() 	    反锐化掩码滤波
ImageFilter.Kernel() 	        卷积核滤波
ImageFilter.MinFilter(size) 	最小值滤波器，从 size 参数指定的区域中选择最小像素值，然后将其存储至输出图像中。
ImageFilter.MedianFilter(size) 	中值滤波器，从 size 参数指定的区域中选择中值像素值，然后将其存储至输出图像中。
ImageFilter.MaxFilter(size) 	最大值滤波器
ImageFilter.ModeFilter() 	    模式滤波
==============================  ======================================================================================

1.7 图像颜色处理
------------------

ImageColor 支持多种颜色模式的的命名（即使用固定的格式对颜值进行表示），比如我们熟知的 RGB 色彩模式，除此之外，还有 HSL （色调-饱和度-明度）、HSB （又称 HSV，色调-饱和度-亮度）色彩模式。下面对 HSL 做简单介绍：

    H：即 Hue 色调，取值范围 0 -360，其中 0 表示“red”，120 表示 “green”，240 表示“blue”；

    S：即 Saturation 饱和度，代表色彩的纯度，取值 0~100%，其中 0 代表灰色（gry），100% 表示色光最饱和；

    L：即 Lightness 明度，取值为 0~100%，其中 0 表示“black”黑色，50% 表示正常颜色，100% 则表示白色。



1. 调整亮度（Brightness）：
可以使用ImageEnhance.Brightness类来调整图像的亮度。

2. 调整对比度（Contrast）：
使用ImageEnhance.Contrast类可以调整图像的对比度。

3. 调整色彩饱和度（Color Saturation）：
ImageEnhance.Color类允许你调整图像的色彩饱和度。

4. 调整色调（Hue）：
通过ImageEnhance.Hue类可以调整图像的色调。

5. 调整锐度（Sharpness）：
ImageEnhance.Sharpness类用于调整图像的锐度


::

    from PIL import Image, ImageEnhance

    # 打开图像文件
    image = Image.open('input.jpg')

    # 创建亮度增强对象，并通过enhance()方法将图像的亮度增加了一倍
    enhancer_brightness = ImageEnhance.Brightness(image)
    image_brightened = enhancer_brightness.enhance(2.0)  # 增加亮度，因子为2.0

    # 创建对比度增强对象，并通过enhance()方法将图像的对比度减少了一半
    enhancer_contrast = ImageEnhance.Contrast(image_brightened)
    image_contrast_adjusted = enhancer_contrast.enhance(0.5)  # 减少对比度，因子为0.5

    # 显示处理后的图像
    image_contrast_adjusted.show()

    # 保存处理后的图像
    image_contrast_adjusted.save('output.jpg')

.. note::

    enhance()方法的参数是一个浮点数，表示增强的程度。值为1.0表示保持原样，小于1.0表示减少效果，大于1.0表示增加效果。

获取图像颜色

::

    from PIL import ImageColor

    # 获取颜色名字 "red" 对应的RGB值
    rgb_value = ImageColor.getrgb("red")
    print(f"Red color RGB value: {rgb_value}")

    # 查看所有预定义的颜色名字及其对应的RGB值
    for color_name, rgb in ImageColor.COLORS.items():
        print(f"{color_name}: {rgb}")

提取目标像素的颜色值

::

    from PIL import Image

    # 打开图像文件
    image = Image.open("example.jpg")

    # 获取指定像素的 RGB 值
    x, y = 10, 20
    rgb_value = image.getpixel((x, y))

    print(f"RGB值为： {rgb_value}")


1.8 图像上绘制图形和文本
--------------------------

::

    from PIL import Image, ImageDraw, ImageFont

    # 打开图像文件
    image = Image.open("example.jpg")

    # 创建一个ImageDraw对象
    draw = ImageDraw.Draw(image)

    # 绘制一个矩形
    draw.rectangle([50, 50, 150, 150], outline="red", width=3)

    # 设置字体和大小
    font = ImageFont.truetype("arial.ttf", 20)

    # 在图像上添加文字
    text = "Hello, World!"
    text_position = (50, 50)  # 文字的位置坐标
    text_color = (255, 255, 255)  # 文字的颜色，这里使用RGB格式表示白色
    draw.text(text_position, text, font=font, fill=text_color)

    # 绘制线段
    draw.line((100, 100, 200, 200), fill="red", width=3)

    # 绘制椭圆形
    draw.ellipse((150, 150, 250, 250), outline="blue", width=2)

    # 绘制矩形
    draw.rectangle((50, 200, 150, 300), outline="green", width=3)

    # 绘制多边形
    polygon_points = [(200, 200), (300, 200), (350, 300), (250, 350)]
    draw.polygon(polygon_points, outline="yellow", width=2)

    # 保存修改后的图像
    image.save("output.jpg")

1.9 convert()切换模式
---------------------------------

Pillow 库中的 convert() 方法支持多种不同的模式来转换图像。这里是一些常用的模式：



    "L": 灰度图（Luminosity），将图像转换为灰度图，即黑白图像。

    "RGB": 红绿蓝三原色模式，这是最常见的用于显示设备（如电脑屏幕、电视等）的模式。

    "RGBA": 带有Alpha通道的红绿蓝三原色模式，用于包含透明信息的图像。

    "CMYK": 青、品红、黄、黑四色印刷模式，常用于印刷行业。

    "YCbCr": 一种常用于视频的彩色空间，与 RGB 类似，但适用于压缩。

    "I;16": 16位整数灰度图。

    "F": 浮点数表示的灰度图。

    "P": 使用调色板的RGB图像，用在具有有限颜色深度的旧式系统上。

    "HSV": 色调、饱和度、明度模式，对应于人类对颜色的感知方式。

    "HLS": 色调、亮度、饱和度模式，与 HSV 相似，但是亮度和饱和度分开处理。

    "LAB": 国际照明委员会（CIE）L*a*b*色彩空间。

    "XYZ": 国际照明委员会（CIE）X*Y*Z*色彩空间。

    "YUV": 欧洲电视制式的色彩空间。

例如，以下代码展示了如何将一张图片转换为灰度图：

::

    from PIL import Image

    # 打开一个图像文件
    img = Image.open('example.jpg')

    # 使用 convert 方法转换图像为灰度图
    gray_img = img.convert('L')

    # 显示图像以验证效果
    gray_img.show()


2. Colorama
===============

安装

::

    pip install colorama

2.导入Colorama库。在你的Python代码中，添加以下代码：

::

    from colorama import Fore, Back, Style


3.使用Colorama库为文本添加颜色。例如，将文本颜色更改为红色，可以使用以下代码：

::

    print(Fore.RED + "这是红色文本")

4.使用Style类更改文本样式。例如，将文本样式更改为粗体，可以使用以下代码：

::

    print(Style.BRIGHT + "这是粗体文本")

5.使用Back类更改背景颜色。例如，将背景颜色更改为黄色，可以使用以下代码：

::

    print(Back.YELLOW + "这是黄色背景")

6.重置文本样式和颜色。在使用Colorama库后，可以使用Style.RESET_ALL来重置文本样式和颜色，以便后续的输出不会被影响。例如：

::

    print(Style.RESET_ALL)



1. 例子
---------

::

    from colorama import Fore, Back, Style
    print(Fore.RED + "这是红色文本")
    print(Style.BRIGHT + "这是粗体文本")
    print(Back.YELLOW + "这是黄色背景")
    print(Style.RESET_ALL)
    print('回到了初始化的颜色字体了')

可用的格式化常数有

::

    Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    Style: DIM, NORMAL, BRIGHT, RESET_ALL

    Style.RESET_ALL 重置前景、背景和亮度。Colorama 会在程序退出时自动执行重置。

如果您发现自己在每次打印结束时都要重复发送重置序列来关闭颜色变化，那么 init(autoreset=True) 将自动完成这一操作：

::

    from colorama import init
    init(autoreset=True)
    print(Fore.RED + 'some red text')
    print('automatically back to default color again')

3. requests
=============

下载

::

    $ python -m pip install requests



4. Scrapy
=============


