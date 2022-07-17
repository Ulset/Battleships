from AI import AI
from Player import Player


class Game:
    def __init__(self, player1: Player, player2: Player):
        self.player: Player = player1
        self.player2: Player = player2

        self._setup_game()

    def _game_loop(self):
        while True:
            if self._play_round(self.player, self.player2):
                print(f"Player {self.player.name} won!")
                break
            elif self._play_round(self.player2, self.player):
                print(f"Player {self.player.name} won!")
                break

    @staticmethod
    def _play_round(player: Player, opponent: Player):
        print(f"Its {player.name}'s turn!")
        shot_x, shot_y = player.get_shot()
        shot_hit = opponent.try_shot(int(shot_x), int(shot_y))
        print("Hit!" if shot_hit else "Miss!")
        opponent.print_player_board(show_hits=True)
        print(f"^^ {player.name}'s hits on {opponent.name}")
        print("\n\n")
        return opponent.has_lost()

    def _setup_game(self):
        self.player.set_boats()
        self.player2.set_boats()

    def start_game(self):
        self._game_loop()


if __name__ == '__main__':
    p1 = Player("Sander")
    p2 = AI()

    game = Game(p1, p2)
    game.start_game()
