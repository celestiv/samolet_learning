class Vehicle:
    """
    В зависимости от передаваемого параметра "car" или "bike"
    создаются обьекты разных типов - Автомобиль или Байк.
    """
    def __new__(cls, *args, **kwargs):
        vehicle_type = args[0]
        if vehicle_type == "car":
            return super(Vehicle, cls).__new__(Car)
        elif vehicle_type == "bike":
            return super(Vehicle, cls).__new__(Bike)
        else:
            return None


class Car(Vehicle):
    def drive(self):
        return "driving a car"


class Bike(Vehicle):
    def drive(self):
        return "riding a bike"


vehicle1 = Vehicle("car")
vehicle2 = Vehicle("bike")
print(vehicle1.drive())  # "driving a car"
print(vehicle2.drive())  # "riding a bike"
