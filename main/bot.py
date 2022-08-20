#importing python modules
import pyautogui
import time
import pytesseract
import re
import logging
from datetime import date
import os

#os.system('scrcpy --window-title "Oppo F11" -f -m 1920')
#time.sleep(10)
#Global variables
total = 0
saved = 0
not_saved = 0
t1=time.time()

today = date.today()
aaja = today.strftime("%m-%d-%y")
logfile = (str(aaja) + ".log")
#Logging Everything
logging.basicConfig(filename=(logfile), 
					format='%(asctime)s %(message)s', 
					filemode='a')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

#Tesseract OCR Path
path_of_tesseract = "C:/Users/prabe/scoop/apps/tesseract/current/tesseract.exe"

#some important coordinate variables, change as your screen

#Coordinate of "🟥New Snap" text
scan_1st_chat_co = (569,120, 75, 20)
#Coordinate of "Save in Chat" text
scan_save_chat_co = (500,450, 200, 200)
#Coordinate of Chat_button
chat_button = (565,675, 100, 100)
homepage_heading =(635,35, 100, 50)
#Coordinator of sender name
personname = (560,95, 200, 20)
#Confirm New Snap
new_snap_chat = (550,100, 100, 50)
#Non_new_chat = False
is_in_chat = (505,370, 350, 400)

def person_name():
    pytesseract.pytesseract.tesseract_cmd = path_of_tesseract
    cap = pyautogui.screenshot(region=(personname))
    tesstr = pytesseract.image_to_string(cap,lang ='eng+nep')
    scan = tesstr
    chars =r'[\n]'
    chat_name = (re.sub(chars, '', scan))
    formatted_chat =('\033[1m' + '%20s' % chat_name +'\033[0m' + " : ")
    global snap_banda
    snap_banda = formatted_chat
    return formatted_chat

def snap_homepage():
    pytesseract.pytesseract.tesseract_cmd = path_of_tesseract
    cap = pyautogui.screenshot(region=(homepage_heading))
    tesstr = pytesseract.image_to_string(cap,lang ='eng')
    scan = tesstr
    chars =r'[\n @®>1234567890G!.b]'
    message = (re.sub(chars, '', scan)).lower()
    if message == "chat":
        print(">>%50s<<" % "Looking for Snaps from other Person")
        logger.info(">>%50s<<" % "Looking for Snaps from other Person")
        return "yes"
    elif pyautogui.locateOnScreen('new_snaps_homepage.png', region=(chat_button),confidence=0.9) or pyautogui.locateOnScreen('new_snaps_chats_home.png', region=(chat_button),confidence=0.9):
        return "yes"
    elif pyautogui.locateOnScreen('new_snaps_click_once.png', region=(chat_button),confidence=0.9) or pyautogui.locateOnScreen('new_snaps_chats_nohome.png', region=(chat_button),confidence=0.9):
        return "yes"
    elif pyautogui.locateOnScreen('chat_button_empty.png', region=(chat_button),confidence=0.9) or pyautogui.locateOnScreen('chat_buttom_empty_clicked.png', region=chat_button,confidence=0.9):
        return "yes"
    else:
        return "no"

def is_inside_chats():
    print("%30s"%"Sorry, I was Looking your dm's.")
    logger.info("%30s"%"Sorry, I was Looking your dm's.")
    pyautogui.moveTo(675, 150)
    time.sleep(0.5)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.moveTo(675, 150)
    time.sleep(0.5)
    pyautogui.click(button='right')
    time.sleep(1)
    print("Succesfully in SnapHome")
    logger.info("Succesfully in SnapHome")
    time.sleep(2)

def check_chat_button():
    pyautogui.moveTo(675, 150)
    if pyautogui.locateOnScreen('new_snaps_click_once.png', region=(chat_button),confidence=0.9) or pyautogui.locateOnScreen('new_snaps_chats_nohome.png', region=(chat_button),confidence=0.9):
        click_chat_button()
        return "moved_to_chatpage"
    elif pyautogui.locateOnScreen('new_snaps_homepage.png', region=(chat_button),confidence=0.9) or pyautogui.locateOnScreen('new_snaps_chats_home.png', region=(chat_button),confidence=0.9):
        return "already_in_chatpage"
    elif pyautogui.locateOnScreen('chat_button_empty.png', region=(chat_button),confidence=0.9) or pyautogui.locateOnScreen('chat_buttom_empty_clicked.png', region=chat_button,confidence=0.9):
        print("%50s" %"No New Snaps")
        click_chat_button()
        print("The last snap was from : "+ person_name())
        logger.info("The last snap was from : "+ person_name())
        print
    elif pyautogui.locateOnScreen('intra_chat.png', region=(is_in_chat),confidence=0.9):
        is_inside_chats()
    else:
        print("Some error occured : Chat Button Not Found")
        logger.info("Some error occured : Chat Button Not Found")
        quit()

def click_chat_button():
    time.sleep(2)
    pyautogui.moveTo(600, 730)
    time.sleep(0.3)
    pyautogui.click()

def new_snap_check():
    time.sleep(1)
    if pyautogui.locateOnScreen('new_snap.png', region=(new_snap_chat),confidence=0.9,grayscale=True):
        print("There are new snaps from : " + person_name())
        logger.info("There are new snaps from : " + person_name())
        return "new_snaps"
    elif pyautogui.locateOnScreen('new_chat.png', region=(new_snap_chat),confidence=0.9,grayscale=True):
        print("There are some chats from : " + person_name())
        logger.info("There are some chats from : " + person_name())
        click_first_snap()
        print("You've 30 seconds to talk to this person. Use It. I'm sleeeping till that.")
        logger.info("You've 30 seconds to talk to this person. Use It. I'm sleeeping till that.")
        time.sleep(30)
        pyautogui.moveTo(675, 150)
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(1)
        pyautogui.moveTo(675, 150)
        time.sleep(0.5)
        pyautogui.click(button='right')
        print("%30s"%"New chats cleared.")
        logger.info("%30s"%"New chats cleared.")
        new_snap_check()
    elif pyautogui.locateOnScreen('intra_chat.png',confidence=0.9):
        is_inside_chats()
    else:
        if main_bool():
            click_chat_button()
            new_snap_check()
        else:
            print("%50s"%"Can't Find New Snaps")
            logger.info("%50s"%"Can't Find New Snaps")
            quit()

def personal_chat():
    if pyautogui.locateOnScreen('intra_chat.png',confidence=0.9):
        is_inside_chats()
        return "pm"

def check_every_time():
    if personal_chat() == "pm" or snap_homepage() == "yes":
        return False
    else:
        return True
def click_first_snap():
    time.sleep(0.5)
    pyautogui.moveTo(575, 110)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)

def long_press():
    pyautogui.moveTo(675, 400)
    pyautogui.mouseDown()
    time.sleep(0.4)
    pyautogui.mouseUp()
    time.sleep(1)

def back_to_received_snap():
    pyautogui.moveTo(675, 150)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(0.5)

def next_snap():
    pyautogui.moveTo(675, 250)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)

def save_chat():
    try:
        save_in_chat_box = pyautogui.locateOnScreen('save_in_chat.png', confidence=0.9)
        x, y = pyautogui.center(save_in_chat_box)
        pyautogui.moveTo(x,y)
        time.sleep(0.3)
        pyautogui.click()
        print("%50s" % "Snap Saved Successfully.")
        logger.info("%50s" % "Snap Saved Successfully.")
        time.sleep(1)
        return "success"
    except TypeError:
        print("%50s" %"Not Saved :  Snap is sent with play limit")
        logger.info("%50s" %"Not Saved :  Snap is sent with play limit")
        return "no_save_button"

def peoplewise_snaps():
    while check_every_time():
        long_press()
        global total, saved, not_saved
        if save_chat()=="success":
            total = total+1
            saved = saved + 1
            next_snap()
        else:
            back_to_received_snap()
            time.sleep(9)
            total = total+1
            not_saved = not_saved + 1

def main_bool():
    a = bool(check_chat_button() == "moved_to_chatpage" or check_chat_button() == "already_in_chatpage")
    return a

def main():
    while main_bool():
        new_snap_check()
        click_first_snap()
        peoplewise_snaps()
        print("Watching all loaded snaps from {} completed.".format(person_name()))
        logger.info("Watching all loaded snaps from {} completed.".format(person_name()))
        print("\n")

main()

#Time Calculations
t2 = time.time()
time_taken  = (t2-t1)
time_wasted=time.strftime('%H Hours %M Minutes %S Seconds', time.gmtime(time_taken))

print("%50s"%"")
print("%50s"%"")
print("%50s"%"")
print("%70s"%"<--- Snap's Received as of {} -->".format(today.strftime("%B %d, %Y")))
logger.info("%70s"%"<--- Snap's Received as of {} -->".format(today.strftime("%B %d, %Y")))
print("%50s"%"")
logger.info("%50s"%"Saved Snaps: {}".format(saved))
print("%50s"%"Saved Snaps: {}".format(saved))
logger.info(("%50s"%"Snaps with Limit: {}".format(not_saved)))
print("%50s"%"Snaps with Limit: {}".format(not_saved))
print("%50s"%"Total Snaps: {}".format(total))
logger.info("%50s"%"Total Snaps: {}".format(total))
print("%50s"%"")
print("%50s"%"Total time wasted : {} ".format(time_wasted))
logger.info("%50s"%"Total time wasted : {} ".format(time_wasted))
print("%50s"%"")
print("%50s"%"")