import numpy as np
from src import generate
from src import solve

# 32 given fields
grid1: np.matrix = np.matrix([
    [0, 9, 2, 0, 0, 0, 8, 7, 0],
    [6, 0, 0, 4, 0, 7, 0, 0, 2],
    [3, 0, 0, 5, 0, 2, 0, 0, 9],
    [0, 7, 1, 0, 0, 0, 5, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 6, 0, 0, 0, 9, 8, 0],
    [7, 0, 0, 1, 0, 5, 0, 0, 4],
    [2, 0, 0, 8, 0, 3, 0, 0, 7],
    [0, 5, 4, 0, 0, 0, 2, 3, 0]
    ])

def test_generate_sudoku():
    assert type(generate.generate_full_sudoku()) == np.matrix
    assert solve.validate(generate.generate_full_sudoku()) == True
    # Check if no zero occur / the sudoku has been filled completly.
    grid = generate.generate_full_sudoku().tolist()
    zero = False
    for i in range(len(grid)):
        if 0 in grid[i]:
            zero = True
    assert zero == False
