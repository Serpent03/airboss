# Modules-------------

from googletrans import Translator

#Constants-------------
translator = Translator()

#Backend-------------

def translate(query):
    
    print(translator.translate(query))

if __name__ == "__main__":
    translate("Guten")