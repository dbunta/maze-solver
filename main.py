from window import *

def main():
    window = Window(800, 600)
    cell1 = Cell(window, Point(10, 10), Point(40, 40), True, True, True, False)
    cell1.draw()

    cell2 = Cell(window, Point(10, 50), Point(40, 80), True, True, False, True)
    cell2.draw()

    cell3 = Cell(window, Point(90, 10), Point(120, 40), True, False, True, True)
    cell3.draw()

    cell4 = Cell(window, Point(130, 10), Point(160, 40), False, True, True, True)
    cell4.draw()

    cell1.draw_move(cell2, True)
    # line1 = Line(Point(0, 0), Point(100, 100))
    # window.draw_line(line1, "red")

    # line2 = Line(Point(100, 100), Point(100, 300))
    # window.draw_line(line2, "blue")

    window.wait_for_close()

main()
