#Library ------------

import discord
from discord.ext.commands import Bot
import atisModule as ATIS



#Conditions ------------

bot = Bot(command_prefix='$')
TOKEN = 'NzQ4MDYzMjA3MDUwMTgyNjU2.X0X-Jg.MiPvXFK91KC-aEiWqHWviF9jXjE'


#Backend ------------


@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
	

@bot.command(name = 'yo')
async def yo(ctx):
    await ctx.send("yo")


@bot.command(name = 'atis', help = 'Fetches ATIS information a specific airport. Syntax: $atis [airport name or ICAO]')
async def atis(ctx, id):

    oldPosit = id

    if id[0].islower():
        id = id[0].upper()
    id = id + oldPosit[1:] 
    
    await ctx.send(f'-------------------\n**Airport METAR:**\n```{ATIS.getScrape(id)}```-------------------')


@bot.command(name = 'airport')
async def airport(ctx):
    await ctx.send("hi")

# @bot.command()
















bot.run(TOKEN)