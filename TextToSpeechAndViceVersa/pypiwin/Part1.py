#SAPI.SpVoice is the driver in windows machine.

import win32com.client as mouth
voice = mouth.Dispatch("SAPI.SpVoice")
word_to_say = input("Enter you want to speak :")
voice.Speak(word_to_say)