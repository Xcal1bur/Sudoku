#!/usr/bin/env python3
"""
Solves a given Sudoku puzzle by using a backtracking recursive approach.
"""
from src.sudoku import Sudoku
from src import counter

# 32 given fields
sudoku1: Sudoku = Sudoku([
    [0, 9, 2, 0, 0, 0, 8, 7, 0],
    [6, 0, 0, 4, 0, 7, 0, 0, 2],
    [3, 0, 0, 5, 0, 2, 0, 0, 9],
    [0, 7, 1, 0, 0, 0, 5, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 6, 0, 0, 0, 9, 8, 0],
    [7, 0, 0, 1, 0, 5, 0, 0, 4],
    [2, 0, 0, 8, 0, 3, 0, 0, 7],
    [0, 5, 4, 0, 0, 0, 2, 3, 0]
])
# 20 given fields. Currently not solvable within a reasonable time frame.
sudoku2: Sudoku = Sudoku([
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 0],
    [4, 0, 0, 8, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 7, 0]
])
# 27 given fields
sudoku3: Sudoku = Sudoku([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 1, 0, 3, 8],
    [0, 2, 0, 9, 0, 3, 0, 1, 0],
    [0, 0, 8, 0, 0, 0, 4, 2, 0],
    [0, 0, 0, 0, 4, 0, 6, 9, 0],
    [0, 5, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 3, 0, 0, 6, 0],
    [0, 1, 2, 6, 9, 0, 7, 0, 4],
    [0, 6, 0, 0, 0, 0, 0, 0, 0]
])

# ambigous sudoku
ambigous: Sudoku = Sudoku([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 3, 8],
    [0, 2, 0, 9, 0, 3, 0, 1, 0],
    [0, 0, 8, 0, 0, 0, 4, 2, 0],
    [0, 0, 0, 0, 4, 0, 6, 9, 0],
    [0, 5, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 3, 0, 0, 6, 0],
    [0, 1, 2, 6, 9, 0, 7, 0, 4],
    [0, 6, 0, 0, 0, 0, 0, 0, 0]
])

sudoku4: Sudoku = Sudoku([
    [1, 0, 0, 2, 8, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 5, 6, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 1, 0],
    [0, 7, 0, 0, 0, 4, 1, 0, 3],
    [2, 0, 5, 0, 0, 0, 0, 9, 0],
    [3, 4, 0, 9, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 7, 6],
    [0, 0, 0, 0, 3, 0, 5, 0, 0],
    [0, 0, 0, 0, 9, 7, 0, 0, 0]
])
hardest: Sudoku = Sudoku([
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0], 
    [0, 7, 0, 0, 9, 0, 2, 0, 0], 
    [0, 5, 0, 0, 0, 7, 0, 0, 0], 
    [0, 0, 0, 0, 4, 5, 7, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 3, 0], 
    [0, 0, 1, 0, 0, 0, 0, 6, 8], 
    [0, 0, 8, 5, 0, 0, 0, 1, 0], 
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
])

def main():
    import time
    start = time.time()
    print(sudoku2.print_grid())
    sudoku2.quick_solve(False)
    end = time.time()
    print(sudoku2.print_solution())
    print(sudoku2.print_grid())
    print(end - start, "sec")

    print("="* 30)
    s2 = Sudoku()
    s2.generate_full_sudoku()
    s2.generate_sudoku(49)
    print(s2.print_solution())
    
    print("="* 30)
    s1 = Sudoku(".3.......;...195...;..8....6.;8...6....;4..8....1;....2....;.6....28.;...419..5;.......7.;")
    print(s1.print_grid())

    print("="* 30)
    print(sudoku1.print_grid()) 
    sudoku1.solve()
    print(sudoku1.print_solution())

if __name__ == "__main__":
    main()
