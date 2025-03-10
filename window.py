from tkinter import Tk,BOTH, Canvas
from line import Line
from point import Point

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

    win= Window(800,600)
    line4= Line(Point(0,0),Point(600,600))
    line5= Line(Point(50,0),Point(600,600))
    line6= Line(Point(600,0),Point(600,600))
    win.draw_line(line4, "black")
    win.draw_line(line5, "red")
    win.draw_line(line6, "gray")

    win.wait_for_close()

main()