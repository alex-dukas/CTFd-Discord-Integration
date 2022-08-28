from discord.ext import commands
from config import Config
from utils import jsonio
from utils.api import Api
import discord

jio = jsonio(Config.JSON_FILE_PATH)
api = Api()

class Challenges(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["c", "ctfs"])
    @commands.guild_only()
    async def challenges(self, ctx):
        if jio.is_reg(str(ctx.author.id)):
            chal = api.get_challenges(jio.get_user_token(str(ctx.author.id))).get("data")
            group = dict()
            for c in chal:
                if c.get("category") not in group:
                    group.update({c.get("category"):[c]})
                else:
                    group.get(c.get("category")).append(c)

            embd = discord.Embed(title=f"All Challenges", description=f"[View all challenges]({Config.CTFD_BASE_URL}/challenges)", color=discord.Color.dark_blue())
            total = 0
            total_solved = 0
            for g in group:
                crn = list()
                solved = 0
                s = ""
                for h in group.get(g):
                    if h.get("solved_by_me"):
                        solved += 1
                    crn.append({"id": h.get("id"), "name": h.get("name"), "points": h.get("value"), "sbm": h.get("solved_by_me")})
                for i in crn:
                    extra = ""
                    if i.get("sbm"):
                        extra = "✅"
                    s = s + f"{crn.index(i) + 1}. {extra} {i.get('name')} - *{i.get('points')}* points\n"
                
                total_solved += solved
                total += len(crn)
                embd.add_field(name=f"{g} ({solved}/{len(crn)})", value=s, inline=False)

            embd.set_footer(text=f"You have solved ({total_solved}/{total})")
            await ctx.channel.send(embed=embd)
        else:
            embd = discord.Embed(title="Account Not Linked!", color=discord.Color.red(), description=f"To run this command, link your account with **{Config.PREFIX}link**.")
            await ctx.channel.send(embed=embd)

def setup(client):
	client.add_cog(Challenges(client))