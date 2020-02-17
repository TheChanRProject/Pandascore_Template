import numpy as np
import pandas as pd
import json
from os import getcwd, listdir
import matplotlib.pyplot as plt
import seaborn as sns

# Overwatch Players
data_path = getcwd() + "/data/ow_players"

ow_player_dict = {f"response_{i+1}": pd.read_json(f"{data_path}/{j_file}") for i, j_file in enumerate(listdir(data_path)[:10])}

ow_player_dict['response_1']['role'].value_counts(dropna=False)
ow_player_dict['response_5']['role'].value_counts(dropna=False)
ow_player_dict['response_9']['role'].value_counts(dropna=False)

ow_player_dict['response_1']['current_team'][0]
ow_player_dict['response_9']['current_team'][1]
