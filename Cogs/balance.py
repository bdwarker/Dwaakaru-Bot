import discord
from discord.ext import commands
import time
import os
from dotenv import load_dotenv
from firebase import firebase
load_dotenv()
db = str(os.environ['databaseURL'])
class BalanceCog(commands.Cog, name="balance command"):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.slash_command(name="balance",
                            usage="",
                            description="Displays your balance.")
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def balance(self, ctx, member: discord.Member = None):
        fb = firebase.FirebaseApplication(db, None)
        if member is None:
            try:
                result = fb.get(f'/users/{ctx.author.id}', 'balance')
                await ctx.respond(f'You currently have {result} coins in your account!')
            except:
                await ctx.respond('Please create an account by running the command `/create`')
        else:
            try:
                result = fb.get(f'/users/{member.id}', 'balance')
                await ctx.respond(f'You currently have {result} coins in your account!')
            except:
                await ctx.respond('The mentioned user does not have an account.')

def setup(bot: commands.Bot):
    bot.add_cog(BalanceCog(bot))
