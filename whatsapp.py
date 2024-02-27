import webbrowser as web
import time
import pywhatkit
import keyboard

def whatsapp(number,message):
    numb='91'+ number
    mess=message
    open_chat="https://web.whatsapp.com/send?photo=" +numb+ "&text=" + mess
    web.open(open_chat)
    time.sleep(15)
    keyboard.press('enter')
    
def whatsapp_grp(group_id,message):
    open_chat="https://web.whatsapp.com/accpet?code=" +group_id
    web.open(open_chat)
    time.sleep(15)
    keyboard.write(message)
    time.sleep(1)
    keyboard.press('enter')