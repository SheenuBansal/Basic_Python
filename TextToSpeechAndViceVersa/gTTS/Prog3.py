# Python program to translate
# speech to text and text to speech

import speech_recognition as sr
import pyttsx3, os
import playsound
from gtts import gTTS
from os import path
from pydub import AudioSegment
import ffmpeg
from ffprobe import FFProbe
# Initialize the recognizer
r1 = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



try:
    fh = open("Prog2text", "r")
    mytext = fh.read().replace("\n", " ")
    language = "en"

    to_speak = gTTS(text=mytext, lang=language, slow=False)
    to_speak.save("Prog3aud.mp3")

    src = "Prog3aud.mp3"
    dst = "Prog3.wav"
    sound = AudioSegment.from_mp3(src)
    audio2= sound.export(dst, format="wav")
    with sr.AudioFile("Prog3.wav") as source2:
        r1.adjust_for_ambient_noise(source2, duration=0.2)
        source = os.system("start Prog3.wav")
        os.system("start Prog3.wav")
        audio = r1.listen(source)

        # Using google to recognize audio
        MyText = r1.recognize_google(audio)
        MyText = MyText.lower()

        print("Did you say " + MyText)
        SpeakText(MyText)

except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

except sr.UnknownValueError:
    print("unknown error occured")