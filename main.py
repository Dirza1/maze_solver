from tkinter import Tk, BOTH, Canvas
import time

class Window():
    def __init__(self,width,height):
        self.root = Tk()
        self.root.title("Maze solver")
        self.root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running is True:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas,fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y,fill=fill_color,width=2)

class Cell():
    def __init__(self,
    _x1,
    _x2,
    _y1,
    _y2,
    _win = None,
    has_left_wall = True,
    has_right_wall= True,
    has_top_wall= True,
    has_bottom_wall= True,):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_top_wall = has_top_wall
        self.x1 = _x1
        self.x2 = _x2
        self.y1 = _y1
        self.y2 = _y2
        self.win = _win

    def draw(self):
        if self.has_left_wall is True:
            self.win.draw_line(Line(Point(self.x1,self.y1),Point(self.x1,self.y2)),"black")
        else:
            elf.win.draw_line(Line(Point(self.x1,self.y1),Point(self.x1,self.y2)),"white")
        if self.has_right_wall is True:
            self.win.draw_line(Line(Point(self.x2,self.y1),Point(self.x2,self.y2)),"black")
        else:
            self.win.draw_line(Line(Point(self.x2,self.y1),Point(self.x2,self.y2)),"white")
        if self.has_top_wall is True:
            self.win.draw_line(Line(Point(self.x1,self.y1),Point(self.x2,self.y1)),"black")
        else:
            self.win.draw_line(Line(Point(self.x1,self.y1),Point(self.x2,self.y1)),"white")
        if self.has_bottom_wall is True:
            self.win.draw_line(Line(Point(self.x1,self.y2),Point(self.x2,self.y2)),"black")
        else:
            self.win.draw_line(Line(Point(self.x1,self.y2),Point(self.x2,self.y2)),"white")
        
    def draw_move(self, to_cell, undo=False):
        self_center_x = (self.x1 + self.x2) / 2
        self_center_y = (self.y1 + self.y2) / 2
        to_cell_center_x = (to_cell.x1 + to_cell.x2) / 2
        to_cell_center_y = (to_cell.y1 + to_cell.y2) / 2
        
        if not undo:
            self.win.draw_line(Line(Point(self_center_x,self_center_y),
                                    Point(to_cell_center_x,to_cell_center_y)),"red")
        else:
            self.win.draw_line(Line(Point(self_center_x,self_center_y),
                                    Point(to_cell_center_x,to_cell_center_y)),"gray")


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        _win = None,
    ):
        
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = _win
        

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                x1 = self.x1 + (i * self.cell_size_x)
                y1 = self.y1 + (j * self.cell_size_y)
                x2 = self.x1 + ((i+1) * self.cell_size_x)
                y2 = self.y1 + ((j+1) * self.cell_size_y)

                cell = Cell(x1, x2, y1, y2, self._win)
                column.append(cell)

                self._draw_cell(i,j)
            self._cells.append(column)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        if len(self._cells) > i and len(self._cells[i]) > j:
            self._cells[i][j].draw()
        else:
            x1 = self.x1 + (i * self.cell_size_x)
            y1 = self.y1 + (j * self.cell_size_y)
            x2 = self.x1 + ((i+1) * self.cell_size_x)
            y2 = self.y1 + ((j+1) * self.cell_size_y)

            cell = Cell(x1, x2, y1, y2, self._win)
            cell.draw()
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        
        
        pass

def main():
    win = Window(800, 600)
    maze = Maze (2,2,10,10,79,59,win)
    win.wait_for_close()


if __name__ == "__main__":
    main()