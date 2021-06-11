


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

class DataStore():
    potHoles = {}
    workOrders = {}
    damageClaims = {}
    nextID = 0

    def GetAllPotHoles(self):
        s = ""
        for phID in self.potHoles:
            ph = self.potHoles[phID]
            phData = ph.GetPotHoleData()
            s = s + (phData + "\n")
        return s


    def AddPotHole(self, pothole):
       self.nextID = self.nextID + 1
       pothole.ID = self.nextID
       self.potHoles[self.nextID] = pothole
       return pothole
