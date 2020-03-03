<h1 align="center">
Sudoku
</h1>

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Installation](#installation)
- [Contribution](#contribution)
- [TODO](#todo)
- [License](#license)

# Description

> "Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution." (https://en.wikipedia.org/wiki/Sudoku, 2020.03.02 : 18:52) 

The program aims to solve a given sudoku riddle by brute forcing and backtracking. It will also feature Sudoku generation in the future.  

# Installation

* `git clone` this repository and run `python sudoku.py`
* So far Sudokus are hardcoded which I aim to [improve](#todo)

# Contribution

Please feel free to report bugs or request features by opening an issue.

# TODO

* [X] Generating Sudokus. 
* [ ] Implement different methods of solving.
  * [ ] Improve current algorithm.
* [ ] **Write tests**.
* [ ] Implement different versions of Sudoku like ["Alphabetical Sudoku"](https://en.wikipedia.org/wiki/Sudoku#Alphabetical_Sudoku).
* [ ] Implement method to conveniently enter new riddles.

# License

Copyright (C) 2020 David Voigt

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.
