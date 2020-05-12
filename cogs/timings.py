import discord
from discord.ext import commands

samsung_b_die_3600_lasch_spannung = "```VDIMM       1,35 - 1,38\nVDDG        0,95 - 1,05 (IOD & CCD)\nCLDO VDDP   855 - 1050\n```"
samsung_b_die_3600_lasch_timings = "```tCL        16        tWRWRSCL     4\ntRCDRD     16 (17)   tRFC       288\ntRCDWR     16        tCWL        16\ntRP        16        tRTP        12\ntRAS       32        tRDWR       10\ntRC        42        tWRRD        4\ntRRDS      4         tWRWRSC      1\ntRRDL      6         tWRWRSD      7\ntFAW       24        tWRWRDD      7\ntWTRS      6         tRDRDSC      1\ntWTRL      12        tRDRDSD      5\ntWR        14        tRDRDDD      5\ntRDRDSCL   4         tCKE         1\n```"
samsung_b_die_3600_lasch_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

samsung_b_die_3600_scharf_spannung = "```VDIMM       1,37 - 1,42\nVDDG        0,95 - 1,05 (IOD & CCD)\nCLDO VDDP   855 - 1050\n```"
samsung_b_die_3600_scharf_timings = "```tCL        14        tWRWRSCL     4\ntRCDRD     14 (15)   tRFC       252\ntRCDWR     14        tCWL        14\ntRP        14        tRTP        12\ntRAS       28        tRDWR        8\ntRC        38        tWRRD        2\ntRRDS      4         tWRWRSC      1\ntRRDL      6         tWRWRSD      7\ntFAW       16        tWRWRDD      7\ntWTRS      4         tRDRDSC      1\ntWTRL      8         tRDRDSD      5\ntWR        14        tRDRDDD      5\ntRDRDSCL   4         tCKE         1\n```"
samsung_b_die_3600_scharf_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

samsung_b_die_3733_lasch_spannung = "```VDIMM       1,37 - 1,42\nVDDG        0,95 - 1,05 (IOD & CCD)\nCLDO VDDP   855 - 1050\n```"
samsung_b_die_3733_lasch_timings = "```tCL        16        tWRWRSCL     4\ntRCDRD     16 (17)   tRFC       299\ntRCDWR     16        tCWL        16\ntRP        16        tRTP        12\ntRAS       32        tRDWR       10\ntRC        42        tWRRD        4\ntRRDS      4         tWRWRSC      1\ntRRDL      6         tWRWRSD      7\ntFAW       24        tWRWRDD      7\ntWTRS      6         tRDRDSC      1\ntWTRL      12        tRDRDSD      5\ntWR        14        tRDRDDD      5\ntRDRDSCL   4         tCKE         1\n```"
samsung_b_die_3733_lasch_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

samsung_b_die_3733_scharf_spannung = "```VDIMM       1,42 - 1,47\nVDDG        0,95 - 1,05 (IOD & CCD)\nCLDO VDDP   855 - 1050\n```"
samsung_b_die_3733_scharf_timings = "```tCL        14          tWRWRSCL     4\ntRCDRD     15 (16)     tRFC       261\ntRCDWR     14          tCWL        14\ntRP        14          tRTP        12\ntRAS       28          tRDWR        8\ntRC        38 (42)     tWRRD        2\ntRRDS       4          tWRWRSC      1\ntRRDL       6          tWRWRSD      7\ntFAW       16          tWRWRDD      7\ntWTRS       4          tRDRDSC      1\ntWTRL       8          tRDRDSD      5\ntWR        14          tRDRDDD      5\ntRDRDSCL    4          tCKE         1\n```"
samsung_b_die_3733_scharf_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

samsung_b_die_3800_lasch_spannung = "```VDIMM       1,40 - 1,45\nVDDG        0,95 - 1,05 (IOD & CCD)\nCLDO VDDP   855 - 1050\n```"
samsung_b_die_3800_lasch_timings = "```tCL        16          tWRWRSCL     4\ntRCDRD     16 (17)     tRFC       304\ntRCDWR     16          tCWL        16\ntRP        16          tRTP        12\ntRAS       32          tRDWR       10\ntRC        42          tWRRD        4\ntRRDS       4          tWRWRSC      1\ntRRDL       6          tWRWRSD      7\ntFAW       24          tWRWRDD      7\ntWTRS       6          tRDRDSC      1\ntWTRL      12          tRDRDSD      5\ntWR        14          tRDRDDD      5\ntRDRDSCL    4          tCKE         1\n```"
samsung_b_die_3800_lasch_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

samsung_b_die_3800_scharf_spannung = "```VDIMM       1,45 - 1,50\nVDDG        0,95 - 1,05 (IOD & CCD)\nCLDO VDDP   855 - 1050\n```"
samsung_b_die_3800_scharf_timings = "```tCL        14          tWRWRSCL     4\ntRCDRD     15 (16)     tRFC       266\ntRCDWR     14          tCWL        14\ntRP        14          tRTP        12\ntRAS       28          tRDWR        8\ntRC        38 (42)     tWRRD        2\ntRRDS       4          tWRWRSC      1\ntRRDL       6          tWRWRSD      7\ntFAW       16          tWRWRDD      7\ntWTRS       4          tRDRDSC      1\ntWTRL       8          tRDRDSD      5\ntWR        14          tRDRDDD      5\ntRDRDSCL    4          tCKE         1\n```"
samsung_b_die_3800_scharf_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

samsung_b_die_cads = "```24/20/20/24\n24/20/24/24\n24/24/24/24\n60/20/24/24```"

micron_e_die_3600_lasch_spannung = "```VDIMM       1,35 - 1,37\n```"
micron_e_die_3600_lasch_timings = "```tCL        16   tWRWRSCL     4\ntRCDRD     19   tRFC       570\ntRCDWR     16   tCWL        16\ntRP        16   tRTP        12\ntRAS       40   tRDWR       10\ntRC        65   tWRRD        4\ntRRDS       4   tWRWRSC      1\ntRRDL       7   tWRWRSD      7\ntFAW       24   tWRWRDD      7\ntWTRS       4   tRDRDSC      1\ntWTRL      12   tRDRDSD      5\ntWR        24   tRDRDDD      5\ntRDRDSCL    4   tCKE         1\n```"
micron_e_die_3600_lasch_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

micron_e_die_3733_lasch_spannung = "```VDIMM       1,38\n```"
micron_e_die_3733_lasch_timings = "```tCL        16   tWRWRSCL     4\ntRCDRD     19   tRFC       600\ntRCDWR     16   tCWL        16\ntRP        16   tRTP        12\ntRAS       38   tRDWR       12\ntRC        60   tWRRD        7\ntRRDS       6   tWRWRSC      1\ntRRDL       9   tWRWRSD      7\ntFAW       36   tWRWRDD      7\ntWTRS       5   tRDRDSC      1\ntWTRL      12   tRDRDSD      5\ntWR        24   tRDRDDD      5\ntRDRDSCL    4   tCKE         1\n```"
micron_e_die_3733_lasch_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

micron_e_die_3733_scharf_spannung = "```VDIMM       1,40\n```"
micron_e_die_3733_scharf_timings = "```tCL        16   tWRWRSCL     4\ntRCDRD     19   tRFC       550\ntRCDWR     16   tCWL        16\ntRP        16   tRTP        12\ntRAS       34   tRDWR       10\ntRC        56   tWRRD        7\ntRRDS       6   tWRWRSC      1\ntRRDL       8   tWRWRSD      7\ntFAW       24   tWRWRDD      7\ntWTRS       4   tRDRDSC      1\ntWTRL      10   tRDRDSD      5\ntWR        16   tRDRDDD      5\ntRDRDSCL    4   tCKE         1\n```"
micron_e_die_3733_scharf_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

micron_e_die_3800_lasch_spannung = "```VDIMM       1,38\n```"
micron_e_die_3800_lasch_timings = "```tCL        16   tWRWRSCL     4\ntRCDRD     19   tRFC       625\ntRCDWR     16   tCWL        16\ntRP        16   tRTP        12\ntRAS       40   tRDWR       12\ntRC        65   tWRRD        7\ntRRDS       6   tWRWRSC      1\ntRRDL      10   tWRWRSD      7\ntFAW       36   tWRWRDD      7\ntWTRS       5   tRDRDSC      1\ntWTRL      12   tRDRDSD      5\ntWR        24   tRDRDDD      5\ntRDRDSCL    4   tCKE         1\n```"
micron_e_die_3800_lasch_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

micron_e_die_3800_scharf_spannung = "```VDIMM       1,40\n```"
micron_e_die_3800_scharf_timings = "```tCL        16   tWRWRSCL     4\ntRCDRD     19   tRFC       560\ntRCDWR     16   tCWL        16\ntRP        16   tRTP        12\ntRAS       38   tRDWR       10\ntRC        60   tWRRD        7\ntRRDS       6   tWRWRSC      1\ntRRDL       9   tWRWRSD      7\ntFAW       24   tWRWRDD      7\ntWTRS       4   tRDRDSC      1\ntWTRL      10   tRDRDSD      5\ntWR        16   tRDRDDD      5\ntRDRDSCL    4   tCKE         1\n```"
micron_e_die_3800_scharf_rtts = (
    "```2x8GB    0/0/5\n2x16GB   0/3/1\n4x8GB    7/3/1\n4x16GB   7/3/1```"
)

micron_e_die_cads = "```24/24/24/24```"


class Timings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["t"])
    async def timings(
        self,
        ctx,
        vendor: str = None,
        ics: str = None,
        memclk: int = None,
        preset: str = None,
    ):
        if vendor is None or ics is None or memclk is None or preset is None:
            await ctx.send("Es fehlt ein oder mehrere Argumente")
        else:
            if vendor == "samsung":
                if ics == "bdie":
                    cads = samsung_b_die_cads
                    if memclk == 3600:
                        if preset == "lasch":
                            title = "**Samsung B-Die 3600 Lasche Timings**"
                            clk = "```MEMCLK          3600       FCLK           1800\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = samsung_b_die_3600_lasch_spannung
                            timings = samsung_b_die_3600_lasch_timings
                            rtts = samsung_b_die_3600_lasch_rtts
                        elif preset == "scharf":
                            title = "**Samsung B-Die 3600 Scharfe Timings**"
                            clk = "```MEMCLK          3600       FCLK           1800\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = samsung_b_die_3600_scharf_spannung
                            timings = samsung_b_die_3600_scharf_timings
                            rtts = samsung_b_die_3600_scharf_rtts
                        else:
                            await ctx.send(
                                "Es konnte keine Daten für das angegebene Preset gefunden werden."
                            )
                            return
                    elif memclk == 3733:
                        if preset == "lasch":
                            title = "**Samsung B-Die 3733 Lasche Timings**"
                            clk = "```MEMCLK          3733       FCLK           1866\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = samsung_b_die_3733_lasch_spannung
                            timings = samsung_b_die_3733_lasch_timings
                            rtts = samsung_b_die_3733_lasch_rtts
                        elif preset == "scharf":
                            title = "**Samsung B-Die 3733 Scharfe Timings**"
                            clk = "```MEMCLK          3733       FCLK           1866\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = samsung_b_die_3733_scharf_spannung
                            timings = samsung_b_die_3733_scharf_timings
                            rtts = samsung_b_die_3733_scharf_rtts
                        else:
                            await ctx.send(
                                "Es konnte keine Daten für das angegebene Preset gefunden werden."
                            )
                            return
                    elif memclk == 3800:
                        if preset == "lasch":
                            title = "**Samsung B-Die 3800 Lasche Timings**"
                            clk = "```MEMCLK          3800       FCLK           1900\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = samsung_b_die_3800_lasch_spannung
                            timings = samsung_b_die_3800_lasch_timings
                            rtts = samsung_b_die_3800_lasch_rtts
                        elif preset == "scharf":
                            title = "**Samsung B-Die 3800 Scharfe Timings**"
                            clk = "```MEMCLK          3800       FCLK           1900\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = samsung_b_die_3800_scharf_spannung
                            timings = samsung_b_die_3800_scharf_timings
                            rtts = samsung_b_die_3800_scharf_rtts
                        else:
                            await ctx.send(
                                "Es konnte keine Daten für das angegebene Preset gefunden werden."
                            )
                            return
                    else:
                        await ctx.send(
                            "Es konnten keine Daten für den angegebenen RAM Takt gefunden werden."
                        )
                        return
                else:
                    await ctx.send(
                        "Es konnten keine Daten für die angegebenen Speicher-ICs gefunden werden."
                    )
                    return
            elif vendor == "micron":
                if ics == "edie":
                    cads = micron_e_die_cads
                    if memclk == 3600:
                        if preset == "lasch":
                            title = "**Micron Rev. E 3600 Lasche Timings**"
                            clk = "```MEMCLK          3600       FCLK           1800\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = micron_e_die_3600_lasch_spannung
                            timings = micron_e_die_3600_lasch_timings
                            rtts = micron_e_die_3600_lasch_rtts
                        # elif preset == "scharf":
                        #     title = "**Micron Rev. E 3600 Scharfe Timings**"
                        #     clk = "```MEMCLK     3600      FCLK       1800```"
                        #     spannung = samsung_b_die_3600_lasch_spannung
                        #     timings = samsung_b_die_3600_lasch_timings
                        #     rtts = samsung_b_die_3600_lasch_rtts
                        else:
                            await ctx.send(
                                "Es konnte keine Daten für das angegebene Preset gefunden werden."
                            )
                            return
                    elif memclk == 3733:
                        if preset == "lasch":
                            title = "**Micron Rev. E 3733 Lasche Timings**"
                            clk = "```MEMCLK          3733       FCLK           1866\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = micron_e_die_3733_lasch_spannung
                            timings = micron_e_die_3733_lasch_timings
                            rtts = micron_e_die_3733_lasch_rtts
                        elif preset == "scharf":
                            title = "**Micron Rev. E 3733 Scharfe Timings**"
                            clk = "```MEMCLK          3733       FCLK           1866\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = micron_e_die_3733_scharf_spannung
                            timings = micron_e_die_3733_scharf_timings
                            rtts = micron_e_die_3733_scharf_rtts
                        else:
                            await ctx.send(
                                "Es konnte keine Daten für das angegebene Preset gefunden werden."
                            )
                            return
                    elif memclk == 3800:
                        if preset == "lasch":
                            title = "**Micron Rev. E 3800 Lasche Timings**"
                            clk = "```MEMCLK          3800       FCLK           1900\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = micron_e_die_3800_lasch_spannung
                            timings = micron_e_die_3800_lasch_timings
                            rtts = micron_e_die_3800_lasch_rtts
                        elif preset == "scharf":
                            title = "**Micron Rev. E 3800 Scharfe Timings**"
                            clk = "```MEMCLK          3800       FCLK           1900\nPowerDownMode   Disabled   GearDownMode   Enabled  ```"
                            spannung = micron_e_die_3800_scharf_spannung
                            timings = micron_e_die_3800_scharf_timings
                            rtts = micron_e_die_3800_scharf_rtts
                        else:
                            await ctx.send(
                                "Es konnte keine Daten für das angegebene Preset gefunden werden."
                            )
                            return
                    else:
                        await ctx.send(
                            "Es konnten keine Daten für den angegebenen RAM Takt gefunden werden."
                        )
                        return
                else:
                    await ctx.send(
                        "Es konnten keine Daten für die angegebenen Speicher-ICs gefunden werden."
                    )
                    return
            elif vendor == "hynix":
                if ics == "nix":
                    return
                else:
                    await ctx.send(
                        "Es konnten keine Daten für die angegebenen Speicher-ICs gefunden werden."
                    )
                    return
            else:
                await ctx.send("Der Hersteller konnte nicht gefunden werden.")
                return

        embed = discord.Embed(colour=0xE74C3C,)
        embed.add_field(
            name="**Preset:**", value=title, inline="false",
        )
        embed.add_field(
            name="**Taktraten:**", value=clk, inline="false",
        )
        embed.add_field(
            name="**Spannungen:**", value=spannung, inline="false",
        )
        embed.add_field(
            name="**Timings:**", value=timings, inline="false",
        )
        embed.add_field(
            name="**RTTs:**", value=rtts, inline="false",
        )
        embed.add_field(
            name="**CADs:**", value=cads, inline="false",
        )
        embed.set_author(name=f"Lorettas Timings")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Timings(bot))
