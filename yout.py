import pyttsx3           #convert text to speech
import speech_recognition as sr     #take input as speech


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 110)
file=open("mytxt.txt","r+")
text=file.read()
engine.runAndWait()
def speak(audio):              #speak anything that you want it to speak
    engine.say(audio)
    engine.runAndWait()
speak(text)