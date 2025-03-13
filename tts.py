import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)  
engine.setProperty('volume', 1)  

text = "Hello, this is a text-to-speech API demonstration."

engine.say(text)

engine.runAndWait()