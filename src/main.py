#!/usr/bin/env python3
"""
Solves a given Sudoku puzzle by using a backtracking recursive approach.
"""
import numpy as np
from src import solve
from src import generate

# 32 given fields
sudoku1: list = [
    [0, 9, 2, 0, 0, 0, 8, 7, 0],
    [6, 0, 0, 4, 0, 7, 0, 0, 2],
    [3, 0, 0, 5, 0, 2, 0, 0, 9],
    [0, 7, 1, 0, 0, 0, 5, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 6, 0, 0, 0, 9, 8, 0],
    [7, 0, 0, 1, 0, 5, 0, 0, 4],
    [2, 0, 0, 8, 0, 3, 0, 0, 7],
    [0, 5, 4, 0, 0, 0, 2, 3, 0]
]
# 20 given fields. Currently not solvable within a reasonable time frame.
sudoku2: list = [
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 0],
    [4, 0, 0, 8, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 7, 0]
]
# 27 given fields
sudoku3: list = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 1, 0, 3, 8],
    [0, 2, 0, 9, 0, 3, 0, 1, 0],
    [0, 0, 8, 0, 0, 0, 4, 2, 0],
    [0, 0, 0, 0, 4, 0, 6, 9, 0],
    [0, 5, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 3, 0, 0, 6, 0],
    [0, 1, 2, 6, 9, 0, 7, 0, 4],
    [0, 6, 0, 0, 0, 0, 0, 0, 0]
]

# ambigous sudoku
ambigous: list = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 3, 8],
    [0, 2, 0, 9, 0, 3, 0, 1, 0],
    [0, 0, 8, 0, 0, 0, 4, 2, 0],
    [0, 0, 0, 0, 4, 0, 6, 9, 0],
    [0, 5, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 3, 0, 0, 6, 0],
    [0, 1, 2, 6, 9, 0, 7, 0, 4],
    [0, 6, 0, 0, 0, 0, 0, 0, 0]
]

sudoku4: list = [
    [1, 0, 0, 2, 8, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 5, 6, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 1, 0],
    [0, 7, 0, 0, 0, 4, 1, 0, 3],
    [2, 0, 5, 0, 0, 0, 0, 9, 0],
    [3, 4, 0, 9, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 7, 6],
    [0, 0, 0, 0, 3, 0, 5, 0, 0],
    [0, 0, 0, 0, 9, 7, 0, 0, 0]
]
hardest: list = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0], 
    [0, 7, 0, 0, 9, 0, 2, 0, 0], 
    [0, 5, 0, 0, 0, 7, 0, 0, 0], 
    [0, 0, 0, 0, 4, 5, 7, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 3, 0], 
    [0, 0, 1, 0, 0, 0, 0, 6, 8], 
    [0, 0, 8, 5, 0, 0, 0, 1, 0], 
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

class Counter(object):
    """
    Class for counting (recursive) function calls. 
    """
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.func(*args, **kwargs)

def print_grid(grid: list) -> str:
    """
    Transforms a list representing a Sudoku grid to a printable and readable
    string for printing.

    Parameters
    ----------
    grid: list
        Sudoku grid to transform
        
    Returns
    -------
    str
        A string for printing
    """
    grid_str = ""
    # Rows
    for y in range(0, 9):
        # Indicate a new subgrid after 3 rows
        if y in [3, 6]:
            grid_str += "=" * 9 + "||" + "=" * 9 + "||" + "=" * 9 + "\n"
        # Columns
        for x in range(0, 9):
            # Zero represents an empty field
            if grid[y][x] == 0: 
                grid_str += " " * 3
            else:
                grid_str += " " + str(grid[y][x]) + " "
            # Indicate the end of a subgrid
            if x in [2, 5]:
                grid_str += "||"
            elif x == 8:
                grid_str += "\n"               
    return grid_str

def string_to_grid(s: str) -> list:
    """
    Converts an string to a list representing a Sudoku.

    Parameters
    ----------
    s: str
        String representing a 9x9 Sudoku for transformation to list.
        Empty fields are either "0" or ".".

    Returns
    -------
    list
        Representing a 9x9 Sudoku.
    """
    if len(s) != 81 + 9:
        raise AttributeError
    sudoku: list = []
    row: list = []
    for i, char in enumerate(s):
        if char == ".":
            char = "0"
        if char == ";":
            sudoku.append(row)
            row = []
            continue 
        row.append(int(char))
    return sudoku

def main():
    import time
    start = time.time()
    solve.quick_solve = Counter(solve.quick_solve)
    print(print_grid(solve.quick_solve(sudoku1, [], False)[0]), solve.quick_solve.counter)
    end = time.time()
    print(end - start, "sec")

    print(generate.generate_full_sudoku())
    
    """full = generate.generate_full_sudoku()
    print(full)
    print(print_grid(full))
    gen = generate.generate_sudoku(full, 56)
    print(print_grid(gen))
    print(print_grid(solve.quick_solve(gen, [])[0]))"""

if __name__ == "__main__":
    main()
