import discord
from discord.ext import commands

class Modmail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.modmail_db = self.bot.db['modmail']
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if isinstance(message.channel, discord.TextChannel):
            return self.bot.process_commands(message)
        gc_guild = self.bot.get_guild(773042619734687766)
        mm_category = gc_guild.get_channel(831261004260048976)
        channel = await mm_category.create_text_channel(name=str(message.author))
        self.modmail_db.insert({"_id": channel.id, "user": message.author.id})