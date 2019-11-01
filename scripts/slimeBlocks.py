import utils.util as util
import functions as fc
import keyboard

key = 'k'


def craftSlimeBlocks():
  fc.takeItems()
  util.rightClick()
  util.wait(0.3)
  
  # recipe-slots can change when restarting the game,
  # so make sure the right slot indexes are selected
  fc.craftSlot("slime1")
  fc.craftSlot("slime2")
  fc.craftSlot("slime2")
  util.exitInv()
  fc.dropItems()


if __name__ == "__main__":
  util.wait(5)
  
  while True:
    try:
      if keyboard.is_pressed(key):
        print("Stopped")
        break
      else:
        util.wait(0.1)
        craftSlimeBlocks()
    except:
      break  