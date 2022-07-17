from Board import Board


class Player:
    def __init__(self, name):
        self.name = name
        self._board = Board()

    def set_boats(self):
        print(f"Player {self.name}, time to set your boats!")
        self._board.print_board(show_ships=True)
        boat_sizes = [5, 4]
        for size in boat_sizes:
            print(f'What is the starting cordinates of the boat with length "{size}"? Give it in "x,y" format')
            x, y = input("x,y :").split(",")
            horizontal_inp = input("Should it be horizontal? (yes or no): ")
            is_horizontal = horizontal_inp.lower().startswith("y")
            self._board.place_ship(int(x), int(y), size, is_horizontal)
            self._board.print_board(show_ships=True)

    def print_player_board(self, show_hits=False, show_ships=False):
        self._board.print_board(show_hits=show_hits, show_ships=show_ships)

    def try_shot(self, x, y):
        return self._board.shoot_cord(x, y)

    def get_shot(self):
        print(f"{self.name}, where do you want to shoot?")
        shot = input("x,y: ").split(",")
        return shot

    def has_lost(self):
        return self._board.all_ships_sunk()

