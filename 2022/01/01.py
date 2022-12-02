def get_data(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    return data


def find_max_calories(calories):
    total = 0
    elfs = []
    for calorie in calories:
        if not calorie:
            elfs.append(total)
            total = 0
        else:
            total += int(calorie)

    return max(elfs)


def find_top_3(calories):
    total = 0
    elfs = []
    for calorie in calories:
        if not calorie:
            elfs.append(total)
            total = 0
        else:
            total += int(calorie)
    if total:
        elfs.append(total)

    return sum(sorted(elfs, reverse=True)[:3])


if __name__ == '__main__':
    data = get_data("input.txt")
    print(find_max_calories(data))
    print(find_top_3(data))
