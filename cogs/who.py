from discord.ext import commands
from config import Config
from utils import jsonio
from utils.api import Api
import discord

jio = jsonio(Config.JSON_FILE_PATH)
api = Api()

class Who(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["who"])
    @commands.guild_only()
    async def whosolved(self, ctx, *args):
        uchal = ' '.join([*args])
        if jio.is_reg(str(ctx.author.id)):
            if len(uchal) != 0:
                chal = api.see_who_solved(jio.get_user_token(str(ctx.author.id))).get("data")
                data = api.get_challenges(jio.get_user_token(str(ctx.author.id)), uchal).get("data")
                if len(data) != 0:
                    solved = list()
                    for u in chal:
                        a = chal.get(u)
                        for v in a.get("solves"):
                            if str(v.get("challenge_id")) == str(data[0].get("id")):
                                solved.append(a.get("name"))
                    if len(solved) != 0:
                        embd = discord.Embed(title=f"Who Solved {uchal}?", description=f"[View all challenges]({Config.CTFD_BASE_URL}/challenges)", color=discord.Color.dark_blue())
                        s = ""
                        for i in solved:
                            s = s + f"{solved.index(i) + 1}. {i}\n"
                        embd.add_field(name="Solved Successfully", value=s)
                        await ctx.channel.send(embed=embd)
                    else:
                        embd = discord.Embed(title="Tough one!", color=discord.Color.dark_blue(), description=f"No one has solved `{uchal}`. Be the first!")
                        await ctx.channel.send(embed=embd)
                else:
                    embd = discord.Embed(title="Error!", color=discord.Color.red(), description=f"`{uchal}` is not a valid challenge. Use **{Config.PREFIX}ctfs** to list all CTFs")
                    await ctx.channel.send(embed=embd)
            else:
                embd = discord.Embed(title="Error!", color=discord.Color.red(), description=f"You must supply a challenge. Ex: `{Config.PREFIX}whosolved pdfcrypt`")
                await ctx.channel.send(embed=embd)
        else:
            embd = discord.Embed(title="Account Not Linked!", color=discord.Color.red(), description=f"To run this command, link your account with **{Config.PREFIX}link**.")
            await ctx.channel.send(embed=embd)

def setup(client):
	client.add_cog(Who(client))