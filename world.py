#!/usr/bin/python3

import math
import enum

class Tile(enum.Enum):
  EMPTY = 0
  WALL = 1

class World:
  def __init__(this, width, height, seed):
    this.cx = width * 0.5
    this.cy = height * 0.5
    print("world constructor called")

  def toMapC(this, x, y):
    return ((x - this.cx) / 16, (y - this.cy) / 16)

  def fromMapC(this, x, y):
    return (x * 16 + this.cx, y * 16 + this.cy)

  def getTileAt(this, x, y):
    if (math.abs(x) < 5 and math.abs(y) < 5):
      return Tile.EMPTY
    else:
      return Tile.WALL

  def addEnt(ent):
    ents.push(ent)

  def getEnts():
    return []

  ents = []
  

  
