import requests
import json
API_END_POINT = 'http://prices.runescape.wiki/api/v1/osrs'
headers = {
    'User-Agent': 'Flipping Tracker - Flippy bot | By: Eldermah#2060',
    'From': 'didyouhidethebody@gmail.com' 
}
def latest_prices():
    URL = API_END_POINT + '/latest'
    response = requests.get(URL)
    
    # API was not succesfully reached
    if(response.status_code != 200):
        return 
    #return json.dumps(response.json(), sort_keys= True, indent=4)
    return response.json()

def item_map():
    URL = API_END_POINT + '/mapping'
    response = requests.get(URL)
    
    # API was not succesfully reached
    if(response.status_code != 200):
        return 
    return response.json()
    
def prices(minutes = 5):

    if(minutes == 5):
        URL = API_END_POINT + '/5m'
    elif(minutes == 60):    
        URL = API_END_POINT + '/1h'
    else:
        return
    response = requests.get(URL)
    
    # API was not succesfully reached
    if(response.status_code != 200):
        return 
    return response.json()

def item_time_series(id, timestep):

    if(timestep == 5):
        URL = API_END_POINT + '?timestep=5m&id=' + id
    elif(timestep == 60):    
        URL = API_END_POINT + '?timestep=1h&id=' + id
    elif(timestep == 360):    
        URL = API_END_POINT + '?timestep=6hm&id=' + id
    else:
        return
    response = requests.get(URL)
    
    # API was not succesfully reached
    if(response.status_code != 200):
        return 
    return response.json()