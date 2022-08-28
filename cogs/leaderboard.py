from discord.ext import commands
from config import Config
from utils import jsonio
from utils.api import Api
import discord
import re

jio = jsonio(Config.JSON_FILE_PATH)
api = Api()

class Lb(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["lb", "top"])
    @commands.guild_only()
    async def leaderboard(self, ctx):
        if jio.is_reg(str(ctx.author.id)):
            ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
            top = api.get_top_10(jio.get_user_token(str(ctx.author.id))).get("data")
            me = api.get_user(jio.get_user_token(str(ctx.author.id))).get("data")
            embd = discord.Embed(title=f"Top 10 by Most Points", description=f"[View full leaderboard]({Config.CTFD_BASE_URL}/scoreboard)", color=discord.Color.dark_blue())
            for i in top:
                pos = i.get("pos")
                if pos == 11:  break
                if pos in [1, 2, 3]:
                    possible = {1:"🥇", 2:"🥈",3:"🥉"}
                    extra = possible.get(pos) + " "
                else:
                    extra = ""
                embd.add_field(name=f"{ordinal(int(pos))} Place", value=f"{extra}[{i.get('name')}]({Config.CTFD_BASE_URL + i.get('account_url')}) - *{i.get('score')}* points", inline=False)

            place = me.get("place")
            if place is None:
                text = "You have not solved any challenges!"
            else:
                text = f"You are in {place} place!"
            embd.set_footer(text=text)
            await ctx.channel.send(embed=embd)
        else:
            embd = discord.Embed(title="Account Not Linked!", color=discord.Color.red(), description=f"To run this command, link your account with **{Config.PREFIX}link**.")
            await ctx.channel.send(embed=embd)

def setup(client):
	client.add_cog(Lb(client))