
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
    potHoles = {}
    workOrders = {}
    damageClaims = {}
    nextPotHoleID = 0
    nextWorkOrderID = 0
    nextdamageClaimID = 0

    def __init__(self) :
        self.ReadDataStore ()

    def __del__(self) :
        self.WriteDataStore ()

    def ReadDataStore(self) :

        try :
            if os.path.isfile ( 'PotHoles.json' ) :
                with open ( 'PotHoles.json', 'r' ) as openfile :
                    json_object = openfile.read()
                    ptHoles = jsonpickle.decode ( json_object )
                    self.potHoles = ptHoles
        except(Exception) as e:
            print ( "<<< EXCEPTION >>>" )
            print ( e )
        finally :
            print ( "Completed" )

    def WriteDataStore(self) :
        jpPotHoles = jsonpickle.encode ( self.potHoles )
        with open ( "PotHoles.json", "w" ) as outfile :
            outfile.write ( jpPotHoles )

    def GetAllPotHolesReport(self):
        return self.potHoles

    def GetAllWorkOrdersReport(self):
        return self.workOrders

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