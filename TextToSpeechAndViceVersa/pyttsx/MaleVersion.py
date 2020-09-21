import pyttsx3 as speech
engine= speech.init()
engine.setProperty('rate',200)
engine.setProperty('volume',10.3)
engine.say('hello beta')
engine.say('Good Morning ')
engine.runAndWait()

# get details of speaking rate etc. in this way and
# then u can set whtevru want
rate = engine.getProperty("rate")
print(rate)

## get details of all voices available
voices = engine.getProperty("voices")
print(voices)

# set another voice
engine.setProperty("voice", voices[1].id)
engine.say("Good Morning Handsome")
engine.runAndWait()