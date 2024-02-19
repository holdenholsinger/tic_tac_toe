class Grid:
    WINNING_LINES = [["x", "x", "x"], ["o", "o", "o"]]
    def __init__(self):
        self.game_grid = [["", "", ""] for _ in range(3)]

        self.col1 = [self.game_grid[0][0], self.game_grid[1][0], self.game_grid[2][0]]
        self.col2 = [self.game_grid[0][1], self.game_grid[1][1], self.game_grid[2][1]]
        self.col3 = [self.game_grid[0][2], self.game_grid[1][2], self.game_grid[2][2]]

        self.diagonal1 = []
        self.diagonal2 = []

    def reset(self):
        self.game_grid = [["", "", ""] for _ in range(3)]

    @property
    def row_win_condition_met(self):
        for row in self.game_grid:
            if row in Grid.WINNING_LINES:
                return True
        return False

    @property
    def column_win_condition_met(self):
        pass

    @property
    def diagonal_win_condition_met(self):
        pass

    @property
    def is_full_grid(self):
        for row in self.game_grid:
            for slot in row:
                if not slot:
                    return False
        return True

    @property
    def winning_player(self):
        pass
        # should return 'x' or 'o'