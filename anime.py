from bs4 import BeautifulSoup
import requests

def getAnime(query):
    query = query.replace(" ", "%20")


    webRequest = requests.get(f'https://www.google.com/search?q={query}')
    #webRequest = requests.get("https://en.wikipedia.org/wiki/List_of_game_engines")
    webProcess = BeautifulSoup(webRequest.text, "html.parser")


    text = webProcess.find('h3', {"class" : "Uo8X3b"})
    print(text.get_text())

    #set up
    
if __name__ == "__main__":
    getAnime("Fairy tail")