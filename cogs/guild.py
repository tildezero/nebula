import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext, manage_commands

class Guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    slash_guilds = [773042619734687766]

    @cog_ext.cog_slash(name="guild", description="Checks if you are in the guild, and gives you the guild member role", options=[manage_commands.create_option(name="username", description="Your username on hypixel", option_type=3, required=True)], guild_ids=slash_guilds)
    async def _guild(self, ctx: SlashContext, username):
        req_player = await self.bot.session.get(f"https://api.slothpixel.me/api/players/{username}")
        res_player = await req_player.json()
        if res_player['links']['DISCORD'] != str(ctx.author):
            return await ctx.send(f"Your Minecraft and Discord accounts are not linked! Please update your discord link on hypixel from {res_player['links']['DISCORD']} to {str(ctx.author)}", hidden=True)
        req_guild = await self.bot.session.get(f"https://api.slothpixel.me/api/guilds/{username}")
        res_guild = await req_guild.json()
        if not res_guild['name'] == "Galaxy Crusaders":
            return await ctx.send(f"You are not in the guild!", hidden=True)
        role = ctx.guild.get_role(828657324877021204)
        await ctx.author.add_roles(role)
        await ctx.send("Welcome to the guild! I have sucessfully added your guild role. Enjoy!", hidden=True)





def setup(bot):
    bot.add_cog(Guild(bot))
