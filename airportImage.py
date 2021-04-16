# Modules-------------

import requests
from bs4 import BeautifulSoup
from requests.api import get

#Constants-------------


#Backend-------------

def getImageData(url):
    
    r = requests.get(url) 
    return r.text

def getData(query):

    html = getImageData(f"https://ourairports.com/airports/{query}/")
    soup = BeautifulSoup(html, 'html.parser') 
    for item in soup.find_all('img'):
        print(item['src'])

getData("VIDP")


