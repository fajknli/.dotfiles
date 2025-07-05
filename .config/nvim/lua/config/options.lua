vim.opt.clipboard = ""  -- 不自动将操作同步到系统剪贴板
--vim.opt.clipboard = 'unnamedplus'  -- 共用系统剪贴板
-- 使用 vim.opt 统一设置
vim.opt.relativenumber = true      -- 等同于 vim.wo.relativenumber
vim.opt.mouse = 'a'                -- 在所有模式下启用鼠标支持
vim.opt.scrolloff = 8              -- 保持光标上下始终有 8 行上下文
vim.opt.cmdheight = 1              -- 设置命令行的高度为 1
vim.opt.showmatch = true           -- 启用匹配括号的高亮显示
vim.opt.matchtime = 2              -- 修正：匹配括号的延时为 0.2 秒（注意原配置中的 'mat' 应为 'matchtime'）
vim.opt.errorbells = false         -- 禁用错误铃声
vim.opt.visualbell = false         -- 禁用视觉铃声

-- 折叠设置
vim.opt.foldenable = true          -- 启用折叠
vim.opt.foldmethod = "indent"      -- 按缩进折叠（其他选项见下文）
vim.opt.foldlevel = 99             -- 默认不折叠任何代码（99表示全部展开）
vim.opt.foldlevelstart = 99        -- 打开文件时默认展开所有折叠
vim.opt.foldcolumn = "1"           -- 左侧折叠指示列（0-12表示宽度）


-- 注意：timeoutlen 通常使用 vim.o，但也可以用 vim.opt
-- 性能相关设置
vim.opt.timeoutlen = 500           -- 命令超时等待时间（毫秒）
vim.opt.ttimeoutlen = 10           -- 键码超时时间（建议比timeoutlen小）
vim.opt.ttyfast = true             -- 优化终端重绘性能
vim.opt.lazyredraw = true          -- 执行宏/寄存器时不重绘（提升性能）

-- 显示相关
vim.opt.wrap = false               -- 关闭自动换行
vim.opt.cursorline = true          -- 高亮当前行
vim.opt.cursorcolumn = true        -- 高亮当前列（可选，可能影响性能）
vim.opt.number = true              -- 显示行号
vim.opt.relativenumber = true      -- 相对行号

-- 编码与文件格式
vim.opt.encoding = "utf-8"         -- 建议使用连字符格式
vim.opt.fileencoding = "utf-8"     -- 文件写入编码
vim.opt.fileformats = "unix,dos,mac" -- 自动检测行尾格式

-- 文件备份与交换
vim.opt.backup = false             -- 禁用备份文件
vim.opt.writebackup = false        -- 写入时不创建备份
vim.opt.swapfile = true            -- 启用交换文件（安全保护）
vim.opt.directory:prepend(vim.fn.stdpath('data') .. "/swap//") -- 交换文件目录（注意末尾双斜杠）

-- 搜索与高亮
vim.opt.hlsearch = true            -- 高亮搜索结果
vim.opt.incsearch = true           -- 实时搜索高亮
vim.opt.ignorecase = true          -- 搜索忽略大小写
vim.opt.smartcase = true           -- 有大写字母时区分大小写

-- 其他重要设置
vim.opt.undofile = true            -- 启用持久撤销（推荐）
vim.opt.undodir = vim.fn.stdpath('data') .. "/undo" -- 撤销文件目录
vim.opt.clipboard = "unnamedplus"  -- 系统剪贴板集成

-- 会话设置（优化版）
vim.opt.sessionoptions = {    -- 使用 table 完整赋值更清晰
  "buffers",     -- 保存缓冲区
  "curdir",      -- 当前目录
  "folds",       -- 折叠状态
  "globals",     -- 全局变量（注意可能包含敏感信息）
  "tabpages",    -- 标签页
  "winsize",     -- 窗口大小
  "skiprtp",     -- 建议添加：不保存运行时路径（避免环境差异问题）
  "localoptions" -- 建议添加：本地选项
}

-- 搜索设置（优化版）
vim.opt.ignorecase = true     -- 搜索时忽略大小写
vim.opt.smartcase = true      -- 当搜索包含大写字母时区分大小写
vim.opt.hlsearch = true       -- 高亮所有匹配结果
vim.opt.incsearch = true      -- 增量搜索（输入时实时显示匹配）
-- vim.o.magic = true         -- 已弃用（现代 Neovim 中默认启用扩展正则）

-- 性能相关
vim.opt.timeoutlen = 300      -- 映射等待时间（毫秒）
vim.opt.ttimeoutlen = 50      -- 建议添加：键码等待时间（应比 timeoutlen 小）
vim.opt.updatetime = 100      -- 触发 CursorHold 事件的时间（也影响 git-gutter 等插件）

-- 缩进设置（优化版）
vim.opt.expandtab = true      -- 将 Tab 转换为空格
vim.opt.shiftwidth = 4        -- 自动缩进步长
vim.opt.tabstop = 4           -- Tab 显示宽度
vim.opt.softtabstop = 4       -- 建议添加：编辑时的 Tab 行为
vim.opt.smartindent = true    -- 智能缩进（比 autoindent 更智能）
-- vim.o.autoindent = true    -- 被 smartindent 包含，可移除
-- vim.o.smarttab = true      -- 主要用于 C 语言，通常不需要单独设置

-- 文本格式（优化版）
vim.opt.wrap = true           -- 启用自动换行
vim.opt.linebreak = true      -- 在单词边界换行（而非字符边界）
vim.opt.breakindent = true    -- 建议添加：换行后保持缩进
vim.opt.showbreak = "↳ "      -- 建议添加：换行标识符号
vim.opt.textwidth = 0         -- 建议修改：禁用自动换行（用 wrap 控制）
vim.opt.colorcolumn = "80,100,120"   -- 建议添加：80 列参考线

-- 命令行补全增强 (优化版)
vim.opt.wildmenu = true              -- 启用图形化补全菜单
vim.opt.wildignorecase = true        -- 补全时忽略大小写
vim.opt.cmdwinheight = 5             -- 命令行窗口高度
