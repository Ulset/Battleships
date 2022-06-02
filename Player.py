from Board import Board


class Player:
    def __init__(self, name):
        self.name = name
        self._board = Board()

    def set_boats(self):
        print(f"Player {self.name}, time to set your boats!")
        self._board.print_board()
        boat_sizes = [5, 4]
        for size in boat_sizes:
            print(f'What is the starting cordinates of the boat with length "{size}"? Give it in "x,y" format')
            x, y = input("x,y :").split(",")
            horizontal_inp = input("Should it be horizontal? (yes or no): ")
            is_horizontal = horizontal_inp.lower().startswith("y")
            self._board.place_ship(int(x), int(y), size, is_horizontal)
            self._board.print_board()

    def print_player_board(self, only_hits=False):
        self._board.print_board(only_hits)

    def try_shot(self, x, y):
        return self._board.shoot_cord(x, y)
