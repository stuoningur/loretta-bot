import random

import aiohttp
import disnake
from disnake.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tenor_api = self.bot.tenor

    @commands.command(name="8ball", aliases=["magicball", "loretta"])
    async def magic_ball(self, ctx, *, arg):
        """Gibt eine Magic 8 Ball Antwort auf eine Frage"""
        responses = [
            "Das ist sicher.",
            "Es ist entschieden.",
            "Ohne Zweifel.",
            "Ja - definitiv.",
            "Du kannst dich darauf verlassen.",
            "So wie ich das sehe, ja.",
            "Höchstwahrscheinlich.",
            "Die Aussichten sind gut.",
            "Ja.",
            "Die Anzeichen deuten auf ein Ja.",
            "Antwort verschwommen - Versuch es noch einmal.",
            "Frage später noch einmal.",
            "Sage es dir besser nicht jetzt.",
            "Vorhersage jetzt nicht möglich.",
            "Konzentriere dich und frag noch einmal.",
            "Verlass dich nicht darauf.",
            "Meine Antwort ist nein.",
            "Meine Quellen sagen nein.",
            "Die Aussichten sind nicht so gut.",
            "Sehr zweifelhaft.",
        ]
        await ctx.send(f"Frage: {arg}\nAntwort: {random.choice(responses)}")

    @commands.command(aliases=["warum"])
    async def why(self, ctx):
        """Erklärt den Namen des Bots"""
        embed = disnake.Embed(
            title="Das Leben des Brian",
            colour=0xE74C3C,
            url="https://www.youtube.com/watch?v=GryQiamGxpY",
            description="Das Leben des Brian ist eine beißende Persiflage auf die schwülstigen Hollywood-Verfilmungen von Bibelthemen vorangegangener Jahre und karikiert auch viele gesellschaftliche Phänomene wie beispielsweise religiösen oder politischen Fanatismus.",
        )

        embed.set_image(url="https://i.imgur.com/oJfFnzj.png")
        embed.set_thumbnail(url="https://i.imgur.com/BmHab8v.png")
        embed.set_author(
            name="Monty Python",
            url="https://de.wikipedia.org/wiki/Monty_Python",
            icon_url="https://i.imgur.com/1l78cyO.jpg",
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["gifs"])
    async def gif(self, ctx, *, arg):
        """Sucht die Top 10 gifs für das Argument und gibt ein Ergebnis zufällig wieder"""
        lmt = 30
        async with aiohttp.ClientSession() as session:
            url = f"https://api.tenor.com/v1/search?q={arg}&key={self.tenor_api}&limit={lmt}"
            async with session.get(url) as api_request:
                gifs = []
                top_8gifs = await api_request.json()
                for gif in top_8gifs["results"]:
                    gifs.append(gif["itemurl"])
                if gifs:
                    await ctx.send(random.choice(gifs))
                else:
                    return

    @commands.command(name="igfd", aliases=["google"])
    async def google_search(self, ctx, *, arg=None):
        """Erstellt einen IGFD Link"""
        arg = arg.replace(" ", "+")
        search_url = f"https://de.lmgtfy.app/?q={arg}"
        await ctx.send(search_url)

    @commands.command(name="geizhals", aliases=["gh"])
    async def geizhals_search(self, ctx, *, arg=None):
        """Erstellt einen Geizhals Such Link"""
        arg = arg.split("\n")[0].replace(" ", "+")
        search_url = f"https://geizhals.de/?fs={arg}"
        await ctx.send(search_url)

    @commands.command(name="sgehdn")
    async def sgehdn(self, ctx):
        """sgehdn"""
        await ctx.send("https://tenor.com/view/sgehdn-hi-hello-wave-greet-gif-17067641")

    @commands.command(name="ud", aliases=["urban", "urbandictionary"])
    async def urban_dictionary(self, ctx, *, arg=None):
        """Erstellt einen urban dictionary Link"""
        arg = arg.replace(" ", "%20")
        search_url = f"https://www.urbandictionary.com/define.php?term={arg}"
        await ctx.send(search_url)

    @commands.command(name="schmutz")
    async def schmutz(self, ctx):
        """schmutz"""
        await ctx.send(
            "https://tenor.com/view/schmutz-dirt-filth-write-word-gif-16247714"
        )

    @commands.command(name="random")
    async def random(self, ctx, *, arg):
        """random"""
        random_cap = "".join(random.choice((str.upper, str.lower))(c) for c in arg)

        await ctx.send(random_cap)

    @commands.command(name="down")
    async def downjustforme(self, ctx, *, arg=None):
        """Erstellt einen IGFD Link"""
        arg = arg.replace(" ", "+")
        search_url = f"https://downforeveryoneorjustme.com/{arg}"
        await ctx.send(search_url)


def setup(bot):
    bot.add_cog(Fun(bot))
