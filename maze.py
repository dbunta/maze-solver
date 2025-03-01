from window import *
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window = None, seed = None):
        self.cells = []
        self.x1 = x1
        self.y1 = y1
        self.window = window
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        if seed is not None:
            random.seed(seed)
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
    

    def break_walls_r(self, i, j):
        # mark cell as visited
        # check all neighbors of current cell
        # randomly choose a neighbor cell that hasn't been visited
        # if there are no cells to visit, draw current cell and break out of loop
        self.cells[i][j].visited = True
        self.draw_cell(i,j)
        while True:
            u = j-1
            d = j+1
            l = i-1
            r = i+1

            directions = []

            if u >= 0 and not self.cells[i][u].visited:
                directions.append((i,u))
            if d >= 0 and d < self.num_rows and not self.cells[i][d].visited:
                directions.append((i,d))
            if l >= 0 and not self.cells[l][j].visited:
                directions.append((l,j))
            if r >= 0 and r < self.num_cols and not self.cells[r][j].visited:
                directions.append((r,j))

            if len(directions) == 0:
                return 

            new_dir = random.choice(directions)

            if new_dir == (i,u):
                self.cells[i][j].has_top_wall = False
                self.cells[new_dir[0]][new_dir[1]].has_bottom_wall = False
            elif new_dir == (i,d):
                self.cells[i][j].has_bottom_wall = False
                self.cells[new_dir[0]][new_dir[1]].has_top_wall = False
            elif new_dir == (l,j):
                self.cells[i][j].las_left_wall = False
                self.cells[new_dir[0]][new_dir[1]].has_right_wall = False
            elif new_dir == (r,j):
                self.cells[i][j].has_right_wall = False
                self.cells[new_dir[0]][new_dir[1]].has_left_wall = False

            self.break_walls_r(new_dir[0], new_dir[1])
        
    def reset_cells_visited(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self.cells[i][j].visited = False
    
    def solve(self):
        self.solve_r(0,0)

    def solve_r(self, i, j):
        print("here")
        # return true if (i,j) is end cell or leads to an end cell
        # otherwise, return false
        self.cells[i][j].visited = True
        end_cell = (self.num_cols-1, self.num_rows-1)
        if i == end_cell[0] and j == end_cell[1]:
            return True

        u = j-1
        d = j+1
        l = i-1
        r = i+1

        directions = []

        if u >= 0 and not self.cells[i][u].visited and not self.cells[i][j].has_top_wall:
            directions.append((i,u))
        if d >= 0 and d < self.num_rows and not self.cells[i][d].visited and not self.cells[i][j].has_bottom_wall:
            directions.append((i,d))
        if l >= 0 and not self.cells[l][j].visited and not self.cells[i][j].has_left_wall:
            directions.append((l,j))
        if r >= 0 and r < self.num_cols and not self.cells[r][j].visited and not self.cells[i][j].has_right_wall:
            print("right")
            directions.append((r,j))

        for direction in directions:
            if direction == end_cell:
                # if (direction == (i,u) and not self.cells[i][j].has_top_wall) or (direction == (i,d) and not self.cells[i][j].has_bottom_wall) or (direction == (l,j) and not self.cells[i][j].has_left_wall) or (direction == (r,j) and not self.cells[i][j].has_right_wall):
                if direction == (i,u) or direction == (i,d) or direction == (l,j) or direction == (r,j):
                    return True

        for direction in directions:
            print("here")
            self.cells[i][j].draw_move(self.cells[direction[0]][direction[1]])
            self.solve_r(direction[0], direction[1])

        print(self.cells[0][0].has_top_wall)
        print(self.cells[0][0].has_bottom_wall)
        print(self.cells[0][0].has_left_wall)
        print(self.cells[0][0].has_right_wall)
        return False
        

