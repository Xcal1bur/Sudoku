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

def test_generate_full_sudoku():
    gen: np.matrix = generate.generate_full_sudoku()
    assert type(gen) == np.matrix
    assert solve.validate(gen) == True
    # Check if no zero occur / the sudoku has been filled completly.
    grid = gen.tolist()
    zero = False
    for i in range(len(grid)):
        if 0 in grid[i]:
            zero = True
    assert zero == False

    # function can also be used for solving however it's slower
    assert generate.generate_full_sudoku(grid1).tolist() == solve.quick_solve(grid1)[0].tolist()

def test_generate_sudoku():
    gen: np.matrix = generate.generate_sudoku(generate.generate_full_sudoku(), 48)
    assert type(gen) == np.matrix
    assert solve.validate(gen) == True
    assert generate.isFull(gen) == False
    assert len(generate.filled_fields(gen)) == 81 - 48

def test_filled_fields():
    pass

def test_isFull():
    pass