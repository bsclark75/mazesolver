from line import Line
from point import Point

class Cell:
    def __init__(self, top_left, bottom_right, win=None):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win
        self.visited = False

    def __repr__(self):
        return f"Cell: top-left: {self.top_left} bottom-right: {self.bottom_right} top: {self.has_top_wall} left: {self.has_left_wall} right: {self.has_right_wall} bottom: {self.has_bottom_wall}"

    def draw(self):
        top_line = Line(self.top_left, Point(self.top_left.x, self.bottom_right.y))
        if self.has_top_wall:
            self._win.draw_line(top_line, 'black')
        else:
            self._win.draw_line(top_line, 'light gray')
        right_line = Line(Point(self.top_left.x, self.bottom_right.y), self.bottom_right)
        if self.has_right_wall:
            self._win.draw_line(right_line, 'black')
        else:
            self._win.draw_line(right_line, 'light gray')
        bottom_line = Line(Point(self.bottom_right.x, self.top_left.y), self.bottom_right)
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line, 'black')
        else:
            self._win.draw_line(bottom_line, 'light gray')
        left_line = Line(self.top_left, Point(self.bottom_right.x, self.top_left.y))
        if self.has_left_wall:
            self._win.draw_line(left_line, 'black')
        else:
            self._win.draw_line(left_line, 'light gray')

    def draw_move(self, to_cell, undo=False):
       # print(to_cell, undo)
        point_cx = midpoint(self.top_left.x, self.bottom_right.x)
        point_cy = midpoint(self.top_left.y, self.bottom_right.y)
        point_dx = midpoint(to_cell.top_left.x, to_cell.bottom_right.x)
        point_dy = midpoint(to_cell.top_left.y, to_cell.bottom_right.y)
        point_c = Point(point_cx, point_cy)
        point_d = Point(point_dx, point_dy)
        line = Line(point_c, point_d)
        if undo:
            self._win.draw_line(line, 'gray')
        else:
            self._win.draw_line(line, 'red')

def midpoint(value1, value2):
    return (value2 - value1) / 2 + value1
