-- 复制行内链接
function CopyUrlFromLine()
  local line = vim.fn.getline('.')
  -- 匹配 http:// 或 https:// 开头的URL
  -- local url = line:match('https?://[%w-_%.%?%.:/%+=&]+')
  local url = line:match('[%w]+://[%w%-_%.%?%.:/%+=&%%#@,;!]*')
  
  if url then
    vim.fn.setreg('+', url)  -- 复制到系统剪贴板
    print('已复制URL: ' .. url)
  else
    print('未找到URL')
  end
end

vim.keymap.set('n', '<leader>cu', CopyUrlFromLine)

-- 为每个窗口自动设置局部工作目录到当前文件所在目录
vim.api.nvim_create_autocmd({"BufEnter", "BufWinEnter"}, {
  pattern = "*",
  callback = function()
    -- 获取当前缓冲区文件所在目录
    local buf_dir = vim.fn.expand("%:p:h")
    -- 确认是有效目录
    if vim.fn.isdirectory(buf_dir) == 1 then
      -- 使用 lcd 只改变当前窗口的工作目录
      vim.cmd("lcd " .. vim.fn.fnameescape(buf_dir))
    end
  end,
})
