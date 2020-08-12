import discord
from discord.ext import commands
from datetime import datetime as d
import os
from run import get_prefix

requested_games = {}

class Request(commands.Cog):
    """
    This command Allows you to request an event, \nit is still in development
    """

    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                       case_insensitive=True)

    @bot.command(name="Request", description="Command to request various events", aliases=["Req"])
    async def Request(self, ctx):
        user = ctx.message.author.id
        await ctx.send("You have requested to add an event!\nWhat Game would we be playing in this event?")
        msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        msg = msg.content
        await ctx.send(f"Sure, we're gonna play {msg}")
        requested_games[msg] = [f'{user}']

    @bot.command(name="Requested", description="Command to see requests", aliases=["Reqd"])
    @commands.has_any_role("Owner", "Co-Owner", "Admin", "Moderator")
    async def Requested(self, ctx):
        embed = discord.Embed(title="Requested Games")
        for y, x in requested_games.items():
            game = str.join("", x)
            embed.add_field(name=f'{y}', value=f'<@{game}>')
        await ctx.send(embed=embed)





def setup(bot):
    bot.add_cog(Request(bot))
