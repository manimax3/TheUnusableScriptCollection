#!/usr/bin/env python3
import sys
import os
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from pathlib import Path
import subprocess
from itertools import tee, islice

def htmltogfm(hinput):
    result = subprocess.run(['pandoc', '-f', 'html', '-t', 'gfm'], input=hinput, capture_output=True, check=True, text=True)
    return result.stdout


def fileexists(p):
    f = Path(p)
    return f.is_file()


root = ET.fromstring(sys.stdin.read())
items = list(root.findall('./channel/item'))

titles = map(lambda x: x.find('./title').text, items)
descriptions = map(lambda x: x.find('./description').text, items)
enclosure = map(lambda x: x.find('./enclosure'), items)
fileurls, filenames = tee(map(lambda x: x.get('url'), enclosure))
filenames = map(lambda x: os.path.basename(urlparse(x).path), filenames)
mddescriptions = map(htmltogfm, descriptions)

final = filter(lambda x: not fileexists(x[3]), zip(titles, mddescriptions, fileurls, filenames))

if len(sys.argv) > 1:
    count = int(sys.argv[1])
    final = islice(final, count)

for t, d, u, n in final:
    print(t, u, n)
    try:
        subprocess.run(['curl', '-L', u, '-o', n], check=True)
    except subprocess.CalledProcessError:
        if fileexists(n):
            subprocess.run(['rm', n])
        continue
    with open('{} - {}.md'.format(n.split('.')[0], t), 'w') as f:
        f.write(d)
