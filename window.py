from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = ""
        self.canvas = Canvas(self.root)
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while (self.running):
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Line():
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def draw(self, canvas, fill_color):
        canvas.create_line(self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y, fill=fill_color, width=2)

class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Cell():
    def __init__(self, window, point_bottom_left, point_top_right, has_left_wall=True, has_right_wall=True, has_bottom_wall=True, has_top_wall=True):
        self.x_bottom_left = point_bottom_left.x
        self.y_bottom_left = point_bottom_left.y
        self.x_top_right = point_top_right.x
        self.y_top_right = point_top_right.y
        self.has_right_wall = has_right_wall
        self.has_left_wall = has_left_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.window = window
    
    def draw(self):
        point_bottom_right = Point(self.x_top_right, self.y_bottom_left)
        point_top_left = Point(self.x_bottom_left, self.y_top_right)
        point_bottom_left = Point(self.x_bottom_left, self.y_bottom_left)
        point_top_right = Point(self.x_top_right, self.y_top_right)
        if self.has_left_wall:
            left_wall = Line(point_bottom_left, point_top_left)
            self.window.draw_line(left_wall, "black")
        if self.has_right_wall:
            right_wall = Line(point_bottom_right, point_top_right)
            self.window.draw_line(right_wall, "black")
        if self.has_top_wall:
            top_wall = Line(point_top_left, point_top_right)
            self.window.draw_line(top_wall, "black")
        if self.has_bottom_wall:
            bottom_wall = Line(point_bottom_right, point_bottom_left)
            self.window.draw_line(bottom_wall, "black")

    def draw_move(self, to_cell, undo = False):
        self_center_x = self.x_top_right - ((self.x_top_right - self.x_bottom_left)/2)
        print(f"self_center_x: {self_center_x}")
        self_center_y = self.y_top_right - ((self.y_top_right - self.y_bottom_left)/2)
        print(f"self_center_y: {self_center_y}")
        to_center_x = to_cell.x_top_right - ((to_cell.x_top_right - to_cell.x_bottom_left)/2)
        print(f"to_center_x: {to_center_x}")
        to_center_y = to_cell.y_top_right - ((to_cell.y_top_right - to_cell.y_bottom_left)/2)
        print(f"to_center_y: {to_center_y}")
        line = Line(Point(self_center_x, self_center_y), Point(to_center_x, to_center_y))
        self.window.draw_line(line, "red" if undo else "gray")