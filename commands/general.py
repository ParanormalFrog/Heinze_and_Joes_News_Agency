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

def setup(client):
    client.add_cog(General(client))