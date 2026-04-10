# make 命令详解

## 一句话理解 make

make 是一个自动化构建工具，根据 Makefile 中的规则，自动处理文件依赖和编译。

```bash
# 基本用法
make                # 编译第一个目标
make clean          # 执行 clean 规则
make -j4            # 4 线程并行编译
```

## Makefile 基本结构

```makefile
# 目标: 依赖
target: dependency1 dependency2
    command1
    command2
```

**注意**：命令前必须用 **Tab** 缩进，不能用空格。

## 一个最简单的例子

```makefile
# 编译 hello.c 为 hello
hello: hello.c
    gcc -o hello hello.c

# 清理
clean:
    rm -f hello
```

使用：

```bash
make      # 编译
make clean  # 删除编译产物
```

## 变量

```makefile
# 定义变量
CC = gcc
CFLAGS = -Wall -O2
TARGET = myapp
SOURCES = main.c utils.c

# 使用变量
$(TARGET): $(SOURCES)
    $(CC) $(CFLAGS) -o $@ $^

# 清理
clean:
    rm -f $(TARGET)
```

## 自动变量

| 变量 | 说明 |
|------|------|
| `$@` | 目标文件名 |
| `$<` | 第一个依赖文件名 |
| `$^` | 所有依赖文件名（去重） |
| `$+` | 所有依赖文件名（保留重复） |
| `$*` | 目标的主文件名（不含扩展名） |
| `$?` | 比目标新的依赖文件列表 |

```makefile
# 示例
main.o: main.c utils.h
    gcc -c -o $@ $<
    # $@ = main.o
    # $< = main.c
```

## 常用函数

### 通配符

```makefile
# 获取所有 .c 文件
SOURCES = $(wildcard *.c)

# 将 .c 替换为 .o
OBJECTS = $(patsubst %.c,%.o,$(SOURCES))
# 或
OBJECTS = $(SOURCES:.c=.o)
```

### 字符串替换

```makefile
# 替换前缀
SRC = main.c utils.c
OBJ = $(SRC:.c=.o)      # main.o utils.o

# 添加前缀
FILES = $(addprefix src/,main.c utils.c)   # src/main.c src/utils.c

# 去除前缀
PATHS = src/main.c src/utils.c
FILES = $(notdir $(PATHS))                  # main.c utils.c

# 去除后缀
FILE = main.c
NAME = $(basename $(FILE))                  # main
```

### 查找和过滤

```makefile
# 过滤出 .c 文件
C_FILES = $(filter %.c,$(SOURCES))

# 过滤掉 .h 文件
C_FILES = $(filter-out %.h,$(SOURCES))
```

## 条件判断

```makefile
# ifeq/ifneq
ifeq ($(CC),gcc)
    CFLAGS = -Wall
else
    CFLAGS = -Wextra
endif

# ifdef/ifndef
ifdef DEBUG
    CFLAGS += -g
endif
```

## 伪目标

```makefile
.PHONY: clean install test

clean:
    rm -f *.o $(TARGET)

install:
    cp $(TARGET) /usr/local/bin/

test:
    ./run-tests.sh
```

## 模式规则

```makefile
# 通用的 .c 到 .o 规则
%.o: %.c
    $(CC) $(CFLAGS) -c -o $@ $<

# 静态模式规则
$(OBJECTS): %.o: %.c
    $(CC) $(CFLAGS) -c -o $@ $<
```

## 实际例子

### 1. 简单 C 程序

```makefile
CC = gcc
CFLAGS = -Wall -O2
TARGET = myprogram
SOURCES = main.c helper.c
OBJECTS = $(SOURCES:.c=.o)

$(TARGET): $(OBJECTS)
    $(CC) -o $@ $^

%.o: %.c
    $(CC) $(CFLAGS) -c -o $@ $<

.PHONY: clean
clean:
    rm -f $(OBJECTS) $(TARGET)
```

### 2. 多目录项目

```makefile
CC = gcc
CFLAGS = -Wall -Iinclude
TARGET = myapp

SRC_DIR = src
OBJ_DIR = obj
INC_DIR = include

SOURCES = $(wildcard $(SRC_DIR)/*.c)
OBJECTS = $(patsubst $(SRC_DIR)/%.c,$(OBJ_DIR)/%.o,$(SOURCES))

$(TARGET): $(OBJECTS)
    $(CC) -o $@ $^

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJ_DIR)
    $(CC) $(CFLAGS) -c -o $@ $<

$(OBJ_DIR):
    mkdir -p $(OBJ_DIR)

.PHONY: clean
clean:
    rm -rf $(OBJ_DIR) $(TARGET)
```

### 3. 调试和发布配置

```makefile
CC = gcc
TARGET = myapp
SOURCES = main.c utils.c

# 默认配置
ifeq ($(BUILD),debug)
    CFLAGS = -Wall -g -O0 -DDEBUG
    TARGET := $(TARGET)-debug
else
    CFLAGS = -Wall -O2
endif

$(TARGET): $(SOURCES)
    $(CC) $(CFLAGS) -o $@ $^

.PHONY: debug release
debug:
    $(MAKE) BUILD=debug

release:
    $(MAKE) BUILD=release
```

使用：

```bash
make release    # 编译发布版本
make debug      # 编译调试版本
```

### 4. 交叉编译

```makefile
# 本地编译
CC = gcc

# 交叉编译 ARM
CC_ARM = arm-linux-gnueabihf-gcc

# 选择编译器
ifeq ($(ARCH),arm)
    CC = $(CC_ARM)
    TARGET = $(TARGET)-arm
endif

$(TARGET): $(SOURCES)
    $(CC) $(CFLAGS) -o $@ $^
```

使用：

```bash
make              # 本地编译
make ARCH=arm     # ARM 交叉编译
```

## 常用命令

| 命令 | 说明 |
|------|------|
| `make` | 编译第一个目标 |
| `make target` | 编译指定目标 |
| `make -jN` | N 线程并行编译 |
| `make -n` | 预览要执行的命令（不实际执行） |
| `make -B` | 强制重新编译所有 |
| `make -d` | 调试模式，显示依赖分析 |
| `make -C dir` | 进入 dir 目录执行 make |
| `make -f file` | 指定 Makefile 文件名 |
| `make -k` | 出错后继续执行 |
| `make clean` | 执行 clean 规则 |

## 常见变量约定

| 变量 | 说明 |
|------|------|
| `CC` | C 编译器（默认 cc） |
| `CXX` | C++ 编译器（默认 g++） |
| `CFLAGS` | C 编译选项 |
| `CXXFLAGS` | C++ 编译选项 |
| `LDFLAGS` | 链接选项 |
| `LDLIBS` | 链接库 |
| `AR` | 归档工具（ar） |
| `RM` | 删除命令（rm -f） |

```makefile
# 使用约定变量
CC = gcc
CFLAGS = -Wall -O2
LDFLAGS = -lm
SOURCES = main.c
OBJECTS = $(SOURCES:.c=.o)

$(TARGET): $(OBJECTS)
    $(CC) $(LDFLAGS) -o $@ $^ $(LDLIBS)
```

## 常用函数速查

| 函数 | 说明 | 例子 |
|------|------|------|
| `$(wildcard pattern)` | 获取匹配的文件 | `$(wildcard *.c)` |
| `$(patsubst a,b,text)` | 替换模式 | `$(patsubst %.c,%.o,$(SRC))` |
| `$(subst a,b,text)` | 替换字符串 | `$(subst .c,.o,main.c)` |
| `$(addprefix p,list)` | 添加前缀 | `$(addprefix src/,main.c)` |
| `$(addsuffix s,list)` | 添加后缀 | `$(addsuffix .bak,file)` |
| `$(filter p,list)` | 过滤 | `$(filter %.c,$(FILES))` |
| `$(filter-out p,list)` | 反过滤 | `$(filter-out %.h,$(FILES))` |
| `$(dir path)` | 取目录 | `$(dir src/main.c)` → `src/` |
| `$(notdir path)` | 取文件名 | `$(notdir src/main.c)` → `main.c` |
| `$(basename file)` | 去后缀 | `$(basename main.c)` → `main` |
| `$(suffix file)` | 取后缀 | `$(suffix main.c)` → `.c` |
| `$(shell cmd)` | 执行 shell | `$(shell date)` |
| `$(foreach v,list,text)` | 循环 | `$(foreach f,$(FILES),$(f).bak)` |
| `$(if cond,then,else)` | 条件 | `$(if $(DEBUG),-g,)` |

## 调试技巧

```makefile
# 打印变量值
print-%:
    @echo '$* = $($*)'

# 使用
make print-CC       # 打印 CC 的值
make print-CFLAGS   # 打印 CFLAGS 的值

# 或直接
info:
    @echo "CC = $(CC)"
    @echo "CFLAGS = $(CFLAGS)"
    @echo "SOURCES = $(SOURCES)"
```

## 一句话总结

make 核心：目标 + 依赖 + 命令（Tab 缩进）。变量用 `$(VAR)`，自动变量 `$@` 是目标，`$<` 是第一个依赖，`$^` 是所有依赖。常用 `make -j4` 并行编译，`make clean` 清理。函数用 `$(wildcard)` 匹配文件，`$(patsubst)` 替换模式。
