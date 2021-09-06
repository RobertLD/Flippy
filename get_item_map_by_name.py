import json
from osrs_wiki_api import *

list = item_map()
data = {}
for val in list:
    data[str(val['name']).lower()] = val

with open('item_map_name.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)