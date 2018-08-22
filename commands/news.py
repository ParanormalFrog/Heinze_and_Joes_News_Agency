import sys
sys.path.insert(0, '../')
import discord
from discord.ext import commands
import headline_ranker

class News:
    def __init__(self, client):
        self.client = client
    
    hnget_brief = 'Link to interesting news from Hacker News.'
    hnget_description = 'Returns the top ranked news article based on specified keywords.'
    @commands.command(pass_context=True, brief=hnget_brief, description=hnget_description)
    async def hnget(self, ctx):
        articles = headline_ranker.rank_and_drop()
        try:
            news_ebmed = discord.Embed(color=0x2ecc71, description='Matched news article')
            news_ebmed.add_field(name=articles[0].title, value=articles[0].url)
            news_ebmed.add_field(name='Search Score', value=articles[0].rank)
            news_ebmed.add_field(name='Matched Keywords', value=', '.join(articles[0].matches))
            await ctx.send(embed=news_ebmed)
        except Exception as error:
            print('{}: {}'.format(type(error).__name__, error))
            error_embed = discord.Embed(color=0xe74c3c, description='Sad times. No matching news found.\n\n Try adding new search terms with the `keyword` command.')
            await ctx.send(embed=error_embed)

def setup(client):
    client.add_cog(News(client))