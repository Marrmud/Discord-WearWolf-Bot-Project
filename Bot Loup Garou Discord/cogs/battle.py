import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
#On def ici les commandes ou events
  def __init__ (self, client):
    self.client = client #<== permet d'acceder à la variable client dans le main
#(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)(EVENT)




#=========>Message supprimé par utilisateur
    

#(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)(COMMAND)
    #=========>Commande battle
  #@commands.command() #(creat Commands)
  async def battle_cmd(self, ctx, player_2):
    channel = ctx.channel
    player_1 = ctx.author
    player_2_id = player_2.id
    await channel.send("Hey <@!{}> you got tagged in a duel".format(player_2_id))

    def doge ():
      doge = random.randint(1, 5)
      if doge == 1:
        return True
      False

    main_dice = random.randint(0, 6)
    await channel.send("{} launched the dice and got a {} !".format(main_player, main_dice))

    tagged_dice = random.randint(0, 6)
    await channel.send("{} launched the dice and got a {} !".format(tagged_player, tagged_dice))

    if main_dice > tagged_dice:
      await channel.send("{} won !".format(main_player))
    elif main_dice < tagged_dice:
      await channel.send("{} won !".format(tagged_player))
    else:
      await channel.send("Wow ! It's a draw !")
    return
  #.Ping
  


def setup(client):
  client.add_cog(Fun(client))  