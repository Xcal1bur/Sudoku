#!/usr/bin/env python3
"""Contains functions for solving Sudokus."""
import numpy as np
import generate

def backtrack_solve(grid: np.matrix) -> np.matrix:
    """
    Solves a given sudoku grid by brute forcing and backtracking. 
    Reasonably quick for sudokus with >25 given fields.
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y, x] == 0:
                for num in range(1, 10):
                    if generate.possible(y, x, num, grid):
                        grid[y, x] = num
                        ret = backtrack_solve(grid)
                        if type(ret) != np.matrix:
                            grid[y, x] = 0
                        else:
                            return ret
                return
    return grid
