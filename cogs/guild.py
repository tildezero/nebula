import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, manage_commands
from utils.utils import calc

class Guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    slash_guilds = [773042619734687766]

    @cog_ext.cog_slash(name="guild", description="Checks if you are in the guild, and gives you the guild member role", options=[manage_commands.create_option(name="username", description="Your username on hypixel", option_type=3, required=True)], guild_ids=slash_guilds)
    async def _guild(self, ctx: SlashContext, username):
        req_player = await self.bot.session.get(f"https://api.slothpixel.me/api/players/{username}")
        res_player = await req_player.json()
        if "error" in res_player:
            return await ctx.send("An error happened! Please check if the username you provided is correct", hidden=True)
        if res_player['links']['DISCORD'] != str(ctx.author):
            return await ctx.send(f"Your Minecraft and Discord accounts are not linked! Please update your discord link on hypixel from {res_player['links']['DISCORD']} to {str(ctx.author)}", hidden=True)
        req_guild = await self.bot.session.get(f"https://api.slothpixel.me/api/guilds/{username}")
        res_guild = await req_guild.json()
        if not res_guild['name'] == "Galaxy Crusaders":
            return await ctx.send(f"You are not in the guild!", hidden=True)
        role = ctx.guild.get_role(828657324877021204)
        await ctx.author.add_roles(role)
        await ctx.send("Welcome to the guild! I have sucessfully added your guild role. Enjoy!", hidden=True)
    
    @commands.has_any_role(828661477606817824,828662244652220436)
    @commands.command(name='addguildrole', aliases=['agr', 'add-guild-role'])
    async def add_guild_role(self, ctx, user: discord.Member):
        """Manually adds the guild role to a user"""
        guild_role = ctx.guild.get_role(828657324877021204) 
        await user.add_roles(guild_role)
        await ctx.send(f"I have added the guild role to {str(user)}!")
    
    @commands.command(name='inguild')
    async def inguild(self, ctx, username: str):
        """Checks if the given username is in the guild"""
        resp = await self.bot.session.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
        if resp.status == 204:
            return await ctx.send("Invalid username!")
        uuid_data = await resp.json()
        uuid = uuid_data['id']
        guild_resp = await self.bot.session.get(f"https://api.slothpixel.me/api/guilds/{uuid}")
        guild_data = await guild_resp.json()
        if guild_data['name'] == "Galaxy Crusaders":
            await ctx.send(f"{uuid_data['name']} is in the guild!")
        else:
            await ctx.send(f"{uuid_data['name']} is not in the guild :(")
            
    @commands.has_role(828662244652220436)
    @commands.command(name="gexpcheck", aliases=['gexp-check'])
    async def gexp_check(self, ctx):
        async with ctx.typing():
            req = await self.bot.session.get(f"https://api.slothpixel.me/api/guilds/zeromomentum?populatePlayers=true")
            res = await req.json()
            ending_string = ""
            for member in res['members']:
                gexp = calc(member['exp_history'])
                if gexp >= 30000:
                    ending_string += f"{member['profile']['username']} has 30k+ gexp ({gexp})\n"
        if len(ending_string) >= 2000:
            hb = await self.bot.session.post("https://hst.sh/documents", datat = ending_string.encode('utf8'))
            url = f"https://hst.sh/{(await hb.json())['key']}"
            return await ctx.send(f"Here is the GEXP overview! {url}")
        else:
            return await ctx.send(ending_string)

        
def setup(bot):
    bot.add_cog(Guild(bot))
