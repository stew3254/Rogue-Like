#!/usr/bin/python3

import math
import enum
import random

class Tile(enum.Enum):
  EMPTY = 0
  WALL = 1

class World:
# Construct a world in a window of pixel dimensions given, seeded
  def __init__(this, width, height, seed):
    this.cx = width * 0.5
    this.cy = height * 0.5
    this.bx = math.ceil(width / 16)
    this.by = math.ceil(height / 16)
    this.level = 0
    print("world constructor called")

  def toMapC(this, x, y):  # Pixel coords -> map coords
    return ((x - this.cx) / 16, (y - this.cy) / 16)

  def fromMapC(this, x, y):  # Map coords -> pixel coords
    return (x * 16 + this.cx, y * 16 + this.cy)

  def getTileAt(this, x, y):  # Tile at (x, y) in map coords
    if (math.abs(x) < 5 and math.abs(y) < 5):
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
  

  
