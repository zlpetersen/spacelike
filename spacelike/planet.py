

class Planet():
    def __init__(self, name="", faction="", population=0, cities=[], stations=[]):
        self.name = name
        self.faction = faction
        self.population = population
        self.cities = cities
        self.stations = stations

    def get_name(self):
        return self.name