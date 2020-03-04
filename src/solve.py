#!/usr/bin/env python3
"""Contains functions for solving Sudokus."""
import numpy as np
from src import generate

def backtrack_solve(grid: np.matrix, solutions: list = []) -> np.matrix:
    """
    Solves a given sudoku grid by brute forcing and backtracking.
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y, x] == 0:
                for num in range(1, 10):
                    if generate.possible(y, x, num, grid):
                        grid[y, x] = num
                        solutions = backtrack_solve(grid, solutions)
                        grid[y, x] = 0
                return solutions
    solutions.append(grid.copy())
    return solutions