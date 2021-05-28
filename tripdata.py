
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
        speed_consumption = self.car.comsumption * (1.009 ** self.speed)
        return round(speed_consumption * self.dist / 100, 2)

    @property
    def trip_duration(self):
        trip_time = self.dist / self.speed
        return [trip_time, int(trip_time), int(trip_time%1*60)]


    def carbon_diff(self, other):
        return abs(round((self.trip_consumption * 2.85)-(other.trip_consumption * 2.85), 2))


    def fuel_diff(self, other):
        return abs(round(self.trip_consumption - other.trip_consumption, 2))

    def fuel_diff_prcent(self, other):
        if self.trip_consumption >= other.trip_consumption:
            return round((self.trip_consumption - other.trip_consumption) / self.trip_consumption * 100, 0)
        else:
            return round((other.trip_consumption - self.trip_consumption) / other.trip_consumption * 100, 0)

    def time_diff(self, other):
        return [abs(int(self.trip_duration[0] - other.trip_duration[0])), int((self.trip_duration[0]- other.trip_duration[0])%1*60)]

    def __repr__(self):
        return f"trip({self.dist}, {self.car})"