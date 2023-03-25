import discord
from discord.ext import commands
import time
import os
from dotenv import load_dotenv
from firebase import firebase
import asyncio
load_dotenv()
db = str(os.environ['databaseURL'])
class dailyCog(commands.Cog, name="daily command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.slash_command(name="daily",
                            usage="",
                            description="Gives you your daily check-in reward.")
    @commands.cooldown(1, 86400, commands.BucketType.member)
    async def daily(self, ctx):
        fb = firebase.FirebaseApplication(db, None)
        getusr=fb.get(f'/users/{ctx.author.id}', None)
        if getusr != 'None':
            userBalance = fb.get(f'/users/{ctx.author.id}', 'balance')
            userCheckin=fb.get(f'/users/{ctx.author.id}', 'checkin')
            fb.put(f'/users/{ctx.author.id}', name='checkin', data=str(int(userCheckin)+1))
            newCheckin=fb.get(f'/users/{ctx.author.id}', 'checkin')
            fb.put(f'/users/{ctx.author.id}', name='balance', data=str(int(userBalance) + (100 * int(newCheckin))))
            newBalance = fb.get(f'/users/{ctx.author.id}', 'balance')
            await ctx.send(f'<@{ctx.author.id}> recived {(100 * int(newCheckin))} coins! Your current balance is {newBalance}, your check-in streak is {newCheckin}')
        else:
            await ctx.respond('Please create an account by running the command `/create`')
    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond("Sorry! The command is on a cooldown!")
        else:
            raise error  # Here we raise other errors to ensure they aren't ignored

def setup(bot: commands.Bot):
    bot.add_cog(dailyCog(bot))
