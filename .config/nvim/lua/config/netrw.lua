-- 设置netrw
vim.g.netrw_banner = 0  -- hide the banner above
vim.g.netrw_liststyle = 3   -- 0=thin 1=lone 2=wide 3=tree
vim.g.netrw_browse_split = 2     -- 打开方式: 0=当前窗口, 1=水平分割,2=垂直分割, 3=新标签, 4=浮动窗口
vim.g.netrw_altv = 1             -- 垂直分割时右侧打开
vim.g.netrw_winsize = 75         -- 窗口宽度占比

-- 快捷键映射
vim.keymap.set('n', '<leader>e', vim.cmd.Explore, { desc = "Open file explorer" })
vim.keymap.set('n', '-', ':edit %:h<CR>', { desc = "Go to parent directory" }) -- 快速返回上级目录

-- 工作目录管理
vim.keymap.set('n', '<leader>cd', function()
  vim.cmd('cd %:p:h')            -- 切换工作目录到当前文件所在位置
  print('Current dir: ' .. vim.fn.getcwd())
end, { desc = "Set working directory to current file" })

-- 内置文件搜索配置
vim.opt.path:append('**')         -- 允许 :find 递归搜索子目录
vim.keymap.set('n', '<leader>f', ':find ', { desc = "Search file in path" })

-- 终端文件操作增强
vim.keymap.set('n', '<leader>t', ':terminal<CR>', { desc = "Open terminal" })
