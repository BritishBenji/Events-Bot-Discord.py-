import discord
from discord.ext import commands
import os

guilds = []
client = discord.Client()


# noinspection PyShadowingNames
def get_prefix(client, message):
    prefixes = ['::']  # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['::']  # Only allow '::' as a prefix when in DMs, this is optional

    # Allow users to @mention the bot instead of using a prefix when using a command
    return commands.when_mentioned_or(*prefixes)(client, message)


bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                   case_insensitive=True)
bot.remove_command('help')

# collect token here
file1 = open("token.txt", "r")
TOKEN = file1.readlines()
file1.close()
TOKEN = " ".join(TOKEN)


@bot.command
# connects to discord
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    while len(guilds) < 1:
        async for guild in bot.fetch_guilds(limit=150):
            guilds.append(guild.name)
    print(guilds)
    await bot.change_presence(
        activity=discord.Streaming(name="In Development!", url="https://www.twitch.tv/BritishBenji"))


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'cogs.{filename}')

bot.run(TOKEN, bot=True, reconnect=True)
