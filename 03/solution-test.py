def search_map(area_map, right_amount, down_amount):
    row = 0
    column = right_amount
    num_of_trees = 0
    while row != len(area_map) - 1:
        row += down_amount
        if area_map[row][column] == "#":
            num_of_trees += 1

        column = (column + right_amount) % len(area_map[0])

    print(f"Number of Trees: {num_of_trees}")

    return num_of_trees


def load_map(filename):
    with open(filename) as f:
        board = f.read().splitlines()

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