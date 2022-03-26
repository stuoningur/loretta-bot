import datetime

import aiosqlite
import disnake
from disnake.ext import commands

DB = "userspecs.sqlite3"


class AdminTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["logoff", "logout"])
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Fährt den Bot herunter"""
        print(f"{self.bot.user} is shutting down")
        await self.bot.close()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        async with aiosqlite.connect(DB) as db:
            user = ctx.message.author.id
            channel = ctx.message.channel.id
            today = datetime.datetime.now()
            time = today.strftime("%d.%m.%Y %H:%M:%S")

            insert_purge = (user, time, amount, channel)
            await db.execute(
                """INSERT INTO purge_log VALUES (?,?,?,?)""",
                insert_purge,
            )
            await db.commit()

        """Löscht die angegebene Anzahl an Nachrichten"""
        await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purgelog(self, ctx, amount=10):
        async with aiosqlite.connect(DB) as db:
            async with db.execute("""SELECT * FROM purge_log""") as cursor:
                result = await cursor.fetchall()

                embed = disnake.Embed(
                    title="Purgelog:",
                    colour=0xE74C3C,
                )

                for i in result[-amount:]:
                    if ctx.guild.get_member(i[0]) is not None:
                        user = ctx.guild.get_member(i[0]).display_name
                    else:
                        user = "Unbekannt"
                    time = i[1]
                    messages = i[2]
                    channel_name = ctx.guild.get_channel(i[3])
                    embed.add_field(
                        name=f"{time}",
                        value=f"{user} hat {messages} Nachrichten im Kanal {channel_name} gelöscht",
                        inline=False,
                    )

                    embed.set_footer(
                        text=f"Angefordert von {ctx.message.author.display_name}",
                        icon_url=ctx.message.author.avatar.url,
                    )
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def nonpics(self, ctx, amount=0):
        """Löscht die angegebene Anzahl an Nachrichten wenn sie keine Bilder enthalten"""

        def has_attachement(m):
            if not len(m.attachments) > 0:
                return True

        await ctx.channel.purge(limit=amount + 1, check=has_attachement, bulk=False)

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension=None):
        """Laden einer neuen Erweiterung"""
        self.bot.load_extension(extension)

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension=None):
        """Entladen einer Erweiterung"""
        self.bot.unload_extension(extension)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, extension=None):
        """Neuladen einer Erweiterung"""
        self.bot.reload_extension(extension)


def setup(bot):
    bot.add_cog(AdminTools(bot))
