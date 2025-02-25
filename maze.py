from window import *
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window):
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
        y1 = self.y1
        for i in range(0, self.num_cols):
            x1 = self.x1
            y2 = y1 + self.cell_size_y
            rows = []
            for j in range(0, self.num_rows):
                x2 = x1 + self.cell_size_x
                cell = self.draw_cell(x1, y1)
                # point1, point2 = self.draw_cell(x1, y1)
                # cell = Cell(self.window, Point(x1, y1), Point(x2, y2))
                # cell = Cell(self.window, point1, point2)
                rows.append(cell)
                # cell.draw()
                x1 = x2 
            self.cells.append(rows)
            y1 = y2
        pass

    def draw_cell(self, i, j):
        x_top_left = self.x1 + i
        y_top_left = self.y1 + j
        x_bottom_right = x_top_left + self.cell_size_x
        y_bottom_right = y_top_left + self.cell_size_y

        cell = Cell(self.window, Point(x_top_left, y_top_left), Point(x_bottom_right, y_bottom_right))
        cell.draw()

        self.animate()
        return cell
        # return Point(x_top_left, y_top_left), Point(x_bottom_right, y_bottom_right)

    def animate(self):
        self.window.redraw()
        time.sleep(.05)
        pass