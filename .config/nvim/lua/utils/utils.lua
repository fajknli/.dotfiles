-- utils.lua 或 commands.lua

-- 检查是否为粘贴模式
function HasPaste()
  if vim.o.paste then
    return "PASTE MODE  "
  end
  return ""
end

-- 关闭缓冲区但不关闭窗口
vim.api.nvim_create_user_command("Bclose", function()
  local current_buf = vim.fn.bufnr("%")
  local alternate_buf = vim.fn.bufnr("#")

  if vim.fn.buflisted(alternate_buf) == 1 then
    vim.cmd("buffer #")
  else
    vim.cmd("bnext")
  end

  if vim.fn.bufnr("%") == current_buf then
    vim.cmd("enew")
  end

  if vim.fn.buflisted(current_buf) == 1 then
    vim.cmd("bdelete! " .. current_buf)
  end
end, {})

-- 执行命令行（供 VisualSelection 调用）
function CmdLine(str)
  vim.api.nvim_feedkeys(":" .. str, "n", true)
end

-- 可视模式下处理选中内容并操作
function VisualSelection(direction, extra_filter)
  local saved_reg = vim.fn.getreg('"')

  vim.cmd('normal! vgvy')

  local pattern = vim.fn.escape(vim.fn.getreg('"'), "\\/.*'$^~[]")
  pattern = pattern:gsub("\n$", "")

  if direction == 'gv' then
    CmdLine("Ack '" .. pattern .. "' ")
  elseif direction == 'replace' then
    CmdLine("%s/" .. pattern .. "/")
  end

  vim.fn.setreg("/", pattern)
  vim.fn.setreg('"', saved_reg)
end

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
