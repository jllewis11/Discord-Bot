#https://replit.com/talk/learn/Hosting-discordpy-bots-with-replit/11008

import discord
import os
import keep_alive
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online

@client.event
async def on_member_join(ctx, member : discord.Member):
    joinTestEmbed = discord.Embed(
        title = "New Member Alert!",
        color = 0x63cf5b,
        description = "A new user has joined this here server! Please welcome" + member.mention + "!"
    ) 
    joinTestEmbed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=joinTestEmbed)
    message = "This Message is sent via DM"
    await member.send(message)

    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"

@client.command()
async def nuke(ctx, channel):
    await ctx.send("Launching all Soviet Nukes...")
    await ctx.send("Judgement day of " + channel + " has arrived.")
    for x in range(5, 0, -1):
      await ctx.send(x)
      time.sleep(1)
    await ctx.channel.delete()

@client.command()
async def rickroll(ctx):
    await ctx.send("https://i.giphy.com/media/Ju7l5y9osyymQ/giphy.webp")

@client.command()
async def dad(ctx):
  await ctx.send("https://media4.giphy.com/media/tn1cGqW0xWyfm/giphy.gif")

@client.command()
async def DM(ctx, member : discord.Member):
    message = "It's pain in my asshole"
    await member.send(message)



@client.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
@client.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")


@client.command()
async def member(ctx, member : discord.Member):
    joinTestEmbed = discord.Embed(
        title = "Member: ",
        color = 0x63cf5b,
        description = "Hello " + member.mention + "!"
    ) 
    joinTestEmbed.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=joinTestEmbed)
    
keep_alive.keep_alive()


client.run("NzYwMjU1MzA3NDE0MjQxMzEy.X3JY7g.OewQKErykh3gz08ntR5Qb07I55w") #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!

