import urllib.request, urllib.error, urllib.parse
import discord
import requests
import bs4

def getAnime(query):
    query = query.replace(" ", "_")

    #webRequest = requests.get(f"https://animekisa.tv/search?q={query}")

    webRequest = requests.get(f"https://en.wikipedia.org/wiki/{query}")
    webProcess = bs4.BeautifulSoup(webRequest.text, features = "html.parser")
    webContent = (webProcess)
    
    print(webContent.find_all("plot"))
    

getAnime("Fairy tail")