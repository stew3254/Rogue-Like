#!/usr/bin/python3

import pyxel


class App:
	def __init__(self):
		pyxel.init(255, 255, caption="Rogue Like")
		pyxel.run(self.update, self.draw)

	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):
			pyxel.quit()

	def draw(self):
		pyxel.cls(0)
		pyxel.rect(10, 10, 20, 20, 11)
	

App()
