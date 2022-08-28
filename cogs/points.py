from discord.ext import commands
from config import Config
from utils import jsonio
from utils.api import Api
import discord

jio = jsonio(Config.JSON_FILE_PATH)
api = Api()

class Points(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["score"])
    @commands.guild_only()
    async def points(self, ctx, user: discord.Member = None):
        if user is None:
            person = "You"
            user = ctx.author
        else:
            if not jio.is_reg(str(user.id)):
                embd = discord.Embed(title="Account Not Linked!", color=discord.Color.red(), description=f"{user.mention} account is not linked. Tell them to link their account with **{Config.PREFIX}link**.")
                await ctx.channel.send(embed=embd)
                return
            else:
                person = str(user.name)

        if jio.is_reg(str(ctx.author.id)):
            me = api.get_user(jio.get_user_token(str(user.id))).get("data")
            points = int(me.get("score"))
            if points == 0:
                text = "no"
            else:
                text = f"***{points}***"

            embd = discord.Embed(title="Current Points", color=discord.Color.dark_blue(), description=f"{person} currently have {text} points.")
            await ctx.channel.send(embed=embd)
        else:
            embd = discord.Embed(title="Account Not Linked!", color=discord.Color.red(), description=f"To run this command, link your account with **{Config.PREFIX}link**.")
            await ctx.channel.send(embed=embd)

def setup(client):
	client.add_cog(Points(client))