import discord
from discord.ext import commands
import time

class Info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def ping(self, ctx):
    """ Gets the bot's ping """
    before = time.monotonic()
    before_ws = int(round(self.bot.latency * 1000, 1))
    message = await ctx.send("🏓 Pong?")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

def setup(bot):
  bot.add_cog(Info(bot))
