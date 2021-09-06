from json import dump
import discord # Discord connection api
from discord.ext import tasks, commands
import pickle # Sensetive Data is pickled
import time

from osrs_wiki_api import * #OSRS python wrapper
from dumpCog import *
client = discord.Client()

bot = commands.Bot(command_prefix = '!')

TOKEN = pickle.load(open('.TOKEN', 'rb'))


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    
    # Finds price information of given item
    if msg.startswith('!p '):
        latest_data = latest_prices()
        
        # Get name of item requested
        args = msg.split()[1:]
        name = ''
        for i in range(len(args)):
            name += args[i].lower() +' '
        name = name.strip()

        # Load map indexed by name
        map = json.load(open('item_map_name.json', 'r'))
        
        # Extract price information
        item_id = map[name]['id']
        high_price = latest_data['data'][str(item_id)]['high']
        low_price = latest_data['data'][str(item_id)]['low']

        cur_time = time.time()
        high_time = latest_data['data'][str(item_id)]['highTime']
        high_time = round(cur_time - int(high_time))
        low_time = latest_data['data'][str(item_id)]['lowTime']
        low_time = round(cur_time - int(low_time))
        
        # Make and send response
        # response = "Current Price: {}\n".format()
        response = "High Price: {}\nHigh Time: {}\nLow Price: {}\nLow Time: {}\n".format(high_price, high_time, low_price, low_time)
        await message.channel.send(response)


def setup(bot, client):
    bot.add_cog(DumpCog(bot=client))
    client.run(TOKEN)


setup(bot, client)
