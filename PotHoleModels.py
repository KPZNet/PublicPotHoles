
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
    costEstimate = 0.0

    def __init__(self):
        ID = 0

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

class DamageClaim (  ) :
    ID = 0
    potHoleID = 0
    name = ""
    address = ""
    phone = ""
    damageType = ""
    dollarAmount = 0.0
    approved = False

    def __init__(self):
        ID = 0

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
        pass

    def WriteDataStore(self) :
        jp = jsonpickle.encode(self)
        with open ( "PotHoles.json", "w" ) as outfile :
            outfile.write ( jp )

    def GetAllPotHolesReport(self):
        return self.potHoles

    def GetAllWorkOrdersReport(self):
        return self.workOrders

    def GetAllDamageClaimReport(self):
        return self.damageClaims

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

    def AddDamageClaim(self, damageClaim):
       self.nextdamageClaimID = self.nextdamageClaimID + 1
       damageClaim.ID = self.nextdamageClaimID
       self.damageClaims[str(self.nextdamageClaimID)] = damageClaim
       return damageClaim

    @staticmethod
    def FactoryDataRestore():
        try :
            if os.path.isfile ( 'PotHoles.json' ) :
                with open ( 'PotHoles.json', 'r' ) as openfile :
                    json_object = openfile.read()
                    pt = jsonpickle.decode ( json_object )
                    return pt
        except(Exception) as e:
            pass
        finally :
            pass

    @staticmethod
    def FactoryDataSave(ds):
        try :
            jp = jsonpickle.encode ( ds )
            with open ( "PotHoles.json", "w" ) as outfile :
                outfile.write ( jp )
        except(Exception) as e:
            pass
        finally :
            pass