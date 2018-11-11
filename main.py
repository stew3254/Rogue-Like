#!/usr/bin/python3

import pyxel


class App:
	def __init__(self):
		#Initialize the window
		pyxel.init(255, 255, caption="Rogue Like")

		#Load assets
		pyxel.load("assets/rogue_like.pyxel")

		#Run the game
		pyxel.run(self.update, self.draw)

	def update(self):
		#Quit if 'q' is pressed
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

	def draw(self):
		#Clear the screen with black
		pyxel.cls(0)

		#Draw the player model
		pyxel.blt(0, 0, 0, 0, 0, 16, 16)


App()
