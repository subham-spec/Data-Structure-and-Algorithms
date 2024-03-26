class Car:
    name = None
    brand = None
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

if __name__ == "__main__":
    obj1 = Car('Harrier', 'Tata')


'''
The values are stored in the attributes at line 2 and 3
'''