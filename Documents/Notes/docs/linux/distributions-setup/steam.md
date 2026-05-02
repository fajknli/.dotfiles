# Arch Linux 游戏环境搭建总结

> 适用硬件：AMD CPU + AMD 核显/独显（RADV 开源驱动）  
> 适用场景：Wayland 桌面环境（如 niri、Hyprland、Sway 等）

---

## 📦 一、基础环境搭建

### 1. 启用 multilib 仓库

编辑 `/etc/pacman.conf`，取消以下行的注释：

```ini
[multilib]
Include = /etc/pacman.d/mirrorlist
```

更新系统：

```bash
sudo pacman -Syu
```

---

### 2. 安装显卡驱动与 Vulkan 支持

| 层级 | 包名 | 用途 |
|------|------|------|
| 64 位基础 | `mesa` | 开源 OpenGL/Vulkan 驱动 |
| 64 位 Vulkan | `vulkan-radeon` | AMD Vulkan 驱动 |
| 32 位基础 | `lib32-mesa` | 32 位游戏（Steam/Proton）必需 |
| 32 位 Vulkan | `lib32-vulkan-radeon` | 32 位 Vulkan 驱动 |

```bash
sudo pacman -S mesa vulkan-radeon lib32-mesa lib32-vulkan-radeon
```

### 3. 安装 Vulkan 诊断工具

```bash
sudo pacman -S vulkan-tools
```

### 4. 验证 Vulkan 环境

```bash
vulkaninfo --summary | grep -E "deviceName|driverName"
```

**期望输出**（AMD 核显/独显）：

```
deviceName  = AMD Radeon ... (RADV ...)
driverName  = radv
```

出现 `radv` 即为正常。

---

## 🛠️ 二、安装 Steam 与兼容工具

### 1. 安装 Steam

```bash
sudo pacman -S steam
```

### 2. 安装 gamescope（微合成器，解决 Wayland 全屏/鼠标锁定问题）

```bash
sudo pacman -S gamescope
```

### 3. 安装性能监控工具（可选）

```bash
sudo pacman -S mangohud
```

---

## ⚙️ 三、Steam 游戏兼容配置

### 1. 开启 Steam Play（Proton）

1. 打开 Steam → Settings → Compatibility
2. 勾选 **"Enable Steam Play for all other titles"**
3. 下拉选择 **"Proton Experimental"** 或最新稳定版

### 2. 游戏启动选项模板

#### Wayland 环境通用模板（使用 gamescope 嵌套）

```
gamescope -f -W 1600 -H 900 -- SDL_VIDEO_DRIVER=x11 %command% -vulkan -nojoy -fullscreen +fps_max 0 -high
```

**参数说明：**

| 参数 | 作用 |
|------|------|
| `gamescope -f` | 创建独立虚拟显示器，全屏运行 |
| `-W 1600 -H 900` | 指定分辨率，可根据性能调整 |
| `--` | 分隔 gamescope 与游戏参数 |
| `SDL_VIDEO_DRIVER=x11` | 强制通过 XWayland 运行，规避输入问题 |
| `-vulkan` | 强制使用 Vulkan 渲染器 |
| `-nojoy` | 禁用摇杆检测，减少启动延迟 |
| `-fullscreen` | 全屏模式 |
| `+fps_max 0` | 解除帧率上限 |
| `-high` | 提高进程优先级 |

#### 简化版（不需要 gamescope 时）

```
SDL_VIDEO_DRIVER=x11 %command% -vulkan -nojoy -fullscreen +fps_max 0 -high
```

#### 配合 mangohud 监控

```
mangohud gamescope -f -W 1600 -H 900 -- SDL_VIDEO_DRIVER=x11 %command% -vulkan -nojoy -fullscreen +fps_max 0 -high
```

---

## 🔍 四、常见问题排查

| 现象 | 可能原因 | 解决方法 |
|------|----------|----------|
| 游戏无法启动/闪退 | 32 位驱动缺失 | `sudo pacman -S lib32-mesa lib32-vulkan-radeon` |
| 鼠标乱飞/无法全屏 | Wayland 兼容问题 | 启动项加 `SDL_VIDEO_DRIVER=x11` 或用 `gamescope` |
| VAC 无法验证 | 游戏文件损坏 | Steam 右键游戏 → 属性 → 已安装文件 → 验证完整性 |
| 帧率低/卡顿 | 核显性能不足 | 降分辨率（900P/720P），开 FSR，关 Steam 内覆盖 |
| Proton 游戏报 Windows 错误 | 兼容层未正确加载 | 检查游戏属性的兼容性选项，选 Proton Experimental |
| 终端提示 `vulkaninfo: command not found` | 未装诊断工具 | `sudo pacman -S vulkan-tools` |

---

## ✅ 五、验证清单

完成搭建后，逐项确认：

- [ ] `multilib` 仓库已启用
- [ ] `mesa`、`vulkan-radeon`、`lib32-mesa`、`lib32-vulkan-radeon` 已安装
- [ ] `vulkaninfo --summary` 输出包含 `driverName = radv`
- [ ] Steam 已安装并开启 Proton 兼容
- [ ] `gamescope` 已安装（Wayland 用户建议）
- [ ] 游戏启动选项已正确配置

---

## 📝 适用说明

- **AMD 独显**：流程完全一致，性能更强
- **NVIDIA 显卡**：需将上述包替换为 `nvidia`、`nvidia-utils`、`lib32-nvidia-utils`，驱动名预期为 `driverName = nvidia`
- **X11 桌面**：无需 `SDL_VIDEO_DRIVER=x11` 参数，gamescope 也非必需
- **其他发行版**：包名和包管理器不同，但逻辑相同（32位驱动 + Vulkan + Proton）

你遇到的 Mindustry 无法启动，和之前调试 CS2 的原因很类似，大概率也是 **Wayland 兼容性**或游戏自身配置残留的问题。Mindustry 是用 Java 写的，对显示协议比较敏感，这个情况还蛮典型的。

可以按下面的顺序逐一尝试，通常第一种方法就能立竿见影：

**1. 终极救星：重置显示驱动环境变量**
这和你之前给 CS2 加启动参数的道理一样。在 Steam 库中右键 Mindustry → 属性 → 通用，在启动选项中填入：
```bash
env -u SDL_VIDEODRIVER %command%
```
这个命令会**强制清除**可能导致冲突的显示相关环境变量，让游戏像刚安装时一样自动检测。你的 niri 环境可能无意中设置了某个限制，导致 Mindustry 找不到可用的视频驱动。

**2. 如果还是不行，手动指定后备方案**
把启动选项换成指定走 `x11` 或者 `wayland`：
```bash
SDL_VIDEODRIVER=x11 %command%
```
或者反过来再试一次：
```bash
SDL_VIDEODRIVER=wayland %command%
```
（注意别把这两个和第一条的 `env -u` 混在一起写哦）

**3. 检查“旧伤复发”：关闭云同步并删掉 Mod**
有时候游戏更新后，之前残留的配置文件或者 Mod 会捣乱。
- 在游戏属性 → 通用里，**临时取消勾选**“将 Mindustry 的游戏存档储存于 Steam 云”。
- 然后在属性 → 已安装文件中，点“验证游戏文件的完整性”。
- 如果你之前订阅过创意工坊的 Mod，先全部取消订阅，再试试启动。

**4. 排查 Java 本身的问题**
Mindustry 依赖系统 Java。虽然 Arch 一般比较新，但可以确认一下：
```bash
java --version
```
如果版本太旧或没装，游戏自然起不来。

**5. 最后的兜底办法：用 Gamescope 独立窗口运行**
就像之前解决 CS2 问题一样，把启动命令换成：
```bash
gamescope -f -W 1920 -H 1080 -- env -u SDL_VIDEODRIVER %command%
```
这样可以给 Mindustry 创造一个独立的、不受当前桌面环境干扰的运行空间。

通常执行到第 1 步问题就解决了。你赶紧去试试看，如果 Steam 里点击开始后终端有报错信息跳出来，也可以随时贴给我～
