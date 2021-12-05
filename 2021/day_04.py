def is_winning_line(line):
    return all(num is True for num in line)


def is_winning_board(board):
    has_winning_row = any(is_winning_line(row) for row in board)
    has_winning_column = any(is_winning_line(column) for column in zip(*board))
    return has_winning_row or has_winning_column


def mark_number(board, number):
    for row_idx, row in enumerate(board):
        for col_idx, num in enumerate(row):
            if num == number:
                board[row_idx][col_idx] = True


def first_winning_num(boards, inputs):
    for num in inputs:
        for board_idx, board in enumerate(boards):
            mark_number(board, num)
            if is_winning_board(board):
                return num, board_idx


with open("inputs/day_04.txt", "r") as text_file:
    data = text_file.readlines()
    inputs = data[0].strip().split(",")

board, boards = [], []
counter = 2
while counter <= len(data):
    if counter == len(data) or data[counter] == "\n":
        boards.append(board)
        board = []
        counter += 1
        continue
    line = [num for num in data[counter].split()]
    board.append(line)
    counter += 1

num, board_idx = first_winning_num(boards, inputs)
unmarked_num_sum = sum(sum(int(num) for num in row if num is not True) for row in boards[board_idx])
print(num, unmarked_num_sum, int(num) * int(unmarked_num_sum))
