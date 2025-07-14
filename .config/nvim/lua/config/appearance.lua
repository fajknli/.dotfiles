require("colors.fajknli").setup()
-- 设置状态栏的内容，包括当前文件名、行号、列号、编码等信息
vim.o.statusline = '%* [Bf-%n] CWD:%r%{getcwd()}%h%*/'
vim.o.statusline = vim.o.statusline .. '%2* %t%m %*[%l:%c]:%p%%%*'
vim.o.statusline = vim.o.statusline .. '%=%Y%*╱%{&ff}%*╱%{ "[".(&fenc==""?&enc:&fenc).((exists("+bomb") && &bomb)?"+" : "")."]" }%*╱'

-- 自定义高亮组（用于文件名部分）
vim.api.nvim_set_hl(0, 'User2', {
    fg = "#151622",    -- 深色文字（提高对比度）
    bg = "#a0d0a0",    -- 柔和的绿色背景
    bold = true,       -- 加粗文件名
})

-- 活动窗口状态栏样式
vim.api.nvim_set_hl(0, 'StatusLine', {
    bg = "#4e5078",  -- 蓝色背景
    fg = "#a9b5d5",  -- 深色文字
    bold = true,
})

-- 非活动窗口状态栏样式
vim.api.nvim_set_hl(0, 'StatusLineNC', {
    bg = "#222335",  -- 深灰色背景
    fg = "#a9b5d5",  -- 浅灰色文字
    bold = false,    -- 不加粗
})

-- 确保状态栏始终显示
vim.opt.laststatus = 2

