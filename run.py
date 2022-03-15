import requests
import re
import os
from pathlib import Path

names = [
    # put in the names here :)
    "kirinokirino",
    "achan_jp",
    "lisadikaprio",
    "nc_para_",
]
p = re.compile('(<meta property="og:image" content="([^"]+)"\s*/>|<meta content="([^"]+)" property="og:image"\s*/>)')

for name in names:
    print(f"image for {name}")
    res = requests.get(f"https://twitch.tv/{name}")
    r = p.search(res.text)
    if not r:
        print(res.text)
        continue
    url = r[2] or r[3]
    pat = Path(url)
    img_blob = requests.get(url, timeout=5).content
    with open(f"{name}{pat.suffix}", 'wb') as img_file:
        img_file.write(img_blob)

