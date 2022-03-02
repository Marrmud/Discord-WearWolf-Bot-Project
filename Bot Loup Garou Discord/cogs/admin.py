import discord
from discord.ext import commands

class Admin(commands.Cog):
  def __init__(self,client):
    self.clent = client

  @commands.command()
  async def clear(self, ctx, amount=10_000):
    channel=ctx.channel
    deleted = await channel.purge(limit=amount)
    await channel.send('Deleted {} message(s)'.format(len(deleted)))
def setup(client):
  
  client.add_cog(Admin(client))