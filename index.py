import json
import discord
import importlib.machinery
from discord.ext import commands

# Importing token and prefix from json
with open('./utility/config.json') as data_file:
    config_data = json.load(data_file)
token = config_data['token']
prefix = config_data['prefix']

# Initializing client instance
client = discord.Client()

# Log in confirmation
@client.event
async def on_ready():
    print('CubiculumBot Online!')

@client.event
async def on_message(message):
    
    author = message.author
    content = message.content
    args = content.split()[1:]
    command = content.split()[0][1:]

    if message.author == client.user:
        return
    
    if message.content.startswith(prefix):
        await message.channel.send(author.mention)

client.run(token)



