import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
owner_id = int(os.getenv("OWNER_ID"))
bot_activity = os.getenv("BOT_ACTIVITY")
tenor_api_key = os.getenv("TENOR_API")

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    activity=discord.Game(name=bot_activity),
    case_insensitive=True,
    owner_id=owner_id,
)

bot.load_extension("cogs.admin_tools")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.guides")
bot.load_extension("cogs.utilities")
# bot.load_extension("cogs.specs")


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


bot.run(bot_token)
