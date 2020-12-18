def load_seats(filename):
    seats = []
    with open(filename) as f:
        for line in f:
            row = []
            line = line.strip()
            for seat in line:
                row.append(seat)
            seats.append(row)

    return seats


def validate_seat(seats):
    new_seats = []

    for row in range(0, len(seats)):
        new_row = []

        for column in range(0, len(seats[0])):
            seat = seats[row][column]
            num_of_occupied_seats = 0

            # check seat to right
            if column + 1 != len(seats[0]):
                seat_to_right = seats[row][column + 1]
                if seat_to_right == "#":
                    num_of_occupied_seats += 1

            # check seat to left
            if column - 1 != -1:
                seat_to_left = seats[row][column - 1]
                if seat_to_left == "#":
                    num_of_occupied_seats += 1

            # check up
            if row - 1 != -1:
                seat_up = seats[row - 1][column]
                if seat_up == "#":
                    num_of_occupied_seats += 1

            # check down
            if row + 1 != len(seats):
                seat_down = seats[row + 1][column]
                if seat_down == "#":
                    num_of_occupied_seats += 1

            # check diagonal right
            if row + 1 != len(seats) and column + 1 != len(seats[0]):
                seat_right_diag = seats[row + 1][column + 1]
                if seat_right_diag == "#":
                    num_of_occupied_seats += 1

            # check diagonal left
            if row + 1 != len(seats) and column - 1 != -1:
                seat_left_diag = seats[row + 1][column - 1]
                if seat_left_diag == "#":
                    num_of_occupied_seats += 1

            # check diagonal up right
            if row - 1 != -1 and column + 1 != len(seats[0]):
                seat_up_right_diag = seats[row - 1][column + 1]
                if seat_up_right_diag == "#":
                    num_of_occupied_seats += 1

            # check diagonal up left
            if row - 1 != -1 and column - 1 != -1:
                seat_up_right_diag = seats[row - 1][column - 1]
                if seat_up_right_diag == "#":
                    num_of_occupied_seats += 1

            if seat == ".":
                new_row.append(".")

            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if seat == "L":
                if num_of_occupied_seats == 0:
                    # seats[row][column] = "#"
                    new_row.append("#")
                else:
                    new_row.append("L")
            if seat == "#":
                if num_of_occupied_seats >= 4:
                    # seats[row][column] = "L"
                    new_row.append("L")
                else:
                    new_row.append("#")

        new_seats.append(new_row)

    return new_seats


def validate_seat_part_2(seats):
    new_seats = []

    for row in range(0, len(seats)):
        new_row = []

        for column in range(0, len(seats[0])):
            seat = seats[row][column]
            num_of_occupied_seats = 0

            # check seat to right
            if column + 1 != len(seats[0]):
                column_idx = column + 1
                seat_to_right = seats[row][column_idx]
                while seat_to_right == ".":
                    if column_idx + 1 >= len(seats[0]):
                        break
                    else:
                        column_idx += 1
                        seat_to_right = seats[row][column_idx]

                if seat_to_right == "#":
                    num_of_occupied_seats += 1

            # check seat to left
            if column - 1 != -1:
                column_idx = column - 1
                seat_to_left = seats[row][column_idx]
                while seat_to_left == ".":
                    if column_idx - 1 <= -1:
                        break
                    else:
                        column_idx -= 1
                        seat_to_left = seats[row][column_idx]

                if seat_to_left == "#":
                    num_of_occupied_seats += 1

            # check up
            if row - 1 != -1:
                row_idx = row - 1
                seat_up = seats[row_idx][column]
                while seat_up == ".":
                    if row_idx - 1 <= -1:
                        break
                    else:
                        row_idx -= 1
                        seat_up = seats[row_idx][column]

                if seat_up == "#":
                    num_of_occupied_seats += 1

            # check down
            if row + 1 != len(seats):
                row_idx = row + 1
                seat_down = seats[row_idx][column]
                while seat_down == ".":
                    if row_idx + 1 >= len(seats):
                        break
                    else:
                        row_idx += 1
                        seat_down = seats[row_idx][column]

                if seat_down == "#":
                    num_of_occupied_seats += 1

            # check diagonal right
            if row + 1 != len(seats) and column + 1 != len(seats[0]):
                row_idx = row + 1
                col_idx = column + 1

                seat_right_diag = seats[row_idx][col_idx]
                while seat_right_diag == ".":
                    if row_idx + 1 >= len(seats) or col_idx + 1 >= len(seats[0]):
                        break
                    else:
                        row_idx += 1
                        col_idx += 1
                        seat_right_diag = seats[row_idx][col_idx]

                if seat_right_diag == "#":
                    num_of_occupied_seats += 1

            # check diagonal left
            if row + 1 != len(seats) and column - 1 != -1:
                row_idx = row + 1
                col_idx = column - 1
                seat_left_diag = seats[row_idx][col_idx]

                while seat_left_diag == ".":
                    if row_idx + 1 >= len(seats) or col_idx - 1 <= -1:
                        break
                    else:
                        row_idx += 1
                        col_idx -= 1
                        seat_left_diag = seats[row_idx][col_idx]

                if seat_left_diag == "#":
                    num_of_occupied_seats += 1

            # check diagonal up right
            if row - 1 != -1 and column + 1 != len(seats[0]):
                row_idx = row - 1
                col_idx = column + 1
                seat_up_right_diag = seats[row_idx][col_idx]

                while seat_up_right_diag == ".":
                    if row_idx - 1 <= -1 or col_idx + 1 >= len(seats[0]):
                        break
                    else:
                        row_idx -= 1
                        col_idx += 1
                        seat_up_right_diag = seats[row_idx][col_idx]

                if seat_up_right_diag == "#":
                    num_of_occupied_seats += 1

            # check diagonal up left
            if row - 1 != -1 and column - 1 != -1:
                row_idx = row - 1
                col_idx = column - 1
                seat_up_left_diag = seats[row_idx][col_idx]

                while seat_up_left_diag == ".":
                    if row_idx - 1 <= -1 or col_idx - 1 <= -1:
                        break
                    else:
                        row_idx -= 1
                        col_idx -= 1
                        seat_up_left_diag = seats[row_idx][col_idx]

                if seat_up_left_diag == "#":
                    num_of_occupied_seats += 1

            if seat == ".":
                new_row.append(".")

            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if seat == "L":
                if num_of_occupied_seats == 0:
                    # seats[row][column] = "#"
                    new_row.append("#")
                else:
                    new_row.append("L")
            if seat == "#":
                if num_of_occupied_seats >= 5:
                    # seats[row][column] = "L"
                    new_row.append("L")
                else:
                    new_row.append("#")

        new_seats.append(new_row)

    return new_seats

def find_num_of_seats_occupied(seats):
    num_of_occupied_seats = 0
    curr_seats = seats
    while True:
        new_seats = validate_seat_part_2(curr_seats)
        if new_seats == curr_seats:
            break
        else:
            curr_seats = new_seats

    # find num of occupied seats
    for row in curr_seats:
        for seat in row:
            if seat == "#":
                num_of_occupied_seats += 1

    return num_of_occupied_seats


seats_from_file = load_seats("input.txt")
print(find_num_of_seats_occupied(seats_from_file))
# seats = validate_seat(seats_from_file)

# print(find_num_of_seats_occupied(seats))
# ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L']
# ['L', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L']
# ['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.']
# ['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L']
# ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L']
# ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L']
# ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.']
# ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']
# ['L', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L']
# ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L']