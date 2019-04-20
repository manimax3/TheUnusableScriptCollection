#/bin/bash

FILE=${LOGFILE:-"$HOME/.nnotify-log.txt"}
if [ ! -f $FILE ]; then
    touch $FILE
fi

echo $* >> $FILE
