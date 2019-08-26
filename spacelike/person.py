
class Person:
    def __init__(self, fname="", lname="", gender="", ship="", backstory="", job="", faction="", home=None):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.ship = ship
        self.backstory = backstory
        self.job = job
        self.faction = faction
        self.home = home

    def get_info(self):
        return {"fname": self.fname,
                "lname": self.lname,
                "gender": self.gender,
                "ship": self.ship,
                "backstory": self.backstory,
                "job": self.job,
                "faction": self.faction,
                "home": self.home.get_name()}

