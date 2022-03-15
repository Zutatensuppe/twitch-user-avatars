import requests
import re


names = [
    # put in the names here :)
]

for name in names:
    res = requests.get(f"https://twitch.tv/{name}")
    p = re.compile('<meta property="og:image" content="([^"]+)"/>')
    r = p.search(res.text)
    img_blob = requests.get(r[1], timeout=5).content
    with open(f"{name}.jpeg", 'wb') as img_file:
        img_file.write(img_blob)

