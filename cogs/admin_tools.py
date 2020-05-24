from discord.ext import commands


class AdminTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["logoff", "logout"])
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Fährt den Bot herunter"""
        print(f"{self.bot.user} is shutting down")
        await self.bot.logout()

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount=0):
        """Löscht die angegebene Anzahl an Nachrichten"""
        await ctx.channel.purge(limit=amount + 1)

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
