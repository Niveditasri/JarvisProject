from os import startfile
from click import BaseCommand
from pyautogui import click
from keyboard import press
from keyboard import write
from keyboard import press_and_release
from time import sleep
import pyttsx3
import speech_recognition as sr
import webbrowser as web

from jarvis import Speak, takecommand
def WhatsappMsg(name,message):
    startfile("https://web.whatsapp.com/")
    sleep(10)
    click(x=1539, y=772)
    sleep(1)
    write(name)
    sleep(1)
    click(x=1805, y=63)
    sleep(1)
    click(x=784, y=958)
    sleep(1)
    write(message)
    press("enter")
WhatsappMsg('chapran','hello')
def WhatsappCall(name):
    startfile("https://web.whatsapp.com/")
    sleep(10)
    click(x=1539, y=772)
    sleep(1)
    write(name)
    sleep(1)
    click(x=1805, y=63)
    sleep(1)
    click(x=784, y=958)
    sleep(1)
    
def ChromeAuto (command):
    while true:
        query=str(command)
        if 'new tab' in query:
            press_and_release('ctrl+t')
        elif 'close tab' in query:
            press_and_release('ctr+w')
        elif 'new window' in query:
            press_and_release('ctrl+n')
        elif 'history' in query:
            press_and_release('ctrl+h')
        elif 'download' in query:
            press_and_release('ctrl+j')
        elif 'bookmark' in query:
            press_and_release('ctrl+d')
            press("enter")
        elif 'incognito' in query:
            press_and_release('ctrl+shift+n')
        elif 'switch tab' in query:
            tab=query.replace("switch tab","")
            Tab=tab.replace("to","")
            num = Tab
            bb=f'ctrl+{num}'
            press_and_release(bb)
        elif 'open' in query:
            name=query.replace("open ","")
            NameA= str(name)
            if'youtube' in NameA:
                web.open("https://www.youtube.com/")
            else:
                string ="https://www."+NameA+".com"
                string_2=string.replace(" ","")
                web.open(string_2)