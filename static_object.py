import os
import math
import item.py

class Machine:
    def __init__(self, name, mid, sReq, tReq, dChnc, result):
        self.scrapRequired = sReq
        self.toolRequired = tReq
        self.doubtChance = dChnc
        self.doubted = False
        self.fixed = False
        self.result = result
        self.machineID = mid
        self.name = name
    def doubt(self, player):
        if not self.doubted and not self.fixed:
            self.doubted = True
            if os.urandom(2)/65536 < self.doubtChance:
                self.fixed = True
                self.result()
            else:
                player.health -= 5
    def tryFix(self, player):
        if player.hasItem(sReq) and player.hasItem(tReq):
            self.fixed = True
            self.result()

class MachineRegistry:
    List = []
    def register(self, name, sReq, tReq, dChnc, result):
        self.List.append(Machine(self, name, len(self.List), sReq, tReq, dChnc, result))
    def createInstance(mid, count=1):
        return ncopy.deepcopy(self.List[mid])
    def getIDFromName(self, name):
        for machine in self.List:
            if machine.name == name:
                return machine.machineID
        return -1

class Scrap:
    def __init__(self, sid, name, iid, tReq):
        self.itemID = iid
        self.scrapID = sid
        self.name = name
        self.toolRequired = tReq
    def pickup(self, player):
        if player.hasItem(tReq):
            player.addItem(itemID)
            return True
        else:
            return False

class ScrapRegistry:
    List = []
    def register(self, name, iid, tReq):
        self.List.append(Scrap(self, len(self.List), name, iid, tReq)
    def createInstance(sid):
        return copy.deepcopy(self.List[sid])
    def getIDFromName(self, name):
        for scrap in self.List:
            if scrap.name == name:
                return scrap.scrapID
        return -1

class Toolbox:
    def __init__(self, tbid, name, iid):
        self.itemID = iid
        self.toolboxID = tbid
        self.name = name
    def pickup(self, player):
        player.addItem(itemID)
           return True

class ToolboxRegistry:
    List = []
    def register(self, name, iid):
        self.List.append(Scrap(self, len(self.List), name, iid)
    def createInstance(tbid):
        return copy.deepcopy(self.List[tbid])
    def getIDFromName(self, name):
        for toolbox in self.List:
            if toolbox.name == name:
                return toolbox.toolboxID
        return -1

_MachineRegistry = MachineRegistry()
_MachineRegistry.register("Copying Machine", __SCRAP_START + 3, __TOOL_START + 7, 0.1, lambda: return)
_MachineRegistry.register("HVAC System", __SCRAP_START + 1, __TOOL_START + 0, 0.4, lambda: return)
_MachineRegistry.register("Sprinkler Controller", __SCRAP_START + 0, __TOOL_START + 0, 0.4, lambda: return)
_MachineRegistry.register("Ventilation Controller", __SCRAP_START + 1, __TOOL_START + 6, 0.3, lambda: return)
_MachineRegistry.register("Server Rack", __SCRAP_START + 5, __TOOL_START + 4, 0.1, lambda: return)

_ScrapRegistry = ScrapRegistry()
_ScrapRegistry.register("Assorted Metal Bits",0,0)
_ScrapRegistry.register("Wires and Cables",1,6)
_ScrapRegistry.register("Office Supplies",3,0)
_ScrapRegistry.register("Computer Parts",5,5)

_ToolboxRegistry = ToolboxRegistry()
for t in range(11):
    _ToolboxRegistry.register(t.name, t.itemID)
