import numpy as np
import pytest
from src import solve
from src import generate

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
    assert type(solve.possible(0, 0, 1, grid1)) == bool
    assert solve.possible(0, 0, 1, grid1) == True
    assert solve.possible(0, 0, 4, grid1) == True
    assert solve.possible(1, 5, grid1[1, 5], grid1) == True
    assert solve.possible(6, 5, grid1[6, 5], grid1) == True
    # Test subgrid detection
    assert solve.possible(0, 0, 9, grid1) == False
    # Test row detection
    assert solve.possible(0, 0, 2, grid1) == False
    # Test column detection
    assert solve.possible(0, 0, 7, grid1) == False
    # Test all possible numbers for y=0, x=0
    pos: dict = {}
    for x in range(1, 10):
        pos[x] = solve.possible(0, 0, x, grid1)
    assert pos == {1: True, 2: False, 3: False, 4: True, 5: True, 6: False, 7: False, 8: False, 9: False}

def test_validate():
    assert type(solve.validate(grid1)) == bool
    assert solve.validate(grid1) == True
    assert solve.validate(solve.solve(grid1, [])[0]) == True

def test_solve():
    sol: list = solve.solve(grid1, [])
    assert type(sol) == list
    # Test all solutions
    for s in sol:
        if solve.validate(s) == False:
            pytest.fail("test_solve: Not all tested solutions were valid.")

def test_find_candidate():
    c = solve.find_candidate(grid1)
    assert type(c) == tuple
    assert c == ([5, 0], [5])
    # There must not be any candidate for a fully filled Sudoku
    assert solve.find_candidate(generate.generate_full_sudoku()) == ([], [])

def test_quick_solve():
    sol: list = solve.quick_solve(grid1, [])
    assert type(sol) == list
    # Test all solutions
    for s in sol:
        if solve.validate(s) == False:
            pytest.fail("test_quick_solve: Not all tested solutions were valid.")
    # Test if both solving algorithms return the same solution
    assert sol[0].tolist() == solve.solve(grid1, [])[0].tolist()
