# Modules-------------

import urllib.request, urllib.error, urllib.parse
import requests
import bs4

#Constants-------------


#Backend-------------

def getWxData(ID):   #get website data

    dataURL = f'https://www.aviationweather.gov/metar/data?ids={ID}&format=raw&hours=0&taf=off&layout=on'
    dataResponse = urllib.request.urlopen(dataURL)
    webContent = dataResponse.read()    # result in type <byte>

    webContent = str(webContent, 'utf-8')   # convert type <byte> to <str>

    #get airport data

    try:
        argPosition1 = webContent.index("<code>")
        argPosition2 = webContent.index("</code>")

        data = (webContent[argPosition1+6:argPosition2])

        return data
    
    except:

        return "Airport METAR at not found!"

def getScrape(query):
    
    query = str(query)

    if len(query) == 4:
        return getWxData(query)     # check if ICAO is submitted

    else:
        query = query.replace(" ", "+")
        if "airport icao" not in query:
            query = query + " airport icao"
        else:
            pass

        webRequest = requests.get(f"https://www.google.com/search?q={query}&sxsrf=ALeKk01RAkqXw-MoxUbvYpX1pgDWXDsS2g%3A1618557805015&ei=bTt5YPEoycutAaq4oagJ&oq={query}&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyAggAMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgQIABBDOgQILhBDOgoILhDHARCvARBDOgcILhCxAxBDOgoIABCxAxCDARBDOgcIABCxAxBDOggILhDHARCvAToFCAAQkQJQwrEDWNrCA2DjxANoAXACeACAAeMCiAH-G5IBBzAuOC44LjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwixk5DYnYLwAhXJZSsKHSpcCJUQ4dUDCA4&uact=5")
        webContent = bs4.BeautifulSoup(webRequest.text, "html.parser")
        webContent = str(webContent)    # convert to str

        return getWxData(webContent[webContent.find("ICAO")+6:webContent.find("ICAO")+10])


if  __name__ == "__main__":

    getScrape(str(input("enter airport name \n~ ")))