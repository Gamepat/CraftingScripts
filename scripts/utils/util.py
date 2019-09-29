import coords as cr
import keyboard
import pyautogui
from pynput.mouse import Button, Controller
import time



mouse = Controller()


# utilities
def rightClick():
  mouse.click(Button.right, 1)

def leftClick():
  mouse.click(Button.left, 1)

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



# calculates the relative distance between two coordinates
def relDist(src, dest): 
  xDist = cr.gui[dest]["x"] - cr.gui[src]["x"]
  yDist = cr.gui[dest]["y"] - cr.gui[src]["y"]

  return xDist, yDist





if __name__ == "__main__":
  x, y = relDist("origin", "output")

  print(x, y)