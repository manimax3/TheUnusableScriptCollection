#!/bin/zsh
# zsh and kde only
export KDE_FULL_SESSION=true
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep startkde -n)/environ | cut -d= -f2-)
/home/manimax3/.bin/setwallpaper /home/manimax3/Bilder/Wallpapers/$(ls ~/Bilder/Wallpapers/ | shuf -n 1 -) 1
