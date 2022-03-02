import discord
import random
from discord.ext import commands, tasks
import time
import asyncio
import os
from itertools import cycle


#token
token = 'Njg2OTc4NzI5OTA1NDg3OTY0.XmfMog._-3KaMs891ljk3m5RMZ92q1Hmrc'
#Prefix de commande pour le bot
client = commands.Bot(command_prefix='.lg ')
status = cycle(['En raffistolage.','En raffistolage.', "En raffistolage..", "En raffistolage..."])
etat = cycle(['do_not_disturb', 'online'])


#Test Bot Ready
@client.event
async def on_ready():
  #change_status.start()
  channel = client.get_channel(687055572658683940) # <== envoie msg a un specifeid channel
 # await channel.purge(limit=10_000) 
  await channel.send('''```
              ─=≡Σ((( つ◕ل͜◕)つ
  ___                           _ _               __  
 |_ _|   __ _ _ __ ___     __ _| (_)_   _____   _ \ \ 
  | |   / _` | '_ ` _ \   / _` | | \ \ / / _ \ (_) | |
  | |  | (_| | | | | | | | (_| | | |\ V |  __/  _  | |
 |___|  \__,_|_| |_| |_|  \__,_|_|_| \_/ \___| (_) | |
                                                  /_/ 

```''')

# Clignotage
@client.command()
async def flickering(ctx):
	await client.change_presence(status = discord.Status.do_not_disturb, activity = discord.Game("En raffistolage.."))
	await asyncio.sleep(1)
	await client.change_presence(status = discord.Status.online, activity = discord.Game("En raffistolage..."))
	await asyncio.sleep(1)
	await flickering(ctx)

#...
#@tasks.loop(seconds=1)
#async def change_status():
#  await client.change_presence(activity = discord.Game(next(status)))


#Logs Messages
@client.event
async def on_message(message):
  author = message.author
  content = message.content
  print('{}: {}'.format(author, content))  #Renvoie à la console nom + msg
  await client.process_commands(message)



@client.command()
async def commandes(ctx):
  embed = discord.Embed(
    title = 'Commandes',
    description = 'Commandes du bot',
    colour = discord.Colour(0xFA8072)
  )
  #Modif de l'embed
  embed.set_footer(text='NIQUE BIEN TA MERE SALE FILS DE PUTE.')
  #embed.set_image(url = 'https://i.skyrock.net/4178/97294178/pics/3278690356_1_2_oEmc2hCk.jpg')
  embed.set_thumbnail(url = "https://www.afjv.com/2018/12/181210-loups-garous-en-ligne.jpg")
  embed.set_author(name = 'Narrateur', icon_url = 'https://lh3.googleusercontent.com/P1aDP-icNA6fsLKhLSDtsTQpY3fPjHv0k1np1dVxNiiP_93uwQklayMMw1vwXI6xWQc=s180')
  embed.add_field(name = '.dice_battle', value ='Lance une battle de dés contre un joueur', inline = True )
  embed.add_field(name = '.echo', value ='Répète le message', inline = True )
  embed.add_field(name = '.kick', value ='Kick une personne', inline = True )

  await ctx.send(embed = embed)




@client.event
async def on_member_join(ctx,member):
  role = discord.utils.get(member.server.roles, name = 'Thicc')
  await ctx.add_roles(member,role)





#=========>Commande non conventionnel : .iq ==> Qi de l'utilisateur, .echo ==> renvoie le msg rentré sans le .echo
#@client.event
#async def on_message(message):
#  channel = message.channel
#  author = message.author
#  if message.content.startswith('.iq'):
#    await channel.send("{}'s IQ = {}!".format(author, random.randint(-10, 150)))
#  if message.content.startswith('.echo'):
#    msg = message.content.split()
#    output = ''
#    for mot in msg[1:]:
#      output += mot
#      output += ' '
#    await channel.send(output)


#@client.event
#async def on_message_delete(message):
#  author = message.author
#  content = message.content
#  channel = message.channel
#  print('Message supprimé par Utilisateur: {}, sur Channel: {} | "{}"'.format(author, channel, content))


#=========>Commande echo
#client.command()
#async def echo(ctx, *args): #<== tjrs ajouter ctx en arg (*args = infinité arg dans une fonction)
#  out = ''
#  for mot in args:
##    out += mot
#    out += ' '
#  await ctx.send(out)


#Clear
#@client.command(pass_context=True)
#async def clear(ctx, amount=10_000):
#  channel=ctx.channel
#  deleted = await channel.purge(limit=amount)
#  await channel.send('Deleted {} message(s)'.format(len(deleted)))



  
      

#========================Usless mtn=======================================
# retrieve tag from message



#Kick
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):  #<== Appel la methode de discord pour recup un membre du serveur .member (* = tt ce qui vient après membre == reason)
  try:
    await member.kick(reason=reason)
    await ctx.channel.purge(limit = 1)
  except :
    print("\n*** KICKING ERROR : Cannot be kicked (permission error) ***\n")
    await ctx.channel.purge(limit = 1)


#Ban
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):  #Idem
  try:
    await member.ban(reason=reason)
    await ctx.channel.purge(limit = 1)
  except :
    print("\n*** BANNING ERROR : Cannot be banned (permission error) ***\n")
    await ctx.channel.purge(limit = 1)


#Unban
@client.command()
async def unban(ctx, *, member):  #<== Meme raison pour le "*" (Prend tout ce qui vient après comme un seule argument), cette fois ci membre n'est pas sur le serveur
    banned_users = await ctx.guild.bans()  #Chope la liste des gens banni du serv
    member_name, member_discriminator = member.split('#')  #Nb member_discriminator c'est le # après le pseudo
    for utilisateur_banni in banned_users:
        user = utilisateur_banni.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)  #Principale pour unban
            return  #Fin du program (Pas de unban en Unban)


#========================Usless mtn=======================================



#Mute_fight






########

async def dice_cmd(ctx, member):
  channel = ctx.channel
  main_player = ctx.author
  tagged_player = member
  tagged_player_id = member.id
  await channel.send("Hey <@!{}> you got tagged in a duel".format(tagged_player_id))

  time.sleep(0.5)
  main_dice = random.randint(0, 6)
  await channel.send("{} launched the dice and got a {} !".format(main_player, main_dice))

  time.sleep(0.5)
  tagged_dice = random.randint(0, 6)
  await channel.send("{} launched the dice and got a {} !".format(tagged_player, tagged_dice))

  time.sleep(0.5)
  if main_dice > tagged_dice:
	  await channel.send("{} won !".format(main_player))
  elif main_dice < tagged_dice:
	  await channel.send("{} won !".format(tagged_player))
  else:
	  await channel.send("Wow ! It's a draw !")
  return

# Init dice battle
@client.command()
async def dice_battle(ctx):
  channel = ctx.channel
  author = (ctx.author).id
  message = ctx.message
  await channel.send('<@!{}>, please tag someone in duel :'.format(author))

    # vérifie que le message contient un tag et que ce tag n'est pas le même que celui de l'auteur de la commande
  def check(message):
    if len(message.mentions)!=0:
      member_id = (message.mentions[0]).id
      assert member_id != (message.author).id
      return member_id != None
    return False


    # attends un message de l'utilisateur
  try :
    message = await client.wait_for("message", timeout=10, check=check)
  except asyncio.TimeoutError:
    await channel.send("<@!{}> vous avez mit trop de temps... Jeu annulé".format((message.author).id))
    return
  except:
    await channel.send("Trouvez vous des amis...")
    return
        
  member = message.mentions[0]
  await dice_cmd(ctx, member)


#COGS
#Load : Fichier(cogs > extensions qui existent dans le fichier)
@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
#Unload 
@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')



for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}') #<== Loop dans fichier cogs, load seulement ceux qui finissent par.py, retire 3 dernier caractère ".py"


client.run(token)
