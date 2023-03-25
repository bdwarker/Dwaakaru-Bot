import discord
from discord.ext import commands
import time


class HelloCog(commands.Cog, name="hello command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.slash_command(name = "hello",
					usage="",
					description = "Says hello to the user.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def hello(self, ctx):
		await ctx.respond("Halooo!")

def setup(bot:commands.Bot):
	bot.add_cog(HelloCog(bot))