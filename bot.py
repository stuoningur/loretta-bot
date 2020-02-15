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
)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.command()
async def shutdown(ctx):
    """Shuts down the bot when the owner send the command"""
    if ctx.message.author.id == owner_id:
        print("Bot is shutting down")
        await client.logout()


client.run(bot_token)
