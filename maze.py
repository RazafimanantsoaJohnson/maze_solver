from cell import Cell
from point import Point
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win= None, seed= None):
        self.x1= x1
        self.y1= y1
        self.num_rows= num_rows
        self.num_cols= num_cols
        self.cell_size_x= cell_size_x
        self.cell_size_y= cell_size_y
        self._win= win
        self.seed= seed # will just help make the 'random' numbers consistent for the tests.
        self._create_cell()

        if seed!= None: # will help in debugging
            random.seed(seed)

    def _create_cell(self):
        #maze creation
        self._cells= [[Cell( Point(self.x1,self.y1), Point(self.x1, self.y1)) for j in range(self.num_cols)] for i in range(self.num_rows)]
        
        if self._win != None:
            for i in range(self.num_rows):
                for j in range(self.num_cols):
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
        bottom_right_cell= self._cells[self.num_rows-1][self.num_cols-1]
        top_left_cell.has_upper_wall= False
        bottom_right_cell.has_bottom_wall= False    
        
        if (self._win != None):
            print("drawing the entrance and exit")
            top_left_cell.draw()
            bottom_right_cell.draw()

    def _break_walls_r(self, i, j):
        # A recursive depth-first (graph traversal) function which will break walls on its way
        current_cell= self._cells[i][j]
        current_cell.visited= True
        adjacent_cells_indexes= self._get_adjacent_cells(i,j)
        while True:
            possible_directions= []
            for adjacent_cell in adjacent_cells_indexes:
                print(adjacent_cell, len(self._cells), len(self._cells[0]))
                x,y= adjacent_cell
                if not (self._cells[x][y].visited) and not(self._cells[x][y] in possible_directions):
                    possible_directions.append((x,y))
            if len(possible_directions)== 0:
                current_cell.draw()
                return
            else:
                direction= random.randint(0,len(possible_directions)-1)
                x,y= possible_directions[direction]
                if x<i:
                    current_cell.has_upper_wall= False
                    self._cells[x][y].has_bottom_wall= False
                if x>i:
                    current_cell.has_bottom_wall= False
                    self._cells[x][y].has_upper_wall= False
                if y<j:
                    current_cell.has_left_wall= False
                    self._cells[x][y].has_right_wall= False
                if y>j:
                    current_cell.has_right_wall= False
                    self._cells[x][y].has_left_wall= False
                current_cell.draw()
                self._cells[x][y].draw()
                self._break_walls_r(x,y)

            
    def _get_adjacent_cells(self,i,j):
        # we will return a tuple
        adjacent_cells= []
        if (i>= 0 and i<self.num_rows) and (j>=0 and j<self.num_cols):
            if j< self.num_cols-1:
                adjacent_cells.append((i,j+1)) # on the r
            if i>0:
                adjacent_cells.append((i-1,j)) # above
            if i< self.num_rows-1:
                adjacent_cells.append((i+1,j)) # below
            if j<= self.num_cols-1 and j>0:
                adjacent_cells.append((i,j-1)) # on the left
        print(f"Adjacents: {adjacent_cells}")
        return adjacent_cells
        
    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited= False
        
    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited= True
        if i== self.num_rows-1 and j== self.num_cols -1:
            return True
        possible_directions= self._get_adjacent_cells(i,j)
        for possible_direction in possible_directions:
            x,y= possible_direction
            if not(self._cells[x][y].visited):
                is_there_blocking_wall= True
                if x<i:
                    is_there_blocking_wall= is_there_blocking_wall and (self._cells[i][j].has_upper_wall and self._cells[x][y].has_bottom_wall)
                if x>i:
                    is_there_blocking_wall= is_there_blocking_wall and (self._cells[i][j].has_bottom_wall and self._cells[x][y].has_upper_wall)
                if y<j:
                    is_there_blocking_wall= is_there_blocking_wall and (self._cells[i][j].has_left_wall and self._cells[x][y].has_right_wall)
                if y>j:
                    is_there_blocking_wall= is_there_blocking_wall and (self._cells[i][j].has_right_wall and self._cells[x][y].has_left_wall)
                if not(is_there_blocking_wall):
                    self._cells[i][j].draw_move(self._cells[x][y])
                    is_direction_valid= self._solve_r(x,y)
                    if is_direction_valid:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[x][y],True)
        return False

