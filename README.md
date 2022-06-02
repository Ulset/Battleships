# Battleships
Shitty little game of battleships

## Battleship
In this assignment, you will implement the famous board game "Battleship", with one human
player and one player to be the computer.
The game is played on a 10x10 grid, known as "the board".
Each player has their own board and five ships, which occupy different positions on the board.
The ships can be placed both horizontally and vertically, and consists of:
* A battleship (5 squares in length)
* A frigate (4 squares in length)
* Three corvettes (3 squares in length)

### Game setup
The initial setup of the game consists of the players placing their ships onto their respective
boards.
* The ships can be placed both horizontally and vertically.
* The whole ship must fit within the confines of the board.
* Two ships cannot overlap on a board, but there is no rule against two players placing
their ships in the same positions (on their respective boards).
## Game flow
Taking turns, the player and the computer will fire a shot by naming a coordinate on the board.
After each shot the game will calculate and notify if any of the opponent’s ships have been hit.
The player should also be notified if a ship they've hit has been sunk, meaning that all the
coordinates the ship occupies have been hit.
The first player to sink all of the opponent’s ships wins the game
