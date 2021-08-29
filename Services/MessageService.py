import pyautogui as pg
import webbrowser as web
import time
def sendMessage(userData):

    first = True
    for phoneNumber,message in userData:
        time.sleep(4)
        web.open("https://web.whatsapp.com/send?phone="+f'+90{phoneNumber}'+"&text="+message)
        if first:
            time.sleep(6)
            first=False
        width,height = pg.size()
        pg.click(width/2,height/2)
        time.sleep(4)
        pg.press('enter')
        time.sleep(4)
        pg.hotkey('ctrl', 'w')
