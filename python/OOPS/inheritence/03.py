# Multilevel Inheritence

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

class Formula(Car):
    def __init__(self, name, seats, engine):
        super().__init__(name, seats)
        self.engine = engine
    def get_data(self) -> None:
        print(self.name, self.seats, self.engine)

if __name__ == "__main__":
    f1 = Formula("Speed-1200", "1", "2499")
    f1.get_data()

