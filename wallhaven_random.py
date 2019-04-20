#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys
from pathlib import Path

wallpaperids = list()

url = "https://alpha.wallhaven.cc/search?q=&categories=100&purity=100&ratios=16x10&sorting=random&order=desc"
r = requests.get(url)
soup = BeautifulSoup(r.content, features="html5lib")
l = soup.body.main.div.ul
for li in l.find_all("li"):
    wid = li.figure.get("data-wallpaper-id")
    if wid is not None:
        wallpaperids.append(wid)

savepath = Path(sys.argv[1])
limit = 1000

if len(sys.argv) > 2:
    limit = int(sys.argv[2])

for i, wid in enumerate(wallpaperids):
    if(i >= limit):
        break

    url = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.jpg".format(wid)
    urlpng = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.png".format(wid)
    local_filename = url.split('/')[-1]
    final_path = savepath / local_filename
    print("Downloading fileid : " + str(final_path))
    with requests.get(url, stream=True) as rd:
        if rd:
            with open(local_filename, "wb") as f:
                for chunk in rd.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                continue
        else:
            print("Jpg failed trying png version")

    local_filename = urlpng.split('/')[-1]
    final_path = savepath / local_filename
    print("Downloading fileid : " + str(final_path))
    with requests.get(urlpng, stream=True) as rd:
        if not rd:
            print("Png version failed continuing")
            continue
        with open(local_filename, "wb") as f:
            for chunk in rd.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
