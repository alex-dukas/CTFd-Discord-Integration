from discord.ext import commands, tasks
from config import Config
from utils import dataio
from utils.api import Api
import discord

dio = dataio(Config.TEMP_DATA_PATH)
api = Api()

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ctfloop.start()

    @tasks.loop(seconds=Config.UPDATE_TIME)
    async def ctfloop(self):
        def diff(li1, li2):
            return list(set(li1) - set(li2)) + list(set(li2) - set(li1))
        
        await self.client.wait_until_ready()

        # check new challanges
        a = []
        chal = api.get_challenges(Config.ADMIN_TOKEN).get("data")
        for c in chal:
            a.append(c.get("name"))
        jchal = dio.read().get("chal_data")
        if len(jchal) != 0:
            d = diff(a, jchal)
            if len(d) != 0:
                channel = self.client.get_channel(int(Config.UPDATE_CHAN_ID))
                for q in d:
                    embd = discord.Embed(title="New challenge released!", color=discord.Color.dark_blue(), description=f"The new challenge **{q}** has been added. Be the first to get the flag!")
                    await channel.send(embed=embd)
                dio.update_chal(a)
        else:
            dio.update_chal(a)

        # check scoreboard
        a = []
        chal = api.get_top_10(Config.ADMIN_TOKEN).get("data")
        for c in chal:
            a.append(c.get("name"))
        a = a[:10]
        jpos = dio.read().get("pos_data")
        if len(jpos) != 0:
            if a != jpos[:10]:
                channel = self.client.get_channel(int(Config.UPDATE_CHAN_ID))
                embd = discord.Embed(title="Change in leaderboard", color=discord.Color.dark_blue(), description=f"There was a change in the top 10, Use **{Config.PREFIX}leaderboard** to see the new leaderboard.")
                await channel.send(embed=embd)
                dio.update_pos(a[:10])
        else:
            dio.update_pos(a[:10])

def setup(client):
	client.add_cog(Events(client))