import unittest
from maze import Maze
from point import Point

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        
        # Check the number of rows
        self.assertEqual(
            len(m1._cells),
            num_rows,  # Should match num_rows, not num_cols
        )
        
        # Check the number of columns in the first row
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,  # Should match num_cols, not num_rows
        )
    def test_break_enterance_and_exit_wall(self):
        num_cols = 10
        num_rows = 12
        m1 = Maze(Point(0,0),num_rows, num_cols, 10, 10)
        m1._break_entrance_and_exit()
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[num_rows -1][num_cols -1].has_bottom_wall)

    def test_reset_visited(self):
        m1 = Maze(Point(0,0), 12, 10, 10, 10)
        
        # Ensure all cells are initially visited
        for row in m1._cells:
            for cell in row:
                cell.visited = True

        # Call the method to reset
        m1._reset_visited()

        # Check if all cells are now unvisited
        for row in m1._cells:
            for cell in row:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
