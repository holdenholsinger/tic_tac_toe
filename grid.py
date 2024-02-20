class Grid:
    WINNING_LINES = [["x", "x", "x"], ["o", "o", "o"]]

    def __init__(self):
        self.game_grid = [["", "", ""] for _ in range(3)]

    @property
    def diagonals(self) -> list:
        diagonal1 = [self.game_grid[0][0], self.game_grid[1][1], self.game_grid[2][2]]
        diagonal2 = [self.game_grid[0][2], self.game_grid[1][1], self.game_grid[2][0]]
        diagonals = [diagonal1, diagonal2]
        return diagonals

    @property
    def all_possible_lines(self):
        all_lines = self.game_grid + self.cols + self.diagonals
        return all_lines

    @property
    def cols(self) -> list:
        col1 = [self.game_grid[0][0], self.game_grid[1][0], self.game_grid[2][0]]
        col2 = [self.game_grid[0][1], self.game_grid[1][1], self.game_grid[2][1]]
        col3 = [self.game_grid[0][2], self.game_grid[1][2], self.game_grid[2][2]]
        cols = [col1, col2, col3]
        return cols

    @property
    def game_can_continue(self):
        if (self.row_win_condition_met or
            self.column_win_condition_met or
            self.diagonal_win_condition_met or
                self.is_full_grid):
            return False
        return True

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
        for col in self.cols:
            if col in Grid.WINNING_LINES:
                return True
        return False

    @property
    def diagonal_win_condition_met(self):
        for diagonal in self.diagonals:
            if diagonal in Grid.WINNING_LINES:
                return True
        return False

    @property
    def is_full_grid(self):
        for row in self.game_grid:
            for slot in row:
                if not slot:
                    return False
        return True

    @property
    def winning_player(self) -> str:
        winner = 'x' if ["x", "x", "x"] in self.all_possible_lines else 'o'
        return winner

    @property
    def has_winner(self):
        if self.diagonal_win_condition_met or self.column_win_condition_met or self.row_win_condition_met:
            return True
        return False
