import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="help", aliases=["hilfe", "h"], invoke_without_command=True)
    async def help_base(self, ctx):
        embed = discord.Embed(colour=0xE74C3C,)
        embed.add_field(
            name="**Lorettas Anleitungen:**",
            value="```!bios        !cpu    !limit    !mainboard\n!anleitung   !ram    !spd      !ergebnisse```",
            inline="false",
        )
        embed.add_field(
            name="**Lorettas Witzebuch:**",
            value="```!gif *suchbegriff*       !8ball *frage*    !gh *suchbegriff*\n!google *suchbegriff*    !warum```",
            inline="false",
        )
        embed.add_field(
            name="**Lorettas spezifische Spezifikationen:**",
            value="```!specs set *hardware*         !specs show *servermitglied*\n!specs search *suchbegriff*   !specs delete```",
            inline="false",
        )
        embed.add_field(
            name="**Für weitere Informationen zum specs Befehl:**",
            value="```!help specs```",
            inline="false",
        )
        embed.set_author(name="Lorettas Selbsthilfe Gruppe",)
        await ctx.send(embed=embed)

    @help_base.command(name="specs")
    async def help_specs(self, ctx):
        embed = discord.Embed(colour=0xE74C3C,)
        embed.add_field(
            name="**Spezifikationen festlegen:**",
            value="Um deine Spezifikationen bei Loretta zu registrieren, nutze den `!specs set` Befehl gefolgt von deiner Hardware.\nEs wird [Discords Markdown](https://support.discordapp.com/hc/de/articles/210298617) unterstützt, Zeilenumbrüche sind mit Umschalt+Enter möglich.\n**Beispiel**:\n```!specs set\n**CPU:** AMD Ryzen 11 9999X\n**Mainboard:** ASUS ROG Crosshair VIIII Extreme\n**RAM:** 32GB Crucial Ballistix DDR7 @ 9000 CL6```",
            inline="false",
        )
        embed.add_field(
            name="**Spezifikationen anzeigen:**",
            value="Um deine oder andere Spezifikationen anzuzeigen, nutze den `!specs show` Befehl gefolgt von dem Servermitglied. Wenn du dir deine Spezifikationen anzeigen lassen willst, ist die Angabe eines Servermitglieds nicht notwendig.\n**Beispiel**:\n```!specs show @Loretta```",
            inline="false",
        )
        embed.add_field(
            name="**Spezifikationen suchen:**",
            value="Um die Spezifikationen zu durchsuchen, nutze den `!specs search` Befehl gefolgt von dem Suchbegriff.\n**Beispiel**:\n```!specs search Windows 11```",
            inline="false",
        )
        embed.add_field(
            name="**Spezifikationen löschen:**",
            value="Um deine Spezifikationen zu löschen, nutze den `!specs delete` Befehl.\n**Beispiel**:\n```!specs delete```\n**ACHTUNG:** Die Spezifikationen werden dabei unwiderruflich gelöscht.",
            inline="false",
        )
        embed.set_author(name="Lorettas spezifische Spezifikationen",)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
