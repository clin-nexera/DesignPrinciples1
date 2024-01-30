# Where is LSP being violated?
class Vehicle():
    mileage: int
    def go(self, speed):
        """ Move vehicle at given speed
        Arguments:
        - speed (float) : speed in km/h between [0, 120]
        """
        pass

    def mileage(self):
        """Returns how many miles the vehicle has travelled
        Returns:
        - int : a value between [0, inf)
        """
        return self.miles


class Car(Vehicle):
    def go(self, speed):
        """Moves the car at given speed
        - speed (float) : speed in km/h between [0, 180]
        """


class Bike(Vehicle):
    def go(self, speed):
        """Moves the car at given speed
        - speed (float) : speed in km/h between [0, 40]
        """
        pass
    

class ElectricCar(Car):
    def mileage(self):
        """Returns how many miles the vehicle has travelled
        Returns:
        - None
        """
        return None
    

### Notes ###
    # bike.go narrows the range of input arguments. In the parent class, go accepts values between [0, 120] while bike accepts [0, 40]. This means that Vehicle cannot be replaced by Bike.
    # electriccar.mileage returns None while Vehicle's mileage function return a value between [0, inf). This means Vehicle cannot be replaced by ElectricCar