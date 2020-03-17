import random

class Sudoku():
    """
    Class representing a Sudoku grid including methods for solving and generating.
    """

    empty_grid = [[0] * 9] * 9

    def __init__(self, p_grid=empty_grid):
        if type(p_grid) == list:
            self.grid = p_grid
        else:
            self.grid = self.string_to_grid(p_grid)
        self.solved_grid = self.empty_grid
    
    def __printable(self, grid: list) -> str:
        """
        Transforms a list representing a Sudoku grid to a printable and readable
        string for printing.
            
        Returns
        -------
        str
            A string for printing
        """
        grid_str = ""
        # Rows
        for y in range(0, 9):
            # Indicate a new subgrid after 3 rows
            if y in [3, 6]:
                grid_str += "-" * 9 + "+" + "-" * 9 + "+" + "-" * 9 + "\n"
            # Columns
            for x in range(0, 9):
                # Zero represents an empty field
                if grid[y][x] == 0: 
                    grid_str += " " * 3
                else:
                    grid_str += " " + str(grid[y][x]) + " "
                # Indicate the end of a subgrid
                if x in [2, 5]:
                    grid_str += "|"
                elif x == 8:
                    grid_str += "\n"               
        return grid_str

    def print_grid(self) -> str:
        return self.__printable(self.grid)

    def print_solution(self) -> str:
        return self.__printable(self.solved_grid)

    def string_to_grid(self, s) -> list:
        """
        Converts an string to a list representing a Sudoku.

        Parameters
        ----------
        s: str
            String representing a 9x9 Sudoku for transformation to list.
            Empty fields are either "0" or ".".

        Returns
        -------
        list
            Representing a 9x9 Sudoku.
        """
        if len(s) != 81 + 9:
            raise AttributeError
        sudoku: list = []
        row: list = []
        for char in s:
            if char == ".":
                char = "0"
            if char == ";":
                sudoku.append(row)
                row = []
                continue 
            row.append(int(char))
        return sudoku

    def possible(self, y, x, num, grid) -> bool:
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
    
    def validate(self) -> bool:
        """
        Validates the Sudoku grid.

        Returns
        -------
        bool
            True if the given Sudoku is valid, false if not.
        """
        # Rows
        for y in range(0, 9):
            # Columns
            for x in range(0, 9):
                # Don't check empty fields for obvious reasons.
                if self.grid[y][x] != 0:
                    return self.possible(y, x, self.grid[y][x], self.grid)
        return True

    def solve(self):
        """
        Solves the sudoku grid by brute forcing and backtracking.
        """
        # Local function definition to keep solve solve call clean.
        def compute_solution(grid: list, solutions: list = []) -> list:
            """
            Solves a given sudoku grid by brute forcing and backtracking.

            Parameters
            ----------
            solutions: list
                All solutions to the given Sudoku.
            
            Returns
            -------
            solutions: list
                All solutions to the given Sudoku.
            """
            # Rows
            for y in range(0, 9):
                # Columns
                for x in range(0, 9):
                    if grid[y][x] == 0:
                        # Check all possible numbers
                        for num in range(1, 10):
                            if self.possible(y, x, num, grid):
                                grid[y][x] = num
                                solutions = compute_solution(grid, solutions)
                                # Reset cell to zero after backtrack
                                grid[y][x] = 0
                        # Backtrack after no possible number was found.
                        return solutions
            # Append current grid to solutions after arriving at last cell.
            solutions.append(list(map(list, grid)))
            return solutions

        self.solved_grid = compute_solution(list(map(list, self.grid)), [])[0]

    def quick_solve(self, all_solutions: bool = True):
        """
        Solves the Sudoku by backtracking and brute force while being a
        optimized version of the normal solve function hence having a 
        drastically improved runtime for more difficult Sudokus.

        Parameters
        ----------
        all_solutions: bool
            True for computing all possible solutions and False for only one
            solution.
        """
        def find_candidate(grid) -> tuple:
            """
            Determines the next candidate being the field with 
            the lowest amount of possible solutions.

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
                            if self.possible(y, x, num, grid):
                                count += 1
                                sol.append(num) 
                        # Save field positions with the lowest amount of possible solutions
                        # as well as the possible solutions.
                        if count < min:
                            min = count
                            min_pos = [y, x]
                            min_sol = sol
            return min_pos, min_sol

        def finished(grid):
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

        def compute_solution(grid: list, solutions: list = [], find_all = True) -> list:
            """
            Solves a given Sudoku represented by a numpy matrix.

            Parameters
            ----------
            solutions: list
                Containing all found solutions for a Sudoku. Acts as accumulator
                throughout the recursion. Initialize as empty list.
            find_all: bool
                Compute all possible solutions (True) or only compute one solution
                (False) which is possible much faster.
            
            Returns
            -------
            list
                Containing all found solutions for a Sudoku.
            """
            # Fill all fields otherwise append found solution to list.
            if not finished(grid):
                # Get candidate position and possible solutions
                pos, sol = find_candidate(grid)
                y0 = pos[0]
                x0 = pos[1]
                # Iterate through all solutions for a field. Backtrack if no valid was found.
                for num in sol:
                    grid[y0][x0] = num
                    solutions = compute_solution(grid, solutions, find_all)
                    # If all parameter is set to False only return one solution.
                    if solutions != [] and find_all == False:
                        return solutions
                    # In case of backtrack reset field value to zero/empty.
                    grid[y0][x0] = 0
                return solutions
            else:
                solutions.append(list(map(list, grid)))
                return solutions

        solutions = compute_solution(list(map(list, self.grid)), [], all_solutions)
        self.solved_grid = solutions[0]
        return solutions

    def generate_full_sudoku(self):

        def full_sudoku(grid: list):
            """
            Generates a complete, valid Sudoku.
            """    
            for y in range(0, 9):
                for x in range(0, 9):
                    numbers = list(range(1, 10))
                    if grid[y][x] == 0:
                        while len(numbers) > 0:
                            num = random.choice(numbers)
                            if self.possible(y, x, num, grid):
                                grid[y][x] = num
                                ret = full_sudoku(grid)
                                if ret:
                                    return ret
                                else: grid[y][x] = 0
                            numbers.remove(num)
                        return
            return grid

        self.grid = self.solved_grid = full_sudoku(list(map(list, self.grid)))

    def generate_sudoku(self, empty_cells: int):
        """
        Clears randomly chosen cells to create a solvable Sudoku with one solution.

        Parameters
        ----------
        empty_cells: int
            The number of cells to be cleared.
        """

        def filled_fields() -> list:
            """
            Determines all fields in a grid that are not zero / not empty.

            Returns
            -------
            list
                A list containing all positions of non-empty fields. For example 
                [[0, 0], [5, 2], [1, 6]].
            """
            filled: list = []
            for y in range(0, 9):
                for x in range(0, 9):
                    if self.grid[y][x] != 0:
                        filled.append([y, x])
            return filled

        def generate(n: int) -> list:
            non_empty: list = filled_fields()
            while True:
                print(n, len(non_empty))
                # Sudoku has to have a unique solution and there have to be
                # filled fields avialable otherwise backtrack.
                if len(self.quick_solve(True)) == 1 and len(non_empty) != 0:
                    # Select random field from available filled fields.
                    pos = random.choice(non_empty)
                    yr = pos[0]
                    xr = pos[1]
                    if n >= 1:
                        # Replace selected field with a zero and 
                        # temporaly store field value in case of backtrack
                        temp = self.grid[yr][xr]
                        self.grid[yr][xr] = 0
                        # Remove selected field from list so it wont be selected again.
                        non_empty.remove(pos)
                        ret = generate(n - 1)
                        # Differentiate between backtrack and solution.
                        if ret:
                            return ret
                        else:
                            self.grid[yr][xr] = temp
                            continue
                    # The Sudoku only has one solution and n fields have been set to zero
                    else:
                        return self.grid
                else:
                    return
        # Set generated Sudoku grid as new grid.
        self.grid = generate(empty_cells)
            

s = Sudoku([
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
