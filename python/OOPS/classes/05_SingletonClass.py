# Class which have only one object

class Car:
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

if __name__ == "__main__":
    obj1 = Car("Ford", "Endeavour")
    
    print(obj1.brand)
    print(obj1.model)


