def search_map(area_map, right_amount, down_amount):
    row = 0
    column = right_amount
    num_of_trees = 0
    max_rows = len(area_map)
    while row != max_rows - 1:
        row += down_amount
        if area_map[row][column] == "#":
            num_of_trees += 1

        column += right_amount

    print(f"Number of Trees: {num_of_trees}")

    return num_of_trees


def load_map(filename):
    board = []
    with open(filename) as f:
        data = f.readlines()

    for line in data:
        l = line.strip()
        long_line = l * 300
        board.append(long_line + "\n")

    return board


large_map = load_map("input.txt")
search_map(large_map, 1, 1)
search_map(large_map, 3, 1)
search_map(large_map, 5, 1)
search_map(large_map, 7, 1)
search_map(large_map, 1, 2)

# Number of Trees: 87
# Number of Trees: 205
# Number of Trees: 85
# Number of Trees: 79
# Number of Trees: 33