# Python program to translate
# speech to text and text to speech

import speech_recognition as sr
import pyttsx3, os
from gtts import gTTS
from pydub import AudioSegment
import ffmpeg,playsound
from ffprobe import FFProbe
import time
# Initialize the recognizer
r1 = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

with sr.AudioFile("Sample1.wav") as source2:
    r1.adjust_for_ambient_noise(source2, duration=0.2)
    # listens for the user's input
    audio2 = r1.record(source2)

    try :
        # Using google to recognize audio
        MyText = r1.recognize_google(audio2)
        MyText = MyText.lower()

        print("Did you say " + MyText)
        SpeakText(MyText)


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")


### If you want to read an tammil language, we can implement like :
#print(“Text: “+r.recognize_google(audio_text, language = “ta-IN”))
