import discord
from discord.ext import commands
from osrs_wiki_api import * #OSRS python wrapper

client = commands.Bot(command_prefix = '.')
TOKEN = 'ODgwOTExMjQxMzQ5MDM4MTQw.YSlKhg.4gkIWIqoh-3YHx0s67Dohu_7Wz4'
@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_ready():
    print("Bot is ready.")

client.run(TOKEN)
