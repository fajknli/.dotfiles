# pacman
alias xz='sudo pacman -S --color always'
alias cz='sudo pacman -Ss --color always'
alias czaz='pacman -Q --color always | grep'
alias sc='sudo pacman -Rns --color always'
alias sckb='sudo pacman -R $(pacman -Qdtq)'
alias gxqb='sudo pacman -Syu --color always'
alias gxsy='sudo pacman -Syyu --color always'

# AUR 仓库
# alias yxz='yay -S'
# alias ycz='yay -Ss'
# alias ysc='yay -R'
# alias yschc='yay -Sc'
# alias yckb='yay -Ps'
alias arxz='paru -S'
alias arcz='paru -Ss'
alias arsc='paru -Rns'
alias arschc='paru -Sc'
alias arckb='paru -Ps'


# 工具 & 脚本
alias vim='nvim'
#alias bj='vim $(fzf)'
alias ls='ls --color=auto'
alias ll='ls --color=auto -AXhl'
# 查看各子目录大小
alias dh='du -sh * | sort -h'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias -- -="cd -"
alias dl="cd ~/Downloads"
alias cfg="cd ~/.config"
alias cmc="cd ~/.local/share/PrismLauncher/"
alias mkcd='mkdir $1 && cd $1'
# 删除换行符号，转化为单行
# alias c="tr -d '\n' | wl-copy"
alias ckalias='vim ~/.bash_aliases'

# 设置时间 废弃于2025625920
#alias szsj='$HOME/scripts/scripts_setup/ntp_time.sh'

# 播放音乐 废弃于2025625920
# alias pm='bash $HOME/scripts/scripts_tools/fzfpm.sh'
# alias cm='bash $HOME/scripts/scripts_tools/music-name-shift.sh'

# 写文档 废弃于2025625920
#alias bjwd='bash $HOME/scripts/scripts_notes/edit_rst_file.sh'
#alias gxwd='bash $HOME/scripts/scripts_notes/gxwd.sh'
#alias gjwd='bash $HOME/scripts/scripts_notes/gjwd.sh'
alias bjwd='bash $HOME/.local/bin/note_edit-rst-file'

# proxy 废弃于2025625920
#alias vA='bash $HOME/scripts/scripts_proxy_dae/daeConfigSetup.sh'
#alias novA='bash $HOME/scripts/scripts_proxy_dae/stopDaeProxy.sh'
alias vAstatus='systemctl status dae'

# 系统管理
#alias s='sudo -E -u $USER'
alias sudo='sudo -E'
alias sdn='sudo shutdown -h now'
alias rbt='sudo reboot'

# dotfiles
# github
alias dotfiles='/usr/bin/git --git-dir="$HOME/.dotfiles/" --work-tree="$HOME"'
#alias dottree='dotfiles ls-files | sed "s|^|$HOME/|" | tree -a -F --fromfile'
#alias dotauto='dotfiles add -u && dotfiles_github commit -m "added files or modify files" && dotfiles_github push'
# gitea
# alias dotfiles_gitea='/usr/bin/git --git-dir="$HOME/.dotfiles_gitea/" --work-tree="$HOME"'
# alias dottree_gitea='dotfiles_gitea ls-files | sed "s|^|$HOME/|" | tree -a -F --fromfile'
# alias dotauto_gitea='dotfiles_gitea add -u && dotfiles_gitea commit -m "added files or modify files" && dotfiles_gitea push'

# rsync
alias rsyncfast='rsync -avz --info=progress2'


# file quick leap 废弃于2025625920
#alias vimbootstrap='vim scripts/scripts_setup/bootstrap.sh'
#alias bootstrap='./scripts/scripts_setup/bootstrap.sh'

# File Manager 废弃于2025625920
#alias ffm='./scripts/scripts_tools/fm.sh'
