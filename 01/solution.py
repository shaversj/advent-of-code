
def load_file(input_file):
    with open(input_file) as f:
        nums = f.readlines()

    return nums


def find_entries_that_sum_to_2020_part1(nums):
    result = set()
    for idx in range(len(nums)):
        num_1 = int(nums[idx].strip())
        for idx_2 in range(1, len(nums)):
            num_2 = int(nums[idx_2].strip())
            if num_1 + num_2 == 2020:
                print(f"{num_1}, {num_2}: {num_1 * num_2}")


def find_entries_that_sum_to_2020_part2(nums):
    result = set()
    for idx in range(len(nums)):
        num_1 = int(nums[idx].strip())
        for idx_2 in range(1, len(nums)):
            num_2 = int(nums[idx_2].strip())
            for idx_3 in range(2, len(nums)):
                num_3 = int(nums[idx_3].strip())
                if num_1 + num_2 + num_3 == 2020:
                    print(f"{num_1}, {num_2}, {num_3}: {num_1 * num_2 * num_3}")


data = load_file("input.txt")
# find_entries_that_sum_to_2020_part1(data)
find_entries_that_sum_to_2020_part2(data)
