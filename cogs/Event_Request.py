import discord
from discord.ext import commands
from datetime import datetime as d
import os
from run import get_prefix


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
        await ctx.send("You have requested to add an event!\nWhat Game would we be playing in this event?")


def setup(bot):
    bot.add_cog(Request(bot))
