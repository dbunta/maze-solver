import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)

    def test_maze_create_cells2(self):
        num_cols = 50 
        num_rows = 80
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)
        
    def test_maze_create_cells3(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1.cells[0][0].x_top_left, None)
        self.assertEqual(m1.cells[0][0].y_top_left, None)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.break_entrance_and_exit()
        self.assertEqual(m1.cells[0][0].has_left_wall, False)
        self.assertEqual(m1.cells[num_cols-1][num_rows-1].has_right_wall, False)

    # def test_break_walls_r(self):
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     test = m1.break_walls(0,0)
    #     print(test)

    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1.break_walls_r(0,0)
        m1.reset_cells_visited()
        for i in range(0, num_cols):
            for j in range(0, num_rows):
                self.assertFalse(m1.cells[i][j].visited)

    # def test_solve(self):
    #     num_cols = 12
    #     num_rows = 10
    #     m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
    #     m1.break_entrance_and_exit()
    #     m1.break_walls_r(0,0)
    #     m1.reset_cells_visited()
    #     self.assertEqual(m1.solve_r(0,0), True)







if __name__ == "__main__":
    unittest.main()

