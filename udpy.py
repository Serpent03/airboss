from typing import SupportsBytes
import urbandict as ud

def getMeaning(query):
    submitData = ''
    fetchData = ud.define(query)
    
    for k,v in fetchData[0].items():    #parse through dict
        if k != "category":
            submitData = f"**{k}**: {v}\n" + submitData     # add all the statements to a singular text object
    
    return submitData

