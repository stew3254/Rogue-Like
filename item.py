import copy


class Item:
    def __init__(self, name, itemID):
        self.name = name
        self.itemID = itemID
        self.count = 0

class ItemRegistry:
    List = []
    def registerItem(self, name):
        self.List.append(Item(name, len(self.List)))

    def createItemInstance(itemID, count=1):
        newItem = copy.deepcopy(self.List[itemID])
        newItem.count = count

        return newItem

    def getIIDFromName(self, name):
        for item in self.List:
            if item.name == name:
                return item.itemID

        return -1


_ItemRegistry = ItemRegistry()

# Tools
__TOOLS_START = 0
_ItemRegistry.registerItem("Wrench")
_ItemRegistry.registerItem("Net")
_ItemRegistry.registerItem("Bee Poison")
_ItemRegistry.registerItem("Fire Extinguisher")
_ItemRegistry.registerItem("Bootable Flash Drive")
_ItemRegistry.registerItem("Soldering Iron")
_ItemRegistry.registerItem("Standard Toolbox")
_ItemRegistry.registerItem("Electric Toolbox")
_ItemRegistry.registerItem("Welder")
_ItemRegistry.registerItem("Cellphone")

# Scrap
__SCRAP_START = len(_ItemRegistry.List)
_ItemRegistry.registerItem("Assorted Metal Bits")
_ItemRegistry.registerItem("Wires and Cables")
_ItemRegistry.registerItem("Electrical Components")
_ItemRegistry.registerItem("Office Supplies")
_ItemRegistry.registerItem("Plumbing Supplies")
_ItemRegistry.registerItem("Computer Parts")

# Defensive Gear
__DEFENSEGEAR_START = len(_ItemRegistry.List)
_ItemRegistry.registerItem("Steel-toed Boots")
_ItemRegistry.registerItem("Heavy-duty Pants")
_ItemRegistry.registerItem("Hardhat")
_ItemRegistry.registerItem("Netted Gear")
_ItemRegistry.registerItem("ID Card")
_ItemRegistry.registerItem("Work Certificate")
_ItemRegistry.registerItem("Red Tape")
_ItemRegistry.registerItem("Work Coat")
_ItemRegistry.registerItem("Rubber Boots")
_ItemRegistry.registerItem("'Learn You A Haskell For Great Good'")
_ItemRegistry.registerItem("Tritium Sample")

