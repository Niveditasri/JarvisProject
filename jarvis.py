import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import pyautogui
import keyboard
import pyjokes
import requests
from PyDictionary import PyDictionary as Diction
from googletrans import Translator
import datetime
from playsound import playsound
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import pyaudio
import speedtest

Assistant = pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',170)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()
# Speak('hello sir, hello')

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
            
        except:
            return "none"
        return query.lower()
# Speak('Hello I AM JARVIS')

def TaskExe():
    
    Speak("Hello, I am jarvis!")
    Speak("How can I help you?")

    def Music():
        Speak("Tell me the music")
        musicName=takecommand()
        pywhatkit.playonyt(musicName)
        Speak("Your song has been started, Enjoy maam")

    def Whatsapp():
        Speak("Tell me the phone number of the person")
        phone =int(takecommand())
        ph='+91'+phone
        Speak("Tell me the Message")
        msg=takecommand()
        Speak("Tell me the time")
        Speak("Time in hour!!")
        hour=int(takecommand())
        Speak("Tell in minutes!!")
        min=int(takecommand())
        pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
        Speak("Ok maam,Sending Whatsapp Message")
 
    def OpenApps():
        Speak("OK mam , wait a second !!")

        if 'code' in query:
            os.startfile(r"C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'telegram' in query:
            os.startfile(r"C:\\Users\\dell\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
        elif 'zoom' in query:
            os.startfile(r"C:\Users\dell\AppData\Roaming\Zoom\bin\Zoom.exe")
        elif 'facebook' in query:
            webbrowser.open(r"https://www.facebook.com/")
        elif 'instagram' in query:
            webbrowser.open(r"https://www.instagram.com/")
        elif 'google chrome' in query:
            os.startfile(r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        elif 'maps' in query:
            webbrowser.open(r"https://www.google.co.in/maps/@30.7687902,76.572797,17z")
        elif 'youtube' in query:
            webbrowser.open(r"https://www.youtube.com/")
        Speak("Your command has been completed")

    def Dict():
        Speak("Activate the dictionary")
        Speak("Tell me the problem")
        prob1=takecommand()
        if 'meaning' in prob1:
            prob1=prob1.replace("what is the","")
            prob1=prob1.replace("jarvis","")
            prob1=prob1.replace("of")
            prob1=prob1.replace("meaning of","")
            result=Diction.meaning(prob1)
            Speak(f"The Meaning for {prob1} is {result}")
        elif 'synonym' in prob1:
            prob1=prob1.replace("what is this","")
            prob1=prob1.replace("jarvis","")
            prob1=prob1.replace("of")
            prob1=prob1.replace("synonym of","")
            result=Diction.synonym(prob1)
            Speak(f"The synonym fro{prob1} is {result}")
        elif 'antonym' in prob1:
            prob1=prob1.replace("what is this","")
            prob1=prob1.replace("jarvis","")
            prob1=prob1.replace("of")
            prob1=prob1.replace("antonym of","")
            result=Diction.antonym(prob1)
            Speak(f"The antonym fro{prob1} is {result}")
        
        Speak("Exited Dictionary")

    def CloseApps():
        Speak("OK mam , wait a second !!")

        if 'code' in query:
            os.system("TASKKILL /F /im Code.exe")
        if 'telegram' in query:
            os.system("TASKKILL /F /im Telegram.exe")
        if 'zoom' in query:
            os.system("TASKKILL /F /im Zoom.exe")
        if 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")
        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
        if 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")
        if 'instagram' in query:
            os.system("TASKKILL /F /im chrome.exe")
        if 'google chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
        Speak("Your command has been completed")

    def YouTubeAuto():
        Speak("Whats your command ?")
        comm=takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')
        elif 'restart' in comm:
            keyboard.press('0')
        elif 'mute' in comm:
            keyboard.press('m')
        elif 'skip' in comm:
            keyboard.press('1')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'film mode' in comm:
            keyboard.press('t')
        Speak("Done sir")

    def ChromeAuto():
        Speak("Chrome automation started")
        command=takecommand()

        if 'Close in Tab' in command:
            keyboard.press_and_release('ctrl+w')
        elif 'Open in new tab' in command:
            keyboard.press_and_release('ctrl+t')
        elif 'Open in new window' in command:
            keyboard.press_and_release('ctrl+n')
        elif 'history' in command:
            keyboard.press_and_release('ctrl+h')
   
    def TakeHindi():
        command=sr.Recognizer()
        with sr.Microphone() as source:
           print("Listening......")
           command.pause_threshold=1
           audio=command.listen(source)

           try:
               print("Recognising...")
               query=command.recognize_google(audio,language='hindi')
               print(f"You said: {query}")
           except Exception as Error:
               return "none"
           return query.lower()
    
    def Tran():
        Speak("Tell me the line!")
        line=TakeHindi()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        Speak("The translation for this line is:"+Text)

    def screenshot():
        Speak("OK MAAM What should I name that file")
        path=takecommand()
        path1name= path+".png"
        path1="C:\\Users\\dell\\Desktop\\screenshot\\"+ path1name  
        kk=pyautogui.screenshot()
        kk.save(path1)
        os.startfile("C:\\Users\\dell\\Desktop\\screenshot\\")
        Speak("Here is your screenshot")

    def Youtube(term):
        web='https://www.youtube.com/results?search_query='+ term
        webbrowser.open(web)
        Speak("Done maam")
        pywhatkit.playonyt(term)

    def Temp():
        search="Temperature in lucknow"
        url=f"https://www.google.com/search?q={search}"
        r=requests.get(url)
        data=BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_="BNeawe").text
        Speak(f"The temperature outside is {temperature} celcuis")

    def SpeedTest():
        Speak("Checking speed...")
        speed=speedtest.Speedtest()
        downloading=speed.download()
        correctDown=int(downloading/800000)
        uploading=speed.upload()
        correctUpload=int(uploading/800000)

        if 'uploading' in query:
            Speak(f"The uploading speed is {correctUpload} mbp s")
        elif 'downloading' in query:
            Speak(f"The downloading speed is {correctDown} mbp s")
        else:
            Speak(f"The downloading is {correctDown} and the uploading speed is {correctUpload} mbp s")

    while True:
        
        query=takecommand()

        if 'hello' in query:
            Speak('Hello MAAM, I AM JARVIS')
            Speak('YOUR PERSONAL AI ASSISTANT')
            Speak('HOW MAY I HELP YOU')

        elif 'how are you' in query:
            Speak('I AM FINE MAAM')
            Speak('WHAT ABOUT YOU')

        elif 'You need a break' in query:
            Speak('OK MAAM YOU CAN CALL ME ANYTIME')
            Speak("Just say wake up jarvis")
            break

        # elif 'KYA HAAL HAI' in query:
        #     Speak('MAI BADIYA HUN AAP BATAO')
        # elif 'BYE' in query:
        #     Speak("OKMAAMBYE")
        #     break
        # elif 'MAI ACHA HUN' in query:
        #     Speak("main bhi")

        elif 'youtube search' in query:
            Speak("OK MAAM THIS IS WHAT I FOUND FOR YOUR SEARCH")
            query=query.replace("Jarvis","")
            query=query.replace("YouTube search","")
            web='https://www.youtube.com/results?search_query='+ query
            webbrowser.open(web)
            pywhatkit.playonyt(web)
            Speak("Done maam")
            # Youtube(query)

        # elif 'Google Search' in query:
        #     import wikipedia as googleScrap
        #     query=query.replace("Jarvis","")
        #     query=query.replace("Google search","")
        #     query=query.replace("Google","")
        #     Speak("OK MAAM THIS IS WHAT I FOUND FOR YOUR SEARCH")
        #     pywhatkit.search(query)
        #     try:
        #         result=googleScrap.summary2(query,3)
        #         Speak(result)
        #     except:
        #         Speak("No speakable content")

        elif 'Website' in query:
            Speak("OK MAAM, LAUNCHING....")
            query=query.replace("Jarvis","")
            query=query.replace("Website","")
            query=query.replace(" ","")
            web1=query.replace("open","")
            web2="https://www."+web1+".com"
            webbrowser.open(web2)
            Speak("Launched!!")

        elif 'launch' in query:
            Speak("OK MAAM PLEASE TELL ME THE NAME OF THE WEBSITE")
            name=takecommand()
            web="https://www."+name+".com"
            webbrowser.open(web)
            Speak("Done sir!!")

        elif 'facebook' in query:
            Speak("OK MAAM PLEASE TELL ME THE NAME OF THE WEBSITE")
            # name=takecommand()
            # web="https://www."+web1+".com"
            webbrowser.open("https://www.facebook.com")
            Speak("Launched!!")

        elif 'music' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Searching wikipedia.....")
            query=query.replace("Jarvis","")
            query=query.replace("Wikipedia","")
            wiki=wikipedia.summary(query,2)
            Speak(f"According to wikipedia: {wiki}")

        elif 'whatsapp message' in query:
            Whatsapp()
     
        elif 'screenshot' in query:
            screenshot()

        elif 'open code' in query:
            OpenApps()
        
        elif 'open telegram' in query:
            OpenApps()

        elif 'open zoom' in query:
            OpenApps()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open google chrome' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'close Code' in query:
            CloseApps()
        
        elif 'close telegram' in query:
            CloseApps()

        elif 'close zoom' in query:
            CloseApps()

        elif 'close facebook' in query:
            CloseApps()

        elif 'close instagram' in query:
            CloseApps()

        elif 'close google chrome' in query:
            CloseApps()

        elif 'close maps' in query:
            CloseApps()

        elif 'close youtube' in query:
            CloseApps()

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('1')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'pause' in query:
            keyboard.press('k')

        elif 'youtube tool' in query:
            YouTubeAuto()
        
        elif 'Close in Tab' in query:
            keyboard.press_and_release('ctrl+w')

        elif 'Open in new tab' in query:
            keyboard.press_and_release('ctrl+t')

        elif 'Open in new window' in query:
            keyboard.press_and_release('ctrl+n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl+h')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'jokes' in query:
            get=pyjokes.get_joke()
            Speak(get)

        elif 'repeat my words' in query:
            Speak("Speak maam!")
            jj=takecommand()
            Speak(f"You said :{jj}")

        elif 'my location' in query:
            Speak("Ok maam, wait a second!")
            webbrowser.open("https://www.google.co.in/maps/@30.7688441,76.5734856,16.64z")

        elif 'dictionary' in query:
            Dict()

        elif 'i love you' in query:
            Speak("I Love you too maam. You are too beautiful and too sweet. I have never met such a prettiest lady. You are women in disguise.")

        elif 'alarm' in query:
            Speak("Enter the time !")
            time=input(": Enter the time:")
            while True:
                Time_AC= datetime.datetime.now()
                now= Time_AC.strftime("%H:%M:%S")
                if now==time:
                    Speak("Time to wake up maam")
                    playsound('ringtone.mp3')
                    Speak("Alarm closed")
                elif now>time:
                    break
        
        elif 'translator' in query:
            Tran()

        elif 'remember that' in query:
            rememberMsg = query.replace("remember that","")
            rememberMsg = rememberMsg.replace("jarvis","")
            Speak("You told me to remind you that: "+rememberMsg)
            remember = open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif 'What do you remember' in query:

            remember = open('data.txt','r')
            Speak("You told me that "+remember.read())

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("Jarvis","")
            query = query.replace("google serach","")
            query = query.replace("google","")
            Speak("This what i found on the web")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak("No Speakable data available")

        elif 'temperature' in query:
            Temp()

        elif 'downloading speed' in query:
            SpeedTest()

        elif 'uploading speed' in query:
            SpeedTest()

        elif 'internet speed' in query:
            SpeedTest()

        elif 'how to' in query:
            Speak("Getting data from the internet !")
            op=query.replace("jarvis","")
            max_result=1
            how_to_func= search_wikihow(op,max_result)
            assert len(how_to_func)==1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

TaskExe()
Speak("Hello maam, I am your jarvis !!")