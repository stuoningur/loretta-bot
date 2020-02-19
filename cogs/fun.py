import json
import random

import discord
import requests
from discord.ext import commands

from bot import tenor_api_key


class magic_ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball", aliases=["magicball"])
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


class google_search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="igfd", aliases=["google"])
    async def google_search(self, ctx, *, search=None):
        """Erstellt einen IGFD Link"""
        search = search.replace(" ", "+")
        search_url = f"http://www.igfd.org/?q={search}"
        await ctx.send(search_url)


class gif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["gifs"])
    async def gif(self, ctx, *, arg):
        """Sucht die Top 10 gifs für das Argument und gibt ein Ergebnis zufällig wieder"""
        lmt = 10
        print(tenor_api_key)
        api_request = requests.get(
            f"https://api.tenor.com/v1/search?q={arg}&key={tenor_api_key}&limit={lmt}"
        )

        gifs = []
        if api_request.status_code == 200:
            top_8gifs = json.loads(api_request.content)
            for gif in top_8gifs["results"]:
                gifs.append(gif["itemurl"])
            if gifs:
                await ctx.send(random.choice(gifs))
            else:
                return
        else:
            return


class why(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["warum"])
    async def why(self, ctx):
        embed = discord.Embed(
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


def setup(bot):
    bot.add_cog(magic_ball(bot))
    bot.add_cog(google_search(bot))
    bot.add_cog(gif(bot))
    bot.add_cog(why(bot))
