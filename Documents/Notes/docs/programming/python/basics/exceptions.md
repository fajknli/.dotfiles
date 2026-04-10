# Python 异常处理

## 异常的基本概念

异常是程序运行时发生的错误。Python 使用异常处理机制来捕获和处理这些错误，避免程序崩溃。

## try-except 语句

### 基本语法

```python
try:
    # 可能发生异常的代码
    num = int(input("请输入数字: "))
    result = 10 / num
    print(result)
except ValueError:
    # 处理值错误
    print("请输入有效的数字")
except ZeroDivisionError:
    # 处理除零错误
    print("除数不能为零")
```

### 捕获所有异常

```python
try:
    risky_code()
except Exception as e:
    print(f"发生错误: {e}")
```

### 捕获多个异常

```python
try:
    num = int(input("请输入数字: "))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"输入错误或除零错误: {e}")
```

## try-except-else 语句

```python
try:
    num = int(input("请输入数字: "))
except ValueError:
    print("请输入数字")
else:
    # 没有异常时执行
    print(f"您输入的是: {num}")
```

## try-except-else-finally 语句

```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("文件不存在")
else:
    print(f"文件内容: {content}")
finally:
    # 无论是否发生异常都会执行
    if 'file' in locals():
        file.close()
    print("文件操作结束")
```

## 常见内置异常

| 异常 | 说明 |
|------|------|
| `SyntaxError` | 语法错误 |
| `NameError` | 变量未定义 |
| `TypeError` | 类型错误 |
| `ValueError` | 值错误 |
| `IndexError` | 索引越界 |
| `KeyError` | 字典键不存在 |
| `FileNotFoundError` | 文件不存在 |
| `ZeroDivisionError` | 除零错误 |
| `AttributeError` | 属性不存在 |
| `ImportError` | 导入失败 |
| `RuntimeError` | 运行时错误 |

## 主动抛出异常

### raise 语句

```python
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
```

### 抛出原有异常

```python
try:
    risky_operation()
except ValueError as e:
    # 处理后重新抛出
    print("发生值错误")
    raise  # 重新抛出原异常
```

### 抛出新异常（保留原异常）

```python
try:
    risky_operation()
except ValueError as e:
    raise RuntimeError("操作失败") from e
```

## 自定义异常

```python
class ValidationError(Exception):
    """自定义验证异常"""
    pass

class AgeError(ValidationError):
    """年龄验证异常"""
    pass

def validate_age(age):
    if age < 0:
        raise AgeError("年龄不能为负数")
    if age > 150:
        raise AgeError("年龄不能超过150岁")
    return True

try:
    validate_age(-5)
except AgeError as e:
    print(f"年龄验证失败: {e}")
```

## 断言

```python
# assert 条件, 错误信息
def calculate_discount(price, discount):
    assert price > 0, "价格必须大于0"
    assert 0 <= discount <= 1, "折扣必须在0到1之间"
    return price * discount

# 可以在运行时禁用断言
# python -O script.py
```

## 异常链

```python
def read_config():
    try:
        with open("config.json") as f:
            return json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError("配置文件不存在") from e
    except json.JSONDecodeError as e:
        raise RuntimeError("配置文件格式错误") from e
```

## 上下文管理器中的异常

```python
class DatabaseConnection:
    def __enter__(self):
        print("连接数据库")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"发生异常: {exc_val}")
        print("关闭数据库连接")
        return False  # 返回 True 会抑制异常

with DatabaseConnection():
    # 执行数据库操作
    raise ValueError("操作失败")
```

## 最佳实践

### 指定具体的异常类型

```python
# 不推荐
try:
    result = int(input())
except:  # 捕获所有异常
    print("错误")

# 推荐
try:
    result = int(input())
except ValueError:
    print("请输入数字")
except KeyboardInterrupt:
    print("用户取消")
```

### 使用 finally 释放资源

```python
# 推荐使用 with 语句
with open("file.txt") as f:
    content = f.read()

# 或使用 try-finally
f = open("file.txt")
try:
    content = f.read()
finally:
    f.close()
```

### 不要吞没异常

```python
# 不推荐
try:
    risky_operation()
except Exception:
    pass  # 什么都不做，隐藏了错误

# 推荐：至少记录日志
import logging
try:
    risky_operation()
except Exception as e:
    logging.error(f"操作失败: {e}")
```

### 使用异常而不是返回错误码

```python
# 不推荐
def divide(a, b):
    if b == 0:
        return None
    return a / b

# 推荐
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b
```
