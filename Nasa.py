import requests
import os
import pyttsx3
from PIL import Image 

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print("   ")
    
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print("   ")
    
    
Api_key = "nFtlKr7by4DpvRTkz7IMS42UnqWbNuWknyOWmPJe"
def NasaNews(Date):
    Speak("Extracting data from NASA")
    Url = "https://api.nasa.gov/planetary/apod?api_key="+str(Api_key)
    
    Params = {'date':str(Date)}
    
    r=requests.get(Url,params = Params)
    Data =r.json()
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r=requests.get(Image_Url)
    FileName=str(Date) + '.jpg'
    with open(FileName,'wb') as f:
        f.write(Image_r.content)
    #print(FileName)
    # print(Title)
    # print(Info)
    Path_1 ="C:\\Users\\dell\\Desktop\\Jarvis\\"+str(FileName)
    Path_2 ="C:\\Users\\dell\\Desktop\\Jarvis\\NasaDatabase\\"+str(FileName)
    
    os.rename(Path_1,Path_2)
    img = Image.open(Path_2)
    img.show()
    Speak("Title:{Title}")
    Speak("According to NASA: {Info}")
NasaNews('2021-01-01')
    
    