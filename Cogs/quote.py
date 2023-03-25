import dependencies.quote as quotes
import discord
from discord.ext import commands
import time


class QuoteCog(commands.Cog, name="quote command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.slash_command(name="quote", description="Tells a random quote. As a wise old man once said...")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def heck(self, ctx):
		embed=discord.Embed(title="Quote", description="Get ready to be inspired!", color=0x750000)
		embed.set_author(name="Dwaakaru", icon_url=f"{self.bot.user.avatar.url}")
		quote=quotes.get_quote()
		embed.add_field(name="Quote", value = quote['content'], inline=False)
		embed.add_field(name="Author", value=quote['originator']['name'], inline=False)
		await ctx.respond(embed=embed, mention_author=False)

def setup(bot:commands.Bot):
	bot.add_cog(QuoteCog(bot))