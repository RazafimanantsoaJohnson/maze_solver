from line import Line
from point import Point

class Cell:
    def __init__(self, pointA, pointB, window= None):
        self._win= window
        self._x1= pointA.x
        self._x2= pointB.x
        self._y1= pointA.y
        self._y2= pointB.y
        self.has_upper_wall= True
        self.has_bottom_wall= True
        self.has_right_wall= True
        self.has_left_wall= True

    def draw(self):
        walls= []
        walls.append({"line":Line( pointA= Point(self._x1, self._y1), pointB= Point(self._x2, self._y1) ), "value": self.has_upper_wall})
        walls.append({"line":Line( pointA= Point(self._x1, self._y2) , pointB=Point(self._x2, self._y2) ), "value": self.has_bottom_wall})
        walls.append({"line":Line( pointA= Point(self._x1, self._y1), pointB= Point(self._x1, self._y2) ), "value": self.has_left_wall})
        walls.append({"line":Line( pointA= Point(self._x2, self._y1) ,pointB= Point(self._x2, self._y2) ), "value": self.has_right_wall})
        
        for wall in walls:
            if wall["value"]:
                self._win.draw_line(wall["line"], "black")
            else:
                self._win.draw_line(wall["line"], "white")

    def draw_move(self, to_cell, undo= False):
        color= "red"
        if undo:
            color="gray"
        move_line= Line(self.get_middle(), to_cell.get_middle())

        self._win.draw_line(move_line, color) 

    def get_middle(self):
        cell_width= self._x2 - self._x1
        cell_height= self._y2- self._y1 
        return Point((self._x2 - cell_width/2), (self._y2 - cell_height/2))    

