vim.opt.clipboard = ""  -- 不自动将操作同步到系统剪贴板
--vim.opt.clipboard = 'unnamedplus'  -- 共用系统剪贴板
-- 启用相对行号
vim.wo.relativenumber = true
-- 在所有模式下启用鼠标支持
vim.o.mouse = 'a'
-- 保持光标上下始终有 8 行上下文
vim.opt.scrolloff = 8 
-- 设置命令行的高度为 1
vim.o.cmdheight = 1
-- 启用代码折叠列
vim.o.foldcolumn = '1'
-- 启用匹配括号的高亮显示
vim.o.showmatch = true
-- 设置匹配括号的延时为 2
vim.o.mat = 2
-- 禁用错误铃声
vim.o.errorbells = false
-- 禁用视觉铃声
vim.o.visualbell = false
-- 关闭视觉铃声（不闪屏）
vim.o.visualbell = false
-- 设置命令超时等待时间为 500ms
vim.o.timeoutlen = 500
-- 这一行是提高性能，建议开启
vim.opt.ttyfast = true
-- 关闭自动换行
vim.opt.wrap = false
-- 启动本行高亮
vim.opt.cursorline = true

-- 设置编码
vim.o.encoding = "utf8"
vim.o.fileformats = "unix,dos,mac"

-- 禁用备份文件
vim.o.backup = false
vim.o.writebackup = false
vim.o.swapfile = true  -- 保留交换文件
vim.o.directory = vim.fn.stdpath('data') .. "/swap"  -- 设置交换文件目录

-- 使用 Neovim 内建的 Lua 正则引擎
-- vim.o.regexpengine = 0  -- 若不需要传统正则，可以去掉此行

-- 会话设置
vim.opt.sessionoptions:append({ "globals", "buffers", "tabpages", "curdir", "folds", "winsize" })

-- 搜索设置
vim.o.ignorecase = true       -- 忽略大小写
vim.o.smartcase = true        -- 智能大小写匹配
vim.o.hlsearch = true         -- 高亮搜索结果
vim.o.incsearch = true        -- 增量搜索
vim.o.magic = true            -- 启用正则表达式语法
vim.opt.incsearch = true  -- 启用增量搜索
vim.o.timeoutlen = 300        -- 设置按键响应时间
vim.o.updatetime = 100        -- 设置更新延迟，减少闪烁

-- 缩进设置
vim.o.expandtab = true       -- 使用空格代替制表符
vim.o.smarttab = true        -- 智能缩进
vim.o.shiftwidth = 4         -- 每次缩进使用 4 个空格
vim.o.tabstop = 4            -- 制表符等于 4 个空格
vim.o.autoindent = true      -- 自动缩进
vim.o.smartindent = true     -- 智能缩进
vim.o.wrap = true            -- 自动换行

-- 文本格式
vim.o.linebreak = true       -- 自动断行（适用于长行文本）
vim.o.textwidth = 500        -- 设置文本宽度为 500 列



