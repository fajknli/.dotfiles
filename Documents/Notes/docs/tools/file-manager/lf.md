# lf 文件管理器配置与快捷键

## 配置文件位置

```bash
~/.config/lf/lfrc          # 主配置文件
~/.config/lf/cmds           # 自定义命令
~/.config/lf/maps           # 快捷键映射
~/.config/lf/locate         # 快速跳转路径
~/.config/lf/colors         # 颜色配置
~/.config/lf/icons          # 图标配置
```

## 一、基础配置（lfrc）

```bash
# 加载配置文件
source ~/.config/lf/cmds
source ~/.config/lf/maps

# 预览器（使用外部脚本）
set previewer ~/.local/bin/filepreviewer

# Shell 解释器
set shell sh

# 显示相对行号
set relativenumber true

# 显示图标（需要 Nerd Fonts）
set icons

# 显示隐藏文件
set hidden true

# 目录优先显示，点文件最后显示
set dirfirst true

# 面板宽度比例
set ratios 1:2:4

# 输入字段分隔符
set ifs "\n"

# 光标预览样式
set cursorpreviewfmt "\033[7;2m"
```

## 二、自定义命令（cmds）

### 删除命令

```bash
cmd delete ${{
    set -f
    printf "$fx\n"
    printf "delete?[y/n]"
    read ans
    [ "$ans" = "y" ] && rm -rf $fx
}}
```

### 移动到回收站

```bash
cmd trash ${{
    mkdir -p "$HOME"/.trash &>/dev/null
    name=$(basename $f)
    echo "$name"
    if [ -e "$HOME"/.trash/"$name" ]; then 
        [ -n "$name" ] && rm -rf "$HOME"/.trash/"$name"
    else
        IFS="$(printf '\n\t')"; mv -- "$fx" "$HOME"/.trash/
    fi
}}
```

### 打开文件（根据 MIME 类型）

```bash
cmd open &{{
    case $(file --mime-type -Lb $f) in
        text/*)
            nvim -p $fx
            ;;
        image/*)
            imv $f > /dev/null 2>&1 &
            ;;
        application/pdf)
            zathura $f > /dev/null 2>&1 &
            ;;
        video/*|audio/*)
            mpv $f > /dev/null 2>&1 &
            ;;
        *)
            xdg-open "$f" > /dev/null 2>&1 &
            ;;
    esac
}}
```

### 解压文件

```bash
cmd extract ${{
    set -f
    case $f in
        *.tar.bz|*.tar.bz2|*.tbz|*.tbz2) tar -xjvf "$f" ;;
        *.tar.gz|*.tgz) tar -xzvf "$f" ;;
        *.tar.xz|*.txz) tar -xJvf "$f" ;;
        *.tar.zst|*.tzst) tar --zstd -xvf "$f" ;;
        *.tar) tar -xvf "$f" ;;
        *.zip) unzip "$f" ;;
        *.rar) unrar x "$f" ;;
        *.7z) 7z x "$f" ;;
        *.gz) gunzip -k "$f" ;;
        *.bz2) bunzip2 -k "$f" ;;
        *.xz) unxz -k "$f" ;;
        *.zst) unzstd -k "$f" ;;
        *.deb) mkdir -p "${f%.deb}" && ar x "$f" --output="${f%.deb}" ;;
        *.rpm) mkdir -p "${f%.rpm}" && rpm2cpio "$f" | cpio -idmv -D "${f%.rpm}" ;;
        *) echo "不支持的文件格式: $f" ;;
    esac
    lf -remote "send $id reload"
}}
```

### 打包命令

| 命令 | 压缩格式 | 说明 |
|------|----------|------|
| `tar` | tar.gz | 打包为 gzip 压缩包 |
| `zip` | zip | 打包为 zip 压缩包 |
| `tarxz` | tar.xz | 打包为 xz 压缩包（高压缩率） |
| `taronly` | tar | 仅打包，不压缩 |
| `sevenzip` | 7z | 打包为 7z 压缩包（最高压缩率） |

```bash
# 示例：打包为 tar.gz
cmd tar ${{
    if [ -n "$fx" ]; then
        current_dir="$PWD"
        rel_files=""
        for file in $fx; do
            rel_file="${file#$current_dir/}"
            [ "$rel_file" = "$file" ] && rel_file=$(basename "$file")
            rel_files="$rel_files $rel_file"
        done
        first_file="${fx%% *}"
        basename=$(basename "$first_file")
        base="${basename%.*}"
        [ "$base" = "$basename" ] && base="$basename"
        [ -z "$base" ] && base="archive"
        cd "$current_dir"
        tar czf "$base.tar.gz" $rel_files
        lf -remote "send $id echo \"已打包: $base.tar.gz\""
    else
        dirname=$(basename "$PWD")
        tar czf "$dirname.tar.gz" -- * 2>/dev/null
        lf -remote "send $id echo \"已打包整个目录: $dirname.tar.gz\""
    fi
}}
```

### 批量重命名

```bash
cmd bulk-rename ${{
    old="$(mktemp)"
    new="$(mktemp)"
    if [ -n "$fx" ]; then
        fs="$(basename -a -- $fx)"
    else
        fs="$(ls)"
    fi
    printf '%s\n' "$fs" > "$old"
    printf '%s\n' "$fs" > "$new"
    $EDITOR "$new"
    [ "$(wc -l < "$new")" -ne "$(wc -l < "$old")" ] && exit
    paste "$old" "$new" | while IFS= read -r names; do
        src="$(printf '%s' "$names" | cut -f1)"
        dst="$(printf '%s' "$names" | cut -f2)"
        if [ "$src" = "$dst" ] || [ -e "$dst" ]; then
            continue
        fi
        mv -- "$src" "$dst"
    done
    rm -- "$old" "$new"
    lf -remote "send $id unselect"
}}
```

### 循环切换文件权限

```bash
cmd permisson ${{
    case $(stat -c "%a" "$f") in
    644) chmod 755 "$f";;
    755) chmod 600 "$f";;
    600) chmod 644 "$f";;
    *)   chmod 644 "$f";;
    esac
    lf -remote "send $id unselect"
    lf -remote "send $id reload"
    lf -remote "send $id select \"$f\""
}}
```

### 复制当前路径到剪贴板

```bash
cmd cp_path ${{
    pwd | wl-copy
}}
```

### 收集目录内容（供 AI 分析）

```bash
cmd collect &{{
    # 生成包含文件结构和内容的报告
    # 自动跳过二进制文件和大于1MB的文件
    # 结果复制到剪贴板，可作为 AI 提示词
}}
```

## 三、快捷键映射（maps）

### 文件操作

| 快捷键 | 命令 | 作用 |
|--------|------|------|
| `<delete>` | `delete` | 删除当前/选中文件（需确认） |
| `D` | `trash` | 移动到回收站 |
| `R` | `bulk-rename` | 批量重命名 |
| `<c-e>` | `extract` | 解压当前文件 |
| `<c-p>` | `permisson` | 循环切换权限 |
| `<c-y>` | `collect` | 收集目录内容到剪贴板 |
| `<c-r>` | `reload` | 刷新 |
| `<c-t>` | `nvim-tabs` | 用 nvim 多标签打开选中文件 |

### 创建文件/目录

| 快捷键 | 命令 | 作用 |
|--------|------|------|
| `a` | `:push %mkdir<space>` | 创建目录 |
| `t` | `:push %touch<space>` | 创建文件 |

### 打开与执行

| 快捷键 | 命令 | 作用 |
|--------|------|------|
| `<enter>` | `open` | 根据 MIME 类型打开文件 |
| `x` | `$$f` | 执行可执行文件（后台） |
| `X` | `!$f` | 执行可执行文件（显示输出） |

### 快速跳转（locate）

| 快捷键 | 目标路径 |
|--------|----------|
| `,c` | `~/.config` |
| `,clf` | `~/.config/lf` |
| `,cnv` | `~/.config/nvim` |
| `,cnr` | `~/.config/niri` |
| `,ckt` | `~/.config/kitty` |
| `,cfc` | `~/.config/fcitx5` |
| `,cft` | `~/.config/foot` |
| `,cmk` | `~/.config/mako` |
| `,czt` | `~/.config/zathura` |
| `,cwb` | `~/.config/waybar` |
| `,cqb` | `~/.config/qutebrowser` |
| `,lb` | `~/.local/bin` |
| `,ll` | `~/.local/lib` |
| `,ls` | `~/.local/share` |
| `,lsp` | `~/.local/share/PrismLauncher/instances` |
| `,lsf` | `~/.local/share/fonts` |
| `,lsi` | `~/.local/share/fcitx5` |
| `,wp` | `~/Pictures/Wallpaper` |
| `,ss` | `~/Pictures/Screenshots` |
| `,ms` | `~/Music/` |
| `,dl` | `~/Downloads` |
| `,dc` | `~/Documents` |
| `,dn` | `~/Documents/Notes/notes_rst/source` |
| `,dp` | `~/Documents/PDFs` |
| `,ds` | `~/Documents/schematics` |
| `,,` | `~` |
| `,t` | `~/.trash`（回收站） |

### 其他

| 快捷键 | 命令 | 作用 |
|--------|------|------|
| `.pwd` | `cp_path` | 复制当前路径到剪贴板 |
| `` ` `` | `!true` | 查看上次命令输出 |
| `<c-r>` | `reload` | 刷新 |

## 四、颜色配置（colors）

### 文件类型颜色

```bash
# 文件类型
ln      01;36   # 链接
or      31;01   # 失效链接
di      01;34   # 目录
ex      01;32   # 可执行文件
fi      00      # 普通文件

# 压缩包（红色）
*.tar   01;31
*.zip   01;31
*.gz    01;31
*.xz    01;31

# 图片（紫色）
*.jpg   01;35
*.png   01;35

# 音频（青色）
*.mp3   00;36
*.flac  00;36
```

## 五、图标配置（icons）

需要安装 Nerd Fonts 才能正常显示图标。

```bash
# 文件类型图标
di             # 目录
ex             # 可执行文件
fi             # 普通文件
ln             # 链接

# 常见文件类型图标
*.py           # Python
*.js           # JavaScript
*.json         # JSON
*.md           # Markdown
*.rs           # Rust
*.go           # Go
*.sh           # Shell
*.vim          # Vim
*.conf         # 配置文件
*.zip          # 压缩包
*.pdf          # PDF
```

## 六、内置快捷键（补充）

| 快捷键 | 作用 |
|--------|------|
| `h` / `l` | 左/右移动（退出/进入目录） |
| `j` / `k` | 下/上移动 |
| `gg` / `G` | 跳转到顶部/底部 |
| `Ctrl + d` / `Ctrl + u` | 向下/向上翻半页 |
| `Space` | 标记文件 |
| `v` | 切换可视模式 |
| `y` | 复制文件名 |
| `Y` | 复制路径 |
| `p` | 粘贴（移动） |
| `P` | 粘贴（复制） |
| `c` | 复制文件 |
| `u` | 撤销 |
| `s` | 按排序（多次按切换） |
| `/` | 搜索 |
| `n` / `N` | 下一个/上一个搜索结果 |
| `:` | 进入命令模式 |
| `$` | 进入 shell 命令 |

## 七、常用命令

```bash
# 在 lf 内执行
:cd ~/Documents          # 切换目录
:mkdir dirname           # 创建目录
:delete                  # 删除当前文件
:reload                  # 刷新
:echo "message"          # 显示消息
:shell command           # 执行 shell 命令

# 外部调用
lf -remote "send $id reload"           # 刷新指定实例
lf -remote "send $id cd /path"         # 切换目录
lf -remote "send $id echo 'message'"   # 显示消息
```

## 八、一句话总结

lf 核心：`hjkl` 移动，`<enter>` 打开文件，`a` 创建目录，`t` 创建文件，`D` 移到回收站，`R` 批量重命名，`<c-e>` 解压，`<c-y>` 收集目录内容，`,` 触发快速跳转，`:` 执行命令。配合图标和颜色显示，体验类似 ranger 但更轻量。
