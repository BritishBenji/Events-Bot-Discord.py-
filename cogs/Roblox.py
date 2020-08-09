import discord
from discord.ext import commands
from datetime import datetime as d
import os
from run import get_prefix

roblox_users = {
    400912133367529472: "https://www.roblox.com/users/41395787/profile",
    474643611179286549: "https://www.roblox.com/users/877369377/profile",
    201239775582224384: "https://www.roblox.com/users/93627104/profile",
}


class Roblox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                       case_insensitive=True)

    @bot.command(name="Roblox", description="Show's the command callers Username and a Link to their Roblox Account")
    async def Roblox(self, ctx):
        embed = discord.Embed(title="Roblox Games!", color=0x50b51b,
                              description="Join our game of Roblox! \n\nFollow <@{}> into the games! \n\nNeed a link to their profile? It's below!\n\n{}".format(
                                  ctx.author.id, roblox_users.get(ctx.author.id)))
        embed.set_thumbnail(url="https://t5.rbxcdn.com/c9749ac59c201199fc5ec1610dcf7d52")
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Roblox(bot))
