#!/usr/bin/env python3
"""
Contains class for the graphical user interface of a Sudoku game.
"""
from src import sudoku
import tkinter as tk
from tkinter.filedialog import askopenfile
from tkinter.simpledialog import askinteger


class Gui(tk.Frame):
    """
    The Tkinter UI, responsible for drawing the board and accepting user input.
    """
    def __init__(self, parent, board):
        self.parent = parent
        self.board = board
        tk.Frame.__init__(self, parent, bg="white")

        self.row, self.col = 0, 0
        self.margin = 20
        self.side = 50
        self.height = self.width = self.margin * 2 + self.side * 9
        self.__initUI()

    def __initUI(self):
        """
        Concerned with initializing all UI elements.
        """
        self.parent.title("Sudoku")
        self.parent.configure(background="white", bg="white")
        self.pack(fill=tk.BOTH, expand=1)

        # Init menu
        self.menu = tk.Menu(self.parent, background="white")
        self.parent.config(menu=self.menu)
        fileMenu = tk.Menu(self.menu, tearoff=0)
        sudokuMenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=fileMenu, background="white", activebackground="light blue")
        self.menu.add_cascade(label="Sudoku", menu=sudokuMenu, background="white", activebackground="light blue")
        fileMenu.add_command(label="Load", command=self.__load_board, background="white", activebackground="white")
        fileMenu.add_command(label="Save", command=self.__save_board, background="white", activebackground="white")
        sudokuMenu.add_command(label="Solve", command=self.__solve, background="white", activebackground="white")
        sudokuMenu.add_command(label="Generate", command=self.__generate_board, background="white", activebackground="white")
        sudokuMenu.add_command(label="Set", command=self.__set_board, background="white", activebackground="white")
        sudokuMenu.add_command(label="Check", command=self.__check_board, background="white", activebackground="white")
        sudokuMenu.add_command(label="Clear Answers", command=self.__clear_answers, background="white", activebackground="white")
        sudokuMenu.add_command(label="Clear all", command=self.__clear_all, background="white", activebackground="white")

        # Canvas for the grid
        self.canvas = tk.Canvas(self, width=self.width, height=self.height, background="white")
        self.canvas.pack(fill=tk.BOTH, side=tk.TOP)

        self.__draw_grid()
        self.__draw_puzzle()

        # Bind left mouse click and keypress to functions
        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.canvas.bind("<Key>", self.__key_pressed)
        self.canvas.bind("<Return>", (lambda event: self.__set_board()))

    def __load_board(self):
        """
        Concerned with loading a Sudoku grid saved as textfile matching the
        format specified in the README.md
        """
        fname = askopenfile(filetypes=[("Textfiles", "*.txt")])
        with open(file=fname.name, mode=fname.mode) as file:
            grid: str = file.readline().replace("\n", "")
        self.board = sudoku.Sudoku(grid)
        self.__set_board()
        self.__draw_puzzle()

    def __save_board(self):
        """
        Saves the current Sudoku grid as a textfile to a specified location
        on the disk.
        """
        fname = tk.filedialog.asksaveasfilename(filetypes=[("Textfiles", "*.txt")])
        with open(file=fname, mode="w") as file:
            file.write(self.board.grid_to_string(self.board.grid))

    def __set_board(self):
        """
        Sets the current grid as the starting grid.
        """
        if self.board.validate():
            if self.board.start_grid != self.board.grid:
                self.board.start_grid = list(map(list, self.board.grid))
            else:
                self.board.start_grid = self.board.empty_grid
        else:
            tk.messagebox.showerror("Incorrect", "The Sudoku is not valid and cannot be set!", )
        self.__draw_puzzle()

    def __solve(self):
        """
        Solves the current grid and displays the solution.
        """
        self.board.quick_solve(False)
        self.board.grid = self.board.solved_grid
        self.__draw_puzzle()

    def __generate_board(self):
        """
        Generates a new solvable Sudoku grid with a specified amount of
        missing cells.
        """
        self.board.generate_full_sudoku()
        inpt = askinteger("Input", "Enter Number of cleared cells")
        self.board.generate_sudoku(inpt)
        self.__draw_puzzle()

    def __check_board(self):
        """
        Checks whether the current grid is a valid Sudoku by checking for
        Sudoku rule violations.
        """
        if self.board.validate():
            tk.messagebox.showinfo("Correct", "The Sudoku is valid.")
        else:
            tk.messagebox.showwarning("Incorrect", "The Sudoku is not valid!")

    def __draw_grid(self):
        """
        Draws a 9x9 grid divided by lines into 3x3 squares
        """
        for i in range(10):
            if i % 3 == 0:
                color = "black"
            else:
                color = "light grey"

            x0 = self.margin + i * self.side
            y0 = self.margin
            x1 = self.margin + i * self.side
            y1 = self.height - self.margin
            if i % 3 != 0:
                self.canvas.create_line(x0, y0, x1, y1, fill=color, dash=(4, 2))
            else:
                self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = self.margin
            y0 = self.margin + i * self.side
            x1 = self.width - self.margin
            y1 = self.margin + i * self.side
            if i % 3 != 0:
                self.canvas.create_line(x0, y0, x1, y1, fill=color, dash=(4, 2))
            else:
                self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self):
        """
        Fills in the cells while differentiating between given cells
        and answers given by the user.
        """
        self.canvas.delete("numbers")
        for y in range(9):
            for x in range(9):
                answer = self.board.grid[y][x]
                if answer != 0:
                    x0 = self.margin + x * self.side + self.side / 2
                    y0 = self.margin + y * self.side + self.side / 2
                    original = self.board.start_grid[y][x]
                    if original == 0:
                        color = "sea green"
                    else:
                        color = "black"
                    self.canvas.create_text(x0,
                                            y0,
                                            text=answer,
                                            tags="numbers",
                                            fill=color)

    def __clear_answers(self):
        """
        Clears all cells entered by the user while keeping the starting grid.
        """
        self.board.grid = list(map(list, self.board.start_grid))
        self.board.solved_grid = list(map(list, self.board.empty_grid))
        self.__draw_puzzle()

    def __clear_all(self):
        """
        Resets the grid, the starting grid and the solution.
        """
        self.board = sudoku.Sudoku()
        self.__draw_puzzle()

    def __cell_clicked(self, event):
        """
        Determines which cell has been selected at mouse click.
        """
        x, y = event.x, event.y
        if (self.margin < x < self.width - self.margin and self.margin < y < self.height - self.margin):
            self.canvas.focus_set()

            # get row and col numbers from x,y coordinates
            row, col = int((y - self.margin) / self.side), int((x - self.margin) / self.side)

            # if cell was selected already - deselect it
            if (row, col) == (self.row, self.col):
                self.row, self.col = -1, -1
            else:
                self.row, self.col = row, col

        self.__draw_cursor()

    def __draw_cursor(self):
        """
        Outlines the selected cell.
        """
        self.canvas.delete("cursor")
        if self.row >= 0 and self.col >= 0:
            x0 = self.margin + self.col * self.side + 1
            y0 = self.margin + self.row * self.side + 1
            x1 = self.margin + (self.col + 1) * self.side - 1
            y1 = self.margin + (self.row + 1) * self.side - 1
            self.canvas.create_rectangle(
                x0, y0, x1, y1,
                outline="light blue", tags="cursor")

    def __key_pressed(self, event):
        """
        Fills the selected cell with the entered number while only allowing
        changes to grid but not the starting grid.
        """
        if self.row >= 0 and self.col >= 0 and event.char in "1234567890" and self.board.start_grid[self.row][self.col] == 0:
            self.board.grid[self.row][self.col] = int(event.char)
            self.col, self.row = -1, -1
            self.__draw_puzzle()
            self.__draw_cursor()
