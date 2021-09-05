from discord.ext import tasks, commands


class DumpCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.index = 0

        # Dump Detector start
        self.detectDump.start()

    @tasks.loop(seconds=1)
    async def detectDump(self):
        print("tsk")
        return