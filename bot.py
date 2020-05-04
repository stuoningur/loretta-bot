import os
import datetime

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
owner_id = int(os.getenv("OWNER_ID"))
bot_activity = os.getenv("BOT_ACTIVITY")

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    activity=discord.Game(name=bot_activity),
    case_insensitive=True,
    owner_id=owner_id,
)

bot.tenor = os.getenv("TENOR_API")

bot.remove_command("help")

bot.load_extension("cogs.admin_tools")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.guides")
bot.load_extension("cogs.utilities")
bot.load_extension("cogs.specs")
bot.load_extension("cogs.help")
bot.load_extension("cogs.error_handling")


@bot.event
async def on_ready():
    today = datetime.datetime.now()
    time = today.strftime("%d.%m.%Y %H:%M:%S")
    print(f"{time} - Logged in as {bot.user}")


bot.run(bot_token)
