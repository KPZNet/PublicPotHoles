
import json
import os.path
import jsonpickle

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

    def __init__(self) :
        self.potHoles = {}
        self.workOrders = {}
        self.damageClaims = {}
        self.nextPotHoleID = 0
        self.nextWorkOrderID = 0
        self.nextdamageClaimID = 0

        self.ReadDataStore ()

    def __del__(self) :
        self.WriteDataStore ()

    def ReadDataStore(self) :
        try :
            if os.path.isfile ( 'PotHoles.json' ) :
                with open ( 'PotHoles.json', 'r' ) as openfile :
                    json_object = openfile.read()
                    pt = jsonpickle.decode ( json_object )
                    self.potHoles = pt.potHoles
                    self.workOrders = pt.workOrders
                    self.damageClaims = pt.damageClaims
                    self.nextPotHoleID = pt.nextPotHoleID
                    self.nextWorkOrderID = pt.nextWorkOrderID
                    self.nextdamageClaimID = pt.nextdamageClaimID
        except(Exception) as e:
            pass
        finally :
            pass

    def WriteDataStore(self) :
        jp = jsonpickle.encode(self)
        with open ( "PotHoles.json", "w" ) as outfile :
            outfile.write ( jp )

    def GetAllPotHolesReport(self):
        return self.potHoles

    def GetAllWorkOrdersReport(self):
        return self.workOrders

    def AddPotHole(self, pothole):
       self.nextPotHoleID = self.nextPotHoleID + 1
       pothole.ID = self.nextPotHoleID
       self.potHoles[str(self.nextPotHoleID)] = pothole
       return pothole

    def AddWorkOrder(self, workOrder):
       self.nextWorkOrderID = self.nextWorkOrderID + 1
       workOrder.ID = self.nextWorkOrderID
       self.workOrders[str(self.nextWorkOrderID)] = workOrder
       return workOrder