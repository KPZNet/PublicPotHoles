


class PotHole (  ) :
    ID = 1
    streetAddress = "street"
    district = "district 13"
    location = "not set"
    severity = 1
    size = 1
    priority = 0

    def __init__(self):
        ID = 1

class DataStore():
    potHoles = {}
    workOrders = {}
    damageClaims = {}

    def __init__(self) :
        self.potHoles = {}
        self.workOrders = {}
        self.damageClaims = {}

    def AddPotHole(self, ID, pothole):
       self.potholes[ID] = pothole
