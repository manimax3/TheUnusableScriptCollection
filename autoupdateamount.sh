#!/bin/bash

name=$(find /var/log/ -maxdepth 1 -iname "autoupdate-*.log" | sort -r | head -1)

if [ -e $name ]; then
grep -E "^\( *[0-9]+/[0-9]+" $name | wc -l
else
echo 0
fi
