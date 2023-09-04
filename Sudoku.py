import time

class SudokuSolver:

    def __init__(self, board_str):
        self.board = [int(x) if x != '.' else 0 for x in board_str]
        self.size = int(len(self.board) ** 0.5)

    def valid(self, num, pos):
        # check row
        row = pos // self.size
        row_start = pos // self.size * self.size
        is_row_occupied = num in self.board[row_start:row_start + self.size]

        # check col
        col = pos % self.size
        is_column_occupied = num in [self.board[col + x * self.size] for x in range(self.size)]

        # check box
        is_box_occupied = self.in_box(row, col, num)

        return not (is_row_occupied or is_column_occupied or is_box_occupied)

    def in_box(self, row, col, num):
        box_start_row = (row // 3) * 3
        box_start_col = (col // 3) * 3

        for i in range(box_start_row, box_start_row + 3):
            for j in range(box_start_col, box_start_col + 3):
                if self.board[i * 9 + j] == num:
                    return True
        return False

    def __str__(self):
        subgrid_size = int(self.size ** 0.5)

        for i in range(self.size):
            if i % subgrid_size == 0 and i != 0:
                print(" - " * (self.size - 1))
            for j in range(self.size):
                if j % subgrid_size == 0 and j != 0:
                    print("|", end=" ")
                print(self.board[i * self.size + j], end=" ")
            print()

    def print_output(self):
        print('Y')
        print(''.join(str(num) for num in self.board))

    def find_empty(self):
        return self.board.index(0)

    def get_possible_values(self,pos):
        possible_values = []
        for num in range(1, 10):
            if self.valid(num, pos):
                possible_values.append(num)

        return possible_values

    def solve(self):
        if 0 not in self.board:
            return True
        else:
            pos = self.find_empty()

        possibilities = self.get_possible_values(pos)
        if not possibilities:
            return False

        for num in possibilities:
            self.board[pos] = num

            if self.solve():
                return True
            self.board[pos] = 0
        return False


# x = int(input())
#
#
# for _ in range(x):
#     sudoku = input()
#     sudoku_solver = SudokuSolver(sudoku)
#     sudoku_solver.solve()
#     sudoku_solver.print_output()

sudoku_solver = SudokuSolver("7..25..98..6....1....61.3..9....1.......8.4.9..75.28.1.94..3.......4923.61.....4.")
start_time = time.time()
sudoku_solver.solve()
end_time = time.time()
sudoku_solver.print_output()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")