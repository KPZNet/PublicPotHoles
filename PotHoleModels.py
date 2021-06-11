


class PotHole (  ) :
    ID = 1
    streetAddress = "street"
    district = "district 13"
    location = "not set"
    severity = 1
    size = 1
    priority = 0

    def __init__(self):
        ID = 0

    def GetPotHoleData(self):
        s = ""
        s = s + "ID: " + (str ( self.ID ) + "\n")
        s = s + "Street: " + (str(self.streetAddress) + "\n")
        s = s + "District: " + (str(self.district) + "\n")
        s = s + "Severity: " + (str(self.severity) + "\n")
        s = s + "Size: " + (str(self.size) + "\n")
        s = s + "Priority: " + (str(self.priority) + "\n")
        return s

class WorkOrder (  ) :
    ID = 0
    potHoleID = 0
    repairCrewID = 0
    numberOfWorkers = 0
    equipmentAssigned = ""
    hoursApplied = ""
    holeStatus = ""
    fillerMaterial = ""

    def __init__(self):
        ID = 0

    def GetWorkOrderData(self):
        s = ""
        s = s + "ID: " + (str ( self.ID ) + "\n")
        s = s + "potHoleID: " + (str(self.potHoleID) + "\n")
        s = s + "repairCrewID: " + (str(self.repairCrewID) + "\n")
        s = s + "numberOfWorkers: " + (str(self.numberOfWorkers) + "\n")
        s = s + "equipmentAssigned: " + (str(self.equipmentAssigned) + "\n")
        s = s + "hoursApplied: " + (str(self.hoursApplied) + "\n")
        s = s + "holeStatus: " + (str ( self.holeStatus ) + "\n")
        s = s + "fillerMaterial: " + (str ( self.fillerMaterial ) + "\n")
        return s


class DataStore():
    potHoles = {}
    workOrders = {}
    damageClaims = {}
    nextPotHoleID = 0
    nextWorkOrderID = 0
    nextdamageClaimID = 0

    def GetAllPotHoles(self):
        s = ""
        for phID in self.potHoles:
            ph = self.potHoles[phID]
            phData = ph.GetPotHoleData()
            s = s + (phData + "\r\n")
        return s

    def GetAllWorkOrders(self):
        s = ""
        for woID in self.workOrders:
            wo = self.workOrders[woID]
            woData = wo.GetWorkOrderData()
            s = s + (woData + "\r\n")
        return s

    def AddPotHole(self, pothole):
       self.nextPotHoleID = self.nextPotHoleID + 1
       pothole.ID = self.nextPotHoleID
       self.potHoles[self.nextPotHoleID] = pothole
       return pothole

    def AddWorkOrder(self, workOrder):
       self.nextWorkOrderID = self.nextWorkOrderID + 1
       workOrder.ID = self.nextWorkOrderID
       self.workOrders[self.nextWorkOrderID] = workOrder
       return workOrder