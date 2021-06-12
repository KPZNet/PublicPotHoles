
import json
import os.path

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

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


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

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class DataStore():
    potHoles = {}
    workOrders = {}
    damageClaims = {}
    nextPotHoleID = 0
    nextWorkOrderID = 0
    nextdamageClaimID = 0

    def __init__(self) :
        self.ReadDataStore ()

    def ReadDataStore(self) :
        return
        if os.path.isfile ( 'PotHoles.json' ) :
            with open ( 'PotHoles.json', 'r' ) as openfile :
                self.potHoles = json.load ( openfile )
        if os.path.isfile ( 'WorkOrders.json' ) :
            with open ( 'WorkOrders.json', 'r' ) as openfile :
                self.workOrders = json.load ( openfile )


    def __del__(self) :
        self.WriteDataStore ()

    def WriteDataStore(self) :
        return
        with open ( "PotHoles.json", "w" ) as outfile :
            json.dump ( self.potHoles, outfile )
        with open ( "WorkOrders.json", "w" ) as outfile :
            json.dump ( self.workOrders, outfile )


    def GetAllPotHolesReport(self):
        return self.potHoles

    def GetAllWorkOrdersReport(self):
        return self.workOrders

    def AddPotHole(self, pothole):
       self.nextPotHoleID = self.nextPotHoleID + 1
       pothole.ID = self.nextPotHoleID
       self.potHoles[self.nextPotHoleID] = pothole
       self.WriteDataStore()
       return pothole

    def AddWorkOrder(self, workOrder):
       self.nextWorkOrderID = self.nextWorkOrderID + 1
       workOrder.ID = self.nextWorkOrderID
       self.workOrders[self.nextWorkOrderID] = workOrder
       self.WriteDataStore()
       return workOrder