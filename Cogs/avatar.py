import discord
from discord.ext import commands
import time


class AvatarCog(commands.Cog, name="avatar command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.slash_command(name = "avatar", description = "Shows the avatar/profile photo of a given user.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def avatar(self, ctx, user:discord.Member = None):
		embed=discord.Embed(title="User Avatar", color=discord.Color.random())
		embed.set_author(name="Dwaakaru", icon_url=f"{self.bot.user.avatar.url}")
		
		if user == None:
			embed.add_field(name="Avatar of:", value=ctx.author.mention, inline = True)
			embed.add_field(name="Requested By:", value=ctx.author.mention, inline = True)
			embed.set_image(url=ctx.author.avatar.url)
			await ctx.respond(embed=embed)
		
		else:
			userAvatarUrl = user.avatar.url
			embed.add_field(name="Avatar of:", value=user.mention, inline = True)
			embed.add_field(name="Requested By:", value=ctx.author.mention, inline = True)
			embed.set_image(url=userAvatarUrl)
			await ctx.respond(embed=embed)
            

def setup(bot:commands.Bot):
	bot.add_cog(AvatarCog(bot))