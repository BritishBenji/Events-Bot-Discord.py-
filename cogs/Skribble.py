# Eyyyyyyy, Skribbl command go brrrrrrr. Had to physically add the name to my dictionary cause my IDE wouldn't
# leave me alone about it being misspelled
import discord
from discord.ext import commands
from run import get_prefix


# TODO: Add in descriptions for the help command, cause it doesn't like command descriptions, only event descriptions
# I still don't regret stealing the code for Help.py though, I really don't

# Class initialisation, if you're here to edit the bot and add new bits,
# just make sure this bit is here, and the bit at the very bottom
class Skribbl(commands.Cog):
    """
    The Base Command for Skribbl.io!
    """
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                       case_insensitive=True)

    @bot.command(name="Skribbl", aliases=["Scribble", "Skribble", "Scribbl", "Skribble.io"])
    async def Skribbl(self, ctx, *link):
        """
        Use this command followed by a link to your game to send it in chat!
        """
        if len(link) == 0:
            embed = discord.Embed(title="Skribbl.io!", color=0x50b51b,
                                  description="Join our game of Skribbl.io!!!\n\nFind the link in VC!\n")
            embed.set_thumbnail(url="https://skribbl.io/res/logo.gif")
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)
        else:
            link = "".join(link)
            embed = discord.Embed(title="Skribbl.io!", color=0x50b51b,
                                  description=f"Join our game of Skribbl.io using the link below!!!\n\n\n{link}")
            embed.set_thumbnail(url="https://skribbl.io/res/logo.gif")
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)
            print(len(link))


def setup(bot):
    bot.add_cog(Skribbl(bot))
