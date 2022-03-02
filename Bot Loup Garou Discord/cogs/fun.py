import discord
from discord.ext import commands

class Fun(commands.Cog):
#On def ici les commandes ou events
  def __init__ (self, client):
    self.client = client #<== permet d'acceder à la variable client dans le main
#(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)




#=========>Message supprimé par utilisateur
    

#(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)
    #=========>Commande echo
  #@commands.command() #(creat Commands)
  #.echo
  async def echo(self, ctx, *args): #<== tjrs ajouter ctx en arg (*args = infinité arg dans une fonction)
    out = ''
    for mot in args:
      out += mot
      out += ' '
    await ctx.send(out)
  #.Ping
  


def setup(client):
  client.add_cog(Fun(client))  