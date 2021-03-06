from utils.utils import traceback_maker
import discord
from discord.ext import commands
import importlib


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
            await ctx.send(f"Something happened... \n{traceback_maker(e)}")
        else:
            await ctx.send(f"Sucessfully loaded the cog! ({cog}.py)")

    @commands.command()
    async def load(self, ctx, cog):
        """ Loads the given cog. """
        try:
            self.bot.load_extension(f"cogs.{cog}")
        except Exception as e:
            await ctx.send(f"Something happened... \n```py\n{traceback_maker(e)}\n```")
        else:
            await ctx.send(f"Sucessfully loaded the cog! ({cog}.py)")

    @commands.command()
    async def unload(self, ctx, cog):
        """ Unloads the given cog. """
        try:
            self.bot.unload_extension(f"cogs.{cog}")
        except Exception as e:
            await ctx.send(f"Something happened... \n{traceback_maker(e)}")
        else:
            await ctx.send(f"Sucessfully unloaded the cog! ({cog}.py)")

def setup(bot):
    bot.add_cog(Owner(bot))