from gtts import gTTS
import gtts
import os
from playsound import playsound
txt = "Hello, How are you? I am fine thank you."
language = 'fr'


to_speak = gTTS(txt,lang=language,slow= False)
to_speak.save("Prog1aud.mp3")
os.system("start Prog1aud.mp3")

#plasound can also be used to play the file
playsound("Prog1aud.mp3")

#all available languages along with their IETF tag
print(gtts.lang.tts_langs())