from Player import Player


class AI(Player):
    # TODO Build out with logic like trying to hit close to other hits
    def __init__(self):
        super().__init__("AI")

    def set_boats(self):
        self._board.place_ship(0, 0, 5, True)
        self._board.place_ship(0, 0, 5, True)
