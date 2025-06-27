#! /usr/bin/env bash
# Author:        a6dg2uv
# Created Time:  2025-04-20 07:23

chosen=$(printf " Lock\n Suspend\n Reboot\n Poweroff" | \
  fuzzel --dmenu --no-icons --prompt="Power: " --lines=4 --width=30)

case "$chosen" in
  " Lock") swaylock \
  --clock \
  --indicator \
  --indicator-radius 100 \
  --indicator-thickness 10 \
  --effect-blur 7x5 \
  --effect-vignette 0.5:0.5 \
  --fade-in 0.3 \
  --grace 2 \
  --screenshots \
  --ring-color 607bc3 \
  --ring-clear-color b280be \
  --ring-ver-color a0d0a0 \
  --ring-wrong-color F08080 \
  --inside-color 151622 \
  --inside-clear-color 151622 \
  --inside-ver-color 151622 \
  --inside-wrong-color 151622 \
  --key-hl-color dbd07f \
  --bs-hl-color F08080 \
  --line-color 00000000 \
  --line-clear-color 00000000 \
  --line-ver-color 00000000 \
  --line-wrong-color 00000000 \
  --separator-color 00000000 \
  --text-color a9b5d5 \
  --text-clear-color a9b5d5 \
  --text-ver-color a9b5d5 \
  --text-wrong-color a9b5d5 \
  --text-caps-lock-color dbd07f \
  --indicator-caps-lock \
  --font 'Noto Sans Bold' \
  --font-size 48 ;;
  " Suspend") systemctl suspend ;;
  " Reboot") systemctl reboot ;;
  " Poweroff") systemctl poweroff ;;
esac

