import item


class Inventory:
	pass


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
		self.inventory = Inventory()
	
	def equip(self):
		print("Equipped")

	def consumeItem(self):
		print("Consumed")

	def addItem(self):
		print("Added")

	def dropItem(self):
		print("Dropped")

