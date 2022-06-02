BOARD_MAX = 10


class Board:
    def __init__(self):
        self._ships: list[Ship] = []

    def get_ships(self):
        return self._ships

    def place_ship(self, x_ax, y_ax, length, horizontal):
        x_in_range = 0 <= x_ax if not horizontal else 0 <= x_ax and (x_ax + length) < BOARD_MAX
        y_in_range = 0 <= y_ax if horizontal else 0 <= y_ax and (y_ax + length) < BOARD_MAX
        if not x_in_range or not y_in_range:
            raise BoardExpection(f'Ship with starting pos ({x_ax}, {y_ax}) and length {length} does not fit!')

        if self._ship_already_there(x_ax, y_ax, length, horizontal):
            raise BoardExpection('Ship already there')

        new_ship = Ship(x_ax, y_ax, length, horizontal)
        self._ships.append(new_ship)

    def _is_cord_taken(self, x_ax, y_ax):
        for ship in self._ships:
            x_max = ship.x if not ship.horizontal else ship.x + ship.length - 1
            y_max = ship.y if ship.horizontal else ship.y + ship.length - 1
            x_hit = ship.x <= x_ax <= x_max
            y_hit = ship.y <= y_ax <= y_max
            if x_hit and y_hit:
                return ship
        return False

    def _ship_already_there(self, x_ax, y_ax, length, horizontal):
        for offset in range(length):
            x = x_ax if not horizontal else x_ax + offset
            y = y_ax if horizontal else y_ax + offset
            if self._is_cord_taken(x, y):
                return True
        return False

    def print_board(self, only_hits=False):
        board = [[" " for _ in range(BOARD_MAX)] for _ in range(BOARD_MAX)]
        for ship in self.get_ships():
            if only_hits:
                for hit in ship.get_hits():
                    board[BOARD_MAX - 1 - hit[0]][hit[1]] = "X"
            else:
                for offset in range(ship.length):
                    x = ship.x if not ship.horizontal else ship.x + offset
                    y = ship.y if ship.horizontal else ship.y + offset
                    board[BOARD_MAX - 1 - y][x] = "O"

        for line in board:
            for cell in line:
                print(f"|{cell}", end="")
            print()

    def shoot_cord(self, x, y):
        ship_hit = self._is_cord_taken(x, y)
        if ship_hit:
            ship_hit.add_hit(x, y)
            return True
        return False


class Ship:
    def __init__(self, x, y, length, horizontal):
        self.id = f"{x}{y}{horizontal}"
        self.x = x
        self.y = y
        self.length = length
        self.horizontal = horizontal
        self._hits = []

    def add_hit(self, x, y):
        self._hits.append([x, y])

    def get_hits(self):
        return self._hits

    def is_sunk(self):
        return len(self._hits) == self.length


class BoardExpection(Exception):
    pass
