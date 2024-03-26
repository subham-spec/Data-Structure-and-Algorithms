# Hierchical Inheritence

class Car:
    def __init__(self, model, brand):
        self.brand = brand
        self.model = model

class Car_Specs:
    def __init__(self, range):
        self.range = range
     
class Petrol_car(Car, Car_Specs):
    def __init__(self, model, brand, fuel, range):
        Car.__init__(self, model, brand)
        Car_Specs.__init__(self, range)
        self.fuel = fuel

if __name__ == "__main__":
    car1 = Petrol_car("Harrier","Tata","Petrol",736)
