import discord
from discord.ext import commands
import random
from bs4 import BeautifulSoup
from utils.constants import ballresponse


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def fml(self, ctx):
        await ctx.trigger_typing()
        req = await self.bot.session.get("https://www.fmylife.com/random")
        data = await req.text()
        soup = BeautifulSoup(data, "lxml")
        content = soup.find("a", attrs={"class": "article-link"}).text
        await ctx.send(content)

    @commands.command()
    async def topic(self, ctx):
        await ctx.trigger_typing()
        r = await self.bot.session.get("https://conversationstarters.com/generator.php")
        data = r.text()
        soup = BeautifulSoup(r, "lxml")
        div = soup.find("div", attrs={"id": "random"}).text
        await ctx.send(div)
    
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Consult the magical 8ball to receive an answer """
        answer = random.choice(ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")
    
    @commands.command()
    async def gn(self, ctx, user: discord.Member = None):
        """
        Say goodnight to someone
        """
        if user == None:
            await ctx.send(f"{ctx.author.display_name} says goodnight")
        else:
            await ctx.send(f"{ctx.author.display_name} says goodnight to {user.display_name}")

    @commands.command()
    async def gm(self, ctx, user: discord.Member = None):
        """
        Say good morning to someone
        """
        if user == None:
            await ctx.send(f"{ctx.author.display_name} says good morning")
        else:
            await ctx.send(f"{ctx.author.display_name} says good morning to {user.display_name}")

    @commands.command()
    async def ga(self, ctx, user: discord.Member = None):
        """
        Say good afternoon to someone
        """
        if user == None:
            await ctx.send(f"{ctx.author.display_name} says good afternoon")
        else:
            await ctx.send(f"{ctx.author.display_name} says good afternoon to {user.display_name}")

def setup(bot):
    bot.add_cog(Fun(bot))