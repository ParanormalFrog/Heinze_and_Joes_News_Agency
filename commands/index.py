import sys
sys.path.insert(0, '../utility')

import discord
from discord.ext import commands
from config import token, prefix

# Bot description. Shows when calling !help
description = 'CubiculumBot helps us do all kinds of awesome things!'

# Initializing cliant instance
client = commands.Bot(command_prefix=prefix, description=description)

# Extension list to be loaded as the bot comes online
startup_extensions = ['admin', 'general']

# On ready confirmation
@client.event
async def on_ready():
    print('CubiculumBot is online. Running on servers:\n')    
    for s in client.guilds:
        print('  - {} ({})'.format(s.name, s.id))

# Loading all extensions and running bot
if __name__ == '__main__':
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extension, error))

    client.run(token)
