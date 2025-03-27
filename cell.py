from line import Line
from point import Point

class Cell:
    def __init__(self, win, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = win

    def draw(self):
        if self.has_top_wall:
            top_line = Line(self.top_left, Point(self.top_left.x, self.bottom_right.y))
            self._win.draw_line(top_line, 'black')
        if self.has_right_wall:
            right_line = Line(Point(self.top_left.x, self.bottom_right.y), self.bottom_right)
            self._win.draw_line(right_line, 'black')
        if self.has_bottom_wall:
            bottom_line = Line(Point(self.bottom_right.x, self.top_left.y), self.bottom_right)
            self._win.draw_line(bottom_line, 'black')
        if self.has_left_wall:
            left_line = Line(self.top_left, Point(self.bottom_right.x, self.top_left.y))
            self._win.draw_line(left_line, 'black')
