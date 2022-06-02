from AI import AI
from Player import Player


class Game:
    def __init__(self, p1: Player, p2: Player):
        self.player1 = p1
        self.player2 = p2

    def game_loop(self):
        while True:
            self._play_turn(self.player1)
            self._play_turn(self.player2)

    @staticmethod
    def _play_turn(p: Player):
        print(f"Player '{p.name}'s turn!'")
        x, y = input("Where do you wanna hit? 'x,y' format: ").split(",")

    def setup_game(self):
        self.player1.set_boats()
        self.player2.set_boats()


if __name__ == '__main__':
    player1 = Player("Sander")
    player2 = AI()

    game = Game(player1, player2)
    game.setup_game()
