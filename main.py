import discord
from discord.ext import commands
from utils.bot import Bot
import json
from discord_slash import SlashCommand
import motor.motor_asyncio


bot = Bot()
slash = SlashCommand(bot, override_type = True, sync_commands=True)

with open('config.json', 'r', encoding='utf8') as file:
    bot.config = json.load(file)

bot.load_cogs()

bot.run(bot.config['token'])