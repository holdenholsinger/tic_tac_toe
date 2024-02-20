from grid import Grid


class Game:
    def __init__(self):
        self.grid = Grid()

    def announce_winner(self):
        if self.grid.has_winner:
            print(f'The winner is {self.grid.winning_player}')

    def display_grid(self):
        print("Here is the game board: ")
        for row in self.grid.game_grid:
            print(row)

    def player_turn(self):
        letter = input('Which player are you (x or o): ')
        while True:
            row = int(input(f"Which row would you like to place your {letter!r} in (1, 2, or 3): "))
            column = int(input(f"Which column would you like to place your {letter!r} in (1, 2, or 3): "))
            if not self.grid.game_grid[row - 1][column - 1]:
                self.grid.game_grid[row - 1][column - 1] = letter
                break
            print('Try again, that space is occupied.\n')

    def game_loop(self):
        while self.grid.game_can_continue:
            self.display_grid()
            self.player_turn()
            if not self.grid.game_can_continue:
                self.display_grid()
                if self.grid.has_winner:
                    self.announce_winner()
                else:
                    print('Tie game! Everybody wins!')
                keep_playing = input("Want to play again? Type 'y' to keep playing and 'n' to stop: ")
                if keep_playing != 'y':
                    break
                else:
                    self.grid.reset()
