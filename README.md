# Dotfiles Usage

1. clone the repo

```bash

git clone --bare https://github.com/fajknli/.dotfiles.git $HOME/.dotfiles


```

2. adds alias in .bashrc or .profile ...

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

6. How to track file? 

you can use `$HOME/.local/bin/dots` check it , add file or directories in it, then run the script

## Notices

1. automatically track any new files which created after been tracked directory

Check the file `.dotfile/hooks/pre-commit`

More alias at `.bash_alias`

