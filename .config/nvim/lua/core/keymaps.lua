-- keymaps
-- 移动行
vim.keymap.set('n', '<M-j>', ':move .+1<CR>', { desc = 'Move line down', noremap = true, silent = true })
vim.keymap.set('n', '<M-k>', ':move .-2<CR>', { desc = 'Move line up', noremap = true, silent = true })

-- 可视化模式移动更简洁的实现
vim.keymap.set('v', '<M-j>', ":m '>+1<CR>gv=gv", { desc = 'Move selection down', noremap = true, silent = true })
vim.keymap.set('v', '<M-k>', ":m '<-2<CR>gv=gv", { desc = 'Move selection up', noremap = true, silent = true })

-- 剪贴板操作快捷键
vim.keymap.set({'n', 'v'}, '<leader>y', '"+y', { desc = 'Yank to system clipboard', noremap = true, silent = true })
vim.keymap.set({'n', 'v'}, '<leader>p', '"+p', { desc = 'Paste from system clipboard', noremap = true, silent = true })
vim.keymap.set({'n', 'v'}, '<C-c>', '"+y', { desc = 'Yank to system clipboard', noremap = true, silent = true })
vim.keymap.set('i', '<C-v>', '<C-r>+', { desc = 'Paste from clipboard in insert mode', noremap = true, silent = true })

-- 文件操作
vim.keymap.set('n', '<leader>w', ':w<CR>', { desc = 'Save file', noremap = true, silent = true })
vim.keymap.set('n', '<leader>q', ':q<CR>', { desc = 'Quit', noremap = true, silent = true })
vim.keymap.set('n', '<leader>W', ':w !sudo tee % > /dev/null<CR>', { desc = 'Save with sudo', noremap = true, silent = true })

-- 窗口导航
vim.keymap.set('n', '<C-h>', '<C-w>h', { desc = 'Move to left window', noremap = true, silent = true })
vim.keymap.set('n', '<C-j>', '<C-w>j', { desc = 'Move to below window', noremap = true, silent = true })
vim.keymap.set('n', '<C-k>', '<C-w>k', { desc = 'Move to above window', noremap = true, silent = true })
vim.keymap.set('n', '<C-l>', '<C-w>l', { desc = 'Move to right window', noremap = true, silent = true })

-- 水平分割并保持目录上下文
vim.keymap.set('n', '<leader>hh', function()
  -- 先保存当前窗口的局部目录
  local file = vim.fn.input('Horizontal split: ', './', 'file')
  if file ~= '' then
    vim.cmd('split ' .. file)
    -- 新窗口会自动触发上面的自动命令设置正确的lcd
  end
end, { desc = 'Horizontal split with local directory context' })

-- 垂直分割并保持目录上下文
vim.keymap.set('n', '<leader>vv', function()
  local file = vim.fn.input('Vertical split: ', './', 'file')
  if file ~= '' then
    vim.cmd('vsplit ' .. file)
  end
end, { desc = 'Vertical split with local directory context' })

-- 设置窗口大小调整快捷键
vim.keymap.set('n', '<Tab>h', '<C-w>5<', { desc = 'Decrease window width', noremap = true, silent = true })
vim.keymap.set('n', '<Tab>l', '<C-w>5>', { desc = 'Increase window width', noremap = true, silent = true })
vim.keymap.set('n', '<Tab>j', '<C-w>5+', { desc = 'Decrease window height', noremap = true, silent = true })
vim.keymap.set('n', '<Tab>k', '<C-w>5-', { desc = 'Increase window height', noremap = true, silent = true })

-- 窗口最大化/恢复
vim.keymap.set('n', '<leader>w-', ':wincmd _<CR>:wincmd |<CR>', { desc = 'Maximize window', noremap = true, silent = true })
vim.keymap.set('n', '<leader>w=', ':wincmd =<CR>', { desc = 'Balance windows', noremap = true, silent = true })

-- 窗口移动
vim.keymap.set('n', '<leader>wh', ':wincmd H<CR>', { desc = 'Move window left', noremap = true, silent = true })
vim.keymap.set('n', '<leader>wj', ':wincmd J<CR>', { desc = 'Move window down', noremap = true, silent = true })
vim.keymap.set('n', '<leader>wk', ':wincmd K<CR>', { desc = 'Move window up', noremap = true, silent = true })
vim.keymap.set('n', '<leader>wl', ':wincmd L<CR>', { desc = 'Move window right', noremap = true, silent = true })

-- 在当前窗口打开文件
vim.keymap.set('n', '<leader>o', ':edit ', { desc = 'Open file in current window' })

-- 快速切换最近文件
vim.keymap.set('n', '<leader><leader>', '<C-^>', { desc = 'Switch to alternate file', noremap = true, silent = true })

-- 命令行光标移动
vim.keymap.set('c', '<C-a>', '<Home>', { desc = '移动到行首', noremap = true })
vim.keymap.set('c', '<C-e>', '<End>', { desc = '移动到行尾', noremap = true })
vim.keymap.set('c', '<C-b>', '<Left>', { desc = '左移字符', noremap = true })
vim.keymap.set('c', '<C-f>', '<Right>', { desc = '右移字符', noremap = true })
vim.keymap.set('c', '<M-b>', '<S-Left>', { desc = '左移单词', noremap = true })
vim.keymap.set('c', '<M-f>', '<S-Right>', { desc = '右移单词', noremap = true })

-- 更符合现代编辑器的删除操作
vim.keymap.set('c', '<C-d>', '<Del>', { desc = '删除右侧字符', noremap = true })
vim.keymap.set('c', '<C-h>', '<BS>', { desc = '删除左侧字符', noremap = true })
vim.keymap.set('c', '<C-w>', '<C-Right><C-w>', { desc = '删除左侧单词', noremap = true })
vim.keymap.set('c', '<M-d>', '<C-Right><C-w>', { desc = '删除右侧单词', noremap = true })



-- 长行移动
vim.keymap.set('n', 'j', 'gj', { desc = 'Move in graph', noremap = true, silent =true })
vim.keymap.set('n', 'k', 'gk', { desc = 'Move in graph', noremap = true, silent =true })

-- 标签页操作
-- 更一致的键位前缀
vim.keymap.set('n', '<leader>t', ':tabnew<CR>', { desc = 'New tab', noremap = true, silent = true })
--vim.keymap.set('n', '<leader>to', ':tabonly<CR>', { desc = 'Close other tabs', noremap = true, silent = true })
vim.keymap.set('n', '<leader>tc', ':tabclose<CR>', { desc = 'Close tab', noremap = true, silent = true })
vim.keymap.set('n', '<leader>tn', ':tabnext<CR>', { desc = 'Next tab', noremap = true, silent = true })
vim.keymap.set('n', '<leader>tp', ':tabprevious<CR>', { desc = 'Previous tab', noremap = true, silent = true })
vim.keymap.set('n', '<leader>tm', ':tabmove', { desc = 'Move tab', noremap = true, silent = true })

-- 缓冲区操作
--vim.api.nvim_set_keymap('n', '<leader>b', ':enew<CR>', { noremap = true, silent = true })
--vim.api.nvim_set_keymap('n', '<leader>bn', ':bnext<CR>', { noremap = true, silent = true })
--vim.api.nvim_set_keymap('n', '<leader>bd', ':bdelete<CR>', { noremap = true, silent = true })
vim.keymap.set('n', '<leader>bc', ':enew<CR>', { desc = 'New buffer', noremap = true, silent = true })
vim.keymap.set('n', '<leader>bn', ':bnext<CR>', { desc = 'Next buffer', noremap = true, silent = true })
vim.keymap.set('n', '<leader>bp', ':bprevious<CR>', { desc = 'Previous buffer', noremap = true, silent = true })
vim.keymap.set('n', '<leader>bd', ':bdelete<CR>', { desc = 'Delete buffer', noremap = true, silent = true })
vim.keymap.set('n', '<leader>bl', ':buffers<CR>', { desc = 'List buffers', noremap = true, silent = true })

-- 搜索
--vim.api.nvim_set_keymap('n', '<silent> <leader><leader>', ':nohlsearch<CR>', { noremap = true, silent = true })
--vim.api.nvim_set_keymap('v', '<silent> *', ':<C-u>call VisualSelection("", "")<CR>/<C-R>=@/<CR><CR>', { noremap = true, silent = true })
--vim.api.nvim_set_keymap('v', '<silent> #', ':<C-u>call VisualSelection("", "")<CR>?<C-R>=@/<CR><CR>', { noremap = true, silent = true })
-- 更好的可视化搜索实现
vim.keymap.set('v', '*', [[y/<C-R>=escape(@", '/\')<CR><CR>]], { desc = 'Search selected text forward', noremap = true, silent = true })
vim.keymap.set('v', '#', [[y?<C-R>=escape(@", '?\')<CR><CR>]], { desc = 'Search selected text backward', noremap = true, silent = true })
vim.keymap.set('n', '<leader>sc', ':nohlsearch<CR>', { desc = 'Clear search highlight', noremap = true, silent = true })

-- FZF 模糊搜索
--vim.api.nvim_set_keymap('n', '<leader>f', ':FZF<CR>', { noremap = true, silent = true })


-- 拼写检查
vim.keymap.set('n', '<leader>ss', ':setlocal spell!<CR>', { desc = 'Toggle spell check', noremap = true, silent = true })
vim.keymap.set('n', '<leader>sn', ']s', { desc = 'Next spelling error', noremap = true, silent = true })
vim.keymap.set('n', '<leader>sp', '[s', { desc = 'Previous spelling error', noremap = true, silent = true })
vim.keymap.set('n', '<leader>sa', 'zg', { desc = 'Add to dictionary', noremap = true, silent = true })
vim.keymap.set('n', '<leader>s?', 'z=', { desc = 'Spelling suggestions', noremap = true, silent = true })

-- other
-- 快速跳转到行首/行尾
vim.keymap.set('n', 'H', '^', { desc = 'Move to first non-blank char', noremap = true, silent = true })
vim.keymap.set('n', 'L', '$', { desc = 'Move to end of line', noremap = true, silent = true })

-- 保持视觉模式选择
vim.keymap.set('v', '<', '<gv', { desc = 'Indent left and keep selection', noremap = true, silent = true })
vim.keymap.set('v', '>', '>gv', { desc = 'Indent right and keep selection', noremap = true, silent = true })

-- endofline

-- 常用折叠快捷键
-- vim.keymap.set('n', 'zc', 'zc', { desc = 'Fold current' })      -- 折叠当前
-- vim.keymap.set('n', 'zo', 'zo', { desc = 'Unfold current' })    -- 展开当前
-- vim.keymap.set('n', 'za', 'za', { desc = 'Toggle fold' })       -- 切换折叠
-- vim.keymap.set('n', 'zR', 'zR', { desc = 'Unfold all' })        -- 展开所有
-- vim.keymap.set('n', 'zM', 'zM', { desc = 'Fold all' })          -- 折叠所有
-- vim.keymap.set('n', 'zj', 'zj', { desc = 'Next fold' })         -- 跳到下一个折叠
-- vim.keymap.set('n', 'zk', 'zk', { desc = 'Prev fold' })         -- 跳到上一个折叠

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

-- ========== 通用括号操作（支持所有可视模式）==========
-- 添加括号：支持所有可视模式
vim.keymap.set('v', '<leader>s', function()
  -- 获取可视模式类型
  local mode = vim.fn.visualmode()
  
  -- 保存选中的文本
  vim.cmd('normal! "xy')
  local text = vim.fn.getreg('x')
  
  -- 提示用户选择括号类型
  vim.cmd('echo "Surround with: () [] {} <> \\" \' ` * _ ~"')
  local char = vim.fn.getchar()
  local bracket = vim.fn.nr2char(char)
  
  local pairs = {
    ['('] = {'(', ')'}, [')'] = {'(', ')'},
    ['['] = {'[', ']'}, [']'] = {'[', ']'},
    ['{'] = {'{', '}'}, ['}'] = {'{', '}'},
    ['<'] = {'<', '>'}, ['>'] = {'<', '>'},
    ['"'] = {'"', '"'},
    ["'"] = {"'", "'"},
    ['`'] = {'`', '`'},
    ['*'] = {'*', '*'},
    ['_'] = {'_', '_'},
    ['~'] = {'~', '~'},
  }
  
  if pairs[bracket] then
    local left, right = pairs[bracket][1], pairs[bracket][2]
    
    -- 处理不同的可视模式
    if mode == 'V' or mode == '\22' then  -- Visual line 或 Visual block
      -- 对于整行模式，在每行前后添加括号
      local lines = vim.split(text, '\n', {plain = true})
      local new_lines = {}
      for _, line in ipairs(lines) do
        if line ~= '' then
          table.insert(new_lines, left .. line .. right)
        else
          table.insert(new_lines, line)
        end
      end
      local result = table.concat(new_lines, '\n')
      
      -- 使用寄存器来插入，避免特殊字符问题
      vim.fn.setreg('z', result)
      vim.cmd('normal! gv"zp')
    else  -- 字符模式
      local result = left .. text .. right
      vim.fn.setreg('z', result)
      vim.cmd('normal! gv"zp')
    end
    
    vim.cmd('echo ""')
  end
end, { noremap = true, silent = false, desc = "Surround with..." })

-- Normal 模式：给当前单词加括号
vim.keymap.set('n', '<leader>s', function()
  vim.cmd('normal! viw"xy')
  local text = vim.fn.getreg('x')
  
  vim.cmd('echo "Surround with: () [] {} <> \\" \' ` * _ ~"')
  local char = vim.fn.getchar()
  local bracket = vim.fn.nr2char(char)
  
  local pairs = {
    ['('] = {'(', ')'}, [')'] = {'(', ')'},
    ['['] = {'[', ']'}, [']'] = {'[', ']'},
    ['{'] = {'{', '}'}, ['}'] = {'{', '}'},
    ['<'] = {'<', '>'}, ['>'] = {'<', '>'},
    ['"'] = {'"', '"'},
    ["'"] = {"'", "'"},
    ['`'] = {'`', '`'},
    ['*'] = {'*', '*'},
    ['_'] = {'_', '_'},
    ['~'] = {'~', '~'},
  }
  
  if pairs[bracket] then
    local left, right = pairs[bracket][1], pairs[bracket][2]
    local result = left .. text .. right
    vim.fn.setreg('z', result)
    vim.cmd('normal! viw"zp')
  end
  vim.cmd('echo ""')
end, { noremap = true, silent = false, desc = "Surround word with..." })

-- 删除括号
vim.keymap.set('n', '<leader>ds', function()
  local pairs = {
    ['('] = ')', [')'] = '(',
    ['['] = ']', [']'] = '[',
    ['{'] = '}', ['}'] = '{',
    ['<'] = '>', ['>'] = '<',
    ['"'] = '"', ["'"] = "'", ['`'] = '`',
    ['*'] = '*', ['_'] = '_', ['~'] = '~',
  }
  
  local line = vim.api.nvim_get_current_line()
  local row, col = unpack(vim.api.nvim_win_get_cursor(0))
  
  local start_pos, start_char = nil, nil
  for i = col, 0, -1 do
    local c = line:sub(i+1, i+1)
    if pairs[c] then
      start_pos, start_char = i, c
      break
    end
  end
  
  local end_pos = nil
  if start_char and pairs[start_char] then
    for i = col+1, #line do
      if line:sub(i+1, i+1) == pairs[start_char] then
        end_pos = i
        break
      end
    end
  end
  
  if start_pos and end_pos then
    local new_line = line:sub(1, start_pos) .. line:sub(start_pos+2, end_pos) .. line:sub(end_pos+2)
    vim.api.nvim_set_current_line(new_line)
    if col > start_pos then
      vim.api.nvim_win_set_cursor(0, {row, col-1})
    end
  else
    print("No surrounding found")
  end
end, { noremap = true, silent = true, desc = "Delete surrounding" })

-- 修改括号
vim.keymap.set('n', '<leader>cs', function()
  local pairs = {
    ['('] = ')', [')'] = '(',
    ['['] = ']', [']'] = '[',
    ['{'] = '}', ['}'] = '{',
    ['<'] = '>', ['>'] = '<',
    ['"'] = '"', ["'"] = "'", ['`'] = '`',
  }
  
  local line = vim.api.nvim_get_current_line()
  local row, col = unpack(vim.api.nvim_win_get_cursor(0))
  
  local start_pos, start_char = nil, nil
  for i = col, 0, -1 do
    local c = line:sub(i+1, i+1)
    if pairs[c] then
      start_pos, start_char = i, c
      break
    end
  end
  
  local end_pos = nil
  if start_char and pairs[start_char] then
    for i = col+1, #line do
      if line:sub(i+1, i+1) == pairs[start_char] then
        end_pos = i
        break
      end
    end
  end
  
  if not (start_pos and end_pos) then
    print("No surrounding found")
    return
  end
  
  local text = line:sub(start_pos+2, end_pos)
  
  vim.cmd('echo "Change to: () [] {} <> \\" \' `"')
  local char = vim.fn.getchar()
  local bracket = vim.fn.nr2char(char)
  
  local new_pairs = {
    ['('] = {'(', ')'}, [')'] = {'(', ')'},
    ['['] = {'[', ']'}, [']'] = {'[', ']'},
    ['{'] = {'{', '}'}, ['}'] = {'{', '}'},
    ['<'] = {'<', '>'}, ['>'] = {'<', '>'},
    ['"'] = {'"', '"'},
    ["'"] = {"'", "'"},
    ['`'] = {'`', '`'},
  }
  
  if new_pairs[bracket] then
    local left, right = new_pairs[bracket][1], new_pairs[bracket][2]
    local new_line = line:sub(1, start_pos) .. left .. text .. right .. line:sub(end_pos+2)
    vim.api.nvim_set_current_line(new_line)
  end
  vim.cmd('echo ""')
end, { noremap = true, silent = false, desc = "Change surrounding" })


-- ========== 执行文件 ==========
vim.keymap.set("n", "<leader>r", function()
  local ft = vim.bo.filetype
  local cmd = ""

  if ft == "python" then
    cmd = "python3 %"
  elseif ft == "cpp" then
    cmd = "g++ % -o %< && ./%<"
  elseif ft == "c" then
    cmd = "gcc % -o %< && ./%<"
  elseif ft == "java" then
    cmd = "javac % && java %<"
  elseif ft == "javascript" then
    cmd = "node %"
  elseif ft == "typescript" then
    cmd = "ts-node %"
  elseif ft == "lua" then
    cmd = "lua %"
  elseif ft == "sh" then
    cmd = "bash %"
  elseif ft == "go" then
    cmd = "go run %"
  elseif ft == "rust" then
    cmd = "rustc % && ./%<"
  else
    print("Unsupported filetype: " .. ft)
    return
  end

  vim.cmd("w") -- 保存当前文件
  vim.cmd("botright split term://" .. cmd) -- 在底部打开终端运行
  vim.cmd("resize 20") --控制终端高度，为20行
end)
