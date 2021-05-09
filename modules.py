# Modules

import urbandict as ud
import wikipedia
import urllib.request, urllib.error, urllib.parse
import requests
import bs4
from selenium import webdriver

# Backend

#UD and WIKIPEDIA MODULES

def udMeaning(query):
    try:

        submitData = dict(

            Word = "",
            Definition = "",
            Example = ""

        )
        
        fetchData = ud.define(query)

        submitData["Word"] = fetchData[0]["word"]
        submitData["Definition"] = fetchData[0]["def"]
        submitData["Example"] = fetchData[0]["example"]
        
        return submitData

    except Exception as e:
        print(e)

def wpMeaning(query):
    try:
        dataHandle = dict(

            Name = "",
            Thumbnail = "",
            Summary = "",
            Url = ""

        )

        wpPage = wikipedia.page(query)

        dataHandle["Name"] = str(wpPage.title)
        dataHandle["Thumbnail"] = str(wpPage.images[0])
        dataHandle["Summary"] = str(wikipedia.summary(query, sentences = 2))
        dataHandle["Url"] = str(wpPage.url)   # insert into dict

        return dataHandle

    except Exception as e:
        return e

# ATIS MODULE
def getWxData(ID):   #get website data

    dataURL = f'https://www.aviationweather.gov/metar/data?ids={ID}&format=raw&hours=0&taf=off&layout=on'
    dataHandle = urllib.request.urlopen(dataURL)
    webContent = dataHandle.read()    # result in type <byte>

    webContent = str(webContent, 'utf-8')   # convert type <byte> to <str>

    #get airport data

    try:
        argPosition1 = webContent.index("<code>")
        argPosition2 = webContent.index("</code>")

        data = (webContent[argPosition1+6:argPosition2])

        print(data)
        return data
    
    except:

        return "Airport METAR at not found!"

def getIcaoData(query):
    
    query = str(query)

    if len(query) == 4:
        return getWxData(query)     # check if ICAO is submitted

    else:   # if ICAO is not submitted then manually scrape out the information and then pass it on
        query = query.replace(" ", "%20")
        if "airport icao" not in query:
            query = query + " airport icao"
        else:
            pass

        webRequest = requests.get(f"https://www.google.com/search?q={query}&sxsrf=ALeKk01RAkqXw-MoxUbvYpX1pgDWXDsS2g%3A1618557805015&ei=bTt5YPEoycutAaq4oagJ&oq={query}&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyAggAMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgQIABBDOgQILhBDOgoILhDHARCvARBDOgcILhCxAxBDOgoIABCxAxCDARBDOgcIABCxAxBDOggILhDHARCvAToFCAAQkQJQwrEDWNrCA2DjxANoAXACeACAAeMCiAH-G5IBBzAuOC44LjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwixk5DYnYLwAhXJZSsKHSpcCJUQ4dUDCA4&uact=5")
        webProcess = bs4.BeautifulSoup(webRequest.text, "html.parser")
        webContent = str(webProcess)    # convert to str

        return getWxData(webContent[webContent.find("ICAO")+6:webContent.find("ICAO")+10])

# SELENIUM MODULE 
def queryScrapeData(query):

    query = query.replace(" ", "%20")

    # set up selenium and chromedriver
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driverPath = r'E:/Py/Lib/site-packages/chromedriver_py/chromedriver.exe'
    seleniumInstance = webdriver.Chrome(executable_path=driverPath, options=option)
    seleniumInstance.get(f'https://www.google.com/search?q={query}&rlz=1C1RXQR_enIN951IN951&aqs=chrome..69i57.10328j0j4&sourceid=chrome&ie=UTF-8')
    reqElem = seleniumInstance.find_elements_by_xpath('//div[@class="kno-rdesc"]')
    

    returnData = str(reqElem[0].text.replace(f"\n", ": "))
    print(returnData[13:-10]) # remove the wikipedia suffix and the description prefix

    seleniumInstance.close()    # close selenium after scrape


# TRANSLATE MODULE

def translate(query):
    pass