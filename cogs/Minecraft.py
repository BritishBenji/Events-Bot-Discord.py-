import discord
from discord.ext import commands
from datetime import datetime as d
import os
from run import get_prefix


class Minecraft(commands.Cog):
    """
    This Command allows you to tell people you're\nrunning a Minecraft Event!
    """
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                       case_insensitive=True)

    @bot.command(name="Minecraft")
    async def Minecraft(self, ctx, ip):
        """
        Follow the Command with an IP address \nto show the IP in your announcement!
        """
        embed = discord.Embed(title='Minecraft Games Night!', color=0x50b51b,
                              description=f'Join our game of Minecraft!\n\n**IP = {ip}**')
        embed.set_thumbnail(
            url='https://theme.zdassets.com/theme_assets/2155033/bc270c23058d513de5124ffea6bf9199af7a2370'
                '.png')
        embed.set_image(url='https://www.logaster.com/blog/wp-content/uploads/2020/06/image14-3.png')
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Minecraft(bot))