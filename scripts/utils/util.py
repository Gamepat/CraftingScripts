import scripts.utils.coords as cr
import keyboard
import pyautogui
from pynput.mouse import Button, Controller
import time



mouse = Controller()


# utilities
def wait(seconds):
  time.sleep(seconds)

def rightClick():
  mouse.click(Button.right, 1)

def leftClick():
  mouse.click(Button.left, 1)

def extract():
  keyboard.press('shift')
  mouse.click(Button.left, 2)
  keyboard.release('shift')

def shiftClick():
  keyboard.press('shift')
  mouse.click(Button.left, 1)
  keyboard.release('shift')

def viewLeft():
  for i in range(2):
    pyautogui.move(-800, 0)

def viewRight():
  for i in range(2):
    pyautogui.move(800, 0)

def exitInv():
  wait(0.05)
  keyboard.press('e')
  keyboard.release('e')
  wait(0.05)

# this function opens the crafting table for a short moment to reset the view
# needed for some reason, otherwise the player would turn to far
def resetView():
  rightClick()
  wait(0.1)
  keyboard.press('e')
  keyboard.release('e')
  wait(0.05)


# calculates the relative distance between two coordinates
def relDist(src, dest): 
  xDist = cr.gui[dest]["x"] - cr.gui[src]["x"]
  yDist = cr.gui[dest]["y"] - cr.gui[src]["y"]

  return xDist, yDist


# moves the mouse from he source to the destination coordinates
def move(src, dest):
  x, y = relDist(src, dest)
  mouse.move(x, y)
  time.sleep(0.05)




if __name__ == "__main__":
  pass