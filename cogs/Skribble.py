import discord
from discord.ext import commands
from datetime import datetime as d
import os
from run import get_prefix


class Skribbl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                       case_insensitive=True)

    @bot.command(name="Skribbl", aliases=["Scribble", "Skribble", "Scribbl", "Skribble.io"])
    async def Skribbl(self, ctx, link):
        embed = discord.Embed(title="Skribbl.io!", color=0x50b51b,
                              description="Join our game of Skribbl.io using the link below!!!\n\n\n{}".format(link))
        embed.set_thumbnail(url="https://skribbl.io/res/logo.gif")
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Skribbl(bot))
