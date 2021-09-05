from discord.ext import tasks, commands
from osrs_wiki_api import * #OSRS python wrapper

class DumpCog(commands.Cog):
    itemData = None

    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        # Initialize item price data
        itemData = latest_prices()
        # Dump Detector start
        self.detectDump.start()

    @tasks.loop(seconds=30)
    async def detectDump(self):
        # pull from the latest prices api
        # cross reference the item id, price information with the last pulled version
        # cross reference the item id from latest prices, with the item map
        # format message
        latestPrices = latest_prices()

        for key, value in self.itemData['data'].items():
            for lock, pick in value.items():
                if(not(latestPrices['data'][key] == value)):

                    if(latestPrices['data'][key]['low'] < self.itemData['data'][key]['low']):
                        print("Item %s has dropped by %d" % (key, self.itemData['data'][key]['low'] - latestPrices['data'][key]['low']))
                    self.itemData['data'][key].update(latestPrices['data'][key]) 
                    print("Updated item # %s" % (key))
        return