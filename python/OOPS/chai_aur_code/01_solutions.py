
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    def getData(self):
        return f"{self.__brand} {self.__model}"
     
# Inheritecnce
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.__battery_size = battery_size
    
    def getData(self):
        return f"{self.brand} {self.model} {self.battery_size}"

if __name__ == "__main__":
    # my_car = Car("Toyota", "Fortuner")
    # print(my_car.getData())

    ele_car = ElectricCar("Tesla", "Truck", "85kWh")
    print(ele_car.getData())



'''
__init__ --> It is a constructor in python
this in java = self in python

For controlled output we use getters and setters.

To make any instance private, write __name, use 2 _ before the name.
'''