import random
import person
import planet
import ship

class Generator:
    def __init__(self, seed):
        self.seed = seed
        self.fnames = self.load_file("fnames.txt")
        self.mnames = self.load_file("mnames.txt")
        self.xnames = self.load_file("xnames.txt")
        self.lnames = self.load_file("lnames.txt")
        self.factions = self.load_file("factions.txt")
        self.jobs = self.load_file("jobs.txt")
        self.planets = self.load_file("planets.txt")

        self.planetparts = {0: [], 1: [], 2: [], 3: [], 4: []}
        for p in self.planets:
            a = 0
            for ps in p.split("-"):
                if a == 0:
                    ps = ps[0].upper() + ps[1:]
                self.planetparts[a].append(ps)
                a += 1

    def load_file(self, fname):
        with open(fname) as f:
            content = f.readlines()
        return [i.strip() for i in content]

    def generate_system(self):
        pass

    def generate_planet(self):
        name = ""
        suffixes = [" Prime", "",
                    " B", "",
                    " Alpha", "",
                    ' Proxima', "",
                    " IV", "",
                    " V", "",
                    " C", "",
                    " VI", "",
                    " VII", "",
                    " VIII", "",
                    " X", "",
                    " IX", "",
                    " D", "",
                    "", ""]
        syllables = random.randint(2, 4)
        for i in range(syllables):
            name += random.choice(self.planetparts[i])
        name += random.choice(suffixes)
        faction = random.choice(self.factions)
        population = random.randint(0, 10000000000)
        return planet.Planet(name, faction, population)

    def generate_player(self):
        gender = random.choices(['m', 'f', 'x'], weights=[.45, .45, .1])[0]
        if gender == 'f':
            fname = random.choice(self.fnames)
        elif gender == 'm':
            fname = random.choice(self.mnames)
        else:
            fname = random.choice(self.xnames)
        lname = random.choice(self.lnames)
        ship = ""
        backstory = ""
        job = random.choice(self.jobs)
        faction = random.choice(self.factions)
        home = random.choice([self.generate_planet()])
        return person.Person(fname, lname, gender, ship, backstory, job, faction, home)

    def generate_ship(self):
        faction = random.choice(self.factions)
        prefixes = {"Isolation Order": "IOS ",
                    "Industrial Workers of the Galaxy": "IWS ",
                    "Paragons of the Light": "LS ",
                    "Transhumanist Union": "TUS ",
                    "Planetary Independence Alliance": "PIA ",
                    "Imperial Anomaly Order": "Imperial ",
                    "None": ""}
        prefix = prefixes[faction]
        animals = ["Badger", "Dragon", "Wolf", "Beluga", "Whale", "Coyote", "Crocodile", "Phoenix", "Eagle", "Falcon",
                   "Centipede", "Gremlin", "Griffin", "Harpy", "Hawk", "Jellyfish", "Lion", "Lucky", "Peacock",
                   "Pegasus", "Pelican", "Piranha", "Rhino", "Serpent", "Spider", "Termite", "Raven", "Pelican",
                   "Condor", "Albatross", "Tortoise", "Unicorn", "Vulture", "Viper", "Vampire", "Wolf", "Wolverine",
                   "Woodpecker"]
        animal = random.choice(animals)

        name1_list = [animal, animal, animal, animal, animal, animal, animal, "Cryptic", "Cursed", "Baby", "Daddy",
                      "Girl", "Momma", "Dark", "Grieving", "Karmic", "Charming", "Falling", "Frontier", "Final",
                      "Forlorn", "Decrepit", "Barbaric", "Delicate", "Sentimental", "Benevolent", "Altruistic",
                      "Twisted", "Humble", "Bashful", "Depressed", "Diabolical", "Arrogant", "Ferocious", "Tiny",
                      "Dying", "Ancient", "Imaginary", "Mechanical", "Pregnant", "Robotic", "Rusty", "Curious",
                      "Wish Upon a", "Ace of", "Big", "Little", "Divine", "Eternal", "Royal", "Star", "Fire",
                      "Galactic", "Hell", "Ice", "Immortal", "Imperial", "Majestic", "Malevolent", "New", "Pandora\'s",
                      "Perilous", "Rebellious", "Relentless", "Unrelenting", "Reliant", "Remorseless", "Rising",
                      "Shooting", "Silent", "Steel", "Stellar", "Storm", "Thunder", "Unstoppable", "Untouchable",
                      "Vigilant", "Wild", "", "", "", "", ""]
        name1 = random.choice(name1_list)

        name2_list = ["", animal, animal, animal, animal, animal, animal, animal, animal, animal, animal, animal,
                      animal, animal, animal, "Achilles", "Actium", "Adder", "Adventurer", "Agememnon", "Albatross",
                      "Alexander", "Alexandria", "Alice", "Alto", "Amanda", "Amazon", "Ambition", "Analyzer", "Anarchy",
                      "Anastasia", "Andromeda", "Angel", "Angelica", "Anna", "Annihilator", "Antagonist", "Antioch",
                      "Apocalypse", "Apollo", "Aquila", "Aquitaine", "Arcadia", "Arcadian", "Archmage", "Arden", "Ares",
                      "Argo", "Argonaut", "Aries", "Arizona", "Ark", "Armada", "Armageddon", "Arrow", "Artemis",
                      "Arthas", "Ashaton", "Assassin", "Athens", "Atlas", "Aurora", "Avadora", "Avalanche", "Avalon",
                      "Avenger", "Avius", "Babylon", "Baldrin", "Bandit", "Barbara", "Basilisk", "Bastion", "Battalion",
                      "Battlestar", "Bayonet", "Behemoth", "Beholder", "Berserk", "Baby", "Daddy", "Girl", "Momma",
                      "Bishop", "Cloud", "Sparrow", "Viper", "Blade", "Blossom", "Bob", "Bravery", "Britain",
                      "Brotherhood", "Buccaneer", "Burn", "Burninator", "Buzzard", "Caelestis", "Cain", "Calamity",
                      "Calypso", "Carbonaria", "Carnage", "Carthage", "Cataclysm", "Cataphract", "Celina", "Centurion",
                      "Challenger", "Chimera", "Chronos", "Churchill", "Civilization", "Clap", "Claymore", "Colossus",
                      "Comet", "Commissioner", "Condor", "Confidence", "Conqueror", "Conquistador", "Conscience",
                      "Constantine", "Constellation", "Cordoba", "Corsair", "Cossack", "Courage", "Covenant", "Crack",
                      "Crash", "Cromwell", "Crusher", "Cyclone", "Cyclops", "Cyclopse", "Cydonia", "Dagger", "Dakota",
                      "Damascus", "Dart", "Dauntless", "Death", "Defiance", "Defiant", "Deimos", "Deinonychus",
                      "Deonida", "Desire", "Despot", "Destiny", "Destroyer", "Destructor", "Detection", "Detector",
                      "Determination", "Devastator", "Development", "Diplomat", "Discovery", "Dispatcher", "Star",
                      "Tooth", "Dreadnought", "Dream", "Duke", "Elba", "Elena", "Elizabeth", "Elysium", "Emissary",
                      "Empress", "Endeavor", "Enterprise", "Escorial", "Euphoria", "Europa", "Evolution", "Exarch",
                      "Excalibur", "Excursionist", "Executioner", "Executor", "Experience", "Exploration", "Explorer",
                      "Exterminator", "Facade", "Fade", "Fafnir", "Fate", "Flavia", "Fortitude", "Fortune", "Francesca",
                      "Freedom", "Frenzy", "Frontier", "Fudgy", "Core", "Galatea", "Gallimimus", "Gauntlet", "Geisha",
                      "Genesis", "Ghunne", "Gibraltar", "Gladiator", "Gladius", "Globetrotter", "Glorious", "Goliath",
                      "Guard", "Guardian", "Halo", "Hammer", "Hannibal", "Harbinger", "Harlegand", "Harlequin",
                      "Harmony", "Helios", "Herald", "Hercules", "Herminia", "Hope", "Horizon", "Hunter", "Huntress",
                      "Hurricane", "Icarus", "Lance", "Independence", "Inferno", "Infineon", "Infinitum", "Infinity",
                      "Ingenuity", "Innuendo", "Inquisitor", "Insurgent", "Intelligence", "Interceptor", "Intervention",
                      "Intrepid", "Intruder", "Invader", "Invictus", "Invincible", "Irmanda", "Isabella", "Janissary",
                      "Javelin", "Judgment", "Juggernaut", "Karma", "Karnack", "Katherina", "Kennedy", "Khan",
                      "Kingfisher", "Kipper", "Knossos", "Kraken", "Kryptoria", "Kyozist", "Lancaster", "Lavanda",
                      "Legacy", "Leo", "Leviathan", "Liberator", "Liberty", "Lifebringer", "Lightning", "Loki",
                      "Lucidity", "Luisa", "Lullaby", "Lupus", "Mace", "Voyage", "Malta", "Manchester", "Manhattan",
                      "Manticore", "Marauder", "Marchana", "Marduk", "Maria", "Matador", "Memory", "Memphis",
                      "Mercenary", "Merkava", "Messenger", "Meteor", "Millenium", "Midway", "Minotuar", "Montgomery",
                      "Muriela", "Myrmidon", "Navigator", "Nebuchadnezzar", "Nemesis", "Neptune", "Nero", "Neurotoxin",
                      "Neutron", "Nexus", "Niagara", "Night", "Nightfall", "Nightingale", "Nihilus", "Nineveh", "Ninja",
                      "Nirvana", "Nomad", "Normandy", "Nostradamus", "Nuria", "Oberon", "Oblivion", "Observer", "Ohio",
                      "Olavia", "Omen", "Opal", "Oregon", "Orion", "Paladin", "Panama", "Pandora", "Paradise",
                      "Paramount", "Pathfinder", "Patience", "Patriot", "Pennsylvania", "Phalanx", "Philadelphia",
                      "Phobetor", "Phobos", "Pilgrim", "Pinnacle", "Pioneer", "Plaiedes", "Polaris", "Pontiac",
                      "Poseidon", "Praetor", "Prennia", "Priestess", "Prometheus", "Promise", "Prophet", "Providence",
                      "Proximo", "Pursuer", "Pursuit", "Pyrrhus", "Rafaela", "Rampart", "Ramses", "Rascal", "Ravager",
                      "Ravana", "Raven", "Raving", "Reaver", "Remus", "Renault", "Repulse", "Resolution", "Retribution",
                      "Revenant", "Revolution", "Rhapsody", "Rhodes", "Ripper", "Rising", "Romulus", "Roosevelt",
                      "Royal", "Saber", "Sagittarius", "Samurai", "Sandra", "Sara", "Saragossa", "Saratoga",
                      "Scavenger", "Scimitar", "Scorpio", "Scythe", "Seleucia", "Seraphim", "Serenity", "Rising",
                      "Shade", "Shear Razor", "Shirley", "Siberia", "Watcher", "Siren", "Slayer", "Sonne", "Sparta",
                      "Spartacus", "Spectator", "Spectrum", "Stalker", "Stalwart", "Finder", "Fury", "Opal", "Talon",
                      "Fall", "Gazer", "Hammer", "Hunter", "Aurora", "Flare", "Storm", "Spike", "Strike", "Striker",
                      "Sunder", "Suzanna", "Syracuse", "Templar", "Tenacity", "Tennessee", "Teresa", "Terigon",
                      "Thanatos", "Alliance", "Colossus", "Commissioner", "Diplomat", "Executioner", "Exterminator",
                      "Gladiator", "Guardian", "Head", "Harbinger", "Inquisitor", "Javelin", "Leviathan", "Liberator",
                      "Messenger", "Paladin", "Promise", "Prophet", "Siren", "Spectator", "Titan", "Traveler",
                      "Trident", "Vagabond", "Warrior", "Watcher", "Thebes", "Thor", "Thylacine", "Titan", "Titania",
                      "Tomahawk", "Torment", "Totale", "Tourist", "Trafalgar", "Trailblazer", "Tranquility", "Traveler",
                      "Trenxal", "Trident", "Trinity", "Triumph", "Troy", "Twilight", "Typhoon", "Tyrant", "Ulysses",
                      "Unity", "Ural", "Utopia", "Vagabond", "Valhala", "Valhalla", "Valiant", "Valkyrie", "Valor",
                      "Vanguard", "Vanquisher", "Vengeance", "Venom", "Vera", "Verdant", "Verminus", "Vespira",
                      "Victoria", "Victory", "Vindicator", "Virginia", "Vision", "Visitor", "Voyager", "Wind",
                      "Warlock", "Warrior", "Washington", "Watcher", "Wellington", "Wisdom", "Star", "Wyvern", "Xerxes",
                      "Yucatan", "Zenith", "Zephyr", "Zeus", "Zion"]
        name2 = random.choice(name2_list)
        # keep it from using same first + last
        while name1 == name2:
            name1 = random.choice(name1_list)
            name2 = random.choice(name2_list)
        spaceship_name = (prefix + " " + name1 + " " + name2)
        return ship.Ship(spaceship_name, faction=faction)

