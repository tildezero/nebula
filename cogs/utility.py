import discord
from discord.ext import commands
from discord.flags import alias_flag_value
import ksoftapi

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.kclient = ksoftapi.Client(bot.config['ksoft_token']) 
    
    @commands.command()
    async def vote(self, ctx, *, question: commands.clean_content):
        """ Make a vote to ask people questions """
        await ctx.message.delete()
        pollembed = discord.Embed(title= question, colour = discord.Colour(0x7289da))
        pollembed.set_author(name=f"{ctx.author.name} asks: ")
        pogmessage = await ctx.send(embed=pollembed)
        await pogmessage.add_reaction("\U0001f44d")
        await pogmessage.add_reaction("\U0001f44e")
        await pogmessage.add_reaction("\U0001f90f")
    
    @commands.command()
    async def poll(self, ctx, *, question_and_opts: str):
        """ Vote, but you can have custom options """
        EMOJI = "🇦 🇧 🇨 🇩 🇪 🇫 🇬 🇭 🇮 🇯".split(" ")
        q_opts_split = question_and_opts.split(",")
        question = q_opts_split[0].strip()
        answers = [answer.strip() for answer in q_opts_split[1::]]
        desc = ""
        for num, option in enumerate(answers):
            desc += f"{EMOJI[num]} {option}\n"
        embed = discord.Embed(title=question, colour= discord.Colour(0x7289da), description=desc)
        msg = await ctx.send(embed=embed)
        for i in range(len(answers)):
            await msg.add_reaction(EMOJI[i])
    
    @commands.command(aliases=['ly'])
    async def lyrics(self,ctx, *, query):
        """ Return lyrics for a given song """
        try:
            results = await self.kclient.music.lyrics(query=query,clean_up=True)
        except ksoftapi.NoResults:
            await ctx.send('No lyrics found for ' + query)
        else:
            first = results[0]
            embed = discord.Embed(title = f"Lyrics for {first.name} by {first.artist}", description=first.lyrics)
            embed.set_footer(text="Lyrics provided by KSoft.Si")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Utility(bot))