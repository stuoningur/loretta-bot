from discord.ext import commands


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Sendet einen Ping und zeigt die Latenz an"""
        await ctx.send(f"Pong! Die Latenz beträgt {round(self.bot.latency * 1000)}ms")

    @commands.command()
    @commands.is_owner()
    async def passthrough(self, ctx, channel_id, arg):
        channel = self.bot.get_channel(int(channel_id))
        await channel.send(arg)


def setup(bot):
    bot.add_cog(Utilities(bot))
