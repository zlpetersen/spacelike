

class Ship:
    def __init__(self, name="", category="", hp=0, shield=0, size=0, faction="", captain=None, crew=None):
        if crew is None:
            crew = []
        self.name = name
        self.category = category
        self.hp = hp
        self.shield = shield
        self.size = size
        self.faction = faction
        self.captain = captain
        self.crew = crew
