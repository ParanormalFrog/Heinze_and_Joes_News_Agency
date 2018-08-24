import sys
sys.path.insert(0, '../')

import discord
from discord.ext import commands
import headline_ranker
import utility.keyword_list as kw

class News:
    def __init__(self, client):
        self.client = client
    

    # hnget: Command to return the mathced newsarticle with the highest search score
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


    # kwlist: Command to display a list of currently stored keywords
    kwlist_brief = 'List current keywords.'
    kwlist_desc = 'Shows a list of the currently stored keywords used for matching news articles.'
    @commands.command(pass_context=True, brief=kwlist_brief, description=kwlist_desc)
    async def kwlist(self, ctx):
        try:
            kwlist_ebmed = discord.Embed(title='Currently Stored Keywords', color=0x2ecc71)
            kwlist_ebmed.add_field(name='\u200b', value='\n'.join(kw.keywords_to_list('../utility/keywords.txt')))
            await ctx.send(embed=kwlist_ebmed)
        except Exception as error:
            print('{}: {}'.format(type(error).__name__, error))
    

    # kwadd: Command to add keywords to the keyword list
    kwadd_brief = 'Add a new keyword to the list'
    kwadd_desc = '`!kwadd <keyword>` adds a new keyword to the list of search terms.'
    @commands.command(pass_context=True, brief=kwadd_brief, description=kwadd_desc)
    async def kwadd(self, ctx, *args):
        try:
            kw_file = open('../utility/keywords.txt','a')
            await ctx.send('{} keywords successfully added: `{}`'.format(len(args), ', '.join(args)))
            for arg in args:
                kw_file.write(',' + arg)
        except Exception as error:
            print('{}: {}'.format(type(error).__name__, error))


    # kwrm: Command to remove a kwyword from the keyword list
    kwrm_brief = 'Remove a keyword from the list'
    kwrm_desc = '`!kwrm <keyword>` removes a keyword from the list of search terms.'
    @commands.command(pass_context=True, brief=kwrm_brief, description=kwrm_desc)
    async def kwrm(self, ctx, arg):
        try:
            print(' ')
        except Exception as error:
            print('{}: {}'.format(type(error).__name__, error))


def setup(client):
    client.add_cog(News(client))