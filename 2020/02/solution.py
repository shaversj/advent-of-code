def load_puzzle_input(filename):
    with open(filename) as f:
        counter = 0
        total = 0
        for line in f:
            total += 1
            split_line = line.strip().split(":")
            password = split_line[1].strip()

            split_policy = split_line[0].split()
            counter_range = split_policy[0].split("-")
            low, high = int(counter_range[0]), int(counter_range[1])
            letter = split_policy[1]

            if validate_password_part2(password, letter, low, high):
                print(password, letter, low, high)
                counter += 1

        print(f"Valid Passwords: {counter}\n"
              f"Total Passwords in File: {total}")


def validate_password(password, letter, low, high):
    from collections import Counter
    c = Counter(password)
    if c.get(letter):
        count = c.get(letter)
        if low <= count <= high:
            return True
    else:
        return False

    return False


def validate_password_part2(password, letter, low, high):
    from collections import Counter
    c = Counter(password)
    if c.get(letter):
        if password[low - 1] == letter:
            if password[high - 1] == letter:
                return False
            return True
        elif password[high - 1] == letter:
            return True
        else:
            return False
    else:
        return False


load_puzzle_input("input.txt")