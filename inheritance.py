class GroundVehicle():
    def drive(self):
        print("Drive me on the road!")

class FlyingVehicle():
    def fly(self):
         print("Fly me to the sky!")

class FlyingCar(GroundVehicle, FlyingVehicle):
    pass

fc = FlyingCar()

fc.drive()
fc.fly()