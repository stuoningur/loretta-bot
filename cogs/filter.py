from discord.ext import commands
from googleapiclient.discovery import build


class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.youtbe_api = self.bot.youtube_api

    @commands.Cog.listener()
    async def on_message(self, message):
        channel_msg = message.content
        if "https://www.youtube.com/watch?v=" in channel_msg:
            video_id = channel_msg.replace("https://www.youtube.com/watch?v=", "")
            youtube = build("youtube", "v3", developerKey=self.youtbe_api)
            request = youtube.videos().list(part="snippet", id=video_id)
            response = request.execute()
            channel = response["items"][0]["snippet"]["channelId"]
            if channel == "UCYAg4bYdyqENxEyHUX7t1FA":
                await message.delete()
                await message.channel.send("Der Bauer stinkt")


def setup(bot):
    bot.add_cog(Filter(bot))