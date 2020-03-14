import numpy as np
from src import generate
from src import solve

# 32 given fields
grid1: list = [
    [0, 9, 2, 0, 0, 0, 8, 7, 0],
    [6, 0, 0, 4, 0, 7, 0, 0, 2],
    [3, 0, 0, 5, 0, 2, 0, 0, 9],
    [0, 7, 1, 0, 0, 0, 5, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 4, 6, 0, 0, 0, 9, 8, 0],
    [7, 0, 0, 1, 0, 5, 0, 0, 4],
    [2, 0, 0, 8, 0, 3, 0, 0, 7],
    [0, 5, 4, 0, 0, 0, 2, 3, 0]
]

def test_generate_full_sudoku():
    gen: np.matrix = generate.generate_full_sudoku()
    assert type(gen) == list
    assert solve.validate(gen) == True
    # Check if no zero occur / the sudoku has been filled completly.
    zero = False
    for i in range(len(gen)):
        if 0 in gen[i]:
            zero = True
    assert zero == False

    # function can also be used for solving however it's slower
    assert generate.generate_full_sudoku(grid1) == solve.quick_solve(grid1)[0]

def test_generate_sudoku():
    gen: list = generate.generate_sudoku(generate.generate_full_sudoku(), 48)
    assert type(gen) == list
    assert solve.validate(gen) == True
    assert generate.finished(gen) == False
    assert len(generate.filled_fields(gen)) == 81 - 48

def test_filled_fields():
    pass

def test_finished():
    pass