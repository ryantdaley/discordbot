import discord
import os
from discord import ChannelType
from discord.ext.commands import check
import random
client=discord.Client()

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

memes=['Added 1/15/2021  https://youtu.be/3SLR2gujU4U', 
'Added 1/15/2021  https://youtu.be/jc6qQGTG9Sg',
'Added 1/15/2021  https://youtu.be/c0d3NS-vUEI',
'Added 1/15/2021  https://youtu.be/eawIbm2dqtc',
'Added 1/15/2021  https://youtu.be/i5bppJyhwSg',
'Added 1/15/2021  https://youtu.be/aAEJkZUAQH4']    
    
randvids=['https://youtu.be/jNQXAC9IVRw','https://youtu.be/2Qa9YDgtcaM']



@client.event
async def on_message(message):
  if message.author==client.user:
    return
  
  if message.content.startswith("!hello"):
    await message.channel.send("Hello")

  if message.content.startswith("!help"):
    await message.channel.send('''
    Heres what we got so far:
    !hello - bot just replies hello
    !memes - Get some fresh memes
    
    ''''')
  
  if message.content.startswith("!memes"):
    
    rnum=random.randint(0,len(memes)-1)
    await message.channel.send('Looking for some fresh memes? Tenszebra has got you covered: \n\n' + memes[rnum])                             
  


client.run(os.getenv('TOKEN'))