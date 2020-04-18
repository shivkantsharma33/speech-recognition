import speech_recognition as sr
AUDIO_FILE=("song_2.wav")

r=sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)


try:
    print("audio file contains  :"+ r.recognize_google(audio))

except sr.UnknownValueError:
    print("google recognizer could not understand")

except sr.RequestError:
    print("couldn't get the result from google")