-- autocmds
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

-- 只读文件自动退出
vim.api.nvim_create_autocmd("BufReadPost", {
  pattern = "*",
  callback = function()
    if vim.o.readonly then
      vim.cmd("silent! q")
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

local function get_time()
    return os.date("%Y-%m-%d %H:%M")
end

local function set_header()
    -- 改用文件扩展名检测
    local ext_map = {
        sh = "sh", py = "python", lua = "lua",
        c = "c", h = "c", cpp = "cpp", hpp = "cpp",
        java = "java", go = "go", rs = "rust",
        js = "javascript", ts = "typescript", php = "php",
        rb = "ruby", html = "html", css = "css",
        md = "markdown", markdown = "markdown"
    }
    local ext = vim.fn.expand('%:e')
    local filetype = ext_map[ext] or ext
    
    local author = "fajknli"
    local email = "fajknli@gmail.com"
    local filename = vim.fn.expand('%:t')
    local time = get_time()

    local headers = {
        sh = {
            "#!/bin/sh",
            "",
            "# Author:       " .. author,
            "# Emial         " .. email,
            "# Created Time: " .. time,
            "# Filename:     " .. filename,
            "",
            ""
        },
        python = {
            "#!/usr/bin/env python3",
            "",
            "# Author:       " .. author,
            "# Emial         " .. email,
            "# Created Time: " .. time,
            "# Filename:     " .. filename,
            "",
            ""
        },
        lua = {
            "#!/usr/bin/env lua",
            "",
            "-- Author:       " .. author,
            "-- Email:        " .. email,
            "-- Created Time: " .. time,
            "-- Filename:     " .. filename,
            "",
            ""
        },
        c = {
            "/*",
            " * Author:       " .. author,
            " * Email:        " .. email,
            " * Created Time: " .. time,
            " * Filename:     " .. filename,
            " */",
            "",
            ""
        },
        cpp = {
            "/*",
            " * Author:       " .. author,
            " * Email:        " .. email,
            " * Created Time: " .. time,
            " * Filename:     " .. filename,
            " */",
            "",
            ""
        },
        java = {
            "/*",
            " * Author:       " .. author,
            " * Email:        " .. email,
            " * Created Time: " .. time,
            " * Filename:     " .. filename,
            " */",
            "",
            ""
        },
        go = {
            "/*",
            " * Author:       " .. author,
            " * Email:        " .. email,
            " * Created Time: " .. time,
            " * Filename:     " .. filename,
            " */",
            "",
            ""
        },
        rust = {
            "/*",
            " * Author:       " .. author,
            " * Email:        " .. email,
            " * Created Time: " .. time,
            " * Filename:     " .. filename,
            " */",
            "",
            ""
        },
        javascript = {
            "/*",
            " * Author:       " .. author,
            " * Email:        " .. email,
            " * Created Time: " .. time,
            " * Filename:     " .. filename,
            " */",
            "",
            ""
        },
        typescript = {
            "/*",
            " * Author:       " .. author,
            " * Email:        " .. email,
            " * Created Time: " .. time,
            " * Filename:     " .. filename,
            " */",
            "",
            ""
        },
        php = {
            "<?php",
            "/*",
            " * Author:       " .. author,
            " * Email:        " .. email,
            " * Created Time: " .. time,
            " * Filename:     " .. filename,
            " */",
            "",
            ""
        },
        ruby = {
            "#!/usr/bin/env ruby",
            "",
            "# Author:       " .. author,
            "# Email:        " .. email,
            "# Created Time: " .. time,
            "# Filename:     " .. filename,
            "",
            ""
        },
        html = {
            "<!--",
            "  Author:       " .. author,
            "  Email:        " .. email,
            "  Created Time: " .. time,
            "  Filename:     " .. filename,
            "-->",
            "",
            ""
        },
        css = {
            "/*",
            " * Author:       " .. author,
            " * Email:        " .. email,
            " * Created Time: " .. time,
            " * Filename:     " .. filename,
            " */",
            "",
            ""
        },
        markdown = {
            "<!--",
            "  Author:       " .. author,
            "  Email:        " .. email,
            "  Created Time: " .. time,
            "  Filename:     " .. filename,
            "-->",
            "",
            ""
        },
        rst = {
            ".. Author:       " .. author,
            ".. Email:        " .. email,
            ".. Created Time: " .. time,
            ".. Filename:     " .. filename,
            "",
            ""
        },
    }

    -- 更宽松的空文件检测
    local is_empty = vim.fn.line('$') <= 1 and vim.fn.trim(vim.fn.getline(1)) == ''
    if is_empty and headers[filetype] then
        vim.api.nvim_buf_set_lines(0, 0, 0, false, headers[filetype])
        vim.cmd("normal! G")  -- 移动光标到文件末尾
    end
end

-- 注册自动命令
local header_group = vim.api.nvim_create_augroup("FileHeaders", { clear = true })
vim.api.nvim_create_autocmd("BufNewFile", {
    pattern = "*",  -- 改为监听所有文件，在函数内过滤
    group = header_group,
    callback = set_header  -- 直接引用函数
})
