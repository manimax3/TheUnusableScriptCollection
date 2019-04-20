#!/usr/bin/env python3
import re
import sys
import os

i = os.popen("tumbleweed status")
p = re.compile("\D*(\d+)")
output = list()
for line in i:
    line = line.rstrip()
    # print(line)
    output.append(p.match(line).group(1))

if output[0] == output[1]:
    # print("Matched")
    # os.system('$HOME/.bin/nnotify-log.sh No New Tumbleweed Snapshot available')
    pass
else:
    os.system('$HOME/.bin/nnotify-log.sh Tumbleweed Snapshot available')
