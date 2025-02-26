from window import *
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window = None):
        self.cells = []
        self.x1 = x1
        self.y1 = y1
        self.window = window
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.create_cells()
        pass

    def create_cells(self):
        for i in range(0, self.num_cols):
            rows = []
            for j in range(0, self.num_rows):
                cell = Cell(self.window)
                rows.append(cell)
            self.cells.append(rows)

        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self.draw_cell(i, j)

    def draw_cell(self, i, j):
        if self.window is not None:
            xtl = (i * self.cell_size_x) + self.x1
            ytl = (j * self.cell_size_y) + self.y1
            xbr = (i * self.cell_size_x) + self.cell_size_x + self.x1
            ybr = (j * self.cell_size_y) + self.cell_size_y + self.y1
            self.cells[i][j].draw(xtl, ytl, xbr, ybr)
            self.animate()

    def animate(self):
        self.window.redraw()
        # time.sleep(.05)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_left_wall = False
        self.draw_cell(0, 0)
        self.cells[self.num_cols - 1][self.num_rows - 1].has_right_wall = False
        self.draw_cell(self.num_cols-1, self.num_rows-1)