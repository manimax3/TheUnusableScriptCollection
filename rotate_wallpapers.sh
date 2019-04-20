#!/bin/bash
pushd /home/manimax3/Bilder/Wallpapers/

if [ $(ls | wc -l) -gt 5 ]; then
    for file in "$(ls -t | tail -5)"; do
        rm $file
    done
fi

/home/manimax3/.bin/wallhaven_random.py . 5 2>&1 > /dev/null
