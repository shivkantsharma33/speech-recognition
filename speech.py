import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("say somthing")
    audio=r.listen(source)
    print("Got it!")
    
try:
    print("you said \n" + r.recognize_google(audio))
    print("\n audio is recorded")
    
except Exception as e:
    print(e)

with open("microphone.result.wav","wb") as f:
    f.write(audio.get_wav_data())
    
#with open("microphone.result.wav","wb") as f:
 #   e.write(audio.get_wav_data())