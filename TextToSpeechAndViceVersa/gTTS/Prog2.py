from gtts import gTTS
import os

fh = open("Prog2text", "r")
mytext= fh.read().replace("\n"," ")
language = "fr"

to_speak=gTTS(text=mytext,lang=language,slow = False )
to_speak.save("Prog2aud.mp3")
os.system("start Prog2aud.mp3")