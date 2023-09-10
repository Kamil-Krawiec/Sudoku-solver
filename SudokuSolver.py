class SudokuSolver:

    def __init__(self, board_str):
        self.board = [int(x) if x != '.' else 0 for x in board_str]
        self.size = int(len(self.board) ** 0.5)

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

    def output(self):
        return ''.join(str(num) for num in self.board)

    def valid(self, num, pos):
        # check row
        row = pos // self.size
        row_start = pos // self.size * self.size
        is_row_occupied = num in self.board[row_start:row_start + self.size]

        # check col
        col = pos % self.size
        is_column_occupied = num in [self.board[col + x * self.size] for x in range(self.size)]

        # check box
        is_box_occupied = self.__in_box(row, col, num)

        return not (is_row_occupied or is_column_occupied or is_box_occupied)

    def __find_empty(self):
        return self.board.index(0)

    def solve_base(self):
        if 0 not in self.board:
            return True
        else:
            pos = self.__find_empty()

        for num in range(1, 10):
            if self.valid(num, pos):
                self.board[pos] = num

                if self.solve_base():
                    return True
                self.board[pos] = 0
        return False

    def __in_box(self, row, col, num):
        box_start_row = (row // 3) * 3
        box_start_col = (col // 3) * 3

        for i in range(box_start_row, box_start_row + 3):
            for j in range(box_start_col, box_start_col + 3):
                if self.board[i * 9 + j] == num:
                    return True
        return False

    # --------------------------- ADVANCED SECTION ---------------------------
    def __update_with_constraint_propagation(self):
        for pos in range(len(self.board)):
            if self.board[pos] == 0:
                possibilities = self.__get_possible_values(pos)
                if len(possibilities) == 1:
                    num = possibilities.pop()
                    self.board[pos] = num

    def __find_empty_MRV_advanced(self):
        min_possibilities = float('inf')
        min_pos = -1
        for pos in range(len(self.board)):
            if self.board[pos] == 0:
                possibilities = self.__get_possible_values(pos)
                if len(possibilities) < min_possibilities:
                    min_possibilities = len(possibilities)
                    min_pos = pos
        return min_pos

    def __get_possible_values(self, pos):

        # Calculate the possible values
        row = pos // self.size
        col = pos % self.size
        box_start_row = (row // 3) * 3
        box_start_col = (col // 3) * 3

        possible_values = set(range(1, 10))

        for i in range(self.size):
            if self.board[row * self.size + i] in possible_values:
                possible_values.remove(self.board[row * self.size + i])

            if self.board[i * self.size + col] in possible_values:
                possible_values.remove(self.board[i * self.size + col])

            box_row = box_start_row + i // 3
            box_col = box_start_col + i % 3
            if self.board[box_row * self.size + box_col] in possible_values:
                possible_values.remove(self.board[box_row * self.size + box_col])

        return possible_values

    def __solve_advanced_helper(self):
        self.__update_with_constraint_propagation()  # Apply constraints
        if 0 not in self.board:
            return True
        else:
            pos = self.__find_empty_MRV_advanced()

        possibilities = self.__get_possible_values(pos)
        if not possibilities:
            return False

        original_board = self.board[:]  # Create a copy of the current board state

        for num in possibilities:
            self.board[pos] = num

            if self.__solve_advanced_helper():
                return True

            self.board = original_board[:]  # Restore the original board state when backtracking

        return False

    def solve_advanced(self):
        self.__solve_advanced_helper()


# x = int(input())
#
#
# for _ in range(x):
#     sudoku = input()
#     sudoku_solver = SudokuSolver(sudoku)
#     print('Y')
#     sudoku_solver.solve_advanced()
#     print(sudoku_solver.output())
