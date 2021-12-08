# NRooks
Given a chess board with an initial configuration, builds/completes the chess board full of rooks at non-attacking positions. Technologies used: Python3, Numpy.

### Installation and Running

You can proceed with the installation below to run the application from your terminal. Proceed with NRooks as a root directory:

##### MacOS

```
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python3 -m unittest discover tests
python3 app.py
```

##### Windows

```
python
python.exe -m venv .venv
source .venv/Scripts/activate

pip install -r requirements.txt

python.exe -m unittest discover tests
python.exe app.py
```


### Sample Input and Output:

##### Example 1:

```
$ python3 app.py

Submit your board as a list of lists with zeroes and ones, where one represents a rook and zero represents an empty space. Remember that your board should be contained in one line, since zsh might consider it a bad pattern.

[[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 0]]


Initial board:
· · · · R · · ·
· R · · · · · ·
· · · R · · · ·
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
· · · · · R · ·
R · · · · · · ·

Solving...


· · · · R · · ·
· R · · · · · ·
· · · R · · · ·
· · R · · · · ·
· · · · · · R ·
· · · · · · · R
· · · · · R · ·
R · · · · · · ·
```

##### Example 2:

```
$ python3 app.py

Submit your board as a list of lists with zeroes and ones, where one represents a rook and zero represents an empty space. Remember that your board should be contained in one line, since zsh might consider it a bad pattern.

[[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1]] 


Initial board:
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
· · R · · · · ·
· · · · R · · ·
· · · · · · R R

Solving...


Error: More than one rook in a single row
```

##### Example 2:

```
$ python3 app.py

Submit your board as a list of lists with zeroes and ones, where one represents a rook and zero represents an empty space. Remember that your board should be contained in one line, since zsh might consider it a bad pattern.

[[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1, 1]] 


Initial board:
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
· · · · · · · ·
· · R · · · · ·
· · · · R · · ·
· · · · · · R R

Solving...


Error: More than one rook in a single row
```

##### Example 3:

```
$ python3 app.py

Submit your board as a list of lists with zeroes and ones, where one represents a rook and zero represents an empty space. Remember that your board should be contained in one line, since zsh might consider it a bad pattern.

[[1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 1, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0]] 


Initial board:
R · · · · · ·
· · · R · · ·
· · · · · · ·
· R · · · · ·
· · R · · · ·
· · · · · · R
· · · · · · ·
· · · · · · ·

Solving...


Error: Initial board dimensions not 8x8
```

### Files:

**app.py:** Runs the unit tests and then accepts a board as an input.
**solver.py:** Contains all the functions and helper functions to fill the board up.
**/tests:** Contains all the test files with unit tests. It tests for correct solutions when having random boards with different number of initial rooks. It tests for good compliance on the input according to the rules and board size.