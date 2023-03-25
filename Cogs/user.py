import discord
from discord.ext import commands
import time


class UserInfoCog(commands.Cog, name="userinfo command"):
	def __init__(self, bot:commands.bot):
		self.bot = bot
        
	@commands.slash_command(name="user", description="Gets the information about the specified user.")
	@commands.cooldown(1, 2, commands.BucketType.member)
	async def userinfo(self, ctx, member:discord.Member=None):
            if member == None:
                member = ctx.message.author
            embed=discord.Embed(
            title="User Information", 
            colour=discord.Colour.random()
            )
            embed.set_thumbnail(url=member.avatar.url)
            embed.add_field(name="Name", value=member.name)
            embed.add_field(name="Nickname", value=member.nick)
            embed.add_field(name="ID", value=member.id)
            embed.add_field(name="Account Created",value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"))
            embed.add_field(name="Joined",value=member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC"))
            members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
            embed.add_field(name="Join Position", value=str(members.index(member)+1))
            await ctx.respond(embed=embed, mention_author=False)

def setup(bot:commands.Bot):
	bot.add_cog(UserInfoCog(bot))