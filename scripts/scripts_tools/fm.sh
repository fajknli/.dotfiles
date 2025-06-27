#!/bin/bash

PWD=$(pwd)

while true; do

    target=$(exa --icons --color=always -1 | fzf --exact \
        --multi \
        --ansi \
        --preview '[ -f {} ] && bat --color=always {} || ls -l {}' \
        --bind 'j:down,k:up' \
        --bind 'l:accept+reload(cd {})' \
        --bind 'h:reload( cd .. && exa --icons --color=always -1 )'
    )
    if [[ -z "$target" ]]; then
        break  # 按 ESC 退出
    elif [[ -f "$target" ]]; then
        nvim "$target"
    elif [[ -d "$target" ]]; then
        cd "$target"
    fi

done
