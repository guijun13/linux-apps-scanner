import pyautogui
import keyboard
import time
import threading

tab_pressed = False
tab_counter = 0

def tab_handler(e):
    global tab_pressed, tab_counter

    if not tab_pressed:
        tab_pressed = True
        tab_counter_thread = threading.Thread(target=start_counter)
        tab_counter_thread.start()
    else:
        tab_pressed = False
        tab_counter = 0

def start_counter():
    global tab_counter

    while tab_pressed:
        time.sleep(1)
        tab_counter += 1

        if tab_counter >= 3:
            keyboard.press_and_release('enter')
            keyboard.press_and_release('esc')
            tab_counter = 0
            SystemExit

if __name__ == "__main__":
    pyautogui.hotkey('winleft', 'a')
    keyboard.on_press_key('tab', tab_handler)

    keyboard.wait('esc')
