from discord.ext import commands
import discord


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
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bannt einen User"""
        await member.ban(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member: discord.Member, *, reason=None):
        """Entfernt einen Ban von einem User"""
        await member.unban(reason=reason)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kickt einen User"""
        await member.kick(reason=reason)

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
