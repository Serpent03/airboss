#Library ------------

import discord
from discord.ext.commands import Bot
import urllib.request, urllib.error, urllib.parse
import requests
import bs4

#Home Grown ------------
import atisModule as ATIS
import udpy as ud
import anime as an




#Conditions ------------

bot = Bot(command_prefix='$')
TOKEN = 'TOKEN'


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


@bot.command(name = 'hi')
async def airport(ctx, *arguments):
    string = ''
    for arg in arguments:
        string = string + arg + ' '
    await ctx.send(f'{string}')


@bot.command(name = 'ud')
async def urbanDict(ctx, arg):
    await ctx.send(ud.getMeaning(arg))

@bot.command(name = 'fact')
async def fact(ctx):
    webRequest = requests.get("https://www.thefactsite.com/")
    webContent = bs4.BeautifulSoup(webRequest.text, "html.parser")
    webContent = str(webContent)

    await ctx.send(webContent[webContent.find("Did you know"):webContent.find("</p>")])

@bot.command(name = 'anime')
async def anime(ctx, *arguments):
    string = ''
    for arg in arguments:
        string = string + arg + ' '
    await ctx.send(an.getAnime(string))















bot.run(TOKEN)