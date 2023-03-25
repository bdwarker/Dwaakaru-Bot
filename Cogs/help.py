import discord
from discord.ext import commands
from random import randint

class HelpCog(commands.Cog, name="help command"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
  

	@commands.slash_command(name = 'help',
					usage="(commandname)",
					description = "Display the help message.",
					aliases = ['h', '?'])
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def help (self, ctx):
		print("add something")

def setup(bot:commands.Bot):
	bot.remove_command("help")
	bot.add_cog(HelpCog(bot))
