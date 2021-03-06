import discord
from discord.ext import commands
from run import get_prefix


# I literally stole 50 lines of code from StackOverflow (no copyright issues) for this cog.
# I'll personalise it eventually, the whole:
# "Sure you can copy my homework, just change it up a little"


class Help(commands.Cog):
    """
    Shows This Help Command!
    """

    def __init__(self, bot, *cog):
        self.bot = bot

    bot = commands.Bot(command_prefix=get_prefix,
                       description="A bot made to describe the events in your server",
                       case_insensitive=True
                       )

    @commands.group(name="help",
                    description="A customized help command"
                    )
    async def Help(self, ctx, *cog):
        """
        This Command!
        """
        if not cog:
            halp = discord.Embed(title='Command list!',
                                 description='Use `::help <command>` to find out more about them!')
            cogs_desc = ''
            for x in self.bot.cogs:
                cogs_desc += ('{} - {}'.format(x, self.bot.cogs[x].__doc__) + '\n')
            halp.add_field(name='Commands', value=cogs_desc[0:len(cogs_desc) - 1], inline=False)
            cmds_desc = ''
            for y in self.bot.walk_commands():
                if not y.cog_name and not y.hidden:
                    cmds_desc += ('{} - {}'.format(y.name, y.help) + '\n')
            if cmds_desc != '':
                halp.add_field(name='Uncategorized Commands', value=cmds_desc[0:len(cmds_desc) - 1], inline=False)
            await ctx.message.add_reaction(emoji='✉')
            await ctx.author.send('', embed=halp)
        else:
            if len(cog) > 1:
                halp = discord.Embed(title='Error!', description=' ',
                                     color=discord.Color.red())
                await ctx.send('', embed=halp)
            else:
                """
                Command listing within a cog.
                """
                found = False
                for x in self.bot.cogs:
                    for y in cog:
                        if x == y:
                            halp = discord.Embed(title=cog[0] + ' Command Listing',
                                                 description=self.bot.cogs[cog[0]].__doc__)
                            for c in self.bot.get_cog(y).get_commands():
                                if not c.hidden:
                                    halp.add_field(name=c.name, value=c.help, inline=False)
                            found = True
                if not found:
                    """Reminds you if that cog doesn't exist."""
                    halp = discord.Embed(title='Error!', description=f'{cog[0]} isn\'t a Command!',
                                         color=discord.Color.red())
                else:
                    await ctx.message.add_reaction(emoji='✉')
                await ctx.author.send('', embed=halp)


def setup(bot):
    bot.add_cog(Help(bot))
