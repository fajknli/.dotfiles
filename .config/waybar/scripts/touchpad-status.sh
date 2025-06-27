#!/bin/sh
if swaymsg -t get_inputs | grep -A 3 'touchpad' | grep -q '"send_events": "disabled"'; then
    echo '{"text":"󱠲 OFF","class":"disabled"}'
else
    echo '{"text":"󱠬  ON","class":"enabled"}'
fi
