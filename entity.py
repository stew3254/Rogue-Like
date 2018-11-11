import copy

# "eid" means "Entity ID" in this document

class Enemy:
    def __init__(self, name, eid, maxH, speed, toolInts, defItemInts, aiBehavior):
        self.name = name
        self.entityID = eid
        self.health = maxH
        self.maxHealth = maxH
        self.speed = speed
        self.toolInteractions = toolInts
        self.defensiveItemInteractions = defItemInts
        self.aiBehavior = aiBehavior
        self.x = -1
        self.y = -1

class EnemyRegistry:
    List = []
    def registerEnemy(self, name, maxH, speed, toolInts, defItemInts, aiBehavior):
        self.List.append(Enemy(name, len(self.List), maxH, speed, toolInts, defItemInts, aiBehavior)
    def createEnemyInstance(eid, x, y)
        newEnemy = copy.deepcopy(self.List[eid])
        newEnemy.x = x
        newEnemy.y = y
        return newEnemy
