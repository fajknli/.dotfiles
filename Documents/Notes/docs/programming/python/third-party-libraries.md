# Python 第三方库速查

## Requests - HTTP 请求

```python
import requests

# GET 请求
response = requests.get("https://api.github.com/users/octocat")
print(response.status_code)  # 200
print(response.json())       # 解析 JSON
print(response.text)         # 原始文本

# 带参数
params = {"q": "python", "page": 1}
response = requests.get("https://api.github.com/search/repositories", params=params)

# 自定义请求头
headers = {"User-Agent": "MyApp/1.0", "Authorization": "token xxx"}
response = requests.get("https://api.github.com/user", headers=headers)

# POST 请求（表单）
data = {"username": "user", "password": "pass"}
response = requests.post("https://httpbin.org/post", data=data)

# POST 请求（JSON）
json_data = {"name": "张三", "age": 25}
response = requests.post("https://httpbin.org/post", json=json_data)

# 文件上传
files = {"file": open("image.jpg", "rb")}
response = requests.post("https://httpbin.org/post", files=files)

# 下载文件
response = requests.get("https://example.com/image.jpg", stream=True)
with open("image.jpg", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

# 会话（保持 Cookie）
session = requests.Session()
session.post("https://example.com/login", data={"user": "admin", "pass": "123"})
response = session.get("https://example.com/dashboard")

# 超时设置
response = requests.get("https://api.example.com", timeout=5)

# 代理
proxies = {"http": "http://proxy:8080", "https": "https://proxy:8080"}
response = requests.get("https://example.com", proxies=proxies)

# 异常处理
try:
    response = requests.get("https://example.com", timeout=5)
    response.raise_for_status()  # 状态码不是 2xx 时抛出异常
except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")
```

## Pillow - 图像处理

```python
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# 打开和保存
img = Image.open("input.jpg")
img.save("output.png")
img.show()

# 获取信息
print(img.size)      # (1920, 1080)
print(img.format)    # JPEG
print(img.mode)      # RGB

# 调整大小
resized = img.resize((800, 600))
resized.save("resized.jpg")

# 缩略图（保持比例）
img.thumbnail((400, 400))
img.save("thumbnail.jpg")

# 裁剪
cropped = img.crop((100, 100, 500, 500))
cropped.save("cropped.jpg")

# 旋转
rotated = img.rotate(90)
rotated.save("rotated.jpg")

# 翻转
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped.save("flipped.jpg")

# 滤镜
blurred = img.filter(ImageFilter.BLUR)
blurred.save("blurred.jpg")

contour = img.filter(ImageFilter.CONTOUR)
contour.save("contour.jpg")

# 调整颜色
enhancer = ImageEnhance.Brightness(img)
brighter = enhancer.enhance(1.5)
brighter.save("brighter.jpg")

enhancer = ImageEnhance.Contrast(img)
higher_contrast = enhancer.enhance(1.5)

enhancer = ImageEnhance.Color(img)
more_saturated = enhancer.enhance(1.5)

# 绘制图形
draw = ImageDraw.Draw(img)
draw.rectangle([(50, 50), (200, 100)], outline="red", width=3)
draw.text((50, 120), "Hello", fill="white")
img.save("drawn.jpg")

# 粘贴另一张图片
logo = Image.open("logo.png")
img.paste(logo, (10, 10))
img.save("with_logo.jpg")
```

## NumPy - 数值计算

```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2], [3, 4]])

# 特殊数组
zeros = np.zeros((3, 4))      # 全零
ones = np.ones((2, 3))        # 全一
empty = np.empty((2, 2))      # 未初始化
eye = np.eye(3)               # 单位矩阵
range_arr = np.arange(0, 10, 2)   # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)   # [0, 0.25, 0.5, 0.75, 1]

# 随机数组
rand = np.random.rand(3, 3)       # 0-1 均匀分布
randn = np.random.randn(3, 3)     # 标准正态分布
randint = np.random.randint(0, 10, (3, 3))  # 随机整数

# 数组属性
arr.shape      # (5,)
arr2d.shape    # (2, 2)
arr.ndim       # 维度数
arr.size       # 元素个数
arr.dtype      # 数据类型

# 索引和切片
arr[0]         # 第一个元素
arr[-1]        # 最后一个元素
arr[1:4]       # 切片
arr2d[0, 1]    # 第一行第二列
arr2d[:, 1]    # 所有行的第二列

# 运算
arr + 1        # 加法
arr * 2        # 乘法
np.sqrt(arr)   # 平方根
np.exp(arr)    # 指数
np.log(arr)    # 对数

# 统计
np.sum(arr)      # 求和
np.mean(arr)     # 平均值
np.median(arr)   # 中位数
np.std(arr)      # 标准差
np.min(arr)      # 最小值
np.max(arr)      # 最大值

# 矩阵运算
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
np.dot(a, b)     # 矩阵乘法
a @ b            # 矩阵乘法（Python 3.5+）
```

## Pandas - 数据分析

```python
import pandas as pd

# 创建 Series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# 创建 DataFrame
df = pd.DataFrame({
    'name': ['张三', '李四', '王五'],
    'age': [25, 30, 28],
    'city': ['北京', '上海', '广州']
})

# 读取文件
df = pd.read_csv('data.csv')
df = pd.read_excel('data.xlsx')
df = pd.read_json('data.json')

# 写入文件
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)

# 查看数据
df.head()          # 前5行
df.tail()          # 后5行
df.info()          # 基本信息
df.describe()      # 统计信息

# 选择列
df['name']         # 单列
df[['name', 'age']]  # 多列

# 选择行
df.iloc[0]         # 按位置
df.loc[0]          # 按索引
df[df['age'] > 25] # 条件筛选

# 修改数据
df['new_col'] = [1, 2, 3]           # 添加列
df.drop('new_col', axis=1)          # 删除列
df.dropna()                         # 删除缺失值
df.fillna(0)                        # 填充缺失值

# 分组统计
df.groupby('city')['age'].mean()
df.groupby('city').agg({'age': ['mean', 'max', 'min']})

# 合并数据
df1 = pd.DataFrame({'id': [1, 2], 'name': ['A', 'B']})
df2 = pd.DataFrame({'id': [1, 2], 'score': [85, 92]})
merged = pd.merge(df1, df2, on='id')
```

## Matplotlib - 数据可视化

```python
import matplotlib.pyplot as plt
import numpy as np

# 折线图
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Sine Wave')
plt.show()

# 多个曲线
plt.plot(x, np.sin(x), label='sin')
plt.plot(x, np.cos(x), label='cos')
plt.legend()
plt.show()

# 散点图
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y)
plt.show()

# 柱状图
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 20]
plt.bar(categories, values)
plt.show()

# 直方图
data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.show()

# 饼图
sizes = [30, 25, 20, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.show()

# 子图
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(x, np.sin(x))
axes[0, 1].plot(x, np.cos(x))
axes[1, 0].scatter(x, y)
axes[1, 1].hist(data, bins=30)
plt.show()

# 保存图片
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

## Colorama - 终端颜色

```python
from colorama import init, Fore, Back, Style

# 初始化（自动重置）
init(autoreset=True)

# 前景色
print(Fore.RED + "红色文字")
print(Fore.GREEN + "绿色文字")
print(Fore.YELLOW + "黄色文字")
print(Fore.BLUE + "蓝色文字")
print(Fore.MAGENTA + "洋红色文字")
print(Fore.CYAN + "青色文字")

# 背景色
print(Back.RED + "红色背景")
print(Back.GREEN + "绿色背景")
print(Back.YELLOW + "黄色背景")

# 样式
print(Style.BRIGHT + "粗体")
print(Style.DIM + "暗淡")
print(Style.NORMAL + "正常")

# 组合
print(Fore.RED + Back.YELLOW + Style.BRIGHT + "红字黄底粗体")

# 重置
print(Style.RESET_ALL + "恢复默认")
```

## Scrapy - 网页爬虫

```python
# 创建项目
# scrapy startproject myproject

# 定义 Item
# items.py
import scrapy

class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()

# 编写 Spider
# spiders/news_spider.py
import scrapy
from myproject.items import ArticleItem

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = ["https://example.com/news"]

    def parse(self, response):
        for article in response.css("article"):
            item = ArticleItem()
            item["title"] = article.css("h2::text").get()
            item["url"] = article.css("a::attr(href)").get()
            yield item

        # 下一页
        next_page = response.css("a.next::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

# 运行爬虫
# scrapy crawl news -o output.json
```
