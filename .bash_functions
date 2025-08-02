# fzf 快速进入目录
fzfcd() {
  local dir
  dir=$(
    find . -maxdepth 1 -type d ! -name '.' | \
    sed 's|^./||' | \
    awk '/^\./{print "2."$0; next} {print "1."$0}' | \
    sort | cut -d. -f2 | \
    fzf --height 40% --border --layout=reverse --header-first --preview 'ls -lh {} | awk "{\$2=\"\";\$3=\"\";\$4=\"\";print}"'
  ) && cd "$dir"
}

#mcc() { mc; }

#function y() {
#	local tmp="$(mktemp -t "yazi-cwd.XXXXXX")" cwd
#	yazi "$@" --cwd-file="$tmp"
#	IFS= read -r -d '' cwd < "$tmp"
#	[ -n "$cwd" ] && [ "$cwd" != "$PWD" ] && builtin cd -- "$cwd"
#	rm -f -- "$tmp"
#}
#bind -x '"\C-f":"y"'

# use lfcd to jump dir by use lf -last-dir-path
lfcd() {
    tmp="$(mktemp)"
    lf -last-dir-path="$tmp" "$@"
    if [ -f "$tmp" ]; then
        dir="$(cat "$tmp")"
        rm -f "$tmp"
        if [ -d "$dir" ]; then
            cd "$dir" || return
        fi
    fi
}
