from selenium import webdriver

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
    
    
if __name__ == "__main__":
    queryScrapeData("HID device")