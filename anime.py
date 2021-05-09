from bs4 import BeautifulSoup
import requests

def getAnime(query):
    query = query.replace(" ", "+")


    webRequest = requests.get(f'https://www.google.com/search?q={query}&rlz=1C1RXQR_enIN951IN951&oq=Nvidia+control+panel+settings+FS2020&aqs=chrome..69i57.10328j0j4&sourceid=chrome&ie=UTF-8')
    #webRequest = requests.get("https://en.wikipedia.org/wiki/List_of_game_engines")
    webProcess = BeautifulSoup(webRequest.text, "html.parser")


    text = webProcess.find('h3', {"class" : "Uo8X3b"})
    print(text.get_text())

    #set up
    
if __name__ == "__main__":
    getAnime("Fairy tail")