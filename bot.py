import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
owner_id = int(os.getenv("OWNER_ID"))
bot_activity = os.getenv("BOT_ACTIVITY")

client = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    activity=discord.Game(name=bot_activity),
    case_insensitive=True,
    owner_id=owner_id,
)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.command()
@commands.is_owner()
async def shutdown(ctx):
    """Shuts down the bot when the owner send the command"""
    print(f"{client.user} is shutting down")
    await client.logout()


client.run(bot_token)
