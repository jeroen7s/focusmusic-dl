import json
import os
import requests
from pathlib import Path
from urllib.request import urlretrieve
from multiprocessing import Pool

def download_channel(channel, offset=0, firsturl=False):
    Path(os.getcwd() + "/" + channel).mkdir(parents=True, exist_ok=True)
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

Pool().map(download_channel, ["electronic", "downtempo", "classical", "rain"])
