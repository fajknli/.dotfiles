import colorschemes

config.source("keymaps.py")
config.load_autoconfig(False)

# Colorscheme 配色
colorschemes.fajknli(c, 'fajknli', True)
c.colors.webpage.darkmode.enabled = True

# 缩放
c.zoom.default = "150%"

# Editor
#c.editor.command = ['nvim', '-n', '{file}', '-w']
# Session
# 启动时恢复上次会话
c.auto_save.session = True # 自动保存会话
c.auto_save.interval = 15000  # 15秒自动保存一次
c.session.default_name = 'default' # 启动时恢复上次会话
c.session.lazy_restore = True  # 延迟加载标签页以提高启动速度

# TAB
c.tabs.favicons.scale = 2.0
c.tabs.background = True
c.tabs.position = "left"
c.completion.shrink = True
c.tabs.favicons.scale = 1.0
c.tabs.width = 120
c.tabs.mousewheel_switching = False

# Cookies
c.auto_save.interval = 20000
c.content.cookies.accept = 'all'  # 接受所有 cookies
c.content.cookies.store = True    # 存储 cookies
c.content.local_storage = True # 启用本地存储

# Download
c.downloads.location.directory = "~/Downloads"
c.content.private_browsing = True
c.downloads.remove_finished = 1

#bar
c.scrolling.smooth = False

# User agent
c.content.headers.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Clipboard
c.content.javascript.clipboard = "access-paste"

#hits
c.hints.border = "none"
c.hints.chars = "asdghjkl"

# Font
c.fonts.completion.entry = "12px Open sans"
c.fonts.completion.category = "12px Open sans"
c.fonts.debug_console = "12px Open sans"
c.fonts.downloads = "12px Open sans"
c.fonts.hints = "12px Open sans"
c.fonts.keyhint = "12px Open sans"
c.fonts.messages.info = "12px Open sans"
c.fonts.messages.error = "12px Open sans"
c.fonts.prompts = "12px Open sans"
c.fonts.statusbar = "15px Open sans"
c.fonts.tabs.selected = "18px Open sans"
c.fonts.tabs.unselected = "18px Open sans"

# Other
# c.confirm_quit = ["false"]
# c.content.headers.accept_language = "zh-CN;q=0.9,en-US,en;q=0.8"







