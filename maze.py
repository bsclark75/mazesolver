from cell import Cell
from point import Point
import time


class Maze:
    def __init__(self, start_point, num_rows, num_cols, cell_size_x, cell_size_y, win):
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
        x = coords[0]
        y = coords[1]
        row_count = 0
        while row_count <= self.num_rows:
            brx = x + self.cell_size_x
            y = coords[1]
            column_count = 0
            while column_count <= self.num_cols:
                bry = y + self.cell_size_y
                self._cells.append(Cell(self.win, Point(x,y), Point(brx,bry)))
                column_count += 1
                y = bry
            row_count += 1
            x = brx
        for cell in self._cells:
            cell.draw()
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(.05)