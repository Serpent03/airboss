import urbandict as ud
import wikipedia

# Backend
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

if __name__ == "__main__":
    udMeaning("france")