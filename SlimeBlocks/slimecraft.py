import pynput
import keyboard
import pyautogui
from pynput.mouse import Button, Controller

import time

mouse = Controller()




# print current mouse position
def checkPos():
    while True:
        print(mouse.position)
        time.sleep(0.5)

# utilities
def rightClick():
    mouse.click(Button.right, 1)

def leftClick():
    mouse.click(Button.left, 1)

def viewLeft():
    for i in range(2):
        pyautogui.move(-800, 0)

def viewRight():
    for i in range(2):
        pyautogui.move(800, 0)

def shiftClick():
    keyboard.press('shift')
    mouse.click(Button.left, 1)
    keyboard.release('shift')

def secCraft():
    time.sleep(0.1)
    mouse.move(-700, 0)
    time.sleep(0.1)
    shiftClick()
    mouse.move(700, 0)
    time.sleep(0.1)
    shiftClick()
    

# functions

def takeBalls():
    rightClick()
    time.sleep(0.1)
    mouse.move(0, -61)
    leftClick()
    time.sleep(0.05)
    mouse.move(55, 0)
    keyboard.press('shift')
    mouse.click(Button.left, 2)
    keyboard.release('shift')
    time.sleep(0.05)
    mouse.move(-55, 85)
    time.sleep(0.05)
    leftClick()
    time.sleep(0.05)
    keyboard.press('e')
    keyboard.release('e')

def craftSlimes():
    # craft 1
    rightClick()
    time.sleep(0.1)
    mouse.move(-410, -121)
    time.sleep(0.1)
    shiftClick()
    mouse.move(775, 0)
    time.sleep(0.1)
    shiftClick()
    # craft 2 & 3
    secCraft()
    secCraft()
    # exit
    keyboard.press('e')
    keyboard.release('e')


def dropBalls():
    rightClick()
    time.sleep(0.1)
    
    # drop 1
    mouse.move(110, 199)
    time.sleep(0.1)
    shiftClick()
    time.sleep(0.05)
    # drop 2
    mouse.move(55, 0)
    time.sleep(0.1)
    shiftClick()
    time.sleep(0.05)
    # drop 1
    mouse.move(50, 0)
    time.sleep(0.1)
    shiftClick()
    time.sleep(0.05)
    # exit
    keyboard.press('e')
    keyboard.release('e')

    
    
    


def slimeMain():
    viewLeft()
    time.sleep(0.05)
    takeBalls()
    time.sleep(0.05)
    viewRight()
    time.sleep(0.05)
    craftSlimes()
    time.sleep(0.05)
    viewRight()
    time.sleep(0.05)
    dropBalls()
    time.sleep(0.05)
    viewLeft()
    time.sleep(0.05)

    # reset
    rightClick()
    time.sleep(0.1)
    keyboard.press('e')
    keyboard.release('e')

    


if __name__ == "__main__":
    time.sleep(5)
    
    while True:
        try:
            if keyboard.is_pressed('k'):
                print("Exit")
                break
            else:
                time.sleep(0.3)
                slimeMain()
        except:
            break
        
    
    
    #checkPos()
    
