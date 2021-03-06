import discord
from discord.ext import commands
import ksoftapi
from utils.utils import chunks
from utils.constants import ballresponse, zws
from urllib.parse import quote_plus

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.kclient = ksoftapi.Client(bot.config['ksoft_token']) 
    
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
    
    # @commands.command(aliases=['ly_ks'])
    # async def lyrics_ksoft(self,ctx, *, query):
    #     """ Return lyrics for a given song """
    #     try:
    #         results = await self.kclient.music.lyrics(query=query,clean_up=True)
    #     except ksoftapi.NoResults:
    #         await ctx.send('No lyrics found for ' + query)
    #     else:
    #         first = results[0]
            # embed = discord.Embed(title = f"Lyrics for {first.name}", description=first.artist)
            # embed.set_footer(text="Lyrics provided by KSoft.Si")
            # lyrics_list = list(chunks(first.lyrics, 1000))
            # for ly in lyrics_list:
            #     embed.add_field(name=zws, value=ly, inline=False)
            # await ctx.send(embed=embed)

    @commands.command(aliases=['ly'])
    async def lyrics(self, ctx, *, song):
        data = await self.bot.session.get(f"https://some-random-api.ml/lyrics?title={quote_plus(song)}")
        song = await data.json()
        embed = discord.Embed(title = f"Lyrics for {song['title']}", description=song['author'])
        embed.set_footer(text="Lyrics provided by some-random-api")
        lyrics_list = list(chunks(song['lyrics'], 1000))
        for ly in lyrics_list:
            embed.add_field(name=zws, value=ly, inline=False)
        await ctx.send(embed=embed)
        
            
            
                    


def setup(bot):
    bot.add_cog(Utility(bot))