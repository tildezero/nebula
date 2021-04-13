import asyncio
import discord
from discord.ext import commands


class Modmail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.modmail_db = self.bot.db['modmail']
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if not isinstance(message.channel, discord.DMChannel):
            return
        if message.author == self.bot.user:
            return
        gc_guild = self.bot.get_guild(773042619734687766)
        mm_category = gc_guild.get_channel(831261004260048976)
        data = await self.modmail_db.find({"user": message.author.id}).to_list(1000)
        if not data == []:
            thread = data[0]
            channel = gc_guild.get_channel(thread['_id'])
            await channel.send(f"**{str(message.author)}**: {message.content}")
        else:
            await message.author.send("Your modmail thread has been created! Please wait patiently while a mod comes to your ticket")
            channel = await mm_category.create_text_channel(name=str(message.author))
            self.modmail_db.insert_one({"_id": channel.id, "user": message.author.id})

    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=['r'])
    async def reply(self, ctx, *, message):
        if not ctx.channel.category_id == 831261004260048976:
            return await ctx.send("not a modmail category!")
        data = await self.modmail_db.find({"_id": ctx.channel.id}).to_list(100)
        person = data[0]
        user = self.bot.get_user(person['user'])
        await user.send(f"**{str(ctx.author)}**: {message}")
        await ctx.send(f"**{str(ctx.author)}**: {message}")
    
    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=['ar'])
    async def anonreply(self, ctx, *, message):
        if not ctx.channel.category_id == 831261004260048976:
            return await ctx.send("not a modmail category!")
        data = await self.modmail_db.find({"_id": ctx.channel.id}).to_list(100)
        person = data[0]
        user = self.bot.get_user(person['user'])
        await user.send(f"**Staff**: {message}")
        await ctx.send(f"**[Anon] {str(ctx.author)}**: {message}")
    
    @commands.has_permissions(manage_messages=True)
    @commands.command(aliases=['cl'])
    async def close(self, ctx, *, reason=None):
        if not ctx.channel.category_id == 831261004260048976:
            return await ctx.send("not a modmail category!")
        mm_log_channel = ctx.guild.get_channel(831343682169864213)
        fetch = await self.modmail_db.find({"_id": ctx.channel.id}).to_list(10)
        data = fetch[0]
        embed = discord.Embed(title="Modmail Thread Closed", description=f"Channel ID: {ctx.channel.id}\nUser: {data['user']}\nResponsible: {str(ctx.author)}\nReason: {reason}")
        embed.colour = discord.Colour.red()
        await mm_log_channel.send(embed=embed)
        await ctx.send("Closing this channel in 5 seconds!")
        await asyncio.sleep(5)
        await self.modmail_db.delete_many({"_id" : data['_id']})
        await ctx.channel.delete()
    
def setup(bot):
    bot.add_cog(Modmail(bot))