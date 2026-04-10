# localectl - 区域和键盘布局管理

## 一句话理解

localectl 查询和修改系统的区域设置（语言）和键盘布局。

```bash
# 查看当前区域和键盘设置
localectl status

# 设置系统语言
sudo localectl set-locale LANG=zh_CN.UTF-8
```

## 常用场景

### 1. 查看当前区域设置

```bash
# 查看所有区域设置
localectl status

# 输出示例：
#    System Locale: LANG=en_US.UTF-8
#                  LC_COLLATE=C
#       VC Keymap: us
#      X11 Layout: us
#       X11 Model: pc105
#     X11 Variant: 
#     X11 Options: terminate:ctrl_alt_bksp
```

### 2. 设置系统语言

```bash
# 设置为英文
sudo localectl set-locale LANG=en_US.UTF-8

# 设置为中文
sudo localectl set-locale LANG=zh_CN.UTF-8

# 设置多个区域变量
sudo localectl set-locale LANG=zh_CN.UTF-8 LC_COLLATE=C LC_TIME=en_US.UTF-8
```

### 3. 设置键盘布局（虚拟控制台）

```bash
# 查看可用键盘布局
localectl list-keymaps

# 过滤查找
localectl list-keymaps | grep -i us
localectl list-keymaps | grep -i cn

# 设置控制台键盘布局
sudo localectl set-keymap us
sudo localectl set-keymap us-colemak
```

### 4. 设置 X11 键盘布局

```bash
# 设置 X11 键盘布局
sudo localectl set-x11-keymap us

# 设置布局、型号、变体、选项
sudo localectl set-x11-keymap us pc105 altgr-intl

# 设置键盘选项
sudo localectl set-x11-keymap us "" "" "ctrl:nocaps"
sudo localectl set-x11-keymap us "" "" "terminate:ctrl_alt_bksp"
```

### 5. 同时设置所有键盘

```bash
# 同时设置控制台和 X11
sudo localectl set-keymap us
sudo localectl set-x11-keymap us

# 查看当前键盘设置
localectl status | grep -E "VC Keymap|X11 Layout"
```

## 常用选项速查

| 选项 | 说明 | 例子 |
|------|------|------|
| `status` | 显示当前设置 | `localectl status` |
| `set-locale` | 设置系统区域 | `sudo localectl set-locale LANG=en_US.UTF-8` |
| `list-locales` | 列出可用区域 | `localectl list-locales` |
| `set-keymap` | 设置控制台键盘 | `sudo localectl set-keymap us` |
| `list-keymaps` | 列出控制台键盘 | `localectl list-keymaps` |
| `set-x11-keymap` | 设置 X11 键盘 | `sudo localectl set-x11-keymap us` |
| `list-x11-keymap-models` | 列出 X11 键盘型号 | `localectl list-x11-keymap-models` |
| `list-x11-keymap-layouts` | 列出 X11 键盘布局 | `localectl list-x11-keymap-layouts` |
| `list-x11-keymap-variants` | 列出 X11 键盘变体 | `localectl list-x11-keymap-variants` |
| `list-x11-keymap-options` | 列出 X11 键盘选项 | `localectl list-x11-keymap-options` |

## 常见区域设置

| 区域 | 说明 |
|------|------|
| `en_US.UTF-8` | 英文（美国） |
| `en_GB.UTF-8` | 英文（英国） |
| `zh_CN.UTF-8` | 中文（简体） |
| `zh_TW.UTF-8` | 中文（繁体） |
| `ja_JP.UTF-8` | 日文 |
| `ko_KR.UTF-8` | 韩文 |

## 常见问题

### 1. 中文显示乱码怎么办？

```bash
# 1. 生成中文区域
sudo vim /etc/locale.gen
# 取消注释 zh_CN.UTF-8 UTF-8

# 2. 生成区域
sudo locale-gen

# 3. 设置中文区域
sudo localectl set-locale LANG=zh_CN.UTF-8

# 4. 重启或重新登录
```

### 2. 如何临时切换语言？

```bash
# 临时设置（仅当前会话）
export LANG=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8

# 恢复英文
export LANG=en_US.UTF-8
```

### 3. 如何设置大写锁定为 Ctrl？

```bash
# 使用 X11 选项
sudo localectl set-x11-keymap us "" "" "ctrl:nocaps"
```

### 4. 如何查看当前生效的区域变量？

```bash
# 查看所有区域变量
locale

# 查看特定变量
echo $LANG
echo $LC_ALL
echo $LC_CTYPE
```

## 快捷别名

```bash
alias loc='localectl'
alias loc-status='localectl status'
alias loc-lang='sudo localectl set-locale LANG='
alias loc-keymap='sudo localectl set-keymap'
alias loc-x11='sudo localectl set-x11-keymap'
```

## 相关文件

| 文件 | 说明 |
|------|------|
| `/etc/locale.conf` | 系统区域配置文件 |
| `/etc/locale.gen` | 可用区域列表 |
| `/etc/vconsole.conf` | 控制台键盘配置 |
| `/etc/X11/xorg.conf.d/00-keyboard.conf` | X11 键盘配置 |

## 一句话总结

localectl 核心：`localectl status` 查看设置，`sudo localectl set-locale LANG=zh_CN.UTF-8` 设语言，`sudo localectl set-keymap us` 设控制台键盘，`sudo localectl set-x11-keymap us` 设 X11 键盘。中文乱码需先 `locale-gen` 生成中文区域。
