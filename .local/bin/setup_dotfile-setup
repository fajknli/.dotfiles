#!/bin/sh

#2025-06-24-05:37

#dotfile_setup

CONFIG="$HOME/.config";

cd $HOME || exit;

mkdir -p $HOME/dotfile;
echo 'created dotfile dir';

# .confile/dirs
[ ! -d $HOME/dotfile/.config ] && mkdir -p $HOME/dotfile/.config;
[ -d $CONFIG/fcitx ] && cp -r $CONFIG/fcitx $HOME/dotfile/.config;
[ -d $CONFIG/fcitx5 ] && cp -r $CONFIG/fcitx5 $HOME/dotfile/.config;
[ -d $CONFIG/foot ] && cp -r $CONFIG/foot $HOME/dotfile/.config;
[ -d $CONFIG/fuzzel ] && cp -r $CONFIG/fuzzel $HOME/dotfile/.config;
[ -d $CONFIG/gtk-3.0 ] && cp -r $CONFIG/gtk-3.0 $HOME/dotfile/.config;
[ -d $CONFIG/hypr ] && cp -r $CONFIG/hypr $HOME/dotfile/.config;
[ -d $CONFIG/kitty ] && cp -r $CONFIG/kitty $HOME/dotfile/.config;
[ -d $CONFIG/lf ] && cp -r $CONFIG/lf $HOME/dotfile/.config;
[ -d $CONFIG/mako ] && cp -r $CONFIG/mako $HOME/dotfile/.config;
[ -d $CONFIG/mc ] && cp -r $CONFIG/mc $HOME/dotfile/.config;
[ -d $CONFIG/niri ] && cp -r $CONFIG/niri $HOME/dotfile/.config;
[ -d $CONFIG/nvim ] && cp -r $CONFIG/nvim $HOME/dotfile/.config;
[ -d $CONFIG/qutebrowser ] && cp -r $CONFIG/qutebrowser $HOME/dotfile/.config;
[ -d $CONFIG/sway ] && cp -r $CONFIG/sway $HOME/dotfile/.config;
[ -d $CONFIG/waybar ] && cp -r $CONFIG/waybar $HOME/dotfile/.config;
[ -d $CONFIG/zellij ] && cp -r $CONFIG/zellij $HOME/dotfile/.config;
echo '.dotfile/dirs copy done';

# $HOME/.files
[ ! -d $HOME/dotfile/.dotfiles ] && mkdir -p $HOME/dotfile/.dotfiles;
[ -f .alacritty.toml ] && cp .alacritty.toml $HOME/dotfile/.dotfiles;
[ -f .curlrc ] && cp .curlrc $HOME/dotfile/.dotfiles;
[ -f .inputrc ] && cp .inputrc $HOME/dotfile/.dotfiles;
[ -f .profile ] && cp .profile $HOME/dotfile/.dotfiles;
[ -f .shinit ] && cp .shinit $HOME/dotfile/.dotfiles;
[ -f .wgetrc ] && cp .wgetrc $HOME/dotfile/.dotfiles;
[ -f .bash_aliases ] && cp .bash_aliases $HOME/dotfile/.dotfiles;
[ -f .bash_exports ] && cp .bash_exports $HOME/dotfile/.dotfiles;
[ -f .bash_functions ] && cp .bash_functions $HOME/dotfile/.dotfiles;
[ -f .bash_profile ] && cp .bash_profile $HOME/dotfile/.dotfiles;
[ -f .bash_prompt ] && cp .bash_prompt $HOME/dotfile/.dotfiles;
[ -f .bashrc ] && cp .bashrc $HOME/dotfile/.dotfiles;
echo '.dotfile/.files copy done';

# $HOME/scripts
[ -d $HOME/scripts ] && cp -r $HOME/scripts $HOME/dotfile;
echo '.dotfile/scripts copy done';

# $HOME/proxy
[ -d $HOME/proxy ] && cp -r $HOME/proxy $HOME/dotfile;
echo '.dotfile/proxy copy done';

# $HOME/notes
[ -d $HOME/notes ] && cp -r $HOME/notes $HOME/dotfile;
echo '.dotfile/notes copy done';
