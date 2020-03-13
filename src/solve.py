#!/usr/bin/env python3
"""
Contains functions concerned with solving and validating Sudokus.
"""
import numpy as np
from src import generate
from src import main

def possible(y: int, x: int, num: int, grid: list) -> bool:
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
    grid: list
        Representing the Sudoku grid.

    Returns
    -------
    bool
        True if num is valid, False if not.    
    """
    # Check row and column:
    for i in range(0, 9):
        if (grid[y][i] == num) and (i != x):
            return False
        elif (grid[i][x] == num) and (i != y):
            return False

    # Determine 3x3 subgrid the field is in.
    x0: int = (x // 3) * 3
    y0: int = (y // 3) * 3

    # Check subgrid
    for i in range(0,3):
        for k in range(0, 3):
            if (grid[y0+i][x0+k] == num) and (y0+i != y) and (x0+k != x):
                return False
            elif (grid[y0+k][x0+i] == num) and (y0+k != y) and (x0+i != x):
                return False

    # If no violations have been found return true
    return True

def validate(grid: list) -> bool:
    """
    Checks whether a given Sudoku is valid.

    Parameters
    ----------
    grid: list
        Sudoku grid to validate

    Returns
    -------
    bool
        True if the given Sudoku is valid, false if not.
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] != 0:
                if possible(y, x, grid[y][x], grid) == False:
                    return False
    return True

def solve(grid: list, solutions: list = []) -> np.matrix:
    """
    Solves a given sudoku grid by brute forcing and backtracking.

    Parameters
    ----------
    grid: list
        Representing a 9x9 Sudoku.
    solutions: list
        All solutions to the given Sudoku.
    
    Returns
    -------
    solutions: list
        All solutions to the given Sudoku.
    """
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:
                for num in range(1, 10):
                    if possible(y, x, num, grid):
                        grid[y][x] = num
                        solutions = solve(grid, solutions)
                        grid[y][x] = 0
                return solutions
    solutions.append(list(map(list, grid)))
    return solutions

def find_candidate(grid: list) -> tuple:
    """
    Determines the next candidate being the field with 
    the lowest amount of possible solutions.

    Parameters
    ----------
    grid: list
        Representing a 9x9 Sudoku.

    Returns
    -------
    tuple
        Containing the position of the field and the possible solutions.
        Format: ([y, x], [n*]) where "*" indicates zero or more.
    """
    min: int = 9
    min_pos: list = []
    sol: list = []
    min_sol: list = []
    # Rows
    for y in range(0, 9):
        # Columns
        for x in range(0, 9):
            # If field value is 0 find all possible solutions.
            if grid[y][x] == 0:
                count = 0
                sol = []
                for num in range(1, 10):
                    if possible(y, x, num, grid):
                        count += 1
                        sol.append(num) 
                # Save field positions with the lowest amount of possible solutions
                # as well as the possible solutions.
                if count < min:
                    min = count
                    min_pos = [y, x]
                    min_sol = sol
    return min_pos, min_sol

def quick_solve(grid: list, solutions: list = [], find_all: bool = True):
    """
    Solves a given Sudoku represented by a numpy matrix.

    Parameters
    ----------
    grid: list
        Representing a 9x9 Sudoku.
    solutions: list
        Containing all found solutions for a Sudoku. Acts as accumulator
        throughout the recursion. Initialize as empty list.
    all: bool
        Compute all possible solutions (True) or only compute one solution
        (False) which is possible much faster.
    
    Returns
    -------
    list
        Containing all found solutions for a Sudoku.
    """
    # Fill all fields otherwise append found solution to list.
    if not generate.isFull(grid.copy()):
        # Get candidate position and possible solutions
        pos, sol = find_candidate(grid.copy())
        #print(main.grid_to_string(grid), pos, sol)
        #input()
        y0 = pos[0]
        x0 = pos[1]
        # Iterate through all solutions for a field. Backtrack if no valid was found.
        for num in sol:
            grid[y0][x0] = num
            solutions = quick_solve(grid, solutions, find_all)
            # If all parameter is set to False only return one solution.
            if solutions != [] and find_all == False:
                return solutions
            # In case of backtrack reset field value to zero/empty.
            grid[y0][x0] = 0
        return solutions
    else:
        solutions.append(list(map(list, grid)))
        return solutions
