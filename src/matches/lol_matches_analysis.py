import numpy as np
import pandas as pd
import json
from os import getcwd, listdir

json_path = getcwd() + "/data/lol_matches"

json_dict = {f"response_{i+1}": pd.read_json(f"{json_path}/{j_file}") for i, j_file in enumerate(listdir(json_path))}

json_dict['response_20'].columns

vid_urls = []

for i in range(100):
    record = json_dict['response_20']['games'][i]
    for j in range(len(record)):
        vid_urls.append(record[j]['video_url'])

len(vid_urls)
