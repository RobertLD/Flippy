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

    msg = message.content
    
    if msg.startswith('$hello'):
        await message.channel.send('Hello World!')
    
    if msg.startswith('$kayah'):
        await message.channel.send('Kayah is the best girl ever!')
    
    if msg.startswith('$test'):
        data = latest_prices()
        args = msg.split()
        await message.channel.send(data['data'][args[1]][args[2]])


def setup(bot, client):
    bot.add_cog(DumpCog(bot=client))
    client.run(TOKEN)


setup(bot, client)
