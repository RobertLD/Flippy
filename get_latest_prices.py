import json
from osrs_wiki_api import *

data = latest_prices()

with open('latest_prices.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)