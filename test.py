import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols= 12
        num_rows= 10
        m1= Maze(0,0,num_rows, num_cols, 10,10)
        self.assertEqual(
            len(m1._cells),
            num_rows
        ),
        self.assertEqual(
            len(m1._cells[0]),
            num_cols
        )

    def test_draw_entrance_exit(self):
        num_cols= 12   
        num_rows= 10
        m1= Maze(0,0,num_rows,num_cols,10,10)
        m1._break_entrance_and_exit()
        self.assertEqual(
            m1._cells[0][0].has_upper_wall,
            False 
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False
        )
    
    def test_get_adjacent_cells(self):
        num_cols= 12   
        num_rows= 10
        m1= Maze(0,0,num_rows,num_cols,10,10)
        adjacent_tests= [
            m1._get_adjacent_cells(0,3),
            m1._get_adjacent_cells(1,3),
            m1._get_adjacent_cells(num_cols,num_rows),
            m1._get_adjacent_cells(0,0),
            m1._get_adjacent_cells(num_rows-1,num_cols-1)
        ]
        assumptions= [
            [(0,4),(1,3),(0,2)], 
            [(1,4),(0,3),(2,3),(1,2)],
            [],
            [(0,1),(1,0)],
            [(num_rows-2,num_cols-1), (num_rows-1,num_cols-2)]
        ]
        for i in range(len(adjacent_tests)):
            self.assertListEqual(
                assumptions[i],
                adjacent_tests[i]
            )
    def test_reset_visit_state(self):
        num_cols= 12   
        num_rows= 10
        m1= Maze(0,0,num_rows,num_cols,10,10)
        m1._cells[0][3].visited= True
        m1._cells[3][3].visited= True
        m1._cells[5][0].visited= True
        m1._reset_cells_visited()
        self.assertFalse(
            m1._cells[0][3].visited
        )
        self.assertFalse(
            m1._cells[5][0].visited
        )
        self.assertFalse(
            m1._cells[3][3].visited
        )
if __name__== "__main__":
    unittest.main()