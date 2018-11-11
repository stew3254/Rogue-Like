import item


class Inventory:
	pass


class Skills:
	def __init__(self, name, skillID, damage):
		self.name = name
		self.id = skillID
		self.damage = damage

    
class Player:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.health = 100
		self.skills = Skills()
		self.inventory = Inventory()
	
	def equip(self):
		print("Equipped")

	def consumeItem(self):
		print("Consumed")

	def addItem(self):
		print("Added")

	def dropItem(self):
		print("Dropped")
