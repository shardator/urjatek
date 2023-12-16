from engine.hyperlane import HyperLane
from engine.player import Player


class StarSystem:
    def __init__(self, position, build_capacity, defense):
        self.position = position
        self.buildCapacity = build_capacity
        self.defense = defense
        self.fleets = set()
        self.owner = None
        self.outgoingLanes = set()  # Kimenő utak listája
        self.incomingLanes = set()  # Bejövő utak listája

    def set_player(self, player: Player):
        self.owner = player

    def is_owned_by(self, player: Player) -> bool:
        return self.owner is player

    def produce_fleet(self):
        # Implementáljátok, hogy mi történjen flotta gyártásakor
        pass

    def add_outgoing_lane(self, lane: HyperLane) -> None:
        self.outgoingLanes.add(lane)

    def add_incoming_lane(self, lane: HyperLane) -> None:
        self.incomingLanes.add(lane)
