def get_boards_and_nums(filename):
    # build list of tuples containing number and boolean (4, False)
    with open(filename) as f:
        data = f.read().splitlines()
        bingo_nums = ""
        boards = []
        board = []
        for idx in range(0, len(data)):
            if idx == 0:
                bingo_nums = data[idx].split(",")
                continue
            if data[idx] == "":
                if board:
                    boards.append(board)
                board = []
                continue
            if data[idx]:
                row = []
                for num in data[idx].strip().split(" "):
                    if num:
                        row.append((int(num), False))
                board.append(row)
                if idx == len(data) - 1:
                    boards.append(board)
    return boards, bingo_nums


def update_board(boards, bingo_num):
    for board_idx in range(0, len(boards)):
        for row_pos in range(0, len(boards[board_idx])):
            for col_pos in range(0, len(boards[board_idx][0])):
                num = boards[board_idx][row_pos][col_pos][0]
                if bingo_num == num:
                    boards[board_idx][row_pos][col_pos] = (num, True)
                else:
                    continue

    return boards



def search_row_and_column_for_winner(boards):
    # search for winner in row
    for board_idx in range(0, len(boards)):
        for row_pos in range(0, len(boards[board_idx])):
            count = 0
            for col_pos in range(0, len(boards[board_idx][0])):
                if boards[board_idx][row_pos][col_pos][1]:
                    count += 1
                if count == 5:
                    return True, board_idx

    # search for winner in columns
    for board_idx in range(0, len(boards)):
        for col_pos in range(0, len(boards[board_idx][0])):
            count = 0
            for row_pos in range(0, len(boards[board_idx])):
                if boards[board_idx][row_pos][col_pos][1]:
                    count += 1
                if count == 5:
                    return True, board_idx

    return False, 0


def find_sum_of_unmarked_numbers(board):
    total = 0
    for row_idx in range(0, len(board)):
        for col_idx in range(0, len(board[0])):
            if not board[row_idx][col_idx][1]:
                total += board[row_idx][col_idx][0]

    return total


def main(filename):
    from pprint import pprint as pp

    bingo_boards, bingo_numbers = get_boards_and_nums(filename)
    bingo_numbers = list(map(int, bingo_numbers))

    for num in bingo_numbers:
        bingo_boards = update_board(bingo_boards, num)
        results = search_row_and_column_for_winner(bingo_boards)
        if results[0]:
            total_sum = find_sum_of_unmarked_numbers(bingo_boards[results[1]])
            final_score = total_sum * num
            print(results)
            print(final_score)
            break


if __name__ == '__main__':
    main("input.txt")
