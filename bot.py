import datetime
from os import environ

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot_token = environ.get("BOT_TOKEN")
owner_id = int(environ.get("OWNER_ID"))
bot_activity = environ.get("BOT_ACTIVITY")
intents = disnake.Intents().all()

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    activity=disnake.Game(name=bot_activity),
    case_insensitive=True,
    owner_id=owner_id,
    intents=intents,
)

bot.remove_command("help")

bot.tenor = environ.get("TENOR_API")
bot.youtube_api = environ.get("YOUTUBE_API")
bot.stock_channel = environ.get("STOCK_CHANNEL")
bot.nvidia_url = environ.get("NVIDIA_URL")
bot.owm_key = environ.get("OWM_API")
bot.log_channel = environ.get("LOG_CHANNEL")


@bot.event
async def on_ready():
    today = datetime.datetime.now()
    time = today.strftime("%d.%m.%Y %H:%M:%S")
    print(f"{time} - Logged in as {bot.user}")


bot.load_extensions("cogs")

bot.run(bot_token)
