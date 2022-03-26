import datetime

from disnake.ext import commands


class ErrorHandling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Es fehlen erforderliche Argumente.")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("Diesen Befehl gibt es nicht.")
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send("Zuviele Argumente angegeben.")
        elif isinstance(error, commands.NotOwner):
            await ctx.send("Nur Lorettas Mitbewohner darf das.")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("Du hast nicht die benötigten Rechte.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("Ich darf das leider nicht.")
        else:
            today = datetime.datetime.now()
            time = today.strftime("%d.%m.%Y %H:%M:%S")
            print(f"{time} - {error}")


def setup(bot):
    bot.add_cog(ErrorHandling(bot))
