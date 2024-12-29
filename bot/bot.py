import os

import discord
from discord.ext import tasks

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Starting SUPER SECRET STALKER")
    print(f"CHANNEL_ID: {CHANNEL_ID}")
    print(f"GUILD_ID: {GUILD_ID}")

    try:
        channel = client.get_channel(CHANNEL_ID)
        if channel is None:
            raise ValueError(f"Channel with ID {CHANNEL_ID} not found.")

        await channel.send(
            "The bot is now online and ready to stalk... I mean, observe! 👀"
        )
        print("Startup message sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the startup message: {e}")


@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return

        if "mew" in message.content.lower():
            await message.channel.send("mew")
    except Exception as e:
        print(f"An error occurred while processing a message: {e}")


client.run(DISCORD_TOKEN)
