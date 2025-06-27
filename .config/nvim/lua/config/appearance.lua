require("colors.fajknli").setup()

-- 设置 Neovim 的颜色主题为 'habamax'
-- vim.cmd('colorscheme habamax')

-- 启用当前行的高亮显示
-- vim.wo.cursorline = true

-- 设置光标行的高亮样式（更现代写法）
-- vim.api.nvim_set_hl(0, 'CursorLine', {
--   bg = "#5f0000",  -- 深红背景（你原设 darkred）
--   fg = "#ffffff",  -- 白色前景
--   bold = true,
-- })


-- 设置 Neovim 的状态栏为 always 显示
vim.o.laststatus = 2
-- 设置状态栏的内容，包括当前文件名、行号、列号、编码等信息
vim.o.statusline = '%* [Bf-%n] CWD:%r%{getcwd()}%h%*/ '
vim.o.statusline = vim.o.statusline .. '%2* %t%m %*[%l:%c]:%p%%%*'
vim.o.statusline = vim.o.statusline .. '%=%Y%*╱%{&ff}%*╱%{ "[".(&fenc==""?&enc:&fenc).((exists("+bomb") && &bomb)?"+" : "")."]" }%*╱'


-- 为状态栏中的不同部分设置不同的颜色
vim.api.nvim_set_hl(0, 'User1', { bold = true, fg = "#e0e0e0", bg = "#1c1c1c" })  -- 自定义部分 1
vim.api.nvim_set_hl(0, 'User2', { fg = "#e0e0e0", bg = "#3a3a3a" })              -- 自定义部分 2
vim.api.nvim_set_hl(0, 'User3', { fg = "#e0e0e0", bg = "#262626" })              -- 自定义部分 3
vim.api.nvim_set_hl(0, 'User4', { bold = true, fg = "#e0e0e0", bg = "#1c1c1c" }) -- 自定义部分 4



