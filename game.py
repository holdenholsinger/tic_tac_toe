from grid import Grid


class Game:
    def __init__(self):
        self.grid = Grid()

    def announce_winner(self):
        pass


my_game = Game()
print(my_game.grid.is_full_grid)
