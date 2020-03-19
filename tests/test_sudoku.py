from src.sudoku import Sudoku

# 20 given fields. Currently not solvable within a reasonable time frame.
s_20: Sudoku = Sudoku([
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 0],
    [4, 0, 0, 8, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 7, 0]
])
# 27 given fields
s_27: Sudoku = Sudoku([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 6, 0, 0, 1, 0, 3, 8],
    [0, 2, 0, 9, 0, 3, 0, 1, 0],
    [0, 0, 8, 0, 0, 0, 4, 2, 0],
    [0, 0, 0, 0, 4, 0, 6, 9, 0],
    [0, 5, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 3, 0, 0, 6, 0],
    [0, 1, 2, 6, 9, 0, 7, 0, 4],
    [0, 6, 0, 0, 0, 0, 0, 0, 0]
])

# 32 given fields
s_32: Sudoku = Sudoku([
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

# ambigous sudoku
ambigous: Sudoku = Sudoku([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 3, 8],
    [0, 2, 0, 9, 0, 3, 0, 1, 0],
    [0, 0, 8, 0, 0, 0, 4, 2, 0],
    [0, 0, 0, 0, 4, 0, 6, 9, 0],
    [0, 5, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 3, 0, 0, 6, 0],
    [0, 1, 2, 6, 9, 0, 7, 0, 4],
    [0, 6, 0, 0, 0, 0, 0, 0, 0]
])

# Empty Sudoku
s_0: Sudoku = Sudoku()

# False Sudoku
s_false = Sudoku([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6]
    ] * 3)


class Test_Sudoku():

    def test_print_grid(self):
        assert type(s_20.print_grid()) == str
        assert type(s_27.print_grid()) == str
        assert type(ambigous.print_grid()) == str
        assert len(s_20.print_grid()) == 330

    def test_string_to_grid(self):
        test_s = Sudoku()
        test_s.grid = test_s.string_to_grid(".........;..6..1.38;.2.9.3.1.;..8...42.;"
                                            "....4.69.;.54......;...53..6.;.1269.7.4;.6.......;")
        assert type(test_s.string_to_grid(".........;..6..1.38;.2.9.3.1.;..8...42.;"
                                          "....4.69.;.54......;...53..6.;.1269.7.4;.6.......;")) == list
        for i in range(0, 9):
            assert test_s.grid[i] == s_27.grid[i]

    def test_possible(self):
        assert type(s_20.possible(0, 0, 1, s_20.grid)) == bool
        pos: dict = {}
        pos_27: dict = {}
        for num in range(1, 10):
            pos[num] = s_27.possible(3, 4, num, s_27.grid)
            pos_27[num] = s_0.possible(0, 0, num, s_0.grid)
        assert pos == {1: True, 2: False, 3: False, 4: False, 5: True, 6: True, 7: True, 8: False, 9: False}
        assert pos_27 == {1: True, 2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True}

    def test_validate(self):
        assert s_0.validate() is True
        assert s_false.validate() is False
        assert s_20.validate() is True
        assert s_27.validate() is True

    def test_solve(self):
        s_27.solve()
        assert s_27.solved_grid == [
            [1, 8, 3, 2, 5, 6, 9, 4, 7],
            [5, 9, 6, 4, 7, 1, 2, 3, 8],
            [4, 2, 7, 9, 8, 3, 5, 1, 6],
            [6, 3, 8, 7, 1, 9, 4, 2, 5],
            [2, 7, 1, 8, 4, 5, 6, 9, 3],
            [9, 5, 4, 3, 6, 2, 8, 7, 1],
            [8, 4, 9, 5, 3, 7, 1, 6, 2],
            [3, 1, 2, 6, 9, 8, 7, 5, 4],
            [7, 6, 5, 1, 2, 4, 3, 8, 9]
        ]
        s_32.solve()
        assert s_32.solved_grid == [
            [4, 9, 2, 3, 1, 6, 8, 7, 5],
            [6, 8, 5, 4, 9, 7, 3, 1, 2],
            [3, 1, 7, 5, 8, 2, 4, 6, 9],
            [8, 7, 1, 9, 3, 4, 5, 2, 6],
            [9, 2, 3, 6, 5, 8, 7, 4, 1],
            [5, 4, 6, 2, 7, 1, 9, 8, 3],
            [7, 3, 8, 1, 2, 5, 6, 9, 4],
            [2, 6, 9, 8, 4, 3, 1, 5, 7],
            [1, 5, 4, 7, 6, 9, 2, 3, 8]
        ]
        # Check whether all solutions will be found.
        ambigous.solve()
        assert len(ambigous.solved_grid) == 9

        # Generate sudoku by giving empty grid
        s_0.solve(False)
        assert s_0.solved_grid == [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 1, 4, 3, 6, 5, 8, 9, 7],
            [3, 6, 5, 8, 9, 7, 2, 1, 4],
            [8, 9, 7, 2, 1, 4, 3, 6, 5],
            [5, 3, 1, 6, 4, 2, 9, 7, 8],
            [6, 4, 2, 9, 7, 8, 5, 3, 1],
            [9, 7, 8, 5, 3, 1, 6, 4, 2]
        ]

    def test_quick_solve(self):
        s_20.solved_grid = s_20.empty_grid
        s_20.quick_solve(False)
        assert s_20.solved_grid == [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        s_27.solved_grid = s_20.empty_grid
        s_27.quick_solve(False)
        assert s_27.solved_grid == [
            [1, 8, 3, 2, 5, 6, 9, 4, 7],
            [5, 9, 6, 4, 7, 1, 2, 3, 8],
            [4, 2, 7, 9, 8, 3, 5, 1, 6],
            [6, 3, 8, 7, 1, 9, 4, 2, 5],
            [2, 7, 1, 8, 4, 5, 6, 9, 3],
            [9, 5, 4, 3, 6, 2, 8, 7, 1],
            [8, 4, 9, 5, 3, 7, 1, 6, 2],
            [3, 1, 2, 6, 9, 8, 7, 5, 4],
            [7, 6, 5, 1, 2, 4, 3, 8, 9]
        ]
        s_32.solved_grid = s_32.empty_grid
        s_32.quick_solve(False)
        assert s_32.solved_grid == [
            [4, 9, 2, 3, 1, 6, 8, 7, 5],
            [6, 8, 5, 4, 9, 7, 3, 1, 2],
            [3, 1, 7, 5, 8, 2, 4, 6, 9],
            [8, 7, 1, 9, 3, 4, 5, 2, 6],
            [9, 2, 3, 6, 5, 8, 7, 4, 1],
            [5, 4, 6, 2, 7, 1, 9, 8, 3],
            [7, 3, 8, 1, 2, 5, 6, 9, 4],
            [2, 6, 9, 8, 4, 3, 1, 5, 7],
            [1, 5, 4, 7, 6, 9, 2, 3, 8]
        ]

        ambigous.solved_grid == ambigous.empty_grid
        ambigous.quick_solve()
        assert len(ambigous.solved_grid) == 9

    def test_generate_full_sudoku(self):
        s_gen_1 = Sudoku()
        s_gen_1.generate_full_sudoku()
        assert s_gen_1.validate() is True

        s_gen_2 = Sudoku()
        s_gen_2.generate_full_sudoku()
        assert s_gen_2.validate() is True

        s_gen_3 = Sudoku()
        s_gen_3.generate_full_sudoku()
        assert s_gen_3.validate() is True

    def test_generate_sudoku(self):
        # Check whether the correct amount of empty cells was removed
        # / generated.
        s_gen_1 = Sudoku()
        s_gen_1.generate_full_sudoku()
        empty_cells = 48
        s_gen_1.generate_sudoku(empty_cells)
        counter = 0
        for y in range(0, 9):
            for x in range(0, 9):
                if s_gen_1.grid[y][x] == 0:
                    counter += 1
                if s_gen_1.solved_grid[y][x] == 0:
                    counter += 1
        assert counter == empty_cells

        # Test for valid solution.
        generated_solution = s_gen_1.solved_grid
        s_gen_1.solved_grid = s_gen_1.empty_grid
        s_gen_1.quick_solve(False)
        assert generated_solution == s_gen_1.solved_grid

        # Test whether the generated Sudoku is valid
        assert s_gen_1.validate() is True
