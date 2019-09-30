# collection of functions that are used for nearly every recipe

import utils.util as util


# take everything from a full shulkerbox
def emptyShulker():
  util.rightClick()
  util.wait(0.1)
  util.move("origin", "shulkerEmpty")
  util.leftClick()
  util.move("shulkerEmpty", "doubleSlot")
  util.extract()
  util.move("doubleSlot", "tempStore")
  util.leftClick()
  util.exitInv()


# empties all the blocks from the inventory that are the same as hotbar slot 9
def fillShulker():
  util.rightClick()
  util.wait(0.1)
  util.move("origin", "hot9")
  util.rightClick()
  util.extract()
  util.leftClick()
  util.shiftClick()
  util.exitInv()


if __name__ == "__main__":
  util.wait(5)
  #emptyShulker()
  fillShulker()