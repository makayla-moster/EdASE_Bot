import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

class Testing(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="test")
    async def testing(self, ctx: commands.Context):
        response = "Yes, this is working."
        await ctx.send(response)

async def setup(bot: commands.Bot):
    await bot.add_cog(Testing(bot))
