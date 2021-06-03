
class car:
    """Class contains car info"""
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
    """Class contains trip info"""
    fuelprice = 1.60

    def __init__(self, dist, speed, car):
        self.dist = int(dist)
        self.speed = int(speed)
        self.car = car

    @property
    def trip_consumption(self):
        """
        Calculate trip consumption, based on car, distance and speed
        :return Trip consumption
        """
        speed_consumption = self.car.comsumption * (self.car.slope ** self.speed)
        return round(speed_consumption * self.dist / 100, 2)

    @property
    def trip_duration(self):
        """
        Calculate trip duration based on distance and speed
        :return list(trip total time in hours, trip full hours, trip full minutes)
        """
        trip_time = self.dist / self.speed
        return [trip_time, int(trip_time), int(trip_time%1*60)]


    def carbon_diff(self, other):
        """
        Calculate difference in co2 emissions
        :param other: trip(speed2)
        :return co2 difference in kg
        """
        return abs(round((self.trip_consumption * 2.85)-(other.trip_consumption * 2.85), 2))


    def fuel_diff(self, other):
        """
           Calculate difference in fuel consumption
           :param other: trip(speed2)
           :return list(total difference, difference rounded)
           """
        diff = abs(round(self.trip_consumption - other.trip_consumption, 2))
        return [diff, round(diff * self.fuelprice, 2)]

    def fuel_diff_prcent(self, other):
        """
        Calculate difference in fuel consumption in precentage
        :param other: trip(speed2)
        :return fuel consumption difference in precentage value
        """
        if self.trip_consumption >= other.trip_consumption:
            return round((self.trip_consumption - other.trip_consumption) / self.trip_consumption * 100, 0)
        else:
            return round((other.trip_consumption - self.trip_consumption) / other.trip_consumption * 100, 0)

    def time_diff(self, other):
        """
        Calculate difference in trip time
        :param other: trip(speed2)
        :return list(trip full hours, trip full minutes)
        """
        return [abs(int(self.trip_duration[0] - other.trip_duration[0])), int((self.trip_duration[0]- other.trip_duration[0])%1*60)]

    def __repr__(self):
        return f"trip({self.dist}, {self.car})"