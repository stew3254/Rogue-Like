import item

class Skill:
	def __init__(self):
		self.name = ""
		self.id = 0
		self.damage = 0

	def addSkill(self, name, skillID, damage):
		print("Added skill")
    
class Player:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.health = 100
		self.skills = []
		self.inventory = []
                self.isLeft = False
	
	def equip(self, itemID):
		print("Equipped")

	def consumeItem(self, itemID):
            invSlot = self.getInventoryIndex(itemID)
            if invSlot >= 0:
                self.Inventory[invSlot].count -= 1
                if self.Inventory[invSlot].count == 0:
                    self.Inventry.pop(invSlot)

	def addItem(self, item):
            invSlot = self.getInventoryIndex(itemID)
            if invSlot >= 0:
                self.Inventory[invSlot].count += 1
            else:
                self.Inventory.append(_ItemRegistry.createItemInstance(itemID)          
        def hasItem(self, itemID):
            for item in Inventory:
                if item.itemID == itemID:
                    return True
            return False

        def getInventoryIndex(self, itemID):
            for i in range(len(Inventory)):
                if Inventory[i].itemID == itemID:
                    return i 
            return -1

