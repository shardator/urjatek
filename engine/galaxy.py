import random
import pygame

from engine.starsystem import StarSystem
from engine.hyperlane import HyperLane
from engine.galaxy_interface import GalaxyInterface


class Galaxy(GalaxyInterface):
    def __init__(self, num_star_systems: int, width: int, height: int):
        self.systems = []
        self.width = width
        self.height = height
        self.hyperLanes = set()
        self.startingSystems = []

        for i in range(0, num_star_systems):
            ready = False
            x, y = 0, 0

            while not ready:
                x = random.random() * width
                y = random.random() * height

                if (x < 20 or x > width - 20) or (y < 20 or y > height - 20):
                    continue

                ready = True

                for other_system in self.systems:
                    ox, oy = other_system.position

                    if (x - ox) * (x - ox) + (y - oy) * (y - oy) < (15 * 15):
                        ready = False
                        break

            new_system = StarSystem((int(x), int(y)), int(random.random() * 10 + 1), 0)
            self.systems.append(new_system)

        # TODO FIGYELEM: Több kezdő rendszer kell!
        self.startingSystems = [random.choice(list(self.systems))]

    def get_starting_system(self, index: int):
        assert index >= 1
        assert index <= len(self.startingSystems)
        return self.startingSystems[index - 1]

    def draw(self, screen):
        for hyper_lane in self.hyperLanes:
            pygame.draw.line(screen, (0, 0, 255), hyper_lane.start_system.position, hyper_lane.end_system.position)
        for system in self.systems:
            pygame.draw.circle(screen, (255, 255, 0), system.position, 3, width=0)

    def closest_system(self, position: (int, int)):
        x, y = position
        min_distance = None
        result = None
        for system in self.systems:
            sx, sy = system.position
            dx = x - sx
            dy = y - sy
            distance = dx * dx + dy * dy
            if min_distance is None or min_distance > distance:
                min_distance = distance
                result = system
        return result, min_distance

    def add_hyper_lane(self, from_system: StarSystem, to_system: StarSystem):
        for hyper_lane in self.hyperLanes:
            if (hyper_lane.start_system.position is from_system and
                    hyper_lane.end_system.position is to_system):
                return

        h = HyperLane(from_system, to_system, None)
        from_system.add_outgoing_lane(h)
        to_system.add_incoming_lane(h)
        self.hyperLanes.add(h)
