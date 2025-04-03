from cell import Cell
from point import Point
import time


class Maze:
    def __init__(self, start_point, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.start_point = start_point
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
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