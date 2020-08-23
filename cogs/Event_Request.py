import discord
from discord.ext import commands
from run import get_prefix

requested_games = {}


# TODO: Make this into a proper database to allow for rebooting,
#  and to allow the bot to be used in multiple servers without them clashing

class Request(commands.Cog):
    """
    This command Allows you to request an event, \nit is still in development
    """

    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                       case_insensitive=True)

    # It still looks like shit after some changes, need to clean it up with an embed or smthn,
    # just fix it in some way

    @bot.command(name="Request", description="Command to request various events", aliases=["Req"])
    async def Request(self, ctx):
        """
        Run this command by itself to request a game to be reviewed by the moderators!
        """
        userid = ctx.message.author.id
        embed = discord.Embed(title="You have requested to add an event!",
                              description="What Game would we be playing in this event?")
        await ctx.send(embed=embed)
        msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        msg = msg.content
        embed = discord.Embed(title=f"You have requested to play {msg}",
                              description="Are you sure of your decision?\nYes? Or No?")
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        msg2 = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
        msg1 = msg2.content
        if msg1.lower() == "yes":
            await ctx.send("Request Submitted!")
            requested_games[msg] = [f'{userid}']
        if msg1.lower() == "no":
            await ctx.send("Request Declined!")

    # Surprisingly, this command actually kinda works well. Like, I didn't think it would, but someone,
    # somewhere will find a way to break it

    # I found the break, it was in DMs,
    # I'll ignore it for now cause it's an easy fix that doesn't matter all that much

    # TODO: Block this command from being used in DMs

    @bot.command(name="Requested", description="Command to see requests", aliases=["Reqd"])
    @commands.has_any_role("Owner", "Co-Owner", "Admin", "Moderator")
    async def Requested(self, ctx):
        """
        This command shows all the requested events and who requested them
        """
        embed = discord.Embed(title="Requested Games")
        for y, x in requested_games.items():
            game = str.join("", x)
            embed.add_field(name=f'{y}', value=f'<@{game}>')
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    # TODO: Fix an error that prevents you from removing entries that have more than one word in it

    @bot.command(name="Remove", description="Command to remove requests", aliases=["Rmv"])
    @commands.has_any_role("Owner", "Co-Owner", "Admin", "Moderator")
    async def Remove(self, ctx, x):
        """
        This command can be used to remove entries from the "requested" list
        """
        if x in requested_games:
            embed = discord.Embed(title=f"Are you sure you would like to remove {x}?")
            await ctx.send(embed=embed)
            msg = await self.bot.wait_for('message', check=lambda message: message.author == ctx.author)
            msg = msg.content
            if msg.lower() == "yes":
                del requested_games[x]
                await ctx.send(f"Requested game {x} has been deleted!")
            if msg.lower() == "no":
                await ctx.send(f"Requested game {x} has **not** been deleted!")
        else:
            pass


def setup(bot):
    bot.add_cog(Request(bot))
