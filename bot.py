# Made by alex-dukas 2022
from datetime import datetime
from discord.ext import commands
from config import Config
from time import strftime
import discord
from urllib.parse import urlparse

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=Config.PREFIX, intents=intents)
bot.remove_command('help')

# load cogs
cogs = [
    "cogs.points",
    "cogs.link",
    "cogs.help",
    "cogs.leaderboard",
    "cogs.event",
    "cogs.challenges",
    "cogs.who",
    "cogs.tools"
]

for cog in cogs:
    bot.load_extension(cog)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name=urlparse(Config.CTFD_BASE_URL).netloc))
    print(f"Logged in as {bot.user} at {str(datetime.now().strftime('%A, %B %e, %Y at %I:%M %p'))}")

if __name__ == '__main__':
    bot.run(Config.TOKEN)
