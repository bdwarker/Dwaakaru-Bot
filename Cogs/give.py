import discord
from discord.ext import commands
import time
import os
from dotenv import load_dotenv
from firebase import firebase
import asyncio
load_dotenv()
db = str(os.environ['databaseURL'])
class giveCog(commands.Cog, name="give command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.slash_command(name="give",
                            usage="",
                            description="Give a player a certian ammount of coins.")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def give(self, ctx, ammount, member:discord.Member):
        fb = firebase.FirebaseApplication(db, None)
        try:
            if member.id == ctx.author.id:
                await ctx.respond("You can't send your own money to yourself!")
            if not member.bot:
                userBalance = fb.get(f'/users/{ctx.author.id}', 'balance')
                memBalance = fb.get(f'/users/{member.id}', 'balance')
                if int(ammount) <= int(userBalance):
                    fb.put(f'/users/{ctx.author.id}', name='balance', data=str(int(userBalance) - int(ammount)))
                    fb.put(f'/users/{member.id}', name='balance', data=str(int(memBalance) + int(ammount)))
                    newUserBalance = fb.get(f'/users/{ctx.author.id}', 'balance')
                    newMemBalance = fb.get(f'/users/{member.id}', 'balance')
                    await ctx.send(f"{ctx.author.mention} has given {member.mention} {ammount} coins. {ctx.author.mention}'s new balance is {str(newUserBalance)}. {member.mention}'s new balance is {str(newMemBalance)}.")
                else:
                    await ctx.respond("C'mon! You can't give what you don't have!")
            else:
                await ctx.respond("You can't send money to a bot!")

        except:
            await ctx.respond("You or the other person does not have an account!")
def setup(bot: commands.Bot):
    bot.add_cog(giveCog(bot))
