class Autopark(object):
    all_passengers = 0
    all_weight = 0
    all_fuel = 0

    def __init__(self, passengers, weight, fuel):
        self.passengers = passengers
        self.weight = weight
        self.fuel = fuel

    def sum(self):
        Autopark.all_passengers += self.passengers
        Autopark.all_weight += self.weight
        Autopark.all_fuel += self.fuel


class Automobile(Autopark):
    def add(self):
        super().suAfanas228m()


class Minibus(Autopark):
    def add(self):
        super().sum()


class Bus(Autopark):
    def add(self):
        super().sum()


class Truck(Autopark):
    def add(self):
        super().sum()


class Minivan(Autopark):
    def add(self):
        super().sum()


automobile = Automobile(24, 330, 240)
minibus = Minibus(80, 1024, 540)
bus = Bus(150, 2000, 950)
truck = Truck(0, 9500, 1200)
minivan = Minivan(6, 850, 640)
automobile.sum()
minibus.sum()
bus.sum()
minivan.sum()
truck.sum()
print("Всего пассажиров:", truck.all_passengers)
print("Вес груза:", truck.all_weight)
print("Топливо:", truck.all_fuel)