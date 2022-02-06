#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/Xresources
sysmodmap=/etc/X11/xinit/Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then







    xrdb -merge $sysresources

fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then







    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

if [ -n "`/etc/X11/chooser.sh`" ]; then
 command="`/etc/X11/chooser.sh`"
else
 failsafe="yes"
fi

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?* ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi


killall Discord &

setxkbmap -option caps:escape &

xset s noblank &
xset -dpms &
xset s off &

# Display configuration
xrandr --output DP-2 --primary --mode 1920x1080 --rate 144 --left-of DP-4 &
xrandr --output DP-4  --mode 1920x1080 --rate 144 --right-of DP-2 &


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
