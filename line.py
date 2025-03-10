from point import Point

class Line:
    def __init__(self,pointA,pointB):
        self.pointA= pointA
        self.pointB= pointB

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.pointA.x, self.pointA.y, self.pointB.x, self.pointB.y, fill= fill_color, width=6-4
        )
