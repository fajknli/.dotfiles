# Niri 窗口管理器配置与快捷键

## 配置文件位置

```bash
~/.config/niri/config.kdl
```

## 一、基础设置

### 开机自启应用

```kdl
spawn-at-startup "foot"
spawn-at-startup "xwayland-satellite"
```

### 通用设置

```kdl
prefer-no-csd                          // 禁用客户端装饰
screenshot-path "~/Pictures/Screenshots/Screenshot from %Y-%m-%d %H-%M-%S.png"
```

### 环境变量

```kdl
environment {
    DBUS_SESSION_BUS_ADDRESS "unix:path=/run/user/1000/bus"
    QT_QPA_PLATFORM "wayland"
    QT_WAYLAND_DISABLE_WINDOWDECORATION "1"
    GDK_BACKEND "wayland"
    MOZ_ENABLE_WAYLAND "1"
    DISPLAY ":0"                         // 启用 Xwayland
    XMODIFIERS "@im=fcitx"
}
```

### 鼠标光标

```kdl
cursor {
    xcursor-theme "breeze_cursors"
    xcursor-size 22
    hide-when-typing                     // 打字时隐藏光标
    hide-after-inactive-ms 1000          // 1秒无操作后隐藏
}
```

### 概览视图

```kdl
overview {
    zoom 0.4
    backdrop-color "#151622"             // 背景色

    workspace-shadow {
        off
        softness 40
        spread 10
        offset x=0 y=10
        color "#00000090"
    }
}
```

### 剪贴板

```kdl
clipboard {
    disable-primary                       // 禁用主剪贴板（选中即复制）
}
```

### 热键提示

```kdl
hotkey-overlay {
    skip-at-startup
}
```

## 二、窗口规则

### 浮动窗口规则

```kdl
// Zenity 翻译窗口
window-rule {
    match app-id="zenity" title="Translate"
    open-floating true
    default-floating-position x=0 y=0
}

// 浮动终端（sdcv 词典）
window-rule {
    match app-id="floatingfoot"
    open-floating true
}

// 翻译浮动终端
window-rule {
    match app-id="floatingfoot_translate"
    open-floating true
}
```

### 应用窗口规则

```kdl
// Minecraft 游戏窗口
window-rule {
    match title="^Minecraft"
    open-maximized true
}

// 阻止密码管理器被录屏
window-rule {
    block-out-from "screencast"
}

// 录屏窗口高亮
window-rule {
    match is-window-cast-target=true
    focus-ring {
        active-color "#f38ba8"
        inactive-color "#7d0d2d"
    }
    border {
        inactive-color "#7d0d2d"
    }
    shadow {
        color "#7d0d2d70"
    }
    tab-indicator {
        active-color "#f38ba8"
        inactive-color "#7d0d2d"
    }
}
```

## 三、输入设备

```kdl
input {
    keyboard {
        xkb {
            layout "us"
        }
        numlock
    }

    touchpad {
        tap                              // 轻触点击
        natural-scroll                   // 自然滚动
    }

    mouse {
    }

    trackpoint {
    }
}
```

## 四、显示器设置

```kdl
output "DP-3" {
    mode "2560x1440@179.999"             // 分辨率与刷新率
    scale 1.5                            // 缩放 150%
    transform "normal"                   // 不旋转
    background-color "#151622"
}
```

## 五、布局设置

```kdl
layout {
    gaps 2                               // 窗口间距 2px
    default-column-display "normal"
    background-color "#1e2030"

    // 预设列宽比例
    preset-column-widths {
        proportion 0.49
        proportion 0.61
        proportion 0.73
    }

    // 预设窗口高度比例
    preset-window-heights {
        proportion 0.25
        proportion 0.5
        proportion 1.0
    }

    default-column-width { proportion 0.49; }

    // 焦点环
    focus-ring {
        width 1
        active-color "#b4befe"
        inactive-color "#a9b5d5"
    }

    // 边框
    border {
        width 2
        active-color "#b4befe"
        inactive-color "#2e3048"
    }

    // 标签指示器
    tab-indicator {
        hide-when-single-tab
        place-within-column
        gap 5
        width 5
        length total-proportion=1.0
        position "left"
        gaps-between-tabs 2
        corner-radius 5
        active-color "#a0d0a0"
        inactive-color "#585e8f"
        urgent-color "#f08080"
    }

    // 阴影
    shadow {
        softness 30
        spread 5
        offset x=0 y=5
        color "#0007"
    }
}
```

## 六、动画

```kdl
animations {
    slowdown 1.5                         // 动画速度
}
```

## 七、快捷键绑定

### 修饰键说明

| 符号 | 含义 |
|------|------|
| `Mod` | Super 键（Win键） |
| `Win` | Windows 键 |
| `Alt` | Alt 键 |
| `Ctrl` | Ctrl 键 |
| `Shift` | Shift 键 |

### 窗口布局

| 快捷键 | 作用 |
|--------|------|
| `Mod + W` | 切换 Tab 模式 / 纵向排列 |
| `Mod + I` | 将后面窗口合并到当前列 |
| `Mod + U` | 从当前列释放窗口 |

### 窗口焦点切换

| 快捷键 | 作用 |
|--------|------|
| `Mod + Q` / `Mod + H` | 切换到左边窗口 |
| `Mod + E` / `Mod + L` | 切换到右边窗口 |
| `Mod + J` | 切换到下面窗口 |
| `Mod + K` | 切换到上面窗口 |
| `Mod + Alt + H` | 切换到该列第一个窗口 |
| `Mod + Alt + L` | 切换到该列最后一个窗口 |

### 窗口移动

| 快捷键 | 作用 |
|--------|------|
| `Mod + Shift + Q` | 关闭窗口 |
| `Mod + Shift + H` | 窗口左移 |
| `Mod + Shift + L` | 窗口右移 |
| `Mod + Shift + J` | 移动到下一个工作区 |
| `Mod + Shift + K` | 移动到上一个工作区 |
| `Mod + Ctrl + Shift + H` | 移动到列首 |
| `Mod + Ctrl + Shift + L` | 移动到列尾 |

### 窗口大小

| 快捷键 | 作用 |
|--------|------|
| `Mod + F` | 最大化当前列 |
| `Mod + Shift + F` | 全屏窗口 |
| `Mod + C` | 窗口居中 |
| `Mod + Ctrl + H` | 宽度减少 10% |
| `Mod + Ctrl + L` | 宽度增加 10% |
| `Mod + Ctrl + K` | 高度减少 10% |
| `Mod + Ctrl + J` | 高度增加 10% |
| `Mod + Alt + O` | 切换预设窗口高度 |
| `Mod + Alt + P` | 切换预设列宽度 |

### 窗口浮动

| 快捷键 | 作用 |
|--------|------|
| `Mod + V` | 切换窗口浮动 |
| `Mod + Shift + V` | 切换浮动/平铺焦点 |

### 工作区切换

| 快捷键 | 作用 |
|--------|------|
| `Alt + 1...9` | 切换到工作区 1-9 |
| `Mod + 1...9` | 切换到工作区 1-9 |
| `Mod + Shift + 1...9` | 移动窗口到工作区 1-9 |

### 截图

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + Alt + Shift + P` | 区域截图 |
| `Ctrl + Alt + Shift + S` | 全屏截图 |
| `Ctrl + Alt + S` | 窗口截图（当前列） |

### 应用启动

| 快捷键 | 作用 |
|--------|------|
| `Mod + Return` | 启动终端（foot） |
| `Mod + Shift + Return` | 启动浮动终端 |
| `Mod + D` | 启动应用菜单（wmenu） |
| `Win + O` | 打开工作区概览 |
| `Mod + Shift + Slash` | 显示快捷键提示 |

### 自定义脚本启动

| 快捷键 | 作用 |
|--------|------|
| `Alt + I` | 启动网站脚本 |
| `Alt + M` | 启动项目管理脚本 |
| `Alt + N` | 启动笔记脚本 |
| `Alt + C` | 启动配置脚本 |
| `Alt + P` | 启动 PDF 脚本 |
| `Alt + E` | 启动剪贴板脚本 |
| `Alt + Q` | 启动计算器 |
| `Alt + O` | 查看天气 |
| `Alt + H` | 工具提示 |
| `Alt + T` | 翻译 |
| `Alt + Y` | 关闭 Mako 通知 |
| `Alt + R` | 快速笔记 |

### 系统控制

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + Shift + Space` | 锁屏（swaylock） |
| `Mod + Shift + P` | 关闭显示器 |
| `Mod + Shift + Return` | 启动浮动终端 |

### 音频控制

| 快捷键 | 作用 |
|--------|------|
| `XF86AudioRaiseVolume` | 音量增加 |
| `XF86AudioLowerVolume` | 音量减小 |
| `XF86AudioMute` | 静音切换 |
| `Ctrl + Alt + 0` | 音量增加 |
| `Ctrl + Alt + 9` | 音量减小 |
| `Ctrl + Alt + 8` | 静音切换 |

### 亮度控制

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + Alt + Shift + 0` | 亮度增加 |
| `Ctrl + Alt + Shift + 9` | 亮度减小 |

### 录屏控制

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + Alt + Shift + 6` | 开始录屏 |
| `Ctrl + Alt + Shift + 7` | 停止录屏 |

### 其他

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + Alt + Shift + I` | 显示系统信息 |
| `Shift + Return` | Minecraft 中文输入 |

## 八、常用命令

```bash
# 启动 Niri
niri

# 退出 Niri
niri msg action quit

# 切换工作区
niri msg action focus-workspace 1

# 移动窗口到工作区
niri msg action move-column-to-workspace 2

# 关闭窗口
niri msg action close-window

# 查看输出信息
niri msg outputs

# 重新加载配置
niri msg action reload-config
```

## 九、一句话总结

Niri 核心快捷键：`Mod+Return` 开终端，`Mod+D` 开应用菜单，`Mod+Q/H/L` 切换窗口，`Mod+数字` 切换工作区，`Mod+F` 最大化，`Mod+V` 浮动窗口，`Ctrl+Alt+Shift+P` 截图，`Ctrl+Alt+0/9` 调音量，`Ctrl+Alt+Shift+0/9` 调亮度。
