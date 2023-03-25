import dependencies.quote as quotes
import discord
from discord.ext import commands
import time
import dependencies.apod as apod

class SpaceImageCog(commands.Cog, name="Space Image command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.slash_command(name="space", description="Gets the space image of the day.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def space(self, ctx):
            img = apod.getAPOD()
            embed = discord.Embed(title="Space image of the day.", color=discord.Color.red())
            img_url = img['url']
            embed.set_author(name="Erased",icon_url=f"{self.bot.user.avatar.url}")
            embed.set_thumbnail(url='https://assets.materialup.com/uploads/2979c2d8-d5dd-4576-8f4c-40133f4d324c/preview.jpg')
            embed.add_field(name="Title", value=img['title'], inline=False)
            embed.set_image(url=img['url'])
            embed.add_field(name="URL", value='[Click here]('+ img_url + ')', inline=False)
            await ctx.respond(embed=embed, mention_author=False)

def setup(bot:commands.Bot):
	bot.add_cog(SpaceImageCog(bot))