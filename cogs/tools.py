from discord.ext import commands
from config import Config
from utils import jsonio
import discord
import base64
import urllib.parse

jio = jsonio(Config.JSON_FILE_PATH)

class Tools(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def tool(self, ctx, tool=None, *args):
        if jio.is_reg(str(ctx.author.id)):
            data = str(' '.join([*args]))
            if tool != None and tool.lower() in ["b64e", "b64d", "urle", "urld", "whathash"] and len(data) != 0:
                tool = tool.lower()
                if tool == "b64e":
                    out = base64.urlsafe_b64encode(data.encode('UTF-8')).decode('ascii')
                elif tool == "b64d":
                    out = base64.urlsafe_b64decode(data.encode('UTF-8')).decode('ascii')
                elif tool == "urle":
                    out = urllib.parse.quote(data, safe="")
                elif tool == "urld":
                    out = urllib.parse.unquote(data)
                elif tool == "whathash":
                    pass
                    # coming soon
                embd = discord.Embed(title="Output", description=out, color=discord.Color.dark_blue())
                await ctx.channel.send(embed=embd)
            else:
                embd = discord.Embed(title="Oops!", color=discord.Color.red(), description=f"You need to provide a valid tool. Use **{Config.PREFIX}help** for help.")
                await ctx.channel.send(embed=embd)
        else:
            embd = discord.Embed(title="Account Not Linked!", color=discord.Color.red(), description=f"To run this command, link your account with **{Config.PREFIX}link**.")
            await ctx.channel.send(embed=embd)

def setup(client):
	client.add_cog(Tools(client))