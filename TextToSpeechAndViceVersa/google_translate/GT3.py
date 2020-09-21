# Detect a language

from googletrans import Translator, constants

translator = Translator()
detection = translator.detect("हैलो जान")

print("Detected language is :" ,detection.lang )
print("Confidence is :", detection.confidence)
print("Language of the input text is :", constants.LANGUAGES[detection.lang])

print("All languages supported by a googletrans is:")
for i in constants.LANGUAGES :
    print(i,":",constants.LANGUAGES[i])

print("Total languages supported by googletrans is:", len(constants.LANGUAGES))
