import copy

# "eid" means "Entity ID" in this document

class Enemy:
    def __init__(self, name, eid, maxH, speed, toolInts, defItemInts, aiBehavior, salary):
        self.name = name
        self.enemyID = eid
        self.health = maxH
        self.maxHealth = maxH
        self.speed = speed
        self.toolInteractions = toolInts
        self.defensiveItemInteractions = defItemInts
        self.aiBehavior = aiBehavior
        self.salaryDropped = salary
        self.x = -1
        self.y = -1

class EnemyRegistry:
    List = []
    def registerEnemy(self, name, maxH, speed, toolInts, defItemInts, aiBehavior, salary):
        self.List.append(Enemy(name, len(self.List), maxH, speed, toolInts, defItemInts, aiBehavior, salary)
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

def RatAI(worldData):
    pass

_EnemyRegistry = EnemyRegistry()
_EnemyRegistry.registerEnemy("Rat",10,1,[],[], *RatAI)

