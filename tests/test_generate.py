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

def test_possible():
    assert type(generate.possible(0, 0, 1, grid1)) == bool
    assert generate.possible(0, 0, 1, grid1) == True
    assert generate.possible(0, 0, 4, grid1) == True
    assert generate.possible(1, 5, grid1[1, 5], grid1) == True
    assert generate.possible(6, 5, grid1[6, 5], grid1) == True
    # Test subgrid detection
    assert generate.possible(0, 0, 9, grid1) == False
    # Test row detection
    assert generate.possible(0, 0, 2, grid1) == False
    # Test column detection
    assert generate.possible(0, 0, 7, grid1) == False
    # Test all possible numbers for y=0, x=0
    pos: dict = {}
    for x in range(1, 10):
        pos[x] = generate.possible(0, 0, x, grid1)
    assert pos == {1: True, 2: False, 3: False, 4: True, 5: True, 6: False, 7: False, 8: False, 9: False}

def test_validate():
    assert type(generate.validate(grid1)) == bool
    assert generate.validate(grid1) == True
    assert generate.validate(solve.backtrack_solve(grid1)) == True

def test_generate_sudoku():
    assert type(generate.generate_sudoku()) == np.matrix
    assert generate.validate(generate.generate_sudoku()) == True
    # Check if no zero occur / the sudoku has been filled completly.
    grid = generate.generate_sudoku().tolist()
    zero = False
    for i in range(len(grid)):
        if 0 in grid[i]:
            zero = True
    assert zero == False


