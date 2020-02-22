import aiosqlite
import discord
from discord.ext import commands

DB = "userspecs.sqlite3"


class specs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def specs(self, ctx, user=None):
        if user is None:
            user = (str(ctx.message.author.id),)
        elif "@!" in user:
            user = (str(user[3:-1]),)
        else:
            matches = [
                member
                for member in ctx.guild.members
                if user.lower() in member.name.lower()
            ]
            if len(matches) == 0:
                await ctx.send("User nicht gefunden")
            elif len(matches) > 1:
                await ctx.send("Zu viele User")
            else:
                user = (str(matches[0].id),)

        if type(user) is int:
            guild_member = ctx.guild.get_member(int(user[0])).display_name
            async with aiosqlite.connect(DB) as db:
                async with db.execute(
                    """SELECT * FROM user_specs WHERE userid=?""", user
                ) as cursor:
                    result = await cursor.fetchone()
                    embed = discord.Embed(
                        title=f"PC von: {guild_member}",
                        colour=0xE74C3C,
                        description=result[1],
                    )
                    embed.set_footer(
                        text=f"Angefordert von {ctx.message.author.name}",
                        icon_url=ctx.message.author.avatar_url,
                    )
                    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(specs(bot))
