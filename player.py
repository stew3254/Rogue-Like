import item


class Inventory:
	pass


class Player:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.inventory = Inventory()
	
	def consumeItem(self):
		pass

john = Player()
