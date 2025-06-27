-- 启用语法高亮
-- vim.cmd("syntax enable")

-- 设置历史记录条数
vim.o.history = 500

-- 启用文件类型检测和插件
--vim.o.filetype = "plugin"
--vim.o.filetype = "indent"

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

-- 延迟加载 man 插件
vim.cmd([[ autocmd FileType man runtime! ftplugin/man.vim ]])
