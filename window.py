from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title = ""
        self.canvas = Canvas(self.root, bg="white", width=width, height=height)
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
    def __init__(self, window):
        self.x_top_left = None
        self.y_top_left = None
        self.x_bottom_right = None
        self.y_bottom_right = None
        self.has_right_wall = True
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.window = window
    
    def draw(self, x_top_left, y_top_left, x_bottom_right, y_bottom_right):
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left 
        self.x_bottom_right = x_bottom_right
        self.y_bottom_right = y_bottom_right
        point_bottom_right = Point(self.x_bottom_right, self.y_bottom_right)
        point_top_left = Point(self.x_top_left, self.y_top_left)
        point_bottom_left = Point(self.x_top_left, self.y_bottom_right)
        point_top_right = Point(self.x_bottom_right, self.y_top_left)
        left_wall = Line(point_bottom_left, point_top_left)
        print(f"has left wall: {self.has_left_wall}")
        if not self.has_left_wall:
            print(f"white: {point_bottom_left.x}, {point_bottom_left.y}")
        self.window.draw_line(left_wall, "black" if self.has_left_wall else "white")
        right_wall = Line(point_bottom_right, point_top_right)
        self.window.draw_line(right_wall, "black" if self.has_right_wall else "white")
        top_wall = Line(point_top_left, point_top_right)
        self.window.draw_line(top_wall, "black" if self.has_top_wall else "white")
        bottom_wall = Line(point_bottom_right, point_bottom_left)
        self.window.draw_line(bottom_wall, "black" if self.has_bottom_wall else "white")

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