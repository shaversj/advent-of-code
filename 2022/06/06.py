def solve_1(chars):
    chars = ""

    for idx in range(4, len(chars)):
        if len(chars[idx - 4:idx]) == len(set(chars[idx-4:idx])):
            print(idx, chars[idx - 4:idx])
            break


def solve_2(chars):
    chars = ""

    for idx in range(14, len(chars)):
        if len(chars[idx - 14:idx]) == len(set(chars[idx-14:idx])):
            print(idx, chars[idx - 14:idx])
            break

print(solve_2())


