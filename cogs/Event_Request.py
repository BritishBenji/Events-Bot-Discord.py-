import discord
from discord.ext import commands
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

    # TODO: Improve the aesthetic of the request command
    # It looks like shit, need to clean it up with an embed or smthn,
    # just fix it in some way

    @bot.command(name="Request", description="Command to request various events", aliases=["Req"])
    async def Request(self, ctx):
        user = ctx.message.author.id
        await ctx.send("You have requested to add an event!\nWhat Game would we be playing in this event?")
        msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        msg = msg.content
        await ctx.send(f"Sure, we're gonna play {msg}")
        requested_games[msg] = [f'{user}']

    # Surprisingly, this command actually kinda works well. Like, I didn't think it would, but someone,
    # somewhere will find a way to break it

    @bot.command(name="Requested", description="Command to see requests", aliases=["Reqd"])
    @commands.has_any_role("Owner", "Co-Owner", "Admin", "Moderator")
    async def Requested(self, ctx):
        embed = discord.Embed(title="Requested Games")
        for y, x in requested_games.items():
            game = str.join("", x)
            embed.add_field(name=f'{y}', value=f'<@{game}>')
        await ctx.send(embed=embed)

    # TODO: Tidy it up, just tidy it all up

    @bot.command(name="Remove", description="Command to remove requests", aliases=["Rmv"])
    @commands.has_any_role("Owner", "Co-Owner", "Admin", "Moderator")
    async def Remove(self, ctx, x):
        if x in requested_games:
            embed = discord.Embed(title=f"Are you sure you would like to remove {x}?")
            await ctx.send(embed=embed)
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            msg = msg.content
            if msg.lower() == "yes":
                del requested_games[x]
                await ctx.send("Request has been deleted!")
            if msg.lower() == "no":
                await ctx.send("Request has **not** been deleted!")
        else:
            pass


def setup(bot):
    bot.add_cog(Request(bot))
