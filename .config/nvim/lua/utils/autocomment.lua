local function get_time()
    return os.date("%Y-%m-%d %H:%M")
end

local function set_header()
    local filetype = vim.bo.filetype  -- get fily type
    local author = "fajknli"            -- set your name
    local email = "fajknli@gmail.com"
    local filename = vim.fn.expand("%:t")       -- get file name
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
            "#!/user/bin/env python3",
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

    if vim.fn.line('$') == 1 and vim.fn.getline(1) == '' then
        local header = headers[filetype]
        if header then
            vim.api.nvim_buf_set_lines(0, 0, 1, false, header)
        end
    end
end

-- 1. 先创建一个 autogroup（并设置 clear=true）
local header_group = vim.api.nvim_create_augroup("FileHeaders", { clear = true })

-- 2. 将 autocmd 添加到这个组
vim.api.nvim_create_autocmd("BufNewFile", {
    pattern = {
        "*.sh", "*.py", "*.lua", 
        "*.c", "*.h", "*.cpp", "*.hpp", 
        "*.java", "*.go", "*.rs",
        "*.js", "*.ts", "*.php",
        "*.rb", "*.html", "*.css",
        "*.md", "*.markdown", "rst"
    },
    callback = function()
        set_header()
        print("自动插入 Shell 文件头")
        vim.cmd("normal! G")
    end,
    group = header_group  -- 关键！把这个 autocmd 放进 "FileHeaders" 组
})
