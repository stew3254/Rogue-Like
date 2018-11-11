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
    self.chunks = set()
    
    print("world constructor called")

  def reseedLevel(self):
    self.lseed = self.level + hash(self.seed + self.level)

  def toMapC(self, x, y):  # Pixel coords -> map coords
    return ((x - self.cx) / 16, (y - self.cy) / 16)

  def fromMapC(self, x, y):  # Map coords -> pixel coords
    return (x * 16 + self.cx, y * 16 + self.cy)

  def toChunkC(self, x, y):  # Map coords -> chunk coords
    return (x / 256, y / 256)

  def getBlockBase(self, x, y):  # Figure out where the origin of the block here is
    return (x - (x - self.cx) % 16, y - (y - self.cy) % 16)

  def panRel(self, dx, dy):
    self.cx += dx
    self.cy += dy

  def getTileAt(self, x, y):  # Tile at (x, y) in map coords
    (cx, cy) = self.toChunkC(x, y)
    thisc = []
    while thisc == []:
      thisc = [C for C in self.chunks if (C.x == math.floor(cx) and C.y == math.floor(cy))]
      if thisc == []:
        newchunk = Chunk(math.floor(cx), math.floor(cy))
        newchunk.gen()
        self.chunks.add(newchunk)
        
    return thisc[0].getTileAt(x, y)

  def cleanFrom(self, x, y):  # Deletes chunks too far away from the block coords given
    self.chunks = {C for C in self.chunks if (abs(C.x - x) > 3 and abs(C.y - y) > 3)}

  def addEnt(self, ent):  # Put entity on the map
    ents.push(ent)

  def getEnts(self):  # Get master entity list
    return []

  def getPlayer(self):
    return self.p

  
  chunks = set()
  seed = hash(0)
  lseed = hash(0)
  p = player.Player()
  ents = []
  level = 0
  cx = 0.0
  cy = 0.0
  bx = 0.0
  by = 0.0

class Chunk:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.data = [[Tile.WALL for X in range(256)] for Y in range(256)]
    print("Constructor call for chunk at: " + str(x) + ", " + str(y))

  def getTileAt(self, x, y):
    return self.data[math.floor(x % 256)][math.floor(y % 256)]

  def setTileAt(self, x, y, arg):
    self.data[math.floor(x % 256)][math.floor(y % 256)] = arg

  def gen(self):
    print("Generating chunk at " + str(self.x) + ", " + str(self.y))
    for x in range(256):
      self.data[x][0] = Tile.EMPTY
    for y in range(256):
      self.data[0][y] = Tile.EMPTY
    for x in range(-5, 6):
      for y in range(-5, 6):
        self.setTileAt(x, y, Tile.EMPTY)


  data = []
  x = 0
  y = 0

class ChunkBoundary:
  def __init__(self):
    return 0
  
