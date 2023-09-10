import pandas as pd
from SudokuSolver import SudokuSolver
import time
import os

test_cases = [
    "..41..3.8.1....62...82..4.....3.28.9....7....7.16.8...562..17.3.3.....4.1....5...",
    "1.......4....1.38.27.9.4...91.7...........5..86.4.5.9..3......8..9....2.4.......7",
    "7..25..98..6....1....61.3..9....1.......8.4.9..75.28.1.94..3.......4923.61.....4.",
    "4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......",
    # "..............3.85..1.2.......5.7.....4...1...9.......5......73..2.1........4...9",
    # "9..8...........5............2..1...3.1.....6....4...7.7.86.........3.1..4.....2..",
]

results = []

for index, test_case in enumerate(test_cases):
    print(index)
    sudoku_solver = SudokuSolver(test_case)

    start_time = time.time()
    sudoku_solver.solve_advanced()
    end_time = time.time()
    advanced_output = sudoku_solver.output()
    advanced_time = end_time - start_time * 1000

    sudoku_solver_base = SudokuSolver(test_case)
    start_time = time.time()
    sudoku_solver_base.solve_base()
    end_time = time.time()
    base_output = sudoku_solver_base.output()
    base_time = end_time - start_time * 1000

    result_adv = {
        "Test Case": index,
        "IS Advanced Version": True,
        "Match": advanced_output == base_output,
        "Time (s)": advanced_time,
        "sudoku": test_case
    }
    result_bsc = {
        "Test Case": index,
        "IS Advanced Version": False,
        "Match": advanced_output == base_output,
        "Time (s)": base_time,
        "sudoku": test_case
    }

    results.extend([result_bsc,result_adv])


df = pd.DataFrame(results)
# Save the DataFrame as a CSV file
df.to_csv("sudoku_solver_results.csv", header=not os.path.exists("./sudoku_solver_results.csv"),mode='a')

print(df)
