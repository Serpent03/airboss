#   Modules

import urbandict as ud
import wikipedia
import urllib.request, urllib.error, urllib.parse
import requests
import bs4
from selenium import webdriver
import time

#   Configuration

#----------[ Selenium ]----------

# set up selenium and chromedriver
option = webdriver.ChromeOptions()
option.add_argument('headless') # run slenium without window
driverPath = r'E:/Py/Lib/site-packages/chromedriver_py/chromedriver.exe'


#----------[ End ]---------- 


#   Backend

#----------[ Urban Dictionary and Wikipedia Module ]---------- 

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

#----------[ ATIS module for wx, and ICAO fetch module ]---------- 
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


#----------[ Selenium web scraping module ]---------- 
def queryScrapeData(query):

    query = query.replace(" ", "%20")
    url = f'https://www.google.com/search?q={query}&rlz=1C1RXQR_enIN951IN951&aqs=chrome..69i57.10328j0j4&sourceid=chrome&ie=UTF-8'
    seleniumInstance = webdriver.Chrome(executable_path=driverPath, options=option)     # set up a selenium instance.
    seleniumInstance.get(url)

    returnPayload = dict (  # set up a dictionary returning various data
        link = url,
        summary = "",
    )

    try:
        reqElem = seleniumInstance.find_elements_by_xpath('//div[@class="kno-rdesc"]')

        try:    # try to return the list index. If not, return error.
            returnData = str(reqElem[0].text.replace(f"\n", ": "))
            if returnData.find("Wikipedia") != -1:
                returnData = returnData.replace("Wikipedia", "")
            returnData = returnData[13:] # remove the description prefix
            seleniumInstance.close()    # close selenium after scrape
            returnPayload["summary"] = returnData
            return returnPayload

        except Exception as e:
            return e

    except:     # check for other paragraph div classes
        reqElem = seleniumInstance.find_elements_by_xpath('//div[@class="PZPZlf"]')

        try:    # try to return the list index. If not, return error.
            returnData = str(reqElem[0].text.replace(f"\n", ": "))
            seleniumInstance.close()    # close selenium after scrape
            returnPayload["summary"] = returnData
            return returnPayload

        except Exception as e:
            return e

    

    


#----------[ Image module ]---------- 

def imageScrape(query):

    query = query.replace(" ", "%20")
    url = f'https://www.google.com/search?q={query}&rlz=1C1RXQR_enIN951IN951&sxsrf=ALeKk00z0haR2dhtm1zozCDH-qzmFGvWcQ:1620654384218&source=lnms&tbm=isch&sa=X'
    seleniumInstance = webdriver.Chrome(executable_path=driverPath, options=option)
    seleniumInstance.get(url)

    reqElem = seleniumInstance.find_element_by_css_selector('//img[@class="Q4LuWd"]')
    print(reqElem)
    
    
    #returnPayload = [url]




#----------[ Anime module ]---------- 

# I have no idea how to make this without having the self-XXS(?) errors pop up.


#----------[ le testing phase ]---------- 

if __name__ == "__main__":
    imageScrape("dog")