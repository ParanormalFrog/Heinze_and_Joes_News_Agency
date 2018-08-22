import sys
sys.path.insert(0, '..')

import keyword_processor
import discord
from discord.ext import commands

class General:
    def __init__(self, client):
        self.client = client
    
    # Test command for simple feedback from the bot
    test_brief = 'A simple test command.'
    test_description = 'Sends a confirmation message in the current channel (for testing purposes).'
    @commands.command(hidden=False, pass_context=True, brief=test_brief, description=test_description)
    async def test(self, ctx):
        await ctx.send('{}, test successful!'.format(ctx.message.author.mention))

    keyword_brief = 'Add a key word to the list'
    keyword_description = 'adds a key word to the list of search terms'
    @commands.command(hidden=False, pass_context=True, brief=keyword_brief, description=keyword_description)
    async def keyword(self, ctx, word):
        await keyword_processor.generaliser(str(word))
        ctx.send('{} added to list of keywords'.format(str(word)))

def setup(client):
    client.add_cog(General(client))