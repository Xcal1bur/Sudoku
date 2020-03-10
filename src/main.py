#!/usr/bin/env python3
"""Solves a given Sudoku puzzle by using a backtracking recursive approach."""

import numpy as np
from src import solve
from src import generate

# 32 given fields
sudoku1: list = [[0, 9, 2, 0, 0, 0, 8, 7, 0],
[6, 0, 0, 4, 0, 7, 0, 0, 2],
[3, 0, 0, 5, 0, 2, 0, 0, 9],
[0, 7, 1, 0, 0, 0, 5, 2, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 4, 6, 0, 0, 0, 9, 8, 0],
[7, 0, 0, 1, 0, 5, 0, 0, 4],
[2, 0, 0, 8, 0, 3, 0, 0, 7],
[0, 5, 4, 0, 0, 0, 2, 3, 0]]
# 20 given fields. Currently not solvable within a reasonable time frame.
sudoku2: list = [[0, 3, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 0, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 0],
[4, 0, 0, 8, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 2, 0, 0, 0, 0],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 0, 0, 0, 7, 0]]
# 27 given fields
sudoku3: list = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 6, 0, 0, 1, 0, 3, 8],
[0, 2, 0, 9, 0, 3, 0, 1, 0],
[0, 0, 8, 0, 0, 0, 4, 2, 0],
[0, 0, 0, 0, 4, 0, 6, 9, 0],
[0, 5, 4, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 5, 3, 0, 0, 6, 0],
[0, 1, 2, 6, 9, 0, 7, 0, 4],
[0, 6, 0, 0, 0, 0, 0, 8, 0]]

def grid_to_string(grid: np.matrix) -> str:
    """
    Transforms a numpy matrix to a string for better readability when printing.

    Parameters
    ----------
    grid: np.matrix
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
            if grid[y, x] == 0: 
                grid_str += " " * 3
            else:
                grid_str += " " + str(grid[y, x]) + " "
            # Indicate the end of a subgrid
            if x in [2, 5]:
                grid_str += "||"
            elif x == 8:
                grid_str += "\n"               
    return grid_str

def main():
    # Examples:
    #res: list = solve.backtrack_solve(np.matrix(sudoku3))
    #for i in range(len(res)):
    #    print(f"Solution {i}:\n {res[i]} \n\t Valid: {generate.validate(res[i])}")
    #print("Solutions:", len(res))
    full = generate.generate_full_sudoku()
    print(full)
    print(grid_to_string(full))
    gen = generate.generate_sudoku(full, 52)
    print(grid_to_string(gen))
    print("Solutions:", len(solve.backtrack_solve(gen, [])))
    print(grid_to_string(solve.backtrack_solve(gen)[0]))

if __name__ == "__main__":
    main()
