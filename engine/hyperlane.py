class HyperLane:
    def __init__(self, start_system, end_system, owner):
        self.start_system = start_system
        self.end_system = end_system
        self.owner = owner

    def __repr__(self):
        return f"HyperLane({self.start_system}, {self.end_system}, {self.owner})"
