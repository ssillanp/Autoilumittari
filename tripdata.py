
class car:
    def __init__(self, model):
        self.model = model
        self.slope = 1.009

    @property
    def comsumption(self):
        models = {
            'A': 3,
            'B': 3.5,
            'C': 4
        }
        return models[self.model]

    def __repr__(self):
        return f"car({self.model})"

class trip:
    def __init__(self, dist, speed, car):
        self.dist = int(dist)
        self.speed = int(speed)
        self.car = car

    @property
    def trip_consumption(self):
        speed_consumption = self.car.comsumption * 1.009 ** self.speed
        return round(speed_consumption * self.dist / 100, 2)

    @property
    def trip_duration(self):
        trip_time = self.dist / self.speed
        return int(trip_time), int(round(trip_time%1*60, 0))

    def __repr__(self):
        return f"trip({self.dist}, {self.car})"