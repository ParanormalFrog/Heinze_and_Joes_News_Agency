import sys
sys.path.insert(0, '../')

import discord
from discord.ext import commands
import headline_ranker
from utility.keywords import keyword_list

class News:
    def __init__(self, client):
        self.client = client
    
    # COmmand to return the mathced newsarticle with the highest search score
    hnget_brief = 'Link to interesting news from Hacker News.'
    hnget_desc = 'Returns the top ranked news article based on specified keywords.'
    @commands.command(pass_context=True, brief=hnget_brief, description=hnget_desc)
    async def hnget(self, ctx):
        articles = headline_ranker.rank_and_drop()
        try:
            
            hnget_ebmed = discord.Embed(color=0x2ecc71, description='Matched news article')
            hnget_ebmed.add_field(name=articles[0].title, value=articles[0].url)
            hnget_ebmed.add_field(name='Search Score', value=articles[0].rank)
            hnget_ebmed.add_field(name='Matched Keywords', value=', '.join(articles[0].matches))    
            await ctx.send(embed=hnget_ebmed)
        
        except Exception as error:
            
            print('{}: {}'.format(type(error).__name__, error))
            error_embed = discord.Embed(color=0xe74c3c, description='Sad times. No matching news found.\n\n Try adding new search terms with the `keyword` command.')
            await ctx.send(embed=error_embed)

    # Command to display a list of currently stored keywords
    kwlist_brief = 'List current keywords.'
    kwlist_desc = 'Shows a list of the currently stored keywords used for matching news articles.'
    @commands.command(pass_context=True, brief=kwlist_brief, description=kwlist_desc)
    async def kwlist(self, ctx):
        try:

            kwlist_ebmed = discord.Embed(title='Currently Stored Keywords', color=0x2ecc71)
            kwlist_ebmed.add_field(name='\u200b', value='\n'.join(keyword_list))
            await ctx.send(embed=kwlist_ebmed)

        except Exception as error:
            
            print('{}: {}'.format(type(error).__name__, error))

def setup(client):
    client.add_cog(News(client))