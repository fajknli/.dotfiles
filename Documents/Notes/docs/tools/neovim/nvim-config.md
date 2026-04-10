# Neovim 核心配置选项

## 基础设置

| 选项 | 值 | 说明 |
|------|-----|------|
| `mouse` | `a` | 启用鼠标支持 |
| `scrolloff` | `8` | 光标上下保持8行上下文 |
| `cmdheight` | `1` | 命令行高度 |
| `showmatch` | `true` | 高亮匹配括号 |
| `matchtime` | `2` | 匹配括号高亮延时0.2秒 |
| `errorbells` | `false` | 禁用错误铃声 |
| `visualbell` | `false` | 禁用视觉铃声 |

## 折叠设置

| 选项 | 值 | 说明 |
|------|-----|------|
| `foldenable` | `true` | 启用折叠 |
| `foldmethod` | `"indent"` | 按缩进折叠 |
| `foldlevel` | `99` | 默认不折叠 |
| `foldlevelstart` | `99` | 打开文件时全部展开 |
| `foldcolumn` | `"1"` | 显示折叠列 |

## 显示设置

| 选项 | 值 | 说明 |
|------|-----|------|
| `wrap` | `false` | 关闭自动换行 |
| `cursorline` | `true` | 高亮当前行 |
| `cursorcolumn` | `true` | 高亮当前列 |
| `number` | `true` | 显示行号 |
| `relativenumber` | `true` | 显示相对行号 |
| `colorcolumn` | `"80,100,120"` | 显示列参考线 |

## 编码与文件格式

| 选项 | 值 | 说明 |
|------|-----|------|
| `encoding` | `"utf-8"` | 内部编码 |
| `fileencoding` | `"utf-8"` | 文件写入编码 |
| `fileformats` | `"unix,dos,mac"` | 自动检测行尾格式 |

## 备份与交换文件

| 选项 | 值 | 说明 |
|------|-----|------|
| `backup` | `false` | 禁用备份文件 |
| `writebackup` | `false` | 写入时不创建备份 |
| `swapfile` | `true` | 启用交换文件 |
| `directory` | `~/.local/share/nvim/swap//` | 交换文件目录 |

## 搜索设置

| 选项 | 值 | 说明 |
|------|-----|------|
| `hlsearch` | `true` | 高亮搜索结果 |
| `incsearch` | `true` | 实时搜索高亮 |
| `ignorecase` | `true` | 忽略大小写 |
| `smartcase` | `true` | 有大写时区分大小写 |

## 缩进设置

| 选项 | 值 | 说明 |
|------|-----|------|
| `expandtab` | `true` | Tab 转换为空格 |
| `shiftwidth` | `4` | 自动缩进步长 |
| `tabstop` | `4` | Tab 显示宽度 |
| `softtabstop` | `4` | 编辑时 Tab 行为 |
| `smartindent` | `true` | 智能缩进 |

## 文本格式

| 选项 | 值 | 说明 |
|------|-----|------|
| `linebreak` | `true` | 在单词边界换行 |
| `breakindent` | `true` | 换行后保持缩进 |
| `showbreak` | `"↳ "` | 换行标识符 |
| `textwidth` | `0` | 禁用自动换行 |
| `formatoptions` | 移除 `r` 和 `o` | 禁用自动注释延续 |

## 性能优化

| 选项 | 值 | 说明 |
|------|-----|------|
| `timeoutlen` | `300` | 映射等待时间（毫秒） |
| `ttimeoutlen` | `50` | 键码等待时间 |
| `updatetime` | `100` | CursorHold 触发时间 |
| `ttyfast` | `true` | 优化终端重绘 |
| `lazyredraw` | `true` | 宏执行时不重绘 |

## 持久化撤销

| 选项 | 值 | 说明 |
|------|-----|------|
| `undofile` | `true` | 启用持久化撤销 |
| `undodir` | `~/.local/share/nvim/undo` | 撤销文件目录 |

## 命令行补全

| 选项 | 值 | 说明 |
|------|-----|------|
| `wildmenu` | `true` | 图形化补全菜单 |
| `wildignorecase` | `true` | 补全忽略大小写 |
| `cmdwinheight` | `5` | 命令行窗口高度 |

## 会话设置

```lua
vim.opt.sessionoptions = {
    "buffers",     -- 保存缓冲区
    "curdir",      -- 当前目录
    "folds",       -- 折叠状态
    "globals",     -- 全局变量
    "tabpages",    -- 标签页
    "winsize",     -- 窗口大小
    "skiprtp",     -- 不保存运行时路径
    "localoptions" -- 本地选项
}
```

## 状态栏设置

```lua
-- 启用状态栏
vim.opt.laststatus = 2

-- 状态栏内容格式
vim.o.statusline = '%* [Bf-%n] CWD:%r%{getcwd()}%h%*/'
vim.o.statusline = vim.o.statusline .. '%2* %t%m %*[%l:%c]:%p%%%*'
vim.o.statusline = vim.o.statusline .. '%=%Y%*╱%{&ff}%*╱%{ "[".(&fenc==""?&enc:&fenc).((exists("+bomb") && &bomb)?"+" : "")."]" }%*╱'
```

## 一句话总结

核心配置：`number`/`relativenumber` 显示行号，`expandtab`/`shiftwidth=4` 缩进设置，`hlsearch`/`incsearch` 搜索高亮，`undofile` 持久撤销，`foldmethod=indent` 代码折叠，`laststatus=2` 状态栏，`colorcolumn` 列参考线。
