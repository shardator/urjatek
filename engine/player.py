from engine.galaxy_interface import GalaxyInterface
from engine.starsystem import StarSystem
import engine.colors


class Player:
    def __init__(self, index, name, galaxy: GalaxyInterface):
        self.name = name
        self.star_systems = []  # A játékos birtokában lévő csillagrendszerek listája
        self.galaxy = galaxy
        self.index = index
        self.color = engine.colors.get_distinct_color(index)

    def add_star_system(self, star_system: StarSystem):
        star_system.set_player(self)

    def remove_star_system(self, star_system: StarSystem):
        # Implementáljátok, hogy egy csillagrendszert eltávolítson a játékos birtokai közül
        pass

    def is_my_system(self, system: StarSystem) -> bool:
        return system.is_owned_by(self)

    def add_hyper_lane(self, from_system: StarSystem, to_system: StarSystem) -> bool:
        allowed = self.is_my_system(from_system) or self.is_my_system(to_system)
        if allowed:
            self.galaxy.add_hyper_lane(from_system, to_system)
        return allowed

    def next_action(self):
        pass
