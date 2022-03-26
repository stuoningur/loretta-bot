import disnake
import gspread_asyncio
from disnake.ext import commands
from oauth2client.service_account import ServiceAccountCredentials


def get_creds():
    return ServiceAccountCredentials.from_json_keyfile_name(
        "creds.json",
        [
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive",
            "https://www.googleapis.com/auth/spreadsheets",
        ],
    )


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(
        name="help", aliases=["hilfe", "h", "befehle"], invoke_without_command=True
    )
    async def help_base(self, ctx):
        embed = disnake.Embed(
            colour=0xE74C3C,
        )
        embed.add_field(
            name="**Lorettas Anleitungen:**",
            value="```!bios        !cpu    !limit    !mainboard\n!anleitung   !ram    !spd      !ergebnisse```",
            inline=False,
        )
        embed.add_field(
            name="**Lorettas Witzebuch:**",
            value="```!gif *suchbegriff*       !8ball *frage*    !gh *suchbegriff*\n!google *suchbegriff*    !warum```",
            inline=False,
        )
        embed.add_field(
            name="**Lorettas Wahlurne:**",
            value="```!vote *Titel* *Option 1* *Option 2* ... (maximal 20 Optionen)\n\nWenn der Titel oder die Optionen Leerzeichen enthalten, müssen die Anführungszeichen gesetzt werden```",
            inline=False,
        )
        embed.add_field(
            name="**Lorettas spezifische Spezifikationen:**",
            value="```!specs set *hardware*         !specs show *servermitglied*\n!specs search *suchbegriff*   !specs delete```",
            inline=False,
        )
        embed.add_field(
            name="**Für weitere Informationen zum specs Befehl:**",
            value="```!help specs```",
            inline=False,
        )
        embed.add_field(
            name="**Alle vorhandenen Timings-Presets und weitere Informationen zum timings Befehl:**",
            value="```!help timings```",
            inline=False,
        )
        embed.set_author(
            name="Lorettas Selbsthilfe Gruppe",
        )
        await ctx.send(embed=embed)

    @help_base.command(name="specs", aliases=["Specs"])
    async def help_specs(self, ctx):
        embed = disnake.Embed(
            colour=0xE74C3C,
        )
        embed.add_field(
            name="**Spezifikationen festlegen:**",
            value="Um deine Spezifikationen bei Loretta zu registrieren, nutze den `!specs set` Befehl gefolgt von deiner Hardware.\nEs wird [disnakes Markdown](https://support.disnakeapp.com/hc/de/articles/210298617) unterstützt, Zeilenumbrüche sind mit Umschalt+Enter möglich.\n**Beispiel**:\n```!specs set\n**CPU:** AMD Ryzen 11 9999X\n**Mainboard:** ASUS ROG Crosshair VIIII Extreme\n**RAM:** 32GB Crucial Ballistix DDR7 @ 9000 CL6```",
            inline=False,
        )
        embed.add_field(
            name="**Spezifikationen anzeigen:**",
            value="Um deine oder andere Spezifikationen anzuzeigen, nutze den `!specs show` Befehl gefolgt von dem Servermitglied. Wenn du dir deine Spezifikationen anzeigen lassen willst, ist die Angabe eines Servermitglieds nicht notwendig.\n**Beispiel**:\n```!specs show @Loretta```",
            inline=False,
        )
        embed.add_field(
            name="**Spezifikationen suchen:**",
            value="Um die Spezifikationen zu durchsuchen, nutze den `!specs search` Befehl gefolgt von dem Suchbegriff.\n**Beispiel**:\n```!specs search Windows 11```",
            inline=False,
        )
        embed.add_field(
            name="**Spezifikationen löschen:**",
            value="Um deine Spezifikationen zu löschen, nutze den `!specs delete` Befehl.\n**Beispiel**:\n```!specs delete```\n**ACHTUNG:** Die Spezifikationen werden dabei unwiderruflich gelöscht.",
            inline=False,
        )
        embed.set_author(
            name="Lorettas spezifische Spezifikationen",
        )
        await ctx.send(embed=embed)

    @help_base.command(name="timings", aliases=["preset", "presets", "Timings", "Preset", "Presets"])
    async def help_timings(self, ctx):
        agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
        agc = await agcm.authorize()
        document = await agc.open("loretta_timings")
        worksheet = await document.get_worksheet(0)
        values_list = await worksheet.col_values(2)
        new_line = "\n"
        embed = disnake.Embed(
            colour=0xE74C3C,
        )
        embed.add_field(
            name="**Timing Presets abrufen:**",
            value="```!timings *hersteller* *ics* *takt* *preset* *cpu generation* *layout (mainboard hersteller)*\n\nZum Beispiel:\n!timings samsung bdie 3733 scharf zen2 msi```",
            inline=False,
        )
        embed.add_field(
            name="**Aktuell verfügbare Layouts(Hersteller):**",
            value="```ASUS, MSI, ZenTimings(Default)```",
            inline=False,
        )
        embed.add_field(
            name="**Aktuell verfügbare Presets:**",
            value=f"```{new_line.join(values_list[1:])}```",
            inline=False,
        )
        embed.set_author(
            name="Lorettas RAM Timing Presets",
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
