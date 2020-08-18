# I gotta recode a lot of this and take some advice from some dude online:
# "Always assume the end-user is a complete asshole" -
# Michael Reeves, 17 Aug 2017


import discord
from discord.ext import commands
import os

guilds = []
client = discord.Client()


# If you can't tell, I literally just stole the get_prefix code from some other dude, idk who it was,
# and I'm not gonna reference them, because it's Python, and we all know, 'it's free real estate'

# noinspection PyShadowingNames
def get_prefix(client, message):
    prefixes = ['::']  # sets the prefixes, u can keep it as an array of only 1 item if you need only one prefix

    if not message.guild:
        prefixes = ['::']  # Only allow '::' as a prefix when in DMs, this is optional

    # Allow users to @mention the bot instead of using a prefix when using a command
    return commands.when_mentioned_or(*prefixes)(client, message)


# Set's out your prefix, and shortens the module name waaayyyyyy down. Pretty nifty, ngl
bot = commands.Bot(command_prefix=get_prefix, description="A bot made to describe the events in your server",
                   case_insensitive=True)
# Took me so long to get this line working, I stg if this comment changes it, I'm giving up
bot.remove_command('help')

# collect token here
file1 = open("token.txt", "r")
TOKEN = file1.readlines()
file1.close()
TOKEN = " ".join(TOKEN)


@bot.event
# connects to discord
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    while len(guilds) < 1:
        async for guild in bot.fetch_guilds(limit=150):
            guilds.append(guild.name)
    print(guilds)
    await bot.change_presence(
        activity=discord.Streaming(name="In Development!", url="https://www.twitch.tv/BritishBenji"))


# Loads the cogs, prints them out, self explanatory I guess
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'cogs.{filename}')

bot.run(TOKEN, bot=True, reconnect=True)
