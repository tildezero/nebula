import discord
from discord.ext import commands
import importlib

from discord.ext.commands.core import command

class Owner(commands.Cog):
    """ Commands for the bot owner to use. """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.is_owner()
    @commands.command()
    async def reload(self, ctx, cog):
        """ Reloads the given cog. """
        try:
            self.bot.reload_extension(f"cogs.{cog}")
        except Exception as e:
            await ctx.send(f"Something happened... \n```py\n{e.__traceback__}\n```")

def setup(bot):
    bot.add_cog(Owner(bot))