import speech_recognition as sr
import moviepy.editor as mp
clip =mp.VideoFileClip(r"C:\\Users\\vb\\PycharmProjects\\FirstProg\\TextToSpeechAndViceVersa\\SpeechonWomensRighttoVote.mp3")
clip.audio.write_audiofile(r"C:\\Users\\vb\\PycharmProjects\\FirstProg\\TextToSpeechAndViceVersa\\SpeechonWomensRighttoVote.wav")
r = sr.Recognizer()
audio= sr.AudioFile("C:\\Users\\vb\\PycharmProjects\\FirstProg\\TextToSpeechAndViceVersa\\SpeechonWomensRighttoVote.wav")

with audio as source :
    audio_file = r.record(source)

result = r.recognize_google(audio_file, language='en-IN', show_all=True)
result1 = ' '.join(map(str, result))
# Exporting the result to a file
with open('C:/Users/vb/PycharmProjects/FirstProg/TextToSpeechAndViceVersa/recognized.txt','w') as file :
    file.write("Recognized Speech:") 
    file.write("\n") 
    file.write(result1)
    print("Ready!")
    print(result1)
