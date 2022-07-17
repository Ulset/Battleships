import random

from Board import BOARD_MAX
from Player import Player


class AI(Player):
    # TODO Build out with logic like trying to hit close to other hits
    def __init__(self):
        super().__init__("AI")

    def set_boats(self):
        self._board.place_ship(0, 0, 1, True)

    def get_shot(self):
        shot = self.generate_shot()
        print(f"{self.name} is aiming for {','.join([str(x) for x in shot])}")
        return self.generate_shot()

    @staticmethod
    def generate_shot():
        return random.randint(0, BOARD_MAX), random.randint(0, BOARD_MAX)
