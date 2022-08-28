from discord.ext import commands
from config import Config
import discord

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        PREFIX = Config.PREFIX
        embd = discord.Embed(title="Help Is on the Way!", color=discord.Color.dark_blue(), description=f"[View site here]({Config.CTFD_BASE_URL}/)")
        embd.add_field(name=f"**Ping**\n`{PREFIX}ping`", value="*Shows delay between client and server.*\n", inline=False)
        embd.add_field(name=f"**Points**\n`{PREFIX}points [@person]`", value="*Shows the current amount of points you have or someone else has.*\n", inline=False)
        embd.add_field(name=f"**Link Accounts**\n`{PREFIX}link`", value=f"*Links a* ***{Config.CTFD_BASE_URL}*** *account to a Discord account.*\n", inline=False)
        embd.add_field(name=f"**Leaderboard**\n`{PREFIX}leaderboard`", value="*Shows current leaderboard.*\n", inline=False)
        embd.add_field(name=f"**Challenges**\n`{PREFIX}challenges`", value="*Shows all challenges/ctfs, and shows what ones you have completed.*\n", inline=False)
        embd.add_field(name=f"**Who Solved?**\n`{PREFIX}whosolved [challange name]`", value="*Shows a list of everyone that solved a specific challenge.*\n", inline=False)
        embd.add_field(name=f"**Swiss Army Knife**\n`{PREFIX}tool [tool_name] [data]`", value="*Various tools that could help. Options for tool: b64e, b64d, urle, urld*\n", inline=False)
        embd.set_footer(text="Made by BSides St. Pete.")
        await ctx.channel.send(embed=embd)

    @commands.command()
    @commands.guild_only()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {round(self.client.latency * 1000)}ms")

def setup(client):
	client.add_cog(Help(client))