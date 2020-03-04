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

def main():
    # Examples:
    res: list = solve.backtrack_solve(np.matrix(sudoku3))
    for i in range(len(res)):
        print(f"Solution {i}:\n {res[i]} \n\t Valid: {generate.validate(res[i])}")
    print("Solutions:", len(res))
    print(generate.generate_sudoku())

if __name__ == "__main__":
    main()
