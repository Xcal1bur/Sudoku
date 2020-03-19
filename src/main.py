#!/usr/bin/env python3
"""
Solves a given Sudoku puzzle by using a backtracking recursive approach.
"""
import tkinter as tk
from src.sudoku import Sudoku
from src.gui import Gui


def main():
    # Initialize root window and start the loop
    root = tk.Tk()
    Gui(root, Sudoku())
    root.mainloop()


if __name__ == "__main__":
    main()
