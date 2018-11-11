#!/usr/bin/python3

import pyxel
import world


class App:
	def __init__(self):
		self.screen_width = 255
		self.screen_height = 255

		#Initialize the window
		pyxel.init(self.screen_width, self.screen_height, caption="Rogue Like")

		#Load assets
		pyxel.load("assets/rogue_like.pyxel")

		#Create world constructor
		self.w = world.World(self.screen_width, self.screen_height, 0)

		#Run the game
		pyxel.run(self.update, self.draw)

	def update(self):
		#Quit if 'q' is pressed
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
		if pyxel.btnp(pyxel.KEY_W):
			self.w.panRel(0, 1)
		if pyxel.btnp(pyxel.KEY_S):
			self.w.panRel(0, -1)

	def draw(self):
		#Clear the screen with black
		pyxel.cls(0)

		#Draw the background
		for x in range(int((self.screen_width + 1)/16)):
			for y in range(int((self.screen_height + 1)/16)):
				px = x * 16
				py = y * 16
				(bx, by) = self.w.toMapC(px, py)
				#If something is a wall, draw the wall
				if (self.w.getTileAt(x, y) == world.Tile.WALL):
					(px, py) = self.w.getBlockBase(px, py)
					pyxel.blt(px, py, 0, 0, 16, 16, 32)

		#Draw the player model
		pyxel.blt(0, 0, 0, 0, 0, 16, 16, 14)


App()
