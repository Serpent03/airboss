#Library ------------

import discord
from discord.ext.commands import Bot
import urllib.request, urllib.error, urllib.parse
import requests
import bs4

#Home Grown ------------
import modules


#Conditions ------------

bot = Bot(command_prefix='$')
TOKEN = '#'


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
    id = id + oldPosit[1:]      # capitalize
    
    await ctx.send(f'-------------------\n**Airport METAR:**\n```{modules.getIcaoData(id)}```-------------------')


@bot.command(name = 'airport')
async def airport(ctx, *arguments):
    string = ''
    for arg in arguments:
        string = string + arg + ' '
    
    await ctx.send(f'{string}')


@bot.command(name = 'ud')   # get meanings from urban dictionary
async def urbanDict(ctx, *arguments):
    string = ''
    for arg in arguments:
        string = string + arg + ' '
    
    data = modules.udMeaning(string)


    # set up embed

    embed = discord.Embed(
        title = data["Word"],
        color = 0xFFA200
    )

    embed.set_author(
        name = "Urban Dictionary",
        url = "https://www.urbandictionary.com/",
        icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/UD_logo-01.svg/1200px-UD_logo-01.svg.png"
    )

    embed.add_field(
        name = "Definition",
        value = data["Definition"],
    )

    embed.add_field(
        name = "Example",
        value = data["Example"]
    )

    await ctx.send(embed = embed)

@bot.command(name = 'wiki') # get meanings from wikipedia
async def wikiPedia(ctx, *arguments):
    string = ''
    for arg in arguments:
        string = string + arg + ' '
    
    data = modules.wpMeaning(string)

    # set up embed
    if data == Exception:
        await ctx.send(data)
    else:
        embed = discord.Embed(
            title = data["Name"],
            url = data["Url"],
            color = 0xd4d4d4,
        )

        embed.set_author(
            name = "Wikipedia",
            url = "https://www.wikipedia.org/",
            icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Wikipedia_logo_%28svg%29.svg/1200px-Wikipedia_logo_%28svg%29.svg.png"
        )

        embed.set_thumbnail(
            url = data["Thumbnail"]
        )

        embed.add_field(
            name = "Summary",
            value = data["Summary"]
        )

        await ctx.send(embed = embed)


@bot.command(name = 'fact')
async def fact(ctx):
    webRequest = requests.get("https://www.thefactsite.com/")
    webContent = bs4.BeautifulSoup(webRequest.text, "html.parser")
    webContent = str(webContent)

    await ctx.send(webContent[webContent.find("Did you know"):webContent.find("</p>")])


@bot.command(name = 'translate')
async def anime(ctx, *arguments):
    string = ''
    for arg in arguments:
        string = string + arg + ' '
    
    await ctx.send(modules.translate(string))


@bot.command(name = "explain")
async def scrapeQuery(ctx, *arguments):
    string = ''
    for arg in arguments:
        string = string + arg + ' '
    
    await ctx.send(modules.queryScrapeData(string))













bot.run(TOKEN)