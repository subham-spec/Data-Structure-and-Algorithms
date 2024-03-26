# Multiple Inheritance

class Vehicle:
    def __init__(self, name):
        self.name = name
    def get_data(self) -> None:
        print(self.name)

class Car(Vehicle):
    def __init__(self, name, seats):
        super().__init__(name)
        self.seats = seats
    def get_data(self) -> None:
        print(self.name, self.seats)

class Truck(Vehicle):
    def __init__(self, name, load_capacity):
        super().__init__(name)
        self.load_capacity = load_capacity
    def get_data(self) -> None:
        print(self.name, self.load_capacity)

if __name__ == "__main__":
    obj1 = Car("Pajero-Sport", "5")
    obj2 = Truck("Eicher-900", "9-ton")

    obj1.get_data()
    obj2.get_data()