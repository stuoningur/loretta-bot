import os

import discord
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")


client.run(os.getenv("BOT_TOKEN"))
