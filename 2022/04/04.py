def get_data(filename):
    nums = []
    with open(filename) as f:
        for line in f:
            split_line_1 = line.strip().split(",")[0].split("-")
            split_line_2 = line.strip().split(",")[1].split("-")

            nums.append([split_line_1, split_line_2])

    return nums


def solve_1(data):
    num_of_fully_containing_pairs = 0
    for pair in data:
        elf_1_num_1 = int(pair[0][0])
        elf_1_num_2 = int(pair[0][1])
        elf_2_num_1 = int(pair[1][0])
        elf_2_num_2 = int(pair[1][1])
        if set(range(elf_1_num_1, elf_1_num_2 + 1)).issubset(set(range(elf_2_num_1, elf_2_num_2 + 1)))\
                or set(range(elf_2_num_1, elf_2_num_2 + 1)).issubset(set(range(elf_1_num_1, elf_1_num_2 + 1))):
            print(pair)
            num_of_fully_containing_pairs += 1

    print(num_of_fully_containing_pairs)


def solve_2(data):
    num_of_fully_containing_pairs = 0
    for pair in data:
        elf_1_num_1 = int(pair[0][0])
        elf_1_num_2 = int(pair[0][1])
        elf_2_num_1 = int(pair[1][0])
        elf_2_num_2 = int(pair[1][1])
        set_1 = list(range(elf_1_num_1, elf_1_num_2 + 1))
        set_2 = list(range(elf_2_num_1, elf_2_num_2 + 1))

        if any(x in set_2 for x in set_1):
            num_of_fully_containing_pairs += 1

    print(num_of_fully_containing_pairs)


pairs = get_data("input.txt")
# solve_1(pairs)
solve_2(pairs)