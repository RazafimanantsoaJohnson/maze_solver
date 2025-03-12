from tkinter import Tk,BOTH, Canvas
from line import Line
from point import Point
from cell import Cell
from maze import Maze

class Window:
    def __init__(self,width,height):
        self.root= Tk()
        self.root.title= "MAZE SOLVER"
        self.canvas= Canvas(self.root,width= width,height=height, bg="white")
        self.canvas.pack(expand=1)
        self.running= False
        
        self.root.protocol("WM_DELETE_WINDOW",self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        self.running= True
        while self.running:
            self.redraw()

    def close(self):
        self.running= False


def main():

    win= Window(800,800)  
    maze= Maze(50,50,12,10,50,50, win)
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze._reset_cells_visited()
    win.wait_for_close()

main()