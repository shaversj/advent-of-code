def get_data(filename):
    coordinates = []
    with open(filename) as f:
        for line in f:
            split_line = line.strip().split(" -> ")
            x1, y1 = split_line[0].split(",")[0], split_line[0].split(",")[1]
            x2, y2 = split_line[1].split(",")[0], split_line[1].split(",")[1]
            coordinates.append((int(x1), int(y1), int(x2), int(y2)))

    return coordinates


def build_grid(x, y):
    grids = []

    for i in range(0, x + 2):
        grid = []
        for j in range(0, y + 2):
            grid.append(0)

        grids.append(grid)

    return grids


def populate_grid(coords, grid):
    x1, y1, x2, y2 = coords

    if y1 == y2 and x1 < x2:
        row = grid[y2]
        for x in range(x1, x2 + 1):
            if row[x] == 0:
                row[x] = 1
            else:
                row[x] += 1

    if y1 == y2 and x1 > x2:
        row = grid[y2]
        for x in range(x2, x1 + 1):
            if row[x] == 0:
                row[x] = 1
            else:
                row[x] += 1

    if x1 == x2 and y1 < y2:
        # update column
        for y in range(y1, y2 + 1):
            if grid[y][x1] == 0:
                grid[y][x1] = 1
            else:
                grid[y][x1] += 1

    if x1 == x2 and y1 > y2:
        # update column
        for y in range(y2, y1 + 1):
            if grid[y][x1] == 0:
                grid[y][x1] = 1
            else:
                grid[y][x1] += 1

    return grid


def problem_1_main(filename):
    coords = get_data(filename)
    max_horizontal_x = max(sorted(coords, key=lambda x: x[0], reverse=True)[0][0], sorted(coords, key=lambda x: x[2], reverse=True)[0][2])
    max_vertical_y = max(sorted(coords, key=lambda x: x[1], reverse=True)[0][1], sorted(coords, key=lambda x: x[3], reverse=True)[0][3])

    board = build_grid(max_horizontal_x, max_vertical_y)

    for coord in coords:
        board = populate_grid(coord, board)

    count_with_2_or_more = 0
    for row in board:
        count_with_2_or_more += len(list(filter(lambda x: x > 1, row)))

    print(count_with_2_or_more)


if __name__ == '__main__':
    problem_1_main("input.txt")