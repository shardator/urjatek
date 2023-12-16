import pygame

from engine.galaxy import Galaxy
from engine.player import Player


class Game:
    def __init__(self, width: int, height: int, fps: int):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Űrjáték")

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = False

        self.galaxy = Galaxy(100, width, height)
        self.selectedSystem = None
        self.prevMouseState = [0, 0, 0]
        self.hyperLanePlan = None

        self.human_player = Player(1, "Játékos", self.galaxy)
        self.human_player.add_star_system(self.galaxy.get_starting_system(1))
        self.players = [self.human_player]

    def handle_mouse(self):
        mouse_state = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        system, distance = self.galaxy.closest_system(mouse_pos)

        if mouse_state[0] or mouse_state[2]:
            if self.selectedSystem is not None:
                self.hyperLanePlan = (self.selectedSystem.position, mouse_pos)
        elif self.prevMouseState[0] or self.prevMouseState[2]:
            if distance < 36 and system is not self.selectedSystem and self.selectedSystem is not None:
                print(f"LANE: {self.selectedSystem} => {system}")
                self.galaxy.add_hyper_lane(self.selectedSystem, system)
            self.hyperLanePlan = None
        elif distance < 36:
            if self.human_player.is_my_system(system):
                self.selectedSystem = system
        else:
            self.selectedSystem = None

        self.prevMouseState = mouse_state

    def handle_events(self):
        for player in self.players:
            player.next_action()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Ide kerül a játék logika frissítése
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.galaxy.draw(self.screen)
        if self.hyperLanePlan:
            start, end = self.hyperLanePlan
            pygame.draw.line(self.screen, (255, 0, 0), start, end)

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            self.handle_mouse()
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()

        pygame.quit()
