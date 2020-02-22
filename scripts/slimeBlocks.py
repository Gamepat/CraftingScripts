import scripts.utils.util as util
import scripts.functions as fc
import keyboard

key = 'k'
recipe = 1


def craftSlimeBlocks():
  fc.takeItems()
  util.rightClick()
  util.wait(0.3)
  
  # recipe-slots can change when restarting the game,
  # so make sure the right slot indexes are selected
  if recipe == 1:
    for x in range(3):
      fc.craftSlot("slime1")
  
  elif recipe == 2:
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