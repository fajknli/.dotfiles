# fzf 快速进入目录
fzfcd() {
  local dir=$(find . -maxdepth 1 -type d ! -name '.' | sed 's|^./||' | fzf)
  [ -n "$dir" ] && cd "$dir"
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
# lfcd () {
#     # `command` is needed in case `lfcd` is aliased to `lf`
#     cd "$(command lf -print-last-dir "$@")"
# }
lf() {
    local tmp
    tmp="$(mktemp)"
    command lf -last-dir-path="$tmp" "$@"
    if [ -f "$tmp" ]; then
        local dir
        dir="$(cat "$tmp")"
        rm -f "$tmp"
        [ -d "$dir" ] && [ "$dir" != "$PWD" ] && cd "$dir"
    fi
}
