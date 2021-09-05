from json import dump
import discord # Discord connection api
from discord.ext import tasks, commands
import pickle # Sensetive Data is pickled

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
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')
    
    if message.content.startswith('$kayah'):
        await message.channel.send('Kayah is the best girl ever!')
    
    if message.content.startswith('$test'):
        data = latest_prices()
        await message.channel.send(data['data']['2']['high'])


def setup(bot, client):
    bot.add_cog(DumpCog(bot=client))
    client.run(TOKEN)


setup(bot, client)
