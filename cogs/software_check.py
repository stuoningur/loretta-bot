from discord.ext import tasks, commands
import feedparser
import datetime
import discord


class SoftwareCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.software_check.start()

    @tasks.loop(minutes=1.0)
    async def software_check(self):
        channel = self.bot.get_channel(675451281690722330)
        rss_feed = feedparser.parse("https://www.computerbase.de/rss/downloads.xml")
        entries = rss_feed.entries
        keywords = [
            "aida64",
            "hwinfo",
            "capframex",
            "ryzen master",
            "cpu-z",
            "gpu-z",
            "afterburner",
        ]
        for entry in entries:
            if any(keyword in entry.title.lower() for keyword in keywords):
                time_now = datetime.datetime.now()
                published_date = entry.published[:-6]
                published_date_cleaned = datetime.datetime.strptime(
                    published_date, "%Y-%m-%dT%H:%M:%S"
                )
                time_offset = datetime.timedelta(hours=100)
                checked_time = time_now - time_offset
                added_date = published_date_cleaned.strftime("%d.%m.%Y %H:%M")

                if checked_time <= published_date_cleaned <= time_now:
                    print(entry.title)
                    embed = discord.Embed(
                        title=entry.title,
                        colour=0xE74C3C,
                        url=entry.link,
                        description=entry.summary,
                    )
                    embed.set_footer(text=f"Hinzugefügt am: {added_date}")
                    await channel.send(embed=embed)

    @software_check.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(SoftwareCheck(bot))