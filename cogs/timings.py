import discord
from discord.ext import commands
from tabulate import tabulate

import gspread_asyncio
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


class Timings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["t"])
    async def timings(
        self,
        ctx,
        vendor: str = None,
        ics: str = None,
        memclk: str = None,
        preset: str = None,
        generation: str = "zen2",
    ):
        if (
            vendor is None
            or ics is None
            or memclk is None
            or preset is None
            or generation is None
        ):
            await ctx.send("Es fehlt ein oder mehrere Argumente")
        else:
            vendor = vendor.lower()
            ics = ics.lower()
            preset = preset.lower()
            generation = generation.lower()
            agcm = gspread_asyncio.AsyncioGspreadClientManager(get_creds)
            agc = await agcm.authorize()
            document = await agc.open("loretta_timings")
            worksheet = await document.get_worksheet(0)
            table_data = await worksheet.get_all_records()

            timings_data = {}

            for data in table_data:
                if data["Vendor"] == vendor:
                    if data["ICs"] == ics:
                        if str(data["MEMCLK"]) == memclk:
                            if data["Preset"] == preset:
                                if data["Generation"] == generation:
                                    timings_data = data

            if not timings_data:
                await ctx.send(
                    "Es wurde kein Preset für die angegebenen Daten gefunden."
                )
            else:
                base_settings = tabulate(
                    [
                        ["MEMCLK", f"{timings_data['MEMCLK']}"],
                        ["FCLK", f"{timings_data['FCLK']}"],
                        ["PowerDownMode", f"{timings_data['PDM']}"],
                        ["GearDownMode", f"{timings_data['GDM']}"],
                    ],
                    tablefmt="plain",
                )

                voltages = tabulate(
                    [
                        ["VDIMM", f"{timings_data['VDIMM']}"],
                        ["VSOC", f"{timings_data['VSOC']}"],
                        ["VDDG", f"{timings_data['VDDG']}"],
                        ["CLDO VDDP", f"{timings_data['CLDO VDDP']}"],
                        
                    ],
                    tablefmt="plain",
                    colalign=("left", "right"),
                )

                timings = tabulate(
                    [
                        [
                            "tCL",
                            f"{timings_data['tCL']}",
                            "tWRWRSCL",
                            f"{timings_data['tWRWRSCL']}",
                        ],
                        [
                            "tRCDRD",
                            f"{timings_data['tRCDRD']}",
                            "tRFC",
                            f"{timings_data['tRFC']}",
                        ],
                        [
                            "tRCDWR",
                            f"{timings_data['tRCDWR']}",
                            "tCWL",
                            f"{timings_data['tCWL']}",
                        ],
                        [
                            "tRP",
                            f"{timings_data['tRP']}",
                            "tRTP",
                            f"{timings_data['tRTP']}",
                        ],
                        [
                            "tRAS",
                            f"{timings_data['tRAS']}",
                            "tRDWR",
                            f"{timings_data['tRDWR']}",
                        ],
                        [
                            "tRC",
                            f"{timings_data['tRC']}",
                            "tWRRD",
                            f"{timings_data['tWRRD']}",
                        ],
                        [
                            "tRRDS",
                            f"{timings_data['tRRDS']}",
                            "tWRWRSC",
                            f"{timings_data['tWRWRSC']}",
                        ],
                        [
                            "tRRDL",
                            f"{timings_data['tRRDL']}",
                            "tWRWRSD",
                            f"{timings_data['tWRWRSD']}",
                        ],
                        [
                            "tFAW",
                            f"{timings_data['tFAW']}",
                            "tWRWRDD",
                            f"{timings_data['tWRWRDD']}",
                        ],
                        [
                            "tWTRS",
                            f"{timings_data['tWTRS']}",
                            "tRDRDSC",
                            f"{timings_data['tRDRDSC']}",
                        ],
                        [
                            "tWTRL",
                            f"{timings_data['tWTRL']}",
                            "tRDRDSD",
                            f"{timings_data['tRDRDSD']}",
                        ],
                        [
                            "tWR",
                            f"{timings_data['tWR']}",
                            "tRDRDDD",
                            f"{timings_data['tRDRDDD']}",
                        ],
                        [
                            "tRDRDSCL",
                            f"{timings_data['tRDRDSCL']}",
                            "tCKE",
                            f"{timings_data['tCKE']}",
                        ],
                    ],
                    tablefmt="plain",
                    colalign=("left", "right", "left", "right"),
                )

                rtts = tabulate(
                    [["2x8GB\n2x16GB\n4x8GB\n4x16GB", f"{timings_data['RTTs']}"]],
                    tablefmt="plain",
                    colalign=("left", "left"),
                )

                embed = discord.Embed(
                    colour=0xE74C3C,
                )
                embed.add_field(
                    name="**Preset:**",
                    value=f"**{timings_data['Name'].title()}**",
                    inline="false",
                )
                embed.add_field(
                    name="**Taktraten:**",
                    value=f"```{base_settings}```",
                    inline="false",
                )
                embed.add_field(
                    name="**Spannungen:**",
                    value=f"```{voltages}```",
                    inline="false",
                )
                embed.add_field(
                    name="**Timings:**",
                    value=f"```{timings}```",
                    inline="false",
                )
                embed.add_field(
                    name="**ProcODT:**",
                    value=f"```{timings_data['ProcODT']}```",
                    inline="false",
                )
                embed.add_field(
                    name="**RTTs:**",
                    value=f"```{rtts}```",
                    inline="false",
                )
                embed.add_field(
                    name="**CADs:**",
                    value=f"```{timings_data['CADs']}```",
                    inline="false",
                )
                embed.set_author(name=f"Lorettas Timings")
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Timings(bot))
