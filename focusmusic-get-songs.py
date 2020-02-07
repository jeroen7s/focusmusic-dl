import json
import os
from urllib.request import urlretrieve

import requests

url = 'https://focusmusic.fm/api/tracks.php'
offset = 0
channel_index = 0
repeat = 0
channels = ["electronic", "downtempo", "classical", "rain"]
while offset != -1:
    params = { 
        "offset": offset,
        "channel": channels[channel_index]
    }
    response = requests.get(url, params=params, timeout=10)
    response_json = json.loads(response.content)
    response.raise_for_status()
    file_url = response_json.get("url").replace("\\","")
    filename = file_url.split("/")[-1]
    channel_filepath = channels[channel_index] + "/" + filename
    filepath = os.getcwd() + "/" + channel_filepath
    print("getting offset {} filename {}".format(offset,filename))
    print(filepath)
    if os.path.isfile(filepath):
        offset +=1
        repeat +=1
        if repeat > 10:
            channel_index +=1
            repeat = 0
            offset = 0
        continue
    try:
        urlretrieve (file_url, filepath)
        repeat = 0
    except Exception:
        print("File not Found")
    offset +=1
