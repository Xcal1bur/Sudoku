#!/usr/bin/env python3
"""
Contains functions concerned with generating Sudokus.
"""
import random
import numpy as np
from src import solve

def generate_sudoku(grid: list, n: int) -> np.matrix:
    """
    Clears randomly chosen fields to create a solvable Sudoku with one solution.

    Parameters
    ----------
    grid: list
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
        if len(solve.quick_solve(grid, [])) == 1 and len(non_empty) != 0:
            # Select random field from available filled fields.
            pos = random.choice(non_empty)
            yr = pos[0]
            xr = pos[1]
            if n >= 1:
                # Replace selected field with a zero and 
                # temporaly store field value in case of backtrack
                temp = grid[yr][xr]
                grid[yr][xr] = 0
                # Remove selected field from list so it wont be selected again.
                non_empty.remove(pos)
                ret = generate_sudoku(grid, n - 1)
                # Differentiate between backtrack and solution.
                if type(ret) == list:
                    return ret
                else:
                    grid[yr][xr] = temp
                    continue
            # The Sudoku only has one solution and n fields have been set to zero
            else:
                return grid
        else:
            return

def filled_fields(grid: list) -> list:
    """
    Determines all fields in a grid that are not zero / not empty.

    Parameters
    ----------
    grid: list
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
            if grid[y][x] != 0:
                filled.append([y, x])
    return filled

def finished(grid: list) -> bool:
    """
    Returns true if there are no more empty fields in a Sudoku.

    Parameters
    ----------
    grid: list
        Representing a 9x9 Sudoku grid
    
    Returns
    -------
    bool
        True if fully filled, False if not.
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:
                return False
    return True

def generate_full_sudoku(grid: list = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]):
    """
    Generates a complete, valid Sudoku.

    Parameters
    ----------
    grid: list
        Acts as accumulator as this a recursive function.
    
    Returns
    -------
    numpy.matrix
        A fully solved Sudoku.
    """     
    for y in range(0, 9):
        for x in range(0, 9):
            l = list(range(1, 10))
            if grid[y][x] == 0: # Current field has to be 0
                while len(l) > 0:
                    r = random.choice(l)
                    if solve.possible(y, x, r, grid):
                        grid[y][x] = r
                        ret = generate_full_sudoku(grid)
                        # Backtrack when return is None otherwise pass on the
                        # return value to caller.
                        if type(ret) != list:
                            grid[y][x] = 0
                        else:
                            return ret
                    l.remove(r)
                return
    # If all field are != 0 return the finished grid
    return grid
