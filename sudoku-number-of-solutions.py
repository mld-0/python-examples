import time
import pprint

def is_valid(puzzle, row, col, num):
    for x in range(9):
        if puzzle[row][x] == num or puzzle[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for x in range(3):
        for y in range(3):
            if puzzle[x + start_row][y + start_col] == num:
                return False
    return True


def is_initially_valid(puzzle):
    for row in range(9):
        for col in range(9):
            num = puzzle[row][col]
            if num != ".":
                # Temporarily set the cell to empty
                puzzle[row][col] = "."
                if not is_valid(puzzle, row, col, num):
                    return False
                # Restore the cell value
                puzzle[row][col] = num
    return True


def solve(puzzle, count_solutions=False):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == ".":
                for num in map(str, range(1, 10)):
                    if is_valid(puzzle, row, col, num):
                        puzzle[row][col] = num
                        if solve(puzzle, count_solutions):
                            if count_solutions:
                                puzzle[row][col] = "."
                            else:
                                return True
                        else:
                            puzzle[row][col] = "."
                return False
    if count_solutions:
        solutions.append(None)
        return False
    return True


puzzles = [
    [
        [".", "6", ".", "8", ".", ".", "5", ".", "."],
        [".", ".", "5", ".", ".", ".", "3", "6", "7"],
        ["3", "7", ".", ".", "6", "5", "8", ".", "9"],
        ["6", ".", "9", ".", ".", "2", "1", ".", "."],
        [".", ".", "1", "4", "8", "9", "2", ".", "."],
        [".", ".", ".", "3", ".", "6", "9", ".", "."],
        [".", "5", ".", ".", ".", ".", "4", ".", "."],
        [".", "1", ".", "5", "4", "7", ".", ".", "3"],
        [".", "9", "6", ".", "3", "8", ".", "5", "1"],
    ],
    [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "5", ".", ".", ".", "3", "6", "7"],
        ["3", "7", ".", ".", "6", "5", "8", ".", "9"],
        ["6", ".", "9", ".", ".", "2", "1", ".", "."],
        [".", ".", "1", "4", "8", "9", "2", ".", "."],
        [".", ".", ".", "3", ".", "6", "9", ".", "."],
        [".", "5", ".", ".", ".", ".", "4", ".", "."],
        [".", "1", ".", "5", "4", "7", ".", ".", "3"],
        [".", "9", "6", ".", "3", "8", ".", "5", "1"],
    ],
    [
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["3", "7", ".", ".", "6", "5", "8", ".", "9"],
        ["6", ".", "9", ".", ".", "2", "1", ".", "."],
        [".", ".", "1", "4", "8", "9", "2", ".", "."],
        [".", ".", ".", "3", ".", "6", "9", ".", "."],
        [".", "5", ".", ".", ".", ".", "4", ".", "."],
        [".", "1", ".", "5", "4", "7", ".", ".", "3"],
        [".", "9", "6", ".", "3", "8", ".", "5", "1"],
    ],
    [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."],
    ],
]

for puzzle in puzzles:
    solutions = []
    start_time = time.time()
    pprint.pprint(puzzle)
    if is_initially_valid(puzzle):
        solve(puzzle, count_solutions=True)
        print(f"The puzzle has {len(solutions)} solutions.")
    else:
        print("The puzzle is invalid from the start.")
    print("elapsed_ms=(%0.2f)" % ((time.time() - start_time) * 1_000))

