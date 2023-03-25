import discord
from discord.ext import commands
import time
import os
from dotenv import load_dotenv
from firebase import firebase
load_dotenv()
db = str(os.environ['databaseURL'])
class CreateCog(commands.Cog, name="create command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.slash_command(name="create",
                            usage="",
                            description="Creates an economy account.")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def create(self, ctx):
        usrdata = {
            'balance':'5000',
            'checkin':'0'
        }
        fb = firebase.FirebaseApplication(db, None)
        result = fb.put(f'/users/', name=ctx.author.id, data=usrdata)
        await ctx.respond("Account created! You have been given 5000 coins as a gift.")


def setup(bot: commands.Bot):
    bot.add_cog(CreateCog(bot))
