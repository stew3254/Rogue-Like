#!/usr/bin/python3

import math
import enum
import random
import player

def r(x):  # Create a Random from a hash
  R = random.Random()
  R.seed(x)
  return R

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
    self.seed = hash(seed)
    self.reseedLevel()
    
    print("world constructor called")

  def reseedLevel(self):
    self.lseed = self.level + hash(self.seed + self.level)

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
    if (abs(math.floor(x)) < 5 and abs(math.floor(y)) < 5):
      return Tile.EMPTY
    else:
      return Tile.WALL

  def addEnt(self, ent):  # Put entity on the map
    ents.push(ent)

  def getEnts(self):  # Get master entity list
    return []

  def getPlayer(self):
    return self.p

  
  seed = hash(0)
  lseed = hash(0)
  p = player.Player()
  ents = []
  level = 0
  cx = 0.0
  cy = 0.0
  bx = 0.0
  by = 0.0


  
