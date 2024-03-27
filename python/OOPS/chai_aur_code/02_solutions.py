
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    
    def getData(self):
        return f"{self.__brand} {self.__model}"
    
    @staticmethod 
    def description():
        print(f"{Car.__instances}")

if __name__ == "__main__":
    obj1 = Car('Toyota', 'Fortuner')
    print(obj1.getData())
    print(obj1.__model)
    