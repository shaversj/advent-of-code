def process_day(arr, days):
    num_of_days = 0

    while num_of_days != days:
        # count number of 0s in list
        num_of_new_fish = 0
        for idx in range(0, len(arr)):
            num = arr[idx]
            # if value is 0, reset to 6
            if num == 0:
                num_of_new_fish += 1
                arr[idx] = 6
                continue

            # decrease all numbers by 1
            arr[idx] -= 1

        # add fish with number 8
        arr.extend([8] * num_of_new_fish)
        num_of_days += 1

    return len(arr)


with open("input.txt") as f:
    data = f.readlines()
    split_integers = list(map(int, data[0].split(",")))

    print(process_day(split_integers, 80))
