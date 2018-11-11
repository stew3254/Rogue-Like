import copy
import math

# "eid" means "Entity ID" in this document

class Enemy:
    def __init__(self, name, eid, maxH, speed, toolInts, aiBehavior, salary):
        self.name = name
        self.enemyID = eid
        self.health = maxH
        self.maxHealth = maxH
        self.speed = speed
        self.toolInteractions = toolInts
        self.aiBehavior = aiBehavior
        self.salaryDropped = salary
        self.x = -1
        self.y = -1
        self.status = 0
        self.dx = 0
        self.dy = 0

    def genPathTo(worldData, px, py, maxlen):
        dx = self.x - px
        dy = self.y - py
        adx = math.abs(dx)
        ady = math.abs(dy)
        sdx = dx/adx
        sdy = dy/ady
        if math.sqrt(dx * dx + dy * dy) < maxlen and self.status & (__STATUS_CAUGHT + __STATUS_STUNNED) == 0:
            for i in range(self.speed):
                if adx + ady > 1:
                    if adx >= ady and getTileAt(self.x + sdx, self.y) != Tile.EMPTY:
                        self.dx += sdx
                        dx += sdx
                        adx = math.abs(dx)
                        sdx = dx/adx
                    elif getTileAt(self.x, self.y + sdy) != Tile.EMPTY:
                        self.dy += sdy
                        dy += sdy
                        ady = math.abs(dy)
                        sdy = dy/ady 
                    else:
                        return False
        else:
            self.status &= ~__STATUS_STUNNED
            return False
        return True
        
    def path():
        self.x += self.dx
        self.y += self.dy
        
class EnemyRegistry:
    List = []
    def registerEnemy(self, name, maxH, speed, toolInts, aiBehavior, salary):
        self.List.append(Enemy(name, len(self.List), maxH, speed, toolInts, aiBehavior, salary)
    def createEnemyInstance(self, eid, x, y)
        newEnemy = copy.deepcopy(self.List[eid])
        newEnemy.x = x
        newEnemy.y = y
        return newEnemy
    def getEIDFromName(self, name):
        for enemy in self.List:
            if enemy.name = name:
                return enemy.enemyID
        return -1

__STATUS_STUNNED    = 0x0001
__STATUS_CAUGHT     = 0x0002

_EnemyRegistry = EnemyRegistry()
_EnemyRegistry.registerEnemy("Rat",5,1,
    [
        lambda: self.health -= 5,
        lambda: self.status |= __STATUS_STUNNED,
        lambda: return, # Miss
        lambda: return, # Miss
        lambda: return, # Miss
        lambda: return, # Miss
        lambda: self.health -= 15,
        lambda: self.health -= 30,
        lambda: return, # Miss
        lambda: return, # Miss
    ],
    lambda worldData:
        player = worldData.getPlayer()
        if worldData.getTileAt(player.x, player.y) == Tile.HVAC:
            if math.abs(self.x - player.x) + math.abs(self.y - player.y) == 1:
                if not player.hasItem(_ItemRegistry.getIIDFromName("Steel-toed Boots")):
                    player.health -= 1
            elif self.genPathTo(worldData, player.x, player.y, 10):
                self.pathTo()
    )
_EnemyRegistry.registerEnemy("Bird",5,1,
    [
        lambda: self.health -= 5,
        lambda: self.status |= __STATUS_CAUGHT,
        lambda: return, # Miss
        lambda: return, # Miss
        lambda: return, # Miss
        lambda: return, # Miss
        lambda: self.health -= 15,
        lambda: self.health -= 30,
        lambda: return, # Miss
        lambda: return, # Miss
    ],
    lambda worldData:
        player = worldData.getPlayer()
        if worldData.getTileAt(player.x, player.y) == Tile.HVAC:
            if math.abs(self.x - player.x) + math.abs(self.y - player.y) == 1:
                if not player.hasItem(_ItemRegistry.getIIDFromName("Hardhat")):
                    player.health -= 1
            elif self.genPathTo(worldData, player.x, player.y, 10):
                self.pathTo()
    )

