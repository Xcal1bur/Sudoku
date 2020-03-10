#!/usr/bin/env python3
"""Contains function for generating and validating Sudokus."""
import random
import numpy as np
from src import solve

def possible(y: int, x: int, num: int, grid: np.matrix) -> bool:
    """
    Checks whether a number is a possible anwser for a field by checking 
    whether the number has no duplicates
        - in its the row
        - in its the column
        - in its 3x3 subgrid
        
    Parameters
    ----------
    y: int
        Representing the row. 0 <= y <= 8.
    x: int
        Representing the column. 0 <= x <= 8.
    num: int
        Representing the number to check. 1 <= num <= 9
    grid: numpy.matrix
        Representing the Sudoku grid.

    Returns
    -------
    bool
        True if num is valid, False if not.    
    """
    # Check row and column:
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

def validate(grid: np.matrix) -> bool:
    """
    Checks whether a given Sudoku is valid.

    Parameters
    ----------
    grid: numpy.matrix
        Sudoku grid to validate

    Returns
    -------
    bool
        True if the given Sudoku is valid, false if not.
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y, x] != 0:
                if possible(y, x, grid[y, x], grid) == False:
                    return False
    return True

def generate_sudoku(grid: np.matrix, n: int) -> np.matrix:
    """
    Clears randomly chosen fields to create a solvable Sudoku with one solution.

    Parameters
    ----------
    grid: numpy.matrix
        A fully solved, valid Sudoku.
    n: int
        The number of fields to be cleared.
    
    Returns
    -------
    numpy.matrix
        A matrix representing a Sudoku with 0 as empty fields and numbers
        from 1 to 9. 
    """
    non_empty: list = filled_fields(grid.copy())
    while True:
        print(n, len(non_empty))
        # Sudoku has to have a unique solution and there have to be
        # filled fields avialable otherwise backtrack.
        if len(solve.backtrack_solve(grid.copy(), [])) == 1 and len(non_empty) != 0:
            # Select random field from available filled fields.
            pos = random.choice(non_empty)
            yr = pos[0]
            xr = pos[1]
            if n >= 1:
                # Replace selected field with a zero and 
                # temporaly store field value in case of backtrack
                temp = grid[yr, xr]
                grid[yr, xr] = 0
                # Remove selected field from list so it wont be selected again.
                non_empty.remove(pos)
                ret = generate_sudoku(grid.copy(), n - 1)
                # Differentiate between backtrack and solution.
                if type(ret) == np.matrix:
                    return ret
                else:
                    grid[yr, xr] = temp
                    continue
            # The Sudoku only has one solution and n fields have been set to zero
            else:
                return grid.copy()
        else:
            return

def filled_fields(grid: np.matrix) -> list:
    """
    Determines all fields in a grid that are not zero / not empty.

    Parameters
    ----------
    grid: numpy.matrix
        Grid representing a Sudoku.
    
    Returns
    -------
    list
        A list containing all positions of non-empty fields. For example 
        [[0, 0], [5, 2], [1, 6]].
    """
    filled: list = []
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y, x] != 0:
                filled.append([y, x])
    return filled

def generate_full_sudoku(grid: np.matrix = np.matrix([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
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
    Generates a complete, valid Sudoku.

    Parameters
    ----------
    grid: numpy.matrix
        Acts as accumulator as this a recursive function.
    
    Returns
    -------
    numpy.matrix
        A fully solved Sudoku.
    """     
    for y in range(0, 9):
        for x in range(0, 9):
            l = list(range(1, 10))
            if grid[y, x] == 0: # Current field has to be 0
                while len(l) > 0:
                    r = random.choice(l)
                    if possible(y, x, r, grid):
                        grid[y, x] = r
                        ret = generate_full_sudoku(grid)
                        # Backtrack when return is None otherwise pass on the
                        # return value to caller.
                        if type(ret) != np.matrix:
                            grid[y, x] = 0
                        else:
                            return ret
                    l.remove(r)
                return
    # If all field are != 0 return the finished grid
    return grid
