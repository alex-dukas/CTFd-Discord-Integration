from discord.ext import commands
from config import Config
from utils import jsonio

jio = jsonio(Config.JSON_FILE_PATH)

class Link(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def link(self, ctx):
        def msg_check(message):
            if len(message.content) == 64 and message.author.id == ctx.author.id:
                return True
            else:
                return False

        if not jio.is_reg(str(ctx.author.id)):
            await ctx.author.send(f"**How to link** `{Config.CTFD_BASE_URL}` **account to a Discord account**\n\n1. Make an account at {Config.CTFD_BASE_URL}/register. If you're already registerd, login at {Config.CTFD_BASE_URL}/login.\n2. Navigate to {Config.CTFD_BASE_URL}/settings#tokens. Then, click `Generate`.\n3. Copy your API key, then paste it below in this DM (with nothing else).")
            msg = await self.client.wait_for('message', check=msg_check)
            jio.new_token(str(ctx.author.id), str(msg.content))
            await ctx.author.send("**Account successfully linked!**")
        else:
              await ctx.channel.send("**Account already linked!**")

def setup(client):
	client.add_cog(Link(client))