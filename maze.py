from cell import Cell
from point import Point
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win= None):
        self.x1= x1
        self.y1= y1
        self.num_rows= num_rows
        self.num_cols= num_cols
        self.cell_size_x= cell_size_x
        self.cell_size_y= cell_size_y
        self._win= win
        self._create_cell()

    def _create_cell(self):
        #maze creation
        self._cells= [[Cell( Point(self.x1,self.y1), Point(self.x1, self.y1)) for j in range(self.num_rows)] for i in range(self.num_cols)]
        
        if self._win != None:
            for i in range(self.num_cols):
                for j in range(self.num_rows):
                    self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        y= self.y1+(i* self.cell_size_y)
        x= self.x1+(j*self.cell_size_x)
        self._cells[i][j]= Cell(Point(x,y), Point(x+ self.cell_size_x, y+self.cell_size_y), self._win)
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        # manually call redraw to see the changes 
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        top_left_cell= self._cells[0][0]
        bottom_right_cell= self._cells[self.num_cols-1][self.num_rows-1]
        top_left_cell.has_upper_wall= False
        bottom_right_cell.has_bottom_wall= False    
        
        if (self._win != None):
            print("drawing the entrance and exit")
            top_left_cell.draw()
            bottom_right_cell.draw()


