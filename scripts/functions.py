# collection of functions that are used for nearly every recipe

import scripts.utils.util as util


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


# craft a recipe with the given slot index in the crafting-book
def craftSlot(slot):
  util.move("origin", slot)
  util.shiftClick()
  util.wait(0.1)
  util.move(slot, "output")
  util.shiftClick()
  util.wait(0.1)
  util.move("output", "origin")


# take items from left shulker box
def takeItems():
  util.resetView()
  util.viewLeft()
  emptyShulker()
  util.viewRight()

# put items into right shulker box
def dropItems():
  util.viewRight()
  fillShulker()
  util.viewLeft()
  util.wait(0.2)


if __name__ == "__main__":
  util.wait(5)
  pass