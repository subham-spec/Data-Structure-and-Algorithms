
class Car:
    def __init__(self, brand, model):
        self._brand = brand # Protected Member
        self.__model = model # Private Member
    
    def getData(self):
        return f"{self._brand} {self.__model}"

if __name__ == "__main__":

    car1 = Car('Tata', 'Harrier')
    print(car1.getData())

    # print(car1._brand) Can access this here as it is protected
    # print(car1.__model) Can't access this here as it is private
