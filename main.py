#!/usr/bin/python3

import pyxel
import world
import player

godmode = 0

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

	def tryMove(self, x, y):
		(plx, ply) = (self.w.player().x, self.w.player().y)
		if (godmode or world.Tile.isClear(self.w.getTileAt(plx + x, ply + y))):
			self.w.player().x += x
			self.w.player().y += y
			return True
		print("That's a wall")
		return False

	def update(self):
		#Quit if 'q' is pressed
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()
		if pyxel.btnp(pyxel.KEY_W):
			self.tryMove(0, -1)
		if pyxel.btnp(pyxel.KEY_S):
			self.tryMove(0, 1)
		if pyxel.btnp(pyxel.KEY_A):
			self.tryMove(-1, 0)
		if pyxel.btnp(pyxel.KEY_D):
			self.tryMove(1, 0)


	def draw(self):
		#Clear the screen with black
		pyxel.cls(0)

		#Draw the background
		for x in range(int((self.screen_width + 1)/16 + 1)):
			for y in range(int((self.screen_height + 1)/16 + 1)):
				px = x * 16
				py = y * 16
				(bx, by) = self.w.toMapC(px, py)
				#If something is a wall, draw the wall
				if (self.w.getTileAt(bx, by) == world.Tile.WALL):
					(px, py) = self.w.getBlockBase(px, py)
					pyxel.blt(px, py, 0, 0, 16, 16, 32)

		#Draw the player model
		(plx, ply) = self.w.fromMapC(self.w.player().x, self.w.player().y)
		pyxel.blt(plx, ply, 0, 0, 0, 16, 16, 14)


App()
