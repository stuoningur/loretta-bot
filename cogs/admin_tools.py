from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Sendet einen Ping und zeigt die Latenz an"""
        await ctx.send(f"Pong! Die Latenz beträgt {round(self.bot.latency * 1000)}ms")


class shutdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Fährt den Bot herunter"""
        print(f"{self.bot.user} is shutting down")
        await self.bot.logout()


def setup(bot):
    bot.add_cog(ping(bot))
    bot.add_cog(shutdown(bot))
