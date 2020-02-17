import requests
import json
from os import getcwd, listdir, chdir, system
import re
# Inputting Parameters to Get Pandascore Data
url = input("Type in the Pandascore API endpoint you want to query: ")
api_token = input("Input your API token: ")
slash_indices = [(m.start(0), m.end(0)) for m in re.finditer("/", url)]
folder_name = url[slash_indices[2][1]:slash_indices[2][1]+1] + url[slash_indices[2][1]+1:slash_indices[3][0]] + "_" + url[slash_indices[3][1]:]
print(folder_name)
# Creating a Folder Within Data to Store All JSON Files of Similar Search
data_path = getcwd() + "/data"

if folder_name not in listdir(data_path):
    chdir("data")
    system(f"mkdir {folder_name}")
    chdir("..")

# Getting Path to New Folder
json_path = data_path + f"/{folder_name}"


# Creating a Dictionary to Store Responses from Pandascore API
page_dict = {}
num_pages = int(input("How many pages do you want to query: "))
for i in range(num_pages):
    parameters = {'token':api_token, 'page':i+1, 'per_page':100}

    get_response = requests.get(url=url, params=parameters)

    page_dict[f'response_{i+1}'] = get_response.json()

print(f"You have {1000 - num_pages} API calls remaining.")

# Creating JSON Files for Each Page You Query Inside the Folder
for i in range(num_pages):
    system(f"touch {json_path}/{folder_name}_{i+1}.json")


# Getting a List of JSON Files
league_files = listdir(json_path)

# Getting a List of all JSON Responses from Above Dictionary
page_values = list(page_dict.values())

# Storing Each JSON Response to the Proper JSON File
for i, file in enumerate(league_files):
    opened_file = open(f"{json_path}/{file}", "w")
    parsed = json.dumps(page_values[i], indent=4, sort_keys=True)
    opened_file.write(parsed)
