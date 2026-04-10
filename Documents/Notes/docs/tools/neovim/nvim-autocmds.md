# Neovim 自动命令

## 自动切换工作目录

打开文件或进入窗口时，自动将当前工作目录切换到文件所在目录。

```lua
vim.api.nvim_create_autocmd({"BufEnter", "BufWinEnter"}, {
    pattern = "*",
    callback = function()
        local buf_dir = vim.fn.expand("%:p:h")
        if vim.fn.isdirectory(buf_dir) == 1 then
            vim.cmd("lcd " .. vim.fn.fnameescape(buf_dir))
        end
    end,
})
```

## 只读文件自动退出

如果打开的文件是只读模式，自动退出（避免意外编辑）。

```lua
vim.api.nvim_create_autocmd("BufReadPost", {
    pattern = "*",
    callback = function()
        if vim.o.readonly then
            vim.cmd("silent! q")
        end
    end,
})
```

## 保存时自动删除行尾空格

保存以下类型文件时，自动删除行尾多余空格。

```lua
local function clean_extra_spaces()
    local save_cursor = vim.fn.getpos(".")
    local old_query = vim.fn.getreg('/')
    vim.cmd("silent! %s/\\s\\+$//e")
    vim.fn.setpos('.', save_cursor)
    vim.fn.setreg('/', old_query)
end

vim.api.nvim_create_autocmd("BufWritePre", {
    pattern = { "*.txt", "*.js", "*.py", "*.wiki", "*.sh", "*.coffee", "*.lua", "*.c", "*.cpp", "*.go", "*.rs", "*.java" },
    callback = clean_extra_spaces,
})
```

## 自动回到上次编辑位置

打开文件时，自动跳转到上次退出时的光标位置。

```lua
vim.api.nvim_create_autocmd("BufReadPost", {
    pattern = "*",
    callback = function()
        local last_pos = vim.fn.line("'\"")
        if last_pos > 1 and last_pos <= vim.fn.line("$") then
            vim.cmd('normal! g`"')
        end
    end,
})
```

## 自动创建撤销目录并启用持久化撤销

首次启动时自动创建 undo 目录，并启用持久化撤销功能。

```lua
vim.api.nvim_create_autocmd("VimEnter", {
    callback = function()
        local undodir = vim.fn.stdpath("data") .. "/undo"
        if vim.fn.isdirectory(undodir) == 0 then
            vim.fn.mkdir(undodir, "p")
        end
        vim.opt.undofile = true
        vim.opt.undodir = undodir
    end,
})
```

## 自动插入文件头

新建文件时，根据文件类型自动插入文件头（包含作者、邮箱、创建时间）。

支持的文件类型：
- sh、python、lua → shebang + 注释头
- c、cpp、java、go、rust、javascript、typescript、php → C 风格注释头
- html、css、markdown → HTML 风格注释头
- rst → reST 风格注释头

```lua
-- 文件类型映射
local EXT_MAP = {
    sh = "sh", py = "python", lua = "lua",
    c = "c", h = "c", cpp = "cpp", hpp = "cpp",
    java = "java", go = "go", rs = "rust",
    js = "javascript", ts = "typescript", php = "php",
    rb = "ruby", html = "html", css = "css",
    md = "markdown", markdown = "markdown"
}

-- 自动插入文件头（新文件且为空时触发）
vim.api.nvim_create_autocmd("BufNewFile", {
    pattern = "*",
    callback = set_header
})
```

## 用户命令

### 清空所有寄存器

```lua
vim.api.nvim_create_user_command('ClearRegisters', function()
    local registers = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/-"'
    for i = 1, #registers do
        local reg = registers:sub(i, i)
        vim.fn.setreg(reg, '')
    end
    print("All registers cleared!")
end, {})
```

使用：`:ClearRegisters`

## 一句话总结

核心自动命令：`BufWritePre` 自动删除行尾空格，`BufReadPost` 回到上次编辑位置，`VimEnter` 自动创建 undo 目录，`BufNewFile` 自动插入文件头。`:ClearRegisters` 清空所有寄存器。
