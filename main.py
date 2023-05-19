import asyncio
import binarytree
import discord
from discord.ext import commands
from discord import app_commands, Interaction
from dotenv import load_dotenv
import os

# Discord bot initialization
# ---------------------------------------------------------------------------------
# Load variables from the .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DISCORD_PREFIX = os.getenv("PREFIX")
DISCORD_DEV_ID = int(os.getenv('DISCORD_DEV_ID'))

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
    bot = Hivemaster()
    
    # Slash command syncing
    # ======================================================
    
    @bot.command()
    async def localsync(ctx: commands.Context):
        if ctx.author.id != DISCORD_DEV_ID:
            await ctx.reply("`Command failed: missing permission`")
            return
        bot.tree.copy_global_to(guild=ctx.guild)
        await bot.tree.sync(guild=ctx.guild)
        await ctx.reply("Commands synced locally!")
        
    # The Hive Game
    # ======================================================
        
    @bot.tree.command(name="start-game", description="Start a new game of The Hive.")
    async def start_game(interaction: Interaction):
        await interaction.response.send_message("New game started!")
    
    @bot.event
    async def on_ready():
        print(f'Logged into Discord as {bot.user} with prefix {DISCORD_PREFIX}')
    
    print("Starting Hivemaster Discord Bot...")
    async with bot:
        await bot.start(DISCORD_TOKEN)
    
asyncio.run(main())