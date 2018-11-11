import copy

class Item:
    def __init__(self, name, iid):
        self.name = name
        self.itemID = iid
        self.count = 0

class ItemRegistry:
    List = []
    def registerItem(self, name):
        self.List.append(Item(name, len(self.List)))
    def createItemInstance(iid, count=1):
        newItem = copy.deepcopy(self.List[iid])
        newItem.count = count
        return newItem
