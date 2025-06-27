-- 自动重新加载外部修改的文件
vim.api.nvim_create_autocmd({ "FocusGained", "BufEnter" }, {
  pattern = "*",
  callback = function()
    vim.cmd("silent! checktime")
  end,
})

-- 只读文件自动退出
vim.api.nvim_create_autocmd("BufReadPost", {
  pattern = "*",
  callback = function()
    if vim.o.readonly then
      vim.cmd("silent! q")
    end
  end,
})

-- 自动清除搜索高亮
vim.api.nvim_create_autocmd("ModeChanged", {
  pattern = "*",
  callback = function()
    if vim.fn.mode() ~= "n" then
      vim.cmd("nohlsearch")
    end
  end,
})

-- 删除行尾空格函数
function _G.CleanExtraSpaces()
  local save_cursor = vim.fn.getpos(".")
  local old_query = vim.fn.getreg('/')
  vim.cmd("silent! %s/\\s\\+$//e")
  vim.fn.setpos('.', save_cursor)
  vim.fn.setreg('/', old_query)
end

-- 设置 BufWritePre 自动命令清除行尾空格
vim.api.nvim_create_autocmd("BufWritePre", {
  pattern = { "*.txt", "*.js", "*.py", "*.wiki", "*.sh", "*.coffee" },
  callback = function()
    vim.cmd("call v:lua.CleanExtraSpaces()")
  end,
})

-- 自动返回上次退出时的光标位置
vim.api.nvim_create_autocmd("BufReadPost", {
  pattern = "*",
  callback = function()
    local last_pos = vim.fn.line("'\"")
    if last_pos > 1 and last_pos <= vim.fn.line("$") then
      vim.cmd('normal! g`"')
    end
  end,
})

-- 自动命令组：在 VimEnter 时检查 undo 目录并启用持久化撤销
vim.api.nvim_create_autocmd("VimEnter", {
  callback = function()
    local undodir = vim.fn.stdpath("data") .. "/undo"

    -- 如果目录不存在，则创建
    if vim.fn.isdirectory(undodir) == 0 then
      vim.fn.mkdir(undodir, "p")
      vim.notify("创建了 undo 目录: " .. undodir, vim.log.levels.INFO)
    end

    -- 启用 undo 功能
    vim.opt.undofile = true
    vim.opt.undodir = undodir
  end,
  desc = "检查并创建 undo 文件夹，启用持久化撤销",
})


----------------------------------------------------------------------------

-- 文件注释头

vim.api.nvim_create_autocmd("BufNewFile", {
  pattern = { "*.py", "*.sh", "*.pl", "*.js", "*.cpp", "*.go", "*.lua" },  -- 可以扩展到更多语言
  callback = function()
    SetComment()  -- 调用统一的设置注释头函数
  end,
})

-- 让光标跳到文件底部
vim.api.nvim_create_autocmd("BufNewFile", {
  pattern = "*",
  callback = function()
    vim.cmd("normal! G")
  end,
})

-- 获取当前时间的函数
local function get_current_time()
  return os.date("%Y-%m-%d %H:%M")
end

-- 通用的注释头设置函数
function SetComment()
  local filetype = vim.bo.filetype
  local author = "a6dg2uv"  -- 作者可以自定义
  local created_time = get_current_time()

  -- 根据文件类型动态设置文件头注释
  if filetype == "sh" then
    vim.api.nvim_buf_set_lines(0, 0, 1, false, {
      "#! /usr/bin/env bash",
      "# Author:        " .. author,
      "# Created Time:  " .. created_time,
      "",
      ""
    })
  elseif filetype == "py" then
    vim.api.nvim_buf_set_lines(0, 0, 1, false, {
      "#! /usr/bin/env python",
      "# -*- coding: utf-8 -*-",
      "# Author:        " .. author,
      "# Created Time:  " .. created_time,
      "",
      ""
    })
  elseif filetype == "pl" then
    vim.api.nvim_buf_set_lines(0, 0, 1, false, {
      "#! /usr/bin/env perl",
      "# -*- coding: utf-8 -*-",
      "# Author:        " .. author,
      "# Created Time:  " .. created_time,
      "",
      ""
    })
  elseif filetype == "js" then
    vim.api.nvim_buf_set_lines(0, 0, 1, false, {
      "// Author:        " .. author,
      "// Created Time:  " .. created_time,
      "// Script:        " .. vim.fn.expand("%:t"),
      "",
      ""
    })
  elseif filetype == "cpp" then
    vim.api.nvim_buf_set_lines(0, 0, 1, false, {
      "// Author:        " .. author,
      "// Created Time:  " .. created_time,
      "// File:          " .. vim.fn.expand("%:t"),
      "",
      ""
    })
  elseif filetype == "go" then
    vim.api.nvim_buf_set_lines(0, 0, 1, false, {
      "// Author:        " .. author,
      "// Created Time:  " .. created_time,
      "// File:          " .. vim.fn.expand("%:t"),
      "",
      ""
    })
  elseif filetype == "lua" then
    vim.api.nvim_buf_set_lines(0, 0, 1, false, {
      "-- Author:        " .. author,
      "-- Created Time:  " .. created_time,
      "-- File:          " .. vim.fn.expand("%:t"),
      "",
      ""
    })
  end
end

