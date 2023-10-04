class vehicle:
    def __init__(self,brand):
        self.brand = brand
    def drive(self):
        print(f"{self.brand} has been driven!")
class Car(vehicle):
    def bhom(self):
     print(f"{self.brand} has been bhoming!")
class cycle(vehicle):
    def padel(self):
        print(f"{self.brand} has been padeling!")
class jet(vehicle):
    def bomb(self):
        print(f"{self.brand} has been bombing!")
# Creating instances/objects of the subclasses
my_car = Car("Mazda-MX")
my_cycle = cycle("Duranta Bi-cycle")
my_jet = jet("Su-57")

## Accessing methods of the instances
my_car.bhom()
my_cycle.padel()
my_jet.bomb()

