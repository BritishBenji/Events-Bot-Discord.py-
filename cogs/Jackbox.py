import discord
from discord.ext import commands
import os
from run import get_prefix


class Jackbox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                       case_insensitive=True)

    @commands.group(name="Jackbox", description="The Jackbox Commands")
    async def Jackbox(self, ctx):
        """
        All the Commands for Jackbox start with this command!
        """
        if ctx.invoked_subcommand is None:
            embed = discord.Embed(title="Jackbox Games!", color=0x50b51b,
                                  description=f"**Join our game of Jackbox!\n\nURL = https://jackbox.tv/**")
            embed.set_thumbnail(
                url="https://static.wikia.nocookie.net/jackboxgames/images/8/84/Jackbox-logo.png/revision"
                    "/latest/scale-to-width-down/340?cb=20190830222301")
            try:
                embed.set_footer(text=ctx.guild,
                                 icon_url=ctx.guild.icon_url)


            except:
                pass

            await ctx.send(embed=embed)

    @Jackbox.command(name="TKO", description="Command for Tee-K.O. Games")
    async def TKO(self, ctx, code):
        embed = discord.Embed(title="Tee-K.O.!", color=0x50b51b,
                              description=f"**Join our game of Jackbox!\n\nURL = https://jackbox.tv/\n\n\
                              Code = {code}**")
        embed.set_thumbnail(url='https://jackboxgames.b-cdn.net/wp-content/uploads/TeeKO_cropped.png')
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @TKO.error
    async def TKO_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Tee-K.O.!", color=0x50b51b,
                                  description=f"**Join our game of Jackbox!\n\nURL = https://jackbox.tv/**")
            embed.set_thumbnail(url='https://jackboxgames.b-cdn.net/wp-content/uploads/TeeKO_cropped.png')
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

    @Jackbox.command(name="Quiplash", description="Command for Quiplash Games")
    async def Quiplash(self, ctx, code):
        embed = discord.Embed(title="Quiplash!", color=0x50b51b,
                              description=f"Join our game of Jackbox!\n\n**URL = https://jackbox.tv/\n\n\
                                          Code = {code}**")
        embed.set_thumbnail(url="https://jackboxgames.b-cdn.net/wp-content/uploads/2020/04/Quiplash-2.png")
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @Quiplash.error
    async def Quiplash_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Quiplash!", color=0x50b51b,
                                  description=f"Join our game of Jackbox!\n\n**URL = https://jackbox.tv/**")
            embed.set_thumbnail(url="https://jackboxgames.b-cdn.net/wp-content/uploads/2020/04/Quiplash-2.png")
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

    @Jackbox.command(name="STR", description="Command for Split The Room Games")
    async def STR(self, ctx, code):
        embed = discord.Embed(title="Split The Room!", color=0x50b51b,
                              description=f"Join our game of Jackbox!\n\n**URL = https://jackbox.tv/\n\n\
                                          Code = {code}**")
        embed.set_thumbnail(url="https://jackboxgames.b-cdn.net/wp-content/uploads/2019/05/catGraphic-616x1024.png")
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @STR.error
    async def STR_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Split The Room!", color=0x50b51b,
                                  description=f"Join our game of Jackbox!\n\n**URL = https://jackbox.tv/**")
            embed.set_thumbnail(url="https://jackboxgames.b-cdn.net/wp-content/uploads/2019/05/catGraphic-616x1024.png")
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

    @Jackbox.command(name="PS", description="Command for Patently Stupid Games")
    async def PS(self, ctx, code):
        embed = discord.Embed(title="Patently Stupid!", color=0x50b51b,
                              description=f"Join our game of Jackbox!\n\n**URL = https://jackbox.tv/\n\n\
                                        Code = {code}**")
        embed.set_thumbnail(url="https://jackboxgames.b-cdn.net/wp-content/uploads/2019/06/Bulb-803x1024.png")
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url
                         )
        await ctx.send(embed=embed)

    @PS.error
    async def PS_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Patently Stupid!", color=0x50b51b,
                                  description=f"Join our game of Jackbox!\n\n**URL = https://jackbox.tv/**")
            embed.set_thumbnail(url="https://jackboxgames.b-cdn.net/wp-content/uploads/2019/06/Bulb-803x1024.png")
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url
                             )
            await ctx.send(embed=embed)

    @Jackbox.command(name="MVC", description="Command for Mad Verse City Games")
    async def MVC(self, ctx, code):
        embed = discord.Embed(title="Mad Verse City!", color=0x50b51b,
                              description=f'Join our game of Jackbox!\n\n**URL = https://jackbox.tv/\n\n\
                              Code = {code}**')
        embed.set_thumbnail(url='https://jackboxgames.b-cdn.net/wp-content/uploads/2020/04/Bot-01.png')
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @MVC.error
    async def MVC_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Mad Verse City!", color=0x50b51b,
                                  description=f'Join our game of Jackbox!\n\n**URL = https://jackbox.tv/**')
            embed.set_thumbnail(url='https://jackboxgames.b-cdn.net/wp-content/uploads/2020/04/Bot-01.png')
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

    @Jackbox.command(name="Other", description="For Jackbox Games Not Listed")
    async def other(self, ctx, code):
        embed = discord.Embed(title="Jackbox Games!", color=0x50b51b,
                              description=f"**Join our game of Jackbox!\n\nURL = https://jackbox.tv/\n\n\
                                          Code = {code}**")
        embed.set_thumbnail(
            url="https://static.wikia.nocookie.net/jackboxgames/images/8/84/Jackbox-logo.png/revision"
                "/latest/scale-to-width-down/340?cb=20190830222301")
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)

    @other.error
    async def Jackbox_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title="Jackbox Games!", color=0x50b51b,
                                  description="**Join our game of Jackbox!\n\nURL = https://jackbox.tv/\n\n**")
            embed.set_thumbnail(
                url="https://static.wikia.nocookie.net/jackboxgames/images/8/84/Jackbox-logo.png/revision"
                    "/latest/scale-to-width-down/340?cb=20190830222301")
            embed.set_footer(text=ctx.guild,
                             icon_url=ctx.guild.icon_url)
            await ctx.send(embed=embed)

    @Jackbox.command(name="help", description="A help command for the Jackbox Module")
    async def help(self, ctx):
        embed = discord.Embed(title="Jackbox Games!", color=0x50b51b,
                              description="Below is a list of commands usable with the Jackbox Module")
        embed.add_field(name="Mad Verse City", value=f'Can be called using __MVC <Room Code>__', inline=True)
        embed.add_field(name="Other", value=f'Can be called using __Other <Room Code>__', inline=True)
        embed.add_field(name="Patently Stupid", value=f'Can be called using __PS <Room Code>__', inline=True)
        embed.add_field(name="Quiplash", value=f'Can be called using __Quiplash <Room Code>__', inline=True)
        embed.add_field(name="Split The Room", value=f'Can be called using __STR <Room Code>__', inline=True)
        embed.add_field(name="Tee-K.O.", value=f'Can be called using __TKO <Room Code>__', inline=True)
        embed.set_thumbnail(
            url="https://static.wikia.nocookie.net/jackboxgames/images/8/84/Jackbox-logo.png/revision"
                "/latest/scale-to-width-down/340?cb=20190830222301")
        embed.set_footer(text=ctx.guild,
                         icon_url=ctx.guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jackbox(bot))


