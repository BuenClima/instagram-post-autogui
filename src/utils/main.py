import time
import pyautogui
import pyperclip

class Mouse:

    def locate_on_screen(capture):
        return pyautogui.locateOnScreen(capture)

    def click(position = None):
        pyautogui.leftClick(position)

    def move_and_click(position):
        pyautogui.moveTo(position[0], position[1])
        pyautogui.leftClick()

class KeyBoard:

    def copy_and_paste(string):
        pyperclip.copy(string)
        pyautogui.hotkey("ctrl", "v")
        pyperclip.copy("")

    def write(string):
        pyautogui.typewrite(string)

    def tab():
        pyautogui.press('tab')

    def enter():
        pyautogui.press('enter')

    def search_bar():
        pyautogui.hotkey('ctrl', 'l')

    def delete():
        pyautogui.press('delete')

class Logger: 
    def log(string):
        print(string)

def get_tka_caption():
    return "Some caption #some @user"

def sleep(seconds):
    time.sleep(seconds)