import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        welcome_channel = member.guild.get_channel(773042620309700610)
        if member.bot:
            return
        embed = discord.Embed(title="Welcome!", description=f"Welcome to the server, {str(member)}! Please be sure to read the <#773046261213429791>, and enjoy your stay here! We are now at {member.guild.member_count} members.")
        embed.colour = discord.Colour.teal()
        await welcome_channel.send(content=member.mention, embed=embed)
    
def setup(bot):
    bot.add_cog(Events(bot))