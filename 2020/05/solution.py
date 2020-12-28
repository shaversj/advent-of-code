import math


def load_boarding_passes(filename):
    with open(filename) as f:
        max_seat_id = 0
        seat_ids = set()
        for boarding_pass in f:
            row_start, row_end = 0, 127
            col_start, col_end = 0, 7
            final_row, final_col = 0, 0
            for idx, letter in enumerate(boarding_pass):
                if letter == "F" and idx == 0:
                    row_end = math.floor(row_end / 2)
                elif letter == "B" and idx == 0:
                    row_start = math.ceil(row_end / 2)
                elif letter == "F":
                    row_end = math.floor((row_start + row_end) / 2)
                    if idx == 6:
                        final_row = row_start
                elif letter == "B":
                    row_start = math.ceil((row_start + row_end) / 2)
                    if idx == 6:
                        final_row = row_end

                elif letter == "L" and idx == 7:
                    col_end = math.floor(col_end / 2)
                elif letter == "R" and idx == 7:
                    col_start = math.ceil(col_end / 2)
                elif letter == "L":
                    col_end = math.floor((col_start + col_end) / 2)
                    if idx == 9:
                        final_col = col_start
                elif letter == "R":
                    col_start = math.ceil((col_start + col_end) / 2)
                    if idx == 9:
                        final_col = col_end

                # print(row_start, row_end)
                # print(col_start, col_end)
            # print(final_row, final_col)
            seat_id = (final_row * 8) + final_col
            seat_ids.add(seat_id)
            max_seat_id = max(max_seat_id, seat_id)
            print(f"Row: {final_row}, Column: {final_col}")
            print(f"Seat ID: {seat_id}")
            print("----------")

        print(f"Max Seat ID: {max_seat_id}")

        # Part 2
        print(sorted(seat_ids))
        prev_num = 54
        for num in sorted(seat_ids):
            if num == prev_num + 1:
                prev_num = num
                continue
            else:
                print(f"Missing Seat ID: {num - 1}")
                prev_num = num


load_boarding_passes("input.txt")
