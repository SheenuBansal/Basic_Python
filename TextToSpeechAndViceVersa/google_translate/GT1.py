from googletrans import Translator
from pprint import pprint

#initialize the googletrans API
translator =Translator()

#translate a spanish text to english text(by default)
translation = translator.translate("Hola Mundo")
print(f'{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})')

# It automaticallly detects the src and converts it

# Let's translate a spanish text to arabic for instance
translation = translator.translate("Hola Mundo",dest="ar")
print(f'{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})')

translation = translator.translate("Hola Mundo",dest="hi")
print(f'{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})')

# specify source language
translation = translator.translate("Wie gehts ?", src="de")
print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

pprint(translation.extra_data)