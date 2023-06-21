import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
OH1 = int(os.getenv("OFFICE_HOURS_1"))
OH2 = int(os.getenv("OFFICE_HOURS_2"))
InstructorLink = os.getenv("INSTRUCTOR_LINK")
CamperLink = os.getenv("CAMPER_LINK")
botTesting = int(os.getenv("BOT_TESTING_CHANNEL"))
botDMs = int(os.getenv("BOT_DM_CHANNEL"))
botID = int(os.getenv("BOT_USER_ID"))

class DirectMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Checks to see if specific member roles are in specific voice channels and
    # when they leave, shoots them a DM
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = before.channel or after.channel
        instructRole = discord.utils.get(member.roles, name="Instructor")
        campRole = discord.utils.get(member.roles, name="Camper")

        # If the member has the `Instructor` role
        if instructRole is not None and instructRole.name == "Instructor":
            if channel.id == OH1:
                if before.channel is not None and after.channel is None: # after leaving the voice channel
                    await member.send("Hi there, it looks like you just finished an Office Hours session in the #office-hours-1 channel.")
                    await member.send(f"Please fill out this form to record your session: {InstructorLink}")
                    await member.send("Thank you!")
            elif channel.id == OH2:
                if before.channel is not None and after.channel is None: # after leaving the voice channel
                    await member.send("Hi there, it looks like you just finished an Office Hours session in the #office-hours-2 channel.")
                    await member.send(f"Please fill out this form to record your session: {InstructorLink}")
                    await member.send("Thank you!")

        # If the member has the `Camper` role
        if campRole is not None and campRole.name == "Camper":
            if channel.id == OH1:
                if before.channel is not None and after.channel is None: # after leaving the voice channel
                    await member.send("Hi there, it looks like you just finished getting help from the instructors in the #office-hours-1 channel.")
                    await member.send(f"Please fill out this form so we know how well we helped you: {CamperLink}")
                    await member.send("Thank you!")
            elif channel.id == OH2:
                if before.channel is not None and after.channel is None: # after leaving the voice channel
                    await member.send("Hi there, it looks like you just finished getting help from the instructors in the #office-hours-2 channel.")
                    await member.send(f"Please fill out this form so we know how well we helped you: {CamperLink}")
                    await member.send("Thank you!")

    # Checks to see if someone DMs the bot
    # If so, it forwards the message to a specific channel and replies to the
    # person who sent the message
    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel): # if the message is a DM
            channel = self.bot.get_channel(botDMs) # get channel to forward message to
            if message.author.id != botID: # make sure we're not forwarding/sending messages when the bot messages
                newMessage = discord.Embed(title=f"New bot DM from `{message.author}`", description=f"{message.content}", timestamp=message.created_at)
                await channel.send(embed=newMessage) # forwards message to channel
                await message.author.send("I am a bot and cannot respond, but I have forwarded your message to the EdASE instructor team.")
        await self.bot.process_commands(message)

async def setup(bot: commands.Bot):
    await bot.add_cog(DirectMessage(bot))
