import datetime

from disnake.ext import commands


class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Sendet einen Ping und zeigt die Latenz an"""
        await ctx.send(f"Pong! Die Latenz beträgt {round(self.bot.latency * 1000)}ms")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def passthrough(self, ctx, channel_id, arg):
        channel = self.bot.get_channel(int(channel_id))
        await channel.send(arg)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        today = datetime.datetime.now()
        time = today.strftime("%d.%m.%Y %H:%M")
        channel = self.bot.get_channel(self.bot.log_channel)
        await channel.send(
            f"Der User {member.display_name} hat den Server am {time} verlassen. Die User ID ist {str(member.id)}"
        )


def setup(bot):
    bot.add_cog(Utilities(bot))
