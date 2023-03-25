import discord
from discord.ext import commands
import time
import asyncio
from randomuser import RandomUser

class heckCog(commands.Cog, name="heck command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@discord.slash_command(name="heck", description="Hecks a given user.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def heck(self, ctx, member:discord.Member):
            await ctx.send('Hecking: ' + member.mention)
            await asyncio.sleep(1)
            user = RandomUser()
            irl_name = user.get_full_name()
            user_email = user.get_email()
            pwd = user.get_password()
            dob = user.get_dob()
            embed = discord.Embed(
                title = 'Hecked ' + str(member),
                discription='These are their details:'
            )
            embed.add_field(name='Full Name', value = irl_name, inline=False)
            embed.add_field(name='Email', value = user_email, inline=False)
            embed.add_field(name='Password', value = pwd, inline=False)
            embed.add_field(name='Date Of Birth', value = dob, inline=False)
            await asyncio.sleep(1)
            await ctx.respond(embed = embed, mention_author = False)

def setup(bot:commands.Bot):
	bot.add_cog(heckCog(bot))