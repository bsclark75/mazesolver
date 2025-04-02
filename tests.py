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

if __name__ == "__main__":
    unittest.main()
