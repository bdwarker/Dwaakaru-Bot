import discord
from discord.ext import commands
import time


class statsCog(commands.Cog, name="stats command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.slash_command(name="stats", description="I am telling you, this bot has a 90 KDR.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def stats(self, ctx):
		mems = 0
		gids = 0
		for guild in self.bot.guilds:
			for members in guild.members:
				mems += 1
			gids += 1
		embed=discord.Embed(title="Dwaakaru Stats", description="Stats of the discord bot.")
		embed.set_author(name="Dwaakaru", icon_url=f'{self.bot.user.avatar.url}')
		embed.set_thumbnail(url=f'{self.bot.user.avatar.url}')
		embed.add_field(name="Users", value=f"{mems}", inline=False)
		embed.add_field(name="Servers", value=f"{gids}", inline=False)
		embed.add_field(name="Pycord Version", value=f"{discord.__version__}", inline=False)
		await ctx.send(embed=embed)

def setup(bot:commands.Bot):
	bot.add_cog(statsCog(bot))