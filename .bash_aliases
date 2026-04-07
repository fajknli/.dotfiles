# pacman
alias xz='sudo pacman -S --color always'
alias cz='sudo pacman -Ss --color always'
alias czaz='pacman -Q --color always | grep'
alias sc='sudo pacman -Rns --color always'
alias sckb='sudo pacman -R $(pacman -Qdtq)'
alias gxqb='sudo pacman -Syu --color always'
alias gxsy='sudo pacman -Syyu --color always'

# AUR 仓库
alias arxz='paru -S'
alias arcz='paru -Ss'
alias arsc='paru -Rns'
alias arschc='paru -Sc'
alias arckb='paru -Ps'


# 工具 & 脚本
alias ls='ls --color=auto'
alias ll='ls --color=auto -AXhl'
alias dh='du -sh * | sort -h'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias -- -="cd -"
alias dl="cd ~/Downloads"
alias cfg="cd ~/.config"
alias cmc="cd ~/.local/share/PrismLauncher/"
alias mkcd='mkdir $1 && cd $1'
alias ckalias='vim ~/.bash_aliases'

alias vAstatus='systemctl status dae'

# 系统管理
alias sudo='sudo -E'
alias sdn='sudo shutdown -h now'
alias rbt='sudo reboot'

# github
alias dotfiles='/usr/bin/git --git-dir="$HOME/.dotfiles/" --work-tree="$HOME"'

# rsync
alias rsyncfast='rsync -avz --info=progress2'
