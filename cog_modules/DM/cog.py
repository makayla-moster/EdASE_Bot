import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
OH1 = int(os.getenv("OFFICE_HOURS_1"))
OH2 = int(os.getenv("OFFICE_HOURS_2"))
Instructor = os.getenv("INSTRUCTOR_LINK")
Camper = os.getenv("CAMPER_LINK")

class DirectMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = before.channel or after.channel
        if channel.id == OH1:
            if before.channel is None and after.channel is not None:
                print("joined")
                await member.send("hi")
        elif channel.id == OH2:
            if before.channel is None and after.channel is not None:
                print("joined")
                await member.send("hi")

async def setup(bot: commands.Bot):
    await bot.add_cog(DirectMessage(bot))
