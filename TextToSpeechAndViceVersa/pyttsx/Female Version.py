import pyttsx3 as speech
engine = speech.init()
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)
engine.setProperty('rate',200)
engine.setProperty('volume',10.3)
engine.say('aur batao kya haal hai')
engine.runAndWait()

voices1 = engine.getProperty('voices')

for voice in voices1:
    # to get the info. about various voices in our PC
    print("Voice:")
    print("ID: %s" % voice.id)
    print("Name: %s" % voice.name)
    print("Age: %s" % voice.age)
    print("Gender: %s" % voice.gender)
    print("Languages Known: %s" % voice.languages)