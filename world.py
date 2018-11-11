#!/usr/bin/python3

import math
import enum
import random

class Tile(enum.Enum):
  EMPTY = 0
  WALL = 1

class World:
# Construct a world in a window of pixel dimensions given, seeded
  def __init__(self, width, height, seed):
    self.cx = width * 0.5
    self.cy = height * 0.5
    self.bx = math.ceil(width / 16)
    self.by = math.ceil(height / 16)
    self.level = 0
    print("world constructor called")

  def toMapC(self, x, y):  # Pixel coords -> map coords
    return ((x - self.cx) / 16, (y - this.cy) / 16)

  def fromMapC(self, x, y):  # Map coords -> pixel coords
    return (x * 16 + self.cx, y * 16 + this.cy)

  def getBlockBase():
    return ((x - self.cx) - (x - self.cx) % 16 + self.cx, (y - self.cx) - (y - self.cx) % 16 + self.cx)

  def getTileAt(self, x, y):  # Tile at (x, y) in map coords
    if (abs(x) < 5 and abs(y) < 5):
      return Tile.EMPTY
    else:
      return Tile.WALL

  def addEnt(ent):  # Put entity on the map
    ents.push(ent)

  def getEnts():  # Get master entity list
    return []

  ents = []
  level = 0
  grand = random.Random()
  lrand = random.Random()
  

  
