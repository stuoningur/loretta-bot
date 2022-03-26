import disnake
import gspread_asyncio
from disnake.ext import commands
from oauth2client.service_account import ServiceAccountCredentials
from tabulate import tabulate


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
            board: str = "zentimings",
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
            board = board.lower()
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

                asus = tabulate(
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

                zentimings = tabulate(
                    [
                        [
                            "tCL",
                            f"{timings_data['tCL']}",
                            "tRDRDSCL",
                            f"{timings_data['tRDRDSCL']}",
                        ],
                        [
                            "tRCDWR",
                            f"{timings_data['tRCDWR']}",
                            "tWRWRSCL",
                            f"{timings_data['tWRWRSCL']}",
                        ],
                        [
                            "tRCDRD",
                            f"{timings_data['tRCDRD']}",
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
                            "tRDRDSC",
                            f"{timings_data['tRDRDSC']}",
                        ],
                        [
                            "tRRDL",
                            f"{timings_data['tRRDL']}",
                            "tRDRDSD",
                            f"{timings_data['tRDRDSD']}",
                        ],
                        [
                            "tFAW",
                            f"{timings_data['tFAW']}",
                            "tRDRDDD",
                            f"{timings_data['tRDRDDD']}",
                        ],
                        [
                            "tWTRS",
                            f"{timings_data['tWTRS']}",
                            "tWRWRSC",
                            f"{timings_data['tWRWRSC']}",
                        ],
                        [
                            "tWTRL",
                            f"{timings_data['tWTRL']}",
                            "tWRWRSD",
                            f"{timings_data['tWRWRSD']}",
                        ],
                        [
                            "tWR",
                            f"{timings_data['tWR']}",
                            "tWRWRDD",
                            f"{timings_data['tWRWRDD']}",
                        ],
                        [
                            "tRFC",
                            f"{timings_data['tRFC']}",
                            "tCKE",
                            f"{timings_data['tCKE']}",
                        ],
                    ],
                    tablefmt="plain",
                    colalign=("left", "right", "left", "right"),
                )
                msi = tabulate(
                    [
                        [
                            "tCL",
                            f"{timings_data['tCL']}",
                            "tFAW",
                            f"{timings_data['tFAW']}",
                        ],
                        [
                            "tRCDRD",
                            f"{timings_data['tRCDRD']}",
                            "tCWL",
                            f"{timings_data['tCWL']}",
                        ],
                        [
                            "tRCDWR",
                            f"{timings_data['tRCDWR']}",
                            "tCKE",
                            f"{timings_data['tCKE']}",
                        ],
                        [
                            "tRP",
                            f"{timings_data['tRP']}",
                            "tRDRDSCL",
                            f"{timings_data['tRDRDSCL']}",
                        ],
                        [
                            "tRAS",
                            f"{timings_data['tRAS']}",
                            "tRDRDSC",
                            f"{timings_data['tRDRDSC']}",
                        ],
                        [
                            "tRC",
                            f"{timings_data['tRC']}",
                            "tRDRDSD",
                            f"{timings_data['tRDRDSD']}",
                        ],
                        [
                            "tRFC",
                            f"{timings_data['tRFC']}",
                            "tRDRDDD",
                            f"{timings_data['tRDRDDD']}",
                        ],
                        [
                            "tWR",
                            f"{timings_data['tWR']}",
                            "tWRWRSCL",
                            f"{timings_data['tWRWRSCL']}",
                        ],
                        [
                            "tWTRS",
                            f"{timings_data['tWTRS']}",
                            "tWRWRSC",
                            f"{timings_data['tWRWRSC']}",
                        ],
                        [
                            "tWTRL",
                            f"{timings_data['tWTRL']}",
                            "tWRWRSD",
                            f"{timings_data['tWRWRSD']}",
                        ],
                        [
                            "tRRDS",
                            f"{timings_data['tRRDS']}",
                            "tWRWRDD",
                            f"{timings_data['tWRWRDD']}",
                        ],
                        [
                            "tRRDL",
                            f"{timings_data['tRRDL']}",
                            "tRDWR",
                            f"{timings_data['tRDWR']}",
                        ],
                        [
                            "tRTP",
                            f"{timings_data['tRTP']}",
                            "tWRRD",
                            f"{timings_data['tWRRD']}",
                        ],
                    ],
                    tablefmt="plain",
                    colalign=("left", "right", "left", "right"),
                )

                rtts = tabulate(
                    [["Single Rank\nDual Rank", f"{timings_data['RTTs']}"]],
                    tablefmt="plain",
                    colalign=("left", "left"),
                )
                original_rtts = timings_data["RTTs"].replace(" ", "").split("\n")

                sr_rtts = []
                dr_rtts = []

                helper_sr_rtts = []
                helper_dr_rtts = []
                msi_sr_rtts = []
                msi_dr_rtts = []

                sr_rtts = original_rtts[0].split(",")

                dr_rtts = original_rtts[1].split(",")

                for rtt in sr_rtts:
                    helper_sr_rtts.append(rtt.split("/"))

                for rtt in dr_rtts:
                    helper_dr_rtts.append(rtt.split("/"))

                for rtt in helper_sr_rtts:
                    msi_rtt = f"{int(240 / int(rtt[1])) if int(rtt[1]) != 0 else 0}/{int(240 / int(rtt[0])) if int(rtt[0]) != 0 else 0}/{int(240 / int(rtt[2])) if int(rtt[2]) != 0 else 0}"
                    msi_sr_rtts.append(msi_rtt)

                for rtt in helper_dr_rtts:
                    msi_rtt = f"{int(240 / int(rtt[1])) if int(rtt[1]) != 0 else 0}/{int(240 / int(rtt[0])) if int(rtt[0]) != 0 else 0}/{int(240 / int(rtt[2])) if int(rtt[2]) != 0 else 0}"
                    msi_dr_rtts.append(msi_rtt)

                msi_sr_rtts = ", ".join(msi_sr_rtts)
                msi_dr_rtts = ", ".join(msi_dr_rtts)

                msi_rtts = f"{msi_sr_rtts}\n{msi_dr_rtts}"

                msi_rtts = tabulate(
                    [["Single Rank\nDual Rank", f"{msi_rtts}"]],
                    tablefmt="plain",
                    colalign=("left", "left"),
                )

                if board == "msi":
                    timings = msi
                    rtts = msi_rtts
                elif board == "asus":
                    timings = asus
                else:
                    timings = zentimings

                embed = disnake.Embed(
                    colour=0xE74C3C,
                )
                embed.add_field(
                    name="**Preset:**",
                    value=f"**{timings_data['Name'].title()}**",
                    inline=False,
                )
                embed.add_field(
                    name="**Taktraten:**",
                    value=f"```{base_settings}```",
                    inline=False,
                )
                embed.add_field(
                    name="**Spannungen:**",
                    value=f"```{voltages}```",
                    inline=False,
                )
                embed.add_field(
                    name="**Timings:**",
                    value=f"```{timings}```",
                    inline=False,
                )
                embed.add_field(
                    name="**ProcODT:**",
                    value=f"```{timings_data['ProcODT']}```",
                    inline=False,
                )
                embed.add_field(
                    name="**RTTs:**",
                    value=f"```{rtts}```",
                    inline=False,
                )
                embed.add_field(
                    name="**CADs:**",
                    value=f"```{timings_data['CADs']}```",
                    inline=False,
                )
                embed.set_author(name="Lorettas Timings")
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Timings(bot))
