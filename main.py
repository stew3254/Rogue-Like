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
		self.derp = world.World(self.screen_width, self.screen_height, 0)

		#Run the game
		pyxel.run(self.update, self.draw)

	def update(self):
		#Quit if 'q' is pressed
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

	def draw(self):
		#Clear the screen with black
		pyxel.cls(0)

		#Draw the background
		for x in range(int((self.screen_width + 1)/16)):
			for y in range(int((self.screen_height + 1)/16)):

				#If something is a wall, draw the wall
				if (self.derp.getTileAt(x, y) == world.Tile.WALL):
					pyxel.blt(x*16, y*16, 0, 0, 16, 16, 32)

		#Draw the player model
		pyxel.blt(0, 0, 0, 0, 0, 16, 16)


App()
