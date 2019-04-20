#/bin/bash

FILE=${LOGFILE:-"$HOME/.nnotify-log.txt"}
TM=${NNOTIFY_TIMEOUT:-5}

function run {
    if [ ! -f $FILE ]; then
        touch $FILE
    fi

    while [ ! $(cat $FILE | wc -l) -eq 0 ]; do
        notify-send "$(head -1 $FILE)"
        sed -i "1 d" $FILE
    done
}

while true; do
    run
    sleep $TM
done
