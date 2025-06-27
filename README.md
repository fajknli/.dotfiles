# Dotfiles Usage

1. clone the repo

```bash

git clone --bare git@github.com:yourusername/dotfiles.git $HOME/.dotfiles

```

2. adds alias

```bash

alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

```

3. checkout file in work directory

```bash

dotfiles checkout -f

```

4. hides no tracked files (work directory have too many files)

```bash

dotfiles config --local status.showUntrackedFiles no

```

## Notices

1. automatically track any new files which created after been tracked directory

Check the file `.dotfile/hooks/pre-commit`

More alias at .bash_alias

Hello
