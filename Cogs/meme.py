import discord
from discord.ext import commands
import time
import aiohttp
import random
class MemeCog(commands.Cog, name="meme command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.slash_command(name="meme", description="Shows a random meme from r/memes.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def meme(self, ctx):
            async with aiohttp.ClientSession() as cs:
                    async with cs.get('https://www.reddit.com/r/memes/hot.json') as r:
                        res = await r.json()
                        embed = discord.Embed(title="Meme", color = ctx.author.color)
                        embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                        await ctx.respond(embed=embed, content=None)

def setup(bot:commands.Bot):
	bot.add_cog(MemeCog(bot))