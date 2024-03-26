# Single Inheritence

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
     
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def getData(self):
        return f"{self.brand} {self.model} {self.battery_size}"

if __name__ == "__main__":
    ele_car = ElectricCar("Tesla", "Truck", "85kWh")
    print(ele_car.getData())

    print(issubclass(ElectricCar, Car))
    print(isinstance(ele_car, ElectricCar))
    print(isinstance(ele_car, Car))