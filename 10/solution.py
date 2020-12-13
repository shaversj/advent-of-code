def load_adaptors(filename):
    adaptors = []
    with open(filename) as f:
        for line in f:
            adaptors.append(int(line))

    return adaptors


def test_adaptors(adaptors):
    difference_of_1 = 0
    difference_of_3 = 0
    sorted_adaptors = sorted(adaptors)

    # insert 0 to front
    sorted_adaptors.insert(0, 0)

    # take the last number and increase by 3 and insert
    last_num = sorted_adaptors[-1]
    sorted_adaptors.append(last_num + 3)
    print(adaptors)
    print(sorted_adaptors)

    prev_num = 0
    for idx in range(0, len(sorted_adaptors)):
        curr_num = sorted_adaptors[idx]
        if curr_num - prev_num == 1:
            difference_of_1 += 1
        if curr_num - prev_num == 3:
            difference_of_3 += 1

        prev_num = curr_num

    print(f"Difference of 1: {difference_of_1}")
    print(f"Difference of 3: {difference_of_3}")

    print(f"1 Jolt Difference * 3 Jolt Difference: {difference_of_1 * difference_of_3}")


def validate_adaptors_part_2(adaptors, max_num=None):

    if len(adaptors) == 0:
        return False

    total_valid_ways = 0
    sorted_adaptors = sorted(adaptors)

    # insert 0 to front
    sorted_adaptors.insert(0, 0)

    # add max num to end of list
    sorted_adaptors.append(max_num)

    prev_num = 0
    for idx in range(0, len(sorted_adaptors)):
        curr_num = sorted_adaptors[idx]
        difference = curr_num - prev_num
        if idx == 0 and difference == 0:
            prev_num = curr_num
            continue
        if difference not in [1, 2, 3]:
            return False
        prev_num = curr_num

    print(sorted_adaptors)
    return True


def build_combinations_of_adaptors(adaptors):
    from itertools import combinations

    num_of_valid_combinations = 0

    sorted_adaptors = sorted(adaptors)
    max_num = sorted_adaptors[-1] + 3
    output = sum([list(map(list, combinations(adaptors, i))) for i in range(len(adaptors) + 1)], [])
    for combo in output:
        if validate_adaptors_part_2(combo, max_num):
            print(combo, "Yes")
            num_of_valid_combinations += 1

    print(num_of_valid_combinations)


def build_combination_of_adaptors_trial_2(adaptors):
    from itertools import permutations
    num_of_valid_combinations = 0

    sorted_adaptors = sorted(adaptors)
    max_num = sorted_adaptors[-1] + 3
    print(F"Max Num: {max_num}")
    print(len(adaptors))

    for i in range(100, len(adaptors) + 1):
        perm = permutations(adaptors, i)
        for combo in perm:
            if validate_adaptors_part_2(combo, max_num):
                # print(combo, "Yes")
                num_of_valid_combinations += 1

    print(num_of_valid_combinations)


# adaptors_from_file = load_adaptors("input.txt")



# test_adaptors(adaptors_from_file)
# build_combination_of_adaptors_trial_2(adaptors_from_file)

# print(validate_adaptors_part_2([1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19], 22))
arr = [int(line.rstrip()) for line in \
       open('input.txt', 'r').readlines()]
arr.sort()
arr.append(arr[-1]+3)

memo = {0: 1}
for r in arr:
    memo[r] = memo.get(r-3,0) \
              + memo.get(r-2,0) \
              + memo.get(r-1,0)
print(memo[arr[-1]])