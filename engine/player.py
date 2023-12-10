from engine.galaxy import Galaxy
from engine.starsystem import StarSystem


class Player:
    def __init__(self, name, galaxy: Galaxy):
        self.name = name
        self.star_systems = []  # A játékos birtokában lévő csillagrendszerek listája
        self.galaxy = galaxy

    def add_star_system(self, star_system):
        # Implementáljátok, hogy egy csillagrendszert hozzáadjon a játékos birtokaihoz
        pass

    def remove_star_system(self, star_system):
        # Implementáljátok, hogy egy csillagrendszert eltávolítson a játékos birtokai közül
        pass

    def add_hyper_lane(self, from_system: StarSystem, to_system: StarSystem):
        self.galaxy.add_hyper_lane(from_system, to_system)

