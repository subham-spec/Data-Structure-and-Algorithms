class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    @classmethod
    def get_name(self):
        return self.__name__
    
    @staticmethod
    def get_brand(obj):
        return obj.brand

if __name__ == "__main__":
    obj1 = Car('Harrier', 'Tata')
    print(obj1.get_name())
    print(obj1.get_brand(obj1))

