from cell import Cell
from point import Point
import time
import random


class Maze:
    def __init__(self, start_point, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.start_point = start_point
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        coords = self.start_point.get_coords()
        x_start, y_start = coords

        for row_idx in range(self.num_rows):
            row = []
            x = x_start + row_idx * self.cell_size_x
            for col_idx in range(self.num_cols):
                y = y_start + col_idx * self.cell_size_y
                brx = x + self.cell_size_x
                bry = y + self.cell_size_y
                row.append(Cell(Point(x, y), Point(brx, bry), self.win))
            self._cells.append(row)

        if self.win:
            for row in self._cells:
                for cell in row:
                    cell.draw()
            self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(.5)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        if self.win:
            self._cells[0][0].draw()
        self._cells[self.num_rows - 1][self.num_cols -1].has_bottom_wall = False
        if self.win:
            self._cells[self.num_rows - 1][self.num_cols -1].draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []

        # Check all directions safely
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))  # Up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))  # Left
            if j < len(self._cells[0]) - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))  # Right
            if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))  # Down

            if not to_visit:
                self._cells[i][j].draw()
                return

            next_i, next_j = random.choice(to_visit)
            #print((next_i, next_j))

        # Remove walls between current and next cell
            if next_i < i:  # Up
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            elif next_i > i:  # Down
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            elif next_j < j:  # Left
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            elif next_j > j:  # Right
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False

            self._break_walls_r(next_i, next_j)

    def _reset_visited(self):
        for rows in self._cells:
            for cell in rows:
                cell.visited = False
