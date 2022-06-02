from AI import AI
from Player import Player


class Game:
    def __init__(self, player: Player, ai: AI):
        self.player = player
        self.ai = ai

    def game_loop(self):
        while True:
            print(f"{self.player.name}, where do you want to shoot? 'x,y'")
            x, y = input("x,y: ").split(",")
            shot = self.ai.try_shot(int(x), int(y))
            if shot:
                print("You hit!")
            else:
                print("No hit")
            self.ai.print_player_board(show_hits=True)
            print("^ - Opponents board")
            if self.ai.has_lost():
                print("YOU WON!")
                break

            print(f"{self.ai.name}'s Turn!")
            ai_x, ai_y = self.ai.generate_shot()
            ai_shot = player1.try_shot(ai_x, ai_y)
            print(f"{self.ai.name} is aiming for ({ai_x}, {ai_y})")
            if ai_shot:
                print("It hit!")
            else:
                print("It missed.")
            player1.print_player_board(show_ships=True, show_hits=True)
            print("^ - Your board now")
            if self.player.has_lost():
                print("You lost :(")
                break

    def setup_game(self):
        self.player.set_boats()
        self.ai.set_boats()


if __name__ == '__main__':
    player1 = Player("Sander")
    player2 = AI()

    game = Game(player1, player2)
    game.setup_game()
    game.game_loop()
