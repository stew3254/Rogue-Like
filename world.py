#!/usr/bin/python3

import math
import enum
import random

class Player:


  x = 0
  y = 0

class Tile (enum.Enum):
  EMPTY = 0
  WALL = 1

  @classmethod
  def isClear(self, tile):
    if (tile == Tile.EMPTY):
      return True
    return False

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
    return ((x - self.cx) / 16, (y - self.cy) / 16)

  def fromMapC(self, x, y):  # Map coords -> pixel coords
    return (x * 16 + self.cx, y * 16 + self.cy)

  def getBlockBase(self, x, y):  # Figure out where the origin of the block here is
    return (x - (x - self.cx) % 16, y - (y - self.cy) % 16)

  def panRel(self, dx, dy):
    self.cx += dx
    self.cy += dy

  def getTileAt(self, x, y):  # Tile at (x, y) in map coords
    if (abs(x) < 5 and abs(y) < 5):
      return Tile.EMPTY
    else:
      return Tile.WALL

  def addEnt(self, ent):  # Put entity on the map
    ents.push(ent)

  def getEnts(self):  # Get master entity list
    return []

  def player(self):
    return self.p

  p = Player()
  ents = []
  level = 0
  grand = random.Random()
  lrand = random.Random()
  cx = 0.0
  cy = 0.0
  bx = 0.0
  by = 0.0
  

  
