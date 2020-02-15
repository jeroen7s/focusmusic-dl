import json
import os
import requests
from urllib.request import urlretrieve

url = 'https://focusmusic.fm/api/tracks.php'
for channel in ["electronic", "downtempo", "classical", "rain"]:
    offset, firsturl = 0, False
    while 1:
        url = f'https://focusmusic.fm/api/tracks.php?offset={offset}&channel={channel}'
        response_json = json.loads(requests.get(url, timeout=10).content)
        file_url = response_json.get("url").replace("\\","")
        if file_url == firsturl:
            break
        firsturl = firsturl or file_url
        filename = file_url.split("/")[-1]
        filepath = os.getcwd() + "/" + channel + "/" + filename
        print("getting offset {} filename {}".format(offset,filename))
        try:
            urlretrieve (file_url, filepath)
        except Exception:
            print("File not Found")
        offset +=1
