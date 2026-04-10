# Qutebrowser 浏览器快捷键

## 配置文件位置

```bash
~/.config/qutebrowser/config.py
```

## 页面导航

| 快捷键 | 作用 |
|--------|------|
| `o` | 在当前标签页打开 URL（使用搜索引擎） |
| `O` | 在新标签页打开 URL |
| `t` | 新建标签页并打开 URL |
| `T` | 新建标签页并打开 URL（后台加载） |
| `Ctrl + T` | 新建空白标签页 |
| `Alt + H` | 后退 |
| `Alt + L` | 前进 |
| `r` | 刷新页面 |
| `Ctrl + R` | 强制刷新（忽略缓存） |
| `Ctrl + Shift + R` | 强制刷新 |

## 标签页管理

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + Tab` | 下一个标签页 |
| `Ctrl + Shift + Tab` | 上一个标签页 |
| `Alt + J` | 下一个标签页 |
| `Alt + K` | 上一个标签页 |
| `Ctrl + W` | 关闭当前标签页 |
| `Ctrl + Shift + W` | 关闭当前窗口 |
| `Ctrl + Shift + T` | 重新打开最近关闭的标签页 |
| `m` | 固定/取消固定标签页 |
| `M` | 静音/取消静音标签页 |
| `Ctrl + Shift + M` | 静音/取消静音标签页（全局） |
| `z` | 进入标签页选择模式（输入数字切换） |

## 历史记录

| 快捷键 | 作用 |
|--------|------|
| `H` | 查看历史记录（后退历史） |
| `L` | 查看历史记录（前进历史） |
| `Ctrl + H` | 打开历史记录页面 |

## 书签

| 快捷键 | 作用 |
|--------|------|
| `b` | 添加书签 |
| `B` | 打开书签页面 |
| `Ctrl + D` | 添加书签 |

## 查找

| 快捷键 | 作用 |
|--------|------|
| `/` | 在页面中查找 |
| `n` | 下一个匹配项 |
| `N` | 上一个匹配项 |
| `Esc` | 清除查找高亮 |

## 缩放

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + =` | 放大 |
| `Ctrl + -` | 缩小 |
| `Ctrl + 0` | 重置缩放（100%） |

## 下载管理

| 快捷键 | 作用 |
|--------|------|
| `d` | 打开下载页面 |
| `Ctrl + D` | 下载当前页面 |
| `Alt + D` | 下载当前页面（后台） |

## 命令模式

| 快捷键 | 作用 |
|--------|------|
| `:` | 进入命令模式 |
| `Esc` | 退出命令模式 |
| `Ctrl + C` | 退出命令模式 |
| `Tab` | 命令补全 |

## 常用命令

```bash
:open example.com              # 打开 URL
:open -t example.com           # 新标签页打开
:open {url}                    # 使用搜索引擎搜索

:tab-next                      # 下一个标签页
:tab-prev                      # 上一个标签页
:tab-close                     # 关闭标签页
:tab-only                      # 关闭其他标签页

:bookmark-add                  # 添加书签
:bookmark-page                 # 打开书签页面

:history                       # 打开历史记录
:download                      # 打开下载页面

:set content.zoom 120          # 设置缩放
:zoom-in                       # 放大
:zoom-out                      # 缩小

:fullscreen                    # 全屏切换

:reload                        # 刷新
:reload -f                     # 强制刷新

:inspector                     # 打开开发者工具

:config-py                     # 打开配置文件

:adblock-update                # 更新广告过滤规则

:yank                         # 复制当前 URL
:yank title                   # 复制页面标题
:yank pretty-url              # 复制美化后的 URL

:spawn mpv {url}              # 调用外部程序播放视频
```

## 快速启动命令

| 快捷键 | 作用 |
|--------|------|
| `Alt + 1...9` | 快速打开预设的书签或搜索引擎 |

## 常用配置示例

```python
# ~/.config/qutebrowser/config.py

# 设置搜索引擎
c.url.searchengines = {
    'DEFAULT': 'https://www.google.com/search?q={}',
    'b': 'https://www.bing.com/search?q={}',
    'g': 'https://github.com/search?q={}',
    'w': 'https://wiki.archlinux.org/index.php?search={}',
    'yt': 'https://www.youtube.com/results?search_query={}',
}

# 设置主页
c.url.start_pages = 'https://www.google.com'

# 下载目录
c.downloads.location.directory = '~/Downloads'

# 提示下载位置
c.downloads.location.prompt = True

# 默认缩放
c.zoom.default = '100%'

# 广告过滤
c.content.blocking.enabled = True

# 暗色模式
colors.webpage.darkmode.enabled = True
colors.webpage.darkmode.algorithm = 'lightness-cielab'

# 字体
fonts.default_family = 'Noto Sans'
fonts.default_size = '12px'

# 滚动速度
scrolling.smooth = True
```

## 会话管理

| 命令 | 作用 |
|------|------|
| `:session-save` | 保存当前会话 |
| `:session-load` | 加载会话 |
| `:session-delete` | 删除会话 |

## 私密模式

| 命令 | 作用 |
|------|------|
| `:open -p example.com` | 在私密窗口打开 |
| `:private` | 进入私密模式 |

## 提示模式

| 快捷键 | 作用 |
|--------|------|
| `f` | 跟随链接（显示数字） |
| `F` | 在新标签页跟随链接 |
| `;` | 进入提示模式 |
| `;y` | 复制链接 URL |
| `;Y` | 复制链接文本 |
| `;i` | 图片链接 |
| `;I` | 新标签页打开图片 |
| `;d` | 下载链接 |

## 插入模式

| 快捷键 | 作用 |
|--------|------|
| `Ctrl + E` | 进入插入模式（文本输入） |
| `Esc` | 退出插入模式 |
| `Ctrl + V` | 进入插入模式（粘贴） |

## 一句话总结

Qutebrowser 核心：`o` 打开网址，`t` 新标签页打开，`Ctrl+Tab` 切换标签页，`f` 跟随链接，`/` 查找，`b` 添加书签，`d` 查看下载，`:` 执行命令，`Esc` 退出。键盘驱动，无需鼠标。
