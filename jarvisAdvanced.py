import pyttsx3
import speech_recognition as sr
import whatsapp

Assistant = pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
# print(voices)

Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',250)

def Speak(Text):
    print("   ")
    Assistant.say(Text)
    print(f": {Text}")
    print("   ")
    Assistant.runAndWait()
# Speak('hello sir, hello')

def takecommand():
    command=sr.Recognizer()
    with sr.Microphone() as source:
        print("            ")
        print("Listening......")
        command.pause_threshold=1
        audio=command.listen(source)

        try:
            print("Recognising...")
            query=command.recognize_google(audio,language='en-in')
            print(f"You said: {query}\n")
        except:
            return "None"
        
        return query.lower()
    
def TaskGui():
    while True:
        command = takecommand()
        if 'hello' in query:
            Speak("Hello sir, how are you ")
        elif 'whatsapp message' in query:
            query=query.replace("jarvis","")
            query=query.replace("send","")
            query=query.replace("whatsapp message","")
            query=query.replace("to","")
            name=query
TaskGui()
            