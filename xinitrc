#!/bin/sh


killall Discord &

setxkbmap -option caps:escape &

xset s noblank &
xset -dpms &
xset s off &

# Display configuration
xrandr --output DP-1 --primary --mode 1920x1080 --rate 144 --left-of DP-2
xrandr --output DP-2 --mode 1920x1080 --rate 144 --right-of DP-1
# Status Bar
dwmblocks &

# Compositor
#picom --experimental-backends &

# Wallpaper
nitrogen --restore &


killall brave &

udiskie &

while true; do
      dwm >/dev/null 2>&1
done

exec dwm
