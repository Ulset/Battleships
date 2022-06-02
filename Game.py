from AI import AI
from Player import Player


class Game:
    def __init__(self, p1: Player, p2: Player):
        self.player1 = p1
        self.player2 = p2

    def game_loop(self):
        while True:
            print(f"{self.player1.name}, where do you want to shoot? 'x,y'")
            x, y = input("x,y: ").split(",")
            shot = self.player2.try_shot(int(x), int(y))
            if shot:
                print("You hit!")
            else:
                print("No hit")
            self.player2.print_player_board(True)
            print("^ - Your hits")

    def setup_game(self):
        self.player1.set_boats()
        self.player2.set_boats()


if __name__ == '__main__':
    player1 = Player("Sander")
    player2 = AI()

    game = Game(player1, player2)
    game.setup_game()
    game.game_loop()
