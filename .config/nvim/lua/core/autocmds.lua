-- autocmds

local EXT_MAP = {
    sh = "sh", py = "python", lua = "lua",
    c = "c", h = "c", cpp = "cpp", hpp = "cpp",
    java = "java", go = "go", rs = "rust",
    js = "javascript", ts = "typescript", php = "php",
    rb = "ruby", html = "html", css = "css",
    md = "markdown", markdown = "markdown"
}

local function get_header(filetype, author, email, time)
    local templates = {
        sh = { shebang = "#!/bin/sh", comment = "#" },
        python = { shebang = "#!/usr/bin/env python3", comment = "#" },
        lua = { shebang = "#!/usr/bin/env lua", comment = "--" },
        c = { shebang = nil, comment = "//", style = "c" },
        cpp = { shebang = nil, comment = "//", style = "c" },
        java = { shebang = nil, comment = "//", style = "c" },
        javascript = { shebang = nil, comment = "//", style = "c" },
        typescript = { shebang = nil, comment = "//", style = "c" },
        go = { shebang = nil, comment = "//", style = "c" },
        rust = { shebang = nil, comment = "//", style = "c" },
        php = { shebang = "<?php", comment = "//", style = "c" },
        ruby = { shebang = "#!/usr/bin/env ruby", comment = "#" },
        html = { shebang = nil, comment = "<!--", style = "html" },
        css = { shebang = nil, comment = "/*", style = "c" },
        markdown = { shebang = nil, comment = "<!--", style = "html" },
        rst = { shebang = nil, comment = "..", style = "rst" },
    }

    local tmpl = templates[filetype]
    if not tmpl then return nil end

    local lines = {}

    -- 添加 shebang
    if tmpl.shebang then
        table.insert(lines, tmpl.shebang)
        table.insert(lines, "")
    end

    -- 根据样式生成头部
    if tmpl.style == "c" then
        table.insert(lines, tmpl.comment .. " Author:       " .. author)
        table.insert(lines, tmpl.comment .. " Email:        " .. email)
        table.insert(lines, tmpl.comment .. " Created Time: " .. time)
        table.insert(lines, tmpl.comment)
    elseif tmpl.style == "html" then
        table.insert(lines, tmpl.comment)
        table.insert(lines, "  Author:       " .. author)
        table.insert(lines, "  Email:        " .. email)
        table.insert(lines, "  Created Time: " .. time)
        table.insert(lines, "-->")
    elseif tmpl.style == "rst" then
        table.insert(lines, tmpl.comment .. " Author:       " .. author)
        table.insert(lines, tmpl.comment .. " Email:        " .. email)
        table.insert(lines, tmpl.comment .. " Created Time: " .. time)
    else
        -- 默认使用 comment 前缀
        table.insert(lines, tmpl.comment .. " Author:       " .. author)
        table.insert(lines, tmpl.comment .. " Email:        " .. email)
        table.insert(lines, tmpl.comment .. " Created Time: " .. time)
        table.insert(lines, "")
    end

    table.insert(lines, "")
    return lines
end

-- 为每个窗口自动设置局部工作目录到当前文件所在目录
vim.api.nvim_create_autocmd({"BufEnter", "BufWinEnter"}, {
    pattern = "*",
    callback = function()
        local buf_dir = vim.fn.expand("%:p:h")
        if vim.fn.isdirectory(buf_dir) == 1 then
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
local function clean_extra_spaces()
    local save_cursor = vim.fn.getpos(".")
    local old_query = vim.fn.getreg('/')
    vim.cmd("silent! %s/\\s\\+$//e")
    vim.fn.setpos('.', save_cursor)
    vim.fn.setreg('/', old_query)
end

-- 设置 BufWritePre 自动命令清除行尾空格
vim.api.nvim_create_autocmd("BufWritePre", {
    pattern = { "*.txt", "*.js", "*.py", "*.wiki", "*.sh", "*.coffee", "*.lua", "*.c", "*.cpp", "*.go", "*.rs", "*.java" },
    callback = clean_extra_spaces,
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
        if vim.fn.isdirectory(undodir) == 0 then
            vim.fn.mkdir(undodir, "p")
            vim.notify("创建了 undo 目录: " .. undodir, vim.log.levels.INFO)
        end
        vim.opt.undofile = true
        vim.opt.undodir = undodir
    end,
    desc = "检查并创建 undo 文件夹，启用持久化撤销",
})

-- 自动插入文件头
local function set_header()
    local ext = vim.fn.expand('%:e')
    local filetype = EXT_MAP[ext] or ext

    local author = "fajknli"
    local email = "fajknli@gmail.com"
    local time = os.date("%Y-%m-%d %H:%M")

    local is_empty = vim.fn.line('$') <= 1 and vim.fn.trim(vim.fn.getline(1)) == ''
    if is_empty then
        local header_lines = get_header(filetype, author, email, time)
        if header_lines then
            vim.api.nvim_buf_set_lines(0, 0, 0, false, header_lines)
            vim.cmd("normal! G")
        end
    end
end

local header_group = vim.api.nvim_create_augroup("FileHeaders", { clear = true })
vim.api.nvim_create_autocmd("BufNewFile", {
    pattern = "*",
    group = header_group,
    callback = set_header
})

-- 清理所有寄存器
vim.api.nvim_create_user_command('ClearRegisters', function()
    local registers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/-"'
    for i = 1, #registers do
        local reg = registers:sub(i, i)
        vim.fn.setreg(reg, '')
    end
    print("All registers cleared!")
end, {})
