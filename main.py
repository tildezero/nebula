import discord
from discord.ext import commands
from utils.bot import Bot
import json


bot = Bot()

with open('config.json', 'r', encoding='utf8') as file:
    bot.config = json.load(file)

bot.load_cogs()

bot.run(bot.config['token'])