import os
HOME = os.environ["HOME"]
CURSOR_PATH = os.path.join(HOME, ".qutebrowser", "cursor.swift")

unbind = [
        "<Ctrl-s>",
        "<Ctrl-w>",
        "<Ctrl-h>",
        "<Alt-w>",
        "d",
        "H",
        "J",
        "K",
        "L",
        ]


# Reload config
config.bind("<Ctrl-Alt-r>", "config-source")
# Keybindings
config.bind("t", "cmd-set-text -s :open -t")
config.bind("O", "cmd-set-text -s :open -w")
config.bind("P", "cmd-set-text -s :open -p")
config.bind("W", "tab-clone -w")
config.bind("a", "mode-enter insert")
config.bind("<F12>", "devtools")


# Move around on the site
config.bind("b", "scroll-to-perc 0")
config.bind("e", "scroll-to-perc")
config.bind("<Ctrl-n>", "scroll down")
config.bind("<Ctrl-p>", "scroll up")
config.bind("<Ctrl-l>", "scroll right")
config.bind("<Ctrl-h>", "scroll left")
config.bind("<Ctrl-v>", "scroll-page 0 0.5")
config.bind("<Alt-v>",  "scroll-page 0 -0.5")
config.bind("<Ctrl-Shift-v>",  "scroll-page 0 -0.5")
config.bind("<Alt-n>", "navigate next")
config.bind("<Shift-Alt-n>", "navigate next -t")
config.bind("<Alt-p>", "navigate prev")
config.bind("<Shift-Alt-p>", "navigate prev -t")
config.bind("^", "navigate up")
config.bind("<Alt-Shift-^>", "navigate up -t")
config.bind("<Alt-f>", "navigate increment")
config.bind("<Alt-b>", "navigate decrement")
# Tabs
config.bind("<Alt-q>", "back")
config.bind("<Alt-e>", "forward")
config.bind("<Alt-w>", "tab-close")
config.bind("<Alt-t>b", "set-cmd-text -s :buffer")
config.bind("<Ctrl-x>1", "tab-only")
config.bind("<Ctrl-p>", "tab-prev")
config.bind("<Ctrl-P>", "tab-move -")
config.bind("<Ctrl-n>", "tab-next")
config.bind("<Ctrl-N>", "tab-move +")
config.bind("<Ctrl-x>ta", "tab-focus 1")
config.bind("<Ctrl-x>te", "tab-focus last")
config.bind("<Ctrl-x>tp", "tab-pin")
config.bind("<Alt-j>", "tab-next")
config.bind("<Alt-k>", "tab-prev")
config.bind("<Ctrl-x>t1", "tab-only")
config.bind("<Ctrl-x>tM", "tab-move -")
config.bind("<Ctrl-x>tm", "tab-move +")
config.bind("<Ctrl-x>tG", "set-cmd-text -s :tab-give")
config.bind("<Alt-y>", "tab-clone")
config.bind("<Alt-Space>", "set-cmd-text -s :tab-select")
config.bind("<Ctrl-x>tt", "tab-focus")
config.bind("<Ctrl-PgDown>", "tab-next")
config.bind("<Ctrl-PgUp>", "tab-prev")
config.bind("<Ctrl-/>", "undo")
config.bind("<Alt-1>", "tab-focus 1")
config.bind("<Alt-2>", "tab-focus 2")
config.bind("<Alt-3>", "tab-focus 3")
config.bind("<Alt-4>", "tab-focus 4")
config.bind("<Alt-5>", "tab-focus 5")
config.bind("<Alt-6>", "tab-focus 6")
config.bind("<Alt-7>", "tab-focus 7")
config.bind("<Alt-8>", "tab-focus 8")
config.bind("<Alt-9>", "tab-focus -1")
config.bind("<Ctrl-Alt-p>", "print")
config.bind("<Ctrl-x>r<Space>", "mode-enter set_mark")
config.bind("<Ctrl-x>rj", "mode-enter jump_mark")
# mpv
config.bind('<Ctrl-Alt-v>', 'hint links spawn --detach mpv {hint-url}')
# Zooming
config.bind("Ctrl-+", "zoom-in")
config.bind("Ctrl--", "zoom-out")
config.bind("=", "zoom")
# Copying/Yanking
config.bind("yD", "yank domain -s")
config.bind("yM", "yank inline [{title}]({url}) -s")
config.bind("yO", "yank inline [[{url}][{title}]] -s")
config.bind("yP", "yank pretty-url -s")
config.bind("yT", "yank title -s")
config.bind("yY", "yank -s")
config.bind("yd", "yank domain")
config.bind("ym", "yank inline [{title}]({url})")
config.bind("yo", "yank inline [[{url}][{title}]]")
config.bind("yp", "yank pretty-url")
config.bind("yt", "yank title")
config.bind("yy", "yank")
# Macros
config.bind("<F3>", "macro-record")
config.bind("<F4>", "macro-run")
config.bind("<Ctrl-x>(", "macro-record")
config.bind("<Ctrl-x>)", "macro-record")
config.bind("<Ctrl-x>e", "macro-run")
# Downloads
config.bind("<Ctrl-d>c", "download-cancel")
# hint
config.bind("f", "hint")
config.bind("<Alt-Space>", "hint all tab")
config.bind(";I", "hint images tab")
config.bind(";O", "hint links fill :open -t -r {hint-url}")
config.bind(";R", "hint --rapid links window")
config.bind(";W", "hint links yank-primary")
config.bind(";b", "hint all tab-bg")
config.bind(";d", "hint links download")
config.bind(";f", "hint all tab-fg")
config.bind(";h", "hint all hover")
config.bind(";i", "hint images")
config.bind(";o", "hint links fill :open {hint-url}")
config.bind(";r", "hint --rapid links tab-bg")
config.bind(";t", "hint inputs")
config.bind(";w", "hint links yank")
# passthrough
config.bind("<Shift-Escape>", "mode-enter passthrough")
# Quit qutebrowser
config.bind("<Ctrl-q>", "quit --save")
config.bind("<Ctrl-Alt-q>", "quit")

really_quick_marks = {
        "bj": "file:///home/fajknli/notes/notes_rst/build/html/index.html",
        "gh": "https://github.com",
        "fs": "https://www.feishu.cn",
        "bl": "https://www.bilibili.com",
        "ds": "https://chat.deepseek.com",
        "md": "https://modrinth.com",
        "wyy": "https://music.163.com",
        "mc": "https://minecraft.net",
        "lp": "https://lesspass.com",
        "ys": "https://www.colorhexa.com",
        "y": "https://mirrors.ustc.edu.cn",
        "mw": "https://zh.minecraft.wiki",
        "aw": "https://wiki.archlinux.org",
        "lw": "https://linux-wiki.cn",
        "w3": "https://www.w3school.com.cn/index.html",
        "md": "https://www.markdownguide.org/basic-syntax/#overview",
        "home": "https://qutebrowser.org"
        }

c.url.searchengines = {
        "DEFAULT": "https://www.bing.com/?q={}",
        "aw": "https://wiki.archlinux.org/?search={}",
        "ab": "https://bugs.archlinux.org/?project=5&string={}",
        "ap": "https://www.archlinux.org/packages/?sort=&q={}",
        "gh": "https://github.com/search?q={}",
        "dd": "https://duckduckgo.com/?q={}",
        "gg": "https://google.com/search?q={}",
        "gho": "https://github.com/{}",
        "mp": "https://google.com/maps?q={}",
        "so": "https://stackoverflow.com/search?q={}",
        "wk": "https://en.wikipedia.org/wiki/{}",
        "yt": "https://youtube.com/results?search_query={}",
        "bl": "https://search.bilibili.com/all?keywords={}",
        "mcsk": "https://minecraftskins.com/search/skin/{}",
        "mcwiki": "https://zh.minecraft.wifi/w/?:search={}"
        }
c.url.start_pages = [ "https://duckduckgo.com" ]



for suffix, url in really_quick_marks.items():
    config.bind(f"<Space>{suffix}", f"open -t {url}")
    config.bind(f",{suffix}", f"open {url}")
