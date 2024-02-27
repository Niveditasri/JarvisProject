import pyttsx3
import speech_recognition as sr
import webbrowser
import os
import wikipedia
import pywhatkit
Assistant = pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
# print(voices)
Assistant.setProperty('voices',voices[0].id)
def takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold=1
        audio=command.listen(source)

        try:
            print("Recognising...")
            query=command.recognize_google(audio,language='en-in')
            print(f"You said: {query}")
        except Exception as Error:
            return "none"
        return query.lower()

def Speak(audio):
    print("  ")
    print(f": {audio}")
    Assistant.say(audio)
    Assistant.runAndWait()
    print("  ")
def Youtube(term):
    web='https://www.youtube.com/results?search_query='+ term
    webbrowser.open(web)
    Speak("Done maam")
    pywhatkit.playonyt(term)
Speak('Hello I AM JARVIS')
Youtube('Shahrukh khan')   