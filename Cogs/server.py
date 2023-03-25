import discord
from discord.ext import commands
import time


class ServerInfoCog(commands.Cog, name="serverinfo command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.slash_command(name="server", description="Gets the server information.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def server(self, ctx):
            name = str(ctx.guild.name)
            description = str(ctx.guild.description)

            owner = str(ctx.guild.owner)
            id = str(ctx.guild.id)
            region = str(ctx.guild.region)
            memberCount = str(ctx.guild.member_count)

            icon = str(ctx.guild.icon_url)

            embed = discord.Embed(
                title=name + " Server Information",
                description=description,
                color=discord.Color.red()
            )
            embed.set_thumbnail(url=icon)
            embed.add_field(name="Owner", value=owner, inline=True)
            embed.add_field(name="Server ID", value=id, inline=True)
            embed.add_field(name="Region", value=region, inline=True)
            embed.add_field(name="Member Count", value=memberCount, inline=True)

            await ctx.respond(embed=embed, mention_author=False)

def setup(bot:commands.Bot):
	bot.add_cog(ServerInfoCog(bot))