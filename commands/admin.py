import discord
from discord.ext import commands

class Admin:
    def __init__(self, client):
        self.client = client

    # Load an extension manually
    load_brief = 'Load an extension manually.'
    load_description = 'Allows the admin to manually load a specific extension.'
    @commands.command(hidden=False, pass_context=True, brief=load_brief, description=load_description)
    async def load(self, ctx, extension : str):
        try:
            self.client.load_extension(extension)
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('{} has been loaded successfully.'.format(extension))

    # Unload an extension manually
    unload_brief = 'Unload an extension manually.'
    unload_description = 'Allows the admin to manually unload a specific extension.'
    @commands.command(hidden=False, pass_context=True, brief=unload_brief, description=unload_description)
    async def unload(self, ctx, extension : str):
        try:
            self.client.unload_extension(extension)
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('{} has been unloaded successfully.'.format(extension))

    # Reload an extension manually
    reload_brief = 'Reload an extension manually.'
    reload_description = 'Allows the admin to manually reload a specific extension.'
    @commands.command(name='reload', hidden=False, pass_context=True, brief=reload_brief, description=reload_description)
    async def _reload(self, ctx, extension : str):
        try:
            self.client.unload_extension(extension)
            self.client.load_extension(extension)
        except Exception as e:
            await ctx.send('\N{PISTOL}')
            await ctx.send('{}: {}'.format(type(e).__name__, e))
        else:
            await ctx.send('{} has been reloaded successfully.'.format(extension))

def setup(client):
    client.add_cog(Admin(client))
