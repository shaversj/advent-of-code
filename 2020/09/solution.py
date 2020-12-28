def load_numbers(filename):
    nums = []
    with open(filename) as f:
        for line in f:
            nums.append(int(line))

    return nums


def process_numbers(numbers, look_at_previous_num):

    for idx in range(look_at_previous_num, len(numbers)):
        next_valid_number = numbers[idx]
        is_valid_number = False

        for x in range(idx - look_at_previous_num, idx):
            for y in range((idx - look_at_previous_num) + 1, idx):
                if numbers[x] + numbers[y] == next_valid_number:
                    is_valid_number = True
                else:
                    if x == idx - 1 and is_valid_number is False:
                        print(f"Number is not sum of previous {look_at_previous_num}: {next_valid_number}")
                        break


def find_consecutive_numbers(numbers, target_num):
    for idx in range(0, len(numbers)):
        sum_of_range = 0
        nums = []
        i = idx
        while sum_of_range < target_num:
            sum_of_range += numbers[i]
            nums.append(numbers[i])
            if sum_of_range == target_num and len(nums) >= 2:
                nums.sort()
                encryption_weakness = nums[0] + nums[-1]
                return encryption_weakness

            i += 1
            # print(nums)


# numbers = load_numbers("input.txt")
# process_numbers(numbers, 25)
# 2089807806

numbers = load_numbers("input.txt")
print(find_consecutive_numbers(numbers, 2089807806))
