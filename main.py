import asyncio
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os

# Discord bot initialization
# ---------------------------------------------------------------------------------
# Load variables from the .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_PREFIX = os.getenv("PREFIX")

class Hivemaster(commands.Bot):
    
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(
            command_prefix=DISCORD_PREFIX,
            intents=intents,
            activity=discord.Game("The Hive!"),
            status=discord.Status.online
        )
        

        
async def main():
    h = Hivemaster()
    
    @h.event
    async def on_ready():
        print(f'Logged into Discord as {h.user}.')
    
    print("Starting Hivemaster Discord Bot...")
    async with h:
        await h.start(DISCORD_TOKEN)
    
asyncio.run(main())