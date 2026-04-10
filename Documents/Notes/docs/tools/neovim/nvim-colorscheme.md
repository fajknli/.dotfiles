# Neovim 配色主题

## 主题名称

fajknli 自定义主题

## 启用方式

```lua
-- 在 Neovim 配置中
require("colors.fajknli").setup()
```

## 颜色定义

| 名称 | 色值 | 用途 |
|------|------|------|
| `bg` | `#151622` | 背景色 |
| `fg` | `#a9b5d5` | 前景色（文字） |
| `comment` | `#585e8f` | 注释颜色 |
| `cursorln` | `#1e1f2e` | 当前行背景 |
| `selection` | `#2d2f4f` | 选中区域背景 |
| `visual` | `#3b3f61` | 可视模式背景 |
| `special` | `#b280be` | 特殊字符 |

## 基础颜色

| 名称 | 色值 |
|------|------|
| `black` | `#151622` |
| `red` | `#f08080` |
| `green` | `#a0d0a0` |
| `yellow` | `#dbd07f` |
| `blue` | `#607bc3` |
| `magenta` | `#b280be` |
| `cyan` | `#89b4fa` |
| `white` | `#a9b5d5` |

## 明亮色

| 名称 | 色值 |
|------|------|
| `bright_black` | `#1f2032` |
| `bright_white` | `#a9b5d5` |

## 基础高亮组

| 高亮组 | 前景色 | 背景色 | 样式 |
|--------|--------|--------|------|
| `Normal` | `fg` | `bg` | - |
| `Comment` | `comment` | - | 斜体 |
| `CursorLine` | - | `cursorln` | - |
| `CursorColumn` | - | `cursorln` | - |
| `Visual` | - | `visual` | - |
| `LineNr` | `comment` | - | - |
| `CursorLineNr` | `yellow` | - | - |
| `Search` | `fg` | `selection` | - |
| `Pmenu` | - | `selection` | - |
| `PmenuSel` | - | `blue` | - |
| `VertSplit` | `comment` | - | - |
| `StatusLine` | `fg` | `black` | - |
| `ColorColumn` | - | `bright_black` | - |

## Treesitter 高亮组

| 高亮组 | 颜色 | 说明 |
|--------|------|------|
| `@function` | `blue` | 函数 |
| `@keyword` | `magenta` | 关键字 |
| `@comment` | `comment` | 注释（斜体） |
| `@string` | `green` | 字符串 |
| `@type` | `yellow` | 类型 |
| `@variable` | `fg` | 变量 |
| `@field` | `cyan` | 字段 |

## 诊断高亮组

| 高亮组 | 颜色 | 说明 |
|--------|------|------|
| `DiagnosticError` | `red` | 错误 |
| `DiagnosticWarn` | `yellow` | 警告 |
| `DiagnosticInfo` | `cyan` | 信息 |
| `DiagnosticHint` | `green` | 提示 |
| `DiagnosticUnderlineError` | `red` | 错误下划线 |
| `DiagnosticUnderlineWarn` | `yellow` | 警告下划线 |
| `DiagnosticUnderlineInfo` | `cyan` | 信息下划线 |
| `DiagnosticUnderlineHint` | `green` | 提示下划线 |

## Telescope 高亮组

| 高亮组 | 前景色 | 背景色 |
|--------|--------|--------|
| `TelescopeNormal` | `fg` | `bg` |
| `TelescopeBorder` | `comment` | - |
| `TelescopePromptTitle` | `magenta` | - |
| `TelescopeSelection` | - | `selection` |

## GitSigns 高亮组

| 高亮组 | 颜色 |
|--------|------|
| `GitSignsAdd` | `green` |
| `GitSignsChange` | `yellow` |
| `GitSignsDelete` | `red` |

## CMP 补全高亮组

| 高亮组 | 颜色 |
|--------|------|
| `CmpItemAbbr` | `fg` |
| `CmpItemMenu` | `comment` |
| `CmpItemKind` | `cyan` |

## 其他高亮组

| 高亮组 | 颜色 | 样式 |
|--------|------|------|
| `Title` | `special` | 粗体 |
| `Special` | `special` | - |

## 状态栏高亮组

| 高亮组 | 前景色 | 背景色 | 样式 |
|--------|--------|--------|------|
| `User2` | `#151622` | `#a0d0a0` | 粗体 |
| `StatusLine` | `#a9b5d5` | `#4e5078` | 粗体 |
| `StatusLineNC` | `#a9b5d5` | `#222335` | - |

## 主题特点

- 深色背景（`#151622`），适合长时间编码
- 低饱和度颜色，减少视觉疲劳
- 注释使用斜体，易于区分
- 语法高亮语义化（函数蓝色、关键字紫色、字符串绿色）
- 诊断信息使用鲜明颜色（错误红色、警告黄色）
- 状态栏使用绿色高亮文件名

## 一句话总结

自定义深色主题，背景 `#151622`，前景 `#a9b5d5`。注释斜体灰色，函数蓝色，关键字紫色，字符串绿色，错误红色，警告黄色。启用 termguicolors 需要终端支持真彩色。
