import discord
from discord.ext import commands


class bios(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bios(self, ctx):
        """Link zu der besten AM4 Bios Übersicht"""
        embed = discord.Embed(
            title="Ultimative AM4 UEFI/BIOS/AGESA Übersicht",
            colour=0xE74C3C,
            url="https://www.hardwareluxx.de/community/threads/ultimative-am4-uefi-bios-agesa-%C3%9Cbersicht-17-02-19.1228903/",
            description="Anbei findet ihr eine UEFI/BIOS Übersicht mit den jeweils aktuellsten Versionen, sortiert nach aktuellem AGESA Stand. Sollte mal eine Version fehlen oder ihr einen Fehler findet, dann dürft ihr das hier gerne mitteilen.",
        )

        embed.set_image(url="https://i.imgur.com/ytFxJ9B.png")
        embed.set_thumbnail(url="https://i.imgur.com/6wqgd4K.png")
        embed.set_author(
            name="Reous (Mr. AMD)",
            url="https://www.hardwareluxx.de/community/members/reous.55847/",
            icon_url="https://i.imgur.com/ArBeYmq.png",
        )
        embed.set_footer(text="Channel: <#578340164187979796>")
        await ctx.send(embed=embed)


class cpu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cpu(self, ctx):
        """Link zu dem Community CPU und Bios Guide"""
        embed = discord.Embed(
            title="CPU und Bios Guide für Ryzen 3000 (und älter)",
            colour=0xE74C3C,
            url="https://www.computerbase.de/forum/threads/cpu-und-bios-guide-fuer-ryzen-3000-und-aelter.1911429/",
            description="Erklärungen sowie Tipps um das beste aus der CPU rauszuholen",
        )

        embed.set_image(url="https://i.imgur.com/jC0K8W8.png")
        embed.set_thumbnail(url="https://i.imgur.com/vVeSNQS.png")
        embed.set_author(
            name="Verangry",
            url="https://www.computerbase.de/forum/members/verangry.798158/",
            icon_url="https://i.imgur.com/mu0em6U.png",
        )
        embed.set_footer(text="Channel: <#612647199737774104>")
        await ctx.send(embed=embed)


class limit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["limits"])
    async def limit(self, ctx):
        """Link zu Hardwareluxx RAM OC und Limit Thread"""
        embed = discord.Embed(
            title="Ryzen RAM OC Thread + Mögliche Limitierungen",
            colour=0xE74C3C,
            url="https://www.hardwareluxx.de/community/threads/ryzen-ram-oc-thread-m%C3%B6gliche-limitierungen.1216557/",
            description="In diesem Thread werde ich Informationen zum Thema RAM OC Allgemein sammeln, sowie nennenswerte Anleitungen oder Threads verlinken. Habt ihr Fragen zum Thema RAM OC oder braucht Hilfe euren RAM zu übertakten, dann seid ihr hier im richtigen Thread. Zögert nicht zu fragen, wir helfen gerne weiter",
        )

        embed.set_image(url="https://i.imgur.com/isFPomg.png")
        embed.set_thumbnail(url="https://i.imgur.com/RZVRV7K.png")
        embed.set_author(
            name="Reous (Mr. AMD)",
            url="https://www.hardwareluxx.de/community/members/reous.55847/",
            icon_url="https://i.imgur.com/ArBeYmq.png",
        )
        embed.set_footer(text="Channel: <#506902038215655424>")
        await ctx.send(embed=embed)


class mainboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["mobo", "motherboard"])
    async def mainboard(self, ctx):
        """Link zum Hardwareluxx AM4 VRM Thread"""
        embed = discord.Embed(
            title="AMD 3rd Gen AM4 Mainboards & VRM Liste (X570, P560, B550, A520, A420)",
            colour=0xE74C3C,
            url="https://www.hardwareluxx.de/community/threads/amd-3rd-gen-am4-mainboards-vrm-liste-x570-p560-b550-a520-a420.1228904/",
            description="Hier dürfen News und Produkte diskutieret, Informationen erfragt und zusammengetragen, technische Fragen gestellt und schließlich auch Erfahrungen mit dem eigenen System ausgetauscht werden. Der Umfang des Threads hängt von eurer Beteiligung ab und eure Unterstützung beim Sammeln von Informationen zur Vervollständigung der Übersicht ist ausdrücklich erbeten.",
        )

        embed.set_image(url="https://i.imgur.com/owYHwzW.jpg")
        embed.set_thumbnail(url="https://i.imgur.com/Motc8J6.png")
        embed.set_author(
            name="emissary42",
            url="https://www.hardwareluxx.de/community/members/emissary42.38573/",
            icon_url="https://i.imgur.com/DcfAykw.png",
        )
        embed.set_footer(text="Channel: <#578340164187979796>")
        await ctx.send(embed=embed)


# TODO


class manual(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["anleitung"])
    async def manual(self, ctx):
        """Link zu dem Community CPU und Bios Guide"""
        embed = discord.Embed(
            title="CPU und Bios Guide für Ryzen 3000 (und älter)",
            colour=0xE74C3C,
            url="https://www.computerbase.de/forum/threads/cpu-und-bios-guide-fuer-ryzen-3000-und-aelter.1911429/",
            description="Erklärungen sowie Tipps um das beste aus der CPU rauszuholen",
        )

        embed.set_image(url="https://i.imgur.com/jC0K8W8.png")
        embed.set_thumbnail(url="https://i.imgur.com/jb4sJxq.png")
        embed.set_author(
            name="Verangry",
            url="https://www.computerbase.de/forum/members/verangry.798158/",
            icon_url="https://i.imgur.com/mu0em6U.png",
        )
        embed.set_footer(text="Channel: <#612647199737774104>")
        await ctx.send(embed=embed)


class ramkit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ramkits", "ram"])
    async def ramkit(self, ctx):
        """Link zu dem Community CPU und Bios Guide"""
        embed = discord.Embed(
            title="CPU und Bios Guide für Ryzen 3000 (und älter)",
            colour=0xE74C3C,
            url="https://www.computerbase.de/forum/threads/cpu-und-bios-guide-fuer-ryzen-3000-und-aelter.1911429/",
            description="Erklärungen sowie Tipps um das beste aus der CPU rauszuholen",
        )

        embed.set_image(url="https://i.imgur.com/jC0K8W8.png")
        embed.set_thumbnail(url="https://i.imgur.com/jb4sJxq.png")
        embed.set_author(
            name="Verangry",
            url="https://www.computerbase.de/forum/members/verangry.798158/",
            icon_url="https://i.imgur.com/mu0em6U.png",
        )
        embed.set_footer(text="Channel: <#612647199737774104>")
        await ctx.send(embed=embed)


class spd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spd(self, ctx):
        """Link zu dem Community CPU und Bios Guide"""
        embed = discord.Embed(
            title="CPU und Bios Guide für Ryzen 3000 (und älter)",
            colour=0xE74C3C,
            url="https://www.computerbase.de/forum/threads/cpu-und-bios-guide-fuer-ryzen-3000-und-aelter.1911429/",
            description="Erklärungen sowie Tipps um das beste aus der CPU rauszuholen",
        )

        embed.set_image(url="https://i.imgur.com/jC0K8W8.png")
        embed.set_thumbnail(url="https://i.imgur.com/jb4sJxq.png")
        embed.set_author(
            name="Verangry",
            url="https://www.computerbase.de/forum/members/verangry.798158/",
            icon_url="https://i.imgur.com/mu0em6U.png",
        )
        embed.set_footer(text="Channel: <#612647199737774104>")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(bios(bot))
    bot.add_cog(cpu(bot))
    bot.add_cog(limit(bot))
    bot.add_cog(mainboard(bot))
    bot.add_cog(manual(bot))
    bot.add_cog(ramkit(bot))
    bot.add_cog(spd(bot))
