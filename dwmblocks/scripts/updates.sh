#!/bin/bash
case $BLOCK_BUTTON in 
	1) alacritty -e sudo pacman -Syu --noconfirm ;;
esac

cupd=$(checkupdates | wc -l)
echo "Updates:$cupd"

