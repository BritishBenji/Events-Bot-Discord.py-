import discord
from discord.ext import commands
from run import get_prefix

# This module works basically perfectly from the get go, there isn't much to add to it tbf

class CAH(commands.Cog):
    """
    This command will allow you to show the link to your Cards Against Humanity game
    """

    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                       case_insensitive=True)

    @bot.command(name="CAH",
                 description="Command to display a link to a cards against humanity game", aliases=["cards"])
    async def CAH(self, ctx, *link):
        """
        Run this command followed by a link to display your CAH game
        """
        if len(link) > 0:
            print(link)
            embed = discord.Embed(title="Cards Against Humanity!",
                                  description="Follow the link below to join our game of Cards Against Humanity!")
            link = "".join(link)
            embed.add_field(name="link:",
                            value=f"{link}")
            embed.set_thumbnail(url="https://digital.hbs.edu/platform-rctom/wp-content/uploads/sites/4/2015/12/prt_280x188_1370231957.png")
        else:
            embed = discord.Embed(title="Cards Against Humanity!",
                                  description="Join VC to join our game of Cards Against Humanity!")
            embed.set_thumbnail(
                url="https://digital.hbs.edu/platform-rctom/wp-content/uploads/sites/4/2015/12/prt_280x188_1370231957.png")
        await ctx.send(embed=embed)
        print(link)


def setup(bot):
    bot.add_cog(CAH(bot))
