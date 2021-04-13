from discord.ext import commands
import discord
import aiohttp
import os
import motor.motor_asyncio
import json


class Bot(commands.Bot):
    """subclassed commands.Bot because people do this"""
    def __init__(self, *args, **kwargs):
        print("starting up...")

        intents = discord.Intents.default()
        intents.members = True

        super().__init__(
            command_prefix=".", 
            intents=intents, 
            allowed_mentions = discord.AllowedMentions(everyone=False,roles=False, replied_user=False)
        )
        with open ("config.json", "r") as file:
            self.config = json.load(file)

        self.session = aiohttp.ClientSession()
        self.mongo = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://zero:CGyaGGVid4dFRg@nebula.hfwq2.mongodb.net/bot?retryWrites=true&w=majority")
        self.db = self.mongo['bot']

    
    async def on_connect(self):
        print("connected!")
    
    async def on_ready(self):
        print(f"bot ready as {self.user}")
    
    def load_cogs(self):
        for file in os.listdir("cogs"):
            if file.endswith('.py'):
                cog_name = file[:-3]
                self.load_extension(f"cogs.{cog_name}")
        self.load_extension("jishaku")
        print("loaded cogs!")
