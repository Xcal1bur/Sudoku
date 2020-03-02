#!/usr/bin/env python3
"""Solves a given Sudoku puzzle by using a backtracking recursive approach."""

import numpy as np 
import time

def possible(y: int, x: int, num: int, grid) -> bool:
    """
    Checks whether a number is a possible anwser for a field by checking 
    whether the number as no duplicates
        - in the row
        - in the collumn
        - in the 3x3 grid the field belongs to.
    """
    # Check row and collumn:
    for i in range(0, 9):
        if grid[y, i] == num:
            return False
        elif grid[i, x] == num:
            return False

    # Determine 3x3 subgrid the field is in.
    x0: int = (x // 3) * 3
    y0: int = (y // 3) * 3

    # Check subgrid
    for i in range(0,3):
        for k in range(0, 3):
            if grid[y0+i, x0+k] == num:
                return False
            elif grid[y0+k, x0+i] == num:
                return False

    return True

def backtrack_solve(grid: np.matrix) -> np.matrix:
    """
    Solves a given sudoku grid by brute forcing and backtracking. 
    Reasonably quick for sudokus with >25 given fields.
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y, x] == 0:
                for num in range(1, 10):
                    if possible(y, x, num, grid):
                        grid[y, x] = num
                        backtrack_solve(grid)
                        grid[y, x] = 0
                return grid
    print(grid)
    


if __name__ == "__main__":
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
    backtrack_solve(np.matrix(sudoku3))
