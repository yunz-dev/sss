import os

import discord
from discord.ext import tasks

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
CHANNEL_ID = os.getenv("CHANNEL_ID")


intents = discord.Intents.default()
intents.presences = True
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Starting SUPER SECRET STALKER")
    print(CHANNEL_ID)
    print(GUILD_ID)


client.run(DISCORD_TOKEN)
