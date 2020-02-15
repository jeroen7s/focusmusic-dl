import json, requests
from pathlib import Path
from urllib.request import urlretrieve
from multiprocessing import Pool

def download_channel(channel, offset=0, firsturl=False):
    Path(str(Path()) + "/" + channel).mkdir(exist_ok=True)

    while 1:
        url = f'https://focusmusic.fm/api/tracks.php?offset={offset}&channel={channel}'
        file_url = json.loads(requests.get(url, timeout=10).content).get("url").replace("\\","")
        if file_url == firsturl: break
        filepath, firsturl = str(Path()) + "/" + channel + "/" + Path(file_url).name, firsturl or file_url
        if not Path(filepath).exists():
            print(f"getting offset {offset} filename {Path(filepath).name}"); 
            urlretrieve(file_url, filepath)
        offset +=1

Pool().map(download_channel, ["electronic", "downtempo", "classical", "rain"])
