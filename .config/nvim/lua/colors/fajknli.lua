-- 文件：lua/colors/mytheme.lua
local M = {}

function M.setup()
  vim.cmd("highlight clear")
  vim.cmd("syntax reset")
  vim.o.termguicolors = true
  vim.g.colors_name = "mytheme"

  local c = {
    bg        = "#151622",
    fg        = "#cdd6f4",
    -- comment   = "#464a5f",
    comment   = "#585e8f",
    cursorln  = "#1e1f2e",
    selection = "#2d2f4f",
    visual    = "#3b3f61",
    special   = "#b280be",

    black     = "#151622",
    red       = "#F08080",
    green     = "#a0d0a0",
    yellow    = "#dbd07f",
    blue      = "#607bc3",
    magenta   = "#b280be",
    cyan      = "#89b4fa",
    white     = "#a9b5d5",

    bright_black   = "#464a5f",
    bright_white   = "#a9b5d5",
  }

  local set = vim.api.nvim_set_hl

  -- 基础高亮
  set(0, "Normal",      { fg = c.fg, bg = c.bg })
  set(0, "Comment",     { fg = c.comment, italic = true })
  set(0, "CursorLine",  { bg = c.cursorln })
  set(0, "CursorColumn",  { bg = c.cursorln })
  set(0, "Visual",      { bg = c.visual })
  set(0, "LineNr",      { fg = c.comment })
  set(0, "CursorLineNr",{ fg = c.yellow })
  set(0, "Search",      { bg = c.selection, fg = c.fg })
  set(0, "Pmenu",       { bg = c.selection })
  set(0, "PmenuSel",    { bg = c.blue })
  set(0, "VertSplit",   { fg = c.comment })
  set(0, "StatusLine",  { fg = c.fg, bg = c.black })

  -- Treesitter
  set(0, "@function", { fg = c.blue })
  set(0, "@keyword",  { fg = c.magenta })
  set(0, "@comment",  { fg = c.comment, italic = true })
  set(0, "@string",   { fg = c.green })
  set(0, "@type",     { fg = c.yellow })
  set(0, "@variable", { fg = c.fg })
  set(0, "@field",    { fg = c.cyan })

  -- Diagnostic
  set(0, "DiagnosticError",   { fg = c.red })
  set(0, "DiagnosticWarn",    { fg = c.yellow })
  set(0, "DiagnosticInfo",    { fg = c.cyan })
  set(0, "DiagnosticHint",    { fg = c.green })
  set(0, "DiagnosticUnderlineError", { undercurl = true, sp = c.red })
  set(0, "DiagnosticUnderlineWarn",  { undercurl = true, sp = c.yellow })
  set(0, "DiagnosticUnderlineInfo",  { undercurl = true, sp = c.cyan })
  set(0, "DiagnosticUnderlineHint",  { undercurl = true, sp = c.green })

  -- Telescope
  set(0, "TelescopeNormal",    { bg = c.bg, fg = c.fg })
  set(0, "TelescopeBorder",    { fg = c.comment })
  set(0, "TelescopePromptTitle", { fg = c.magenta })
  set(0, "TelescopeSelection", { bg = c.selection })

  -- GitSigns
  set(0, "GitSignsAdd",    { fg = c.green })
  set(0, "GitSignsChange", { fg = c.yellow })
  set(0, "GitSignsDelete", { fg = c.red })

  -- cmp.nvim
  set(0, "CmpItemAbbr",  { fg = c.fg })
  set(0, "CmpItemMenu",  { fg = c.comment })
  set(0, "CmpItemKind",  { fg = c.cyan })

  -- 标题 & 特殊
  set(0, "Title",        { fg = c.special, bold = true })
  set(0, "Special",      { fg = c.special })
end

return M

