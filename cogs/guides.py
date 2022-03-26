import disnake
from disnake.ext import commands


class Guides(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bios(self, ctx):
        """Link zu der besten AM4 Bios Übersicht"""
        embed = disnake.Embed(
            title="Ultimative AM4 UEFI/BIOS/AGESA Übersicht",
            colour=0xE74C3C,
            url="https://www.hardwareluxx.de/community/threads/ultimative-am4-uefi-bios-agesa-%C3%9Cbersicht-17-02-19.1228903/",
            description="Anbei findet ihr eine UEFI/BIOS Übersicht mit den jeweils aktuellsten Versionen, sortiert nach aktuellem AGESA Stand. Sollte mal eine Version fehlen oder ihr einen Fehler findet, dann dürft ihr das hier gerne mitteilen.\n\nChannel: <#578340164187979796>",
        )

        embed.set_image(url="https://i.imgur.com/ytFxJ9B.png")
        embed.set_thumbnail(url="https://i.imgur.com/6wqgd4K.png")
        embed.set_author(
            name="Reous (Mr. AMD)",
            url="https://www.hardwareluxx.de/community/members/reous.55847/",
            icon_url="https://i.imgur.com/ArBeYmq.png",
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def cpu(self, ctx):
        """Link zu dem Community CPU und Bios Guide"""
        embed = disnake.Embed(
            title="CPU und Bios Guide für Ryzen 3000 (und älter)",
            colour=0xE74C3C,
            url="https://www.computerbase.de/forum/threads/cpu-und-bios-guide-fuer-ryzen-3000-und-aelter.1911429/",
            description="Erklärungen und Tipps um das beste aus einer AMD Ryzen CPU rauszuholen.\n\nChannel: <#612647199737774104>",
        )

        embed.set_image(url="https://i.imgur.com/jC0K8W8.png")
        embed.set_thumbnail(url="https://i.imgur.com/vVeSNQS.png")
        embed.set_author(
            name="Verangry",
            url="https://www.computerbase.de/forum/members/verangry.798158/",
            icon_url="https://i.imgur.com/mu0em6U.png",
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["limits"])
    async def limit(self, ctx):
        """Link zu Hardwareluxx RAM OC und Limit Thread"""
        embed = disnake.Embed(
            title="Ryzen RAM OC Thread + Mögliche Limitierungen",
            colour=0xE74C3C,
            url="https://www.hardwareluxx.de/community/threads/ryzen-ram-oc-thread-m%C3%B6gliche-limitierungen.1216557/",
            description="In diesem Thread werde ich Informationen zum Thema RAM OC Allgemein sammeln, sowie nennenswerte Anleitungen oder Threads verlinken. Habt ihr Fragen zum Thema RAM OC oder braucht Hilfe euren RAM zu übertakten, dann seid ihr hier im richtigen Thread. Zögert nicht zu fragen, wir helfen gerne weiter.\n\nChannel: <#506902038215655424>",
        )

        embed.set_image(url="https://i.imgur.com/isFPomg.png")
        embed.set_thumbnail(url="https://i.imgur.com/RZVRV7K.png")
        embed.set_author(
            name="Reous (Mr. AMD)",
            url="https://www.hardwareluxx.de/community/members/reous.55847/",
            icon_url="https://i.imgur.com/ArBeYmq.png",
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["list", "ergebnisse"])
    async def liste(self, ctx):
        """Link zum OC Ergebnisse Google Sheet"""
        embed = disnake.Embed(
            title="RAM OC Ergebnisse - Google Sheet",
            colour=0xE74C3C,
            url="https://docs.google.com/spreadsheets/d/1HKPVfDcFO-aieAOXHFQZp15rwWadbPTVDNgO8vtyDCM",
            description="Eine Sammlung an RAM OC Ergebnissen übersichtlich in einem Google Sheet dargestellt.\n\nChannel: <#590255495592542219>",
        )

        embed.set_image(url="https://i.imgur.com/14yKUIi.png")
        embed.set_thumbnail(url="https://i.imgur.com/OE94LR0.png")
        embed.set_author(
            name="shaav - Philipp",
            url="https://www.hardwareluxx.de/community/members/shaav.25323/",
            icon_url="https://i.imgur.com/DB4ei4M.png",
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["mobo", "motherboard", "vrm"])
    async def mainboard(self, ctx):
        """Link zum Hardwareluxx AM4 VRM Thread"""
        embed = disnake.Embed(
            title="AMD 3rd Gen AM4 Mainboards & VRM Liste (X570, P560, B550, A520, A420)",
            colour=0xE74C3C,
            url="https://www.hardwareluxx.de/community/threads/amd-3rd-gen-am4-mainboards-vrm-liste-x570-p560-b550-a520-a420.1228904/",
            description="Hier dürfen News und Produkte diskutieret, Informationen erfragt und zusammengetragen, technische Fragen gestellt und schließlich auch Erfahrungen mit dem eigenen System ausgetauscht werden. Der Umfang des Threads hängt von eurer Beteiligung ab und eure Unterstützung beim Sammeln von Informationen zur Vervollständigung der Übersicht ist ausdrücklich erbeten.\n\nChannel: <#578340164187979796>",
        )

        embed.set_image(url="https://i.imgur.com/owYHwzW.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/Motc8J6.png")
        embed.set_author(
            name="emissary42",
            url="https://www.hardwareluxx.de/community/members/emissary42.38573/",
            icon_url="https://i.imgur.com/DcfAykw.png",
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["anleitung"])
    async def manual(self, ctx):
        """Link zu der RAM OC Anleitung"""
        embed = disnake.Embed(
            title="RAM OC Anleitung",
            colour=0xE74C3C,
            url="https://www.computerbase.de/forum/threads/amd-ryzen-ram-oc-community.1829356/",
            description="Wir versuchen nicht nur höhere RAM-Taktstufen zu erreichen, sondern auch die dazugehörigen Haupt- & Subtimings auf das System abgestimmt zu optimieren.",
        )
        embed.add_field(
            name="Download",
            value="[Link zur Zen2 PDF Anleitung - Version 2.10 (29.09.2019)](https://cdn.discordapp.com/attachments/506901533821239317/627968448500072448/RAM_OC_Anleitung_Vers_2_10.pdf)\n\n[Link zur Zen1/Zen+ PDF Anleitung - Version 1.30 (11.04.2019)](https://drive.google.com/open?id=1NQcR5ZiBnI-vENU-XSnQvvB3JzmGn2Ze)",
            inline=False,
        )
        embed.add_field(
            name="Wichtige RAM Timings von Reous",
            value="[RAM Timings und deren Einfluss auf Spiele und Anwendungen](https://www.hardwareluxx.de/community/threads/ram-timings-und-deren-einfluss-auf-spiele-und-anwendungen-amd.1269156/#5.0)\n\nChannel: <#590260218512932919>",
            inline=False,
        )
        embed.set_image(url="https://i.imgur.com/4hCP34S.png")
        embed.set_thumbnail(url="https://i.imgur.com/W83EAab.png")
        embed.set_author(
            name="cm87",
            url="https://www.computerbase.de/forum/members/cm87.771841/",
            icon_url="https://i.imgur.com/Fci12gO.png",
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["ramkits", "ram"])
    async def ramkit(self, ctx):
        """Link zum Computerbase RAM-Empfehlungen Artikel"""
        embed = disnake.Embed(
            title="Aus der Community: RAM-Empfehlungen für AMD Ryzen und Intel Core",
            colour=0xE74C3C,
            url="https://www.computerbase.de/thema/ram/rangliste/",
            description="In der Prozessor- und der Grafikkarten-Rangliste spricht ComputerBase bereits seit vier Jahren monatlich CPU- und GPU-Kaufempfehlungen aus. Ab sofort gibt es auch eine Kaufberatung für Arbeitsspeicher. Deren Pflege verantwortet die Community.\n\nChannel: <#612647199737774104>",
        )

        embed.set_image(url="https://i.imgur.com/pOsPkxk.png")
        embed.set_thumbnail(url="https://i.imgur.com/Iml7Mgn.png")
        embed.set_author(
            name="SV3N",
            url="https://www.computerbase.de/forum/members/sv3n.774722/",
            icon_url="https://i.imgur.com/cjo3SMD.png",
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["ics"])
    async def spd(self, ctx):
        """Link zur HARDWARELUXX SPD Datenbank"""
        embed = disnake.Embed(
            title="Hardwareluxx SPD Datenbank",
            colour=0xE74C3C,
            url="https://www.hardwareluxx.de/community/threads/hardwareluxx-spd-datenbank-anleitung-zum-ic-auslesen-v3-update-14-02-20.1073628/",
            description="Sammelthread auf Hardwareluxx für SPD Daten von DDR1 bis DDR4 inkl. Anleitung zum Auslesen der Daten.\n\nChannel: <#545701084409233438>",
        )
        embed.add_field(
            name="Siehe auch",
            value="[Hersteller IC Versionnummern](https://i.imgur.com/sCc4l7l.png)",
            inline=False,
        )
        embed.set_image(url="https://i.imgur.com/OgacaAo.png")
        embed.set_thumbnail(url="https://i.imgur.com/yYBXwTP.png")
        embed.set_author(
            name="emissary42",
            url="https://www.hardwareluxx.de/community/members/emissary42.38573/",
            icon_url="https://i.imgur.com/DcfAykw.png",
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["co", "curveoptimizer", "kurvenoptimierer"])
    async def curve(self, ctx):
        """Link zu dem Community Curve Optimizer Guide"""
        embed = disnake.Embed(
            title="Curve Optimizer Guide Ryzen 5000",
            colour=0xE74C3C,
            url="https://www.computerbase.de/forum/threads/curve-optimizer-guide-ryzen-5000.2015251/",
            description="Anleitung und Erklärungen für den Curve Optimizer bei Zen 3.\n\nChannel: <#612647199737774104>",
        )
        embed.add_field(
            name="PDF Download",
            value="[Link zur Curve Optimizer PDF Anleitung](https://drive.google.com/file/d/1EiVoPjuyaVKlzsL4sUsXwwVUVnch8QdR/view)",
            inline=False,
        )
        embed.set_image(url="https://i.imgur.com/jC0K8W8.png")
        embed.set_thumbnail(url="https://i.imgur.com/D5bEWL2.png")
        embed.set_author(
            name="Verangry",
            url="https://www.computerbase.de/forum/members/verangry.798158/",
            icon_url="https://i.imgur.com/mu0em6U.png",
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Guides(bot))
