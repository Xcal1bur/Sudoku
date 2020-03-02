#!/usr/bin/env python3
"""Contains function for generating and validating Sudokus."""
import random
import numpy as np

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
        if (grid[y, i] == num) and (i != x):
            return False
        elif (grid[i, x] == num) and (i != y):
            return False

    # Determine 3x3 subgrid the field is in.
    x0: int = (x // 3) * 3
    y0: int = (y // 3) * 3

    # Check subgrid
    for i in range(0,3):
        for k in range(0, 3):
            if (grid[y0+i, x0+k] == num) and (y0+i != y) and (x0+k != x):
                return False
            elif (grid[y0+k, x0+i] == num) and (y0+k != y) and (x0+i != x):
                return False

    return True

def check(grid: np.matrix) -> bool:
    """
    Checks whether a given Sudoku is valid.
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y, x] != 0:
                if possible(y, x, grid[y, x], grid) == False:
                    return False
    return True

def generate_sudoku(
    grid: np.matrix = np.matrix(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],])
    ):
    """
    Generates a Sudoku with a given amount of fields. random.randint(1,9)
    """     
    for y in range(0, 9):
        for x in range(0, 9):
            l = list(range(1, 10))
            if grid[y, x] == 0:
                while len(l) > 0:
                    r = random.choice(l)
                    #print(grid)
                    if possible(y, x, r, grid):
                        grid[y, x] = r
                        ret = generate_sudoku(grid)

                        if type(ret) != np.matrix:
                            grid[y, x] = 0
                        else:
                            return ret
                    l.remove(r)
                return
    return grid
