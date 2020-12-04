def load_passport_data(filename):
    passport = []
    num_of_valid_passports = 0
    with open(filename) as f:
        passport_entry = ""
        for line in f:
            if line != "\n":
                passport_entry += line
                passport_entry += " "
                continue

            passport.append(passport_entry)
            passport_entry = ""
        passport.append(passport_entry)

    # print(passport)
    for entry in passport:
        passport_values = []
        split_line = entry.strip().split()
        for value in split_line:
            split_value = value.split(":")
            field = split_value[0]
            value = split_value[1]

            if field == "byr":
                if not value.isnumeric() or len(value) != 4:
                    continue
                if not 1920 <= int(value) <= 2002:
                    continue

            if field == "iyr":
                if not value.isnumeric() or len(value) != 4:
                    continue
                if not 2010 <= int(value) <= 2020:
                    continue

            if field == "eyr":
                if not value.isnumeric() or len(value) != 4:
                    continue
                if not 2020 <= int(value) <= 2030:
                    continue

            if field == "hgt":
                if value[-2:] == "cm":
                    if not 150 <= int(value[:-2]) <= 193:
                        continue
                elif value[-2:] == "in":
                    if not 59 <= int(value[:-2]) <= 76:
                        continue
                else:
                    continue

            if field == "hcl":
                if value[0] != "#" or len(value[1:]) != 6:
                    continue
                valid_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
                results = [char for char in value[1:] if char not in valid_values]
                if results:
                    continue

            if field == "ecl":
                valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if value not in valid_eye_colors:
                    continue

            if field == "pid":
                if len(value) != 9 or not value.isnumeric():
                    continue

            passport_values.append(field)

        #print(sorted(passport_values))
        if validate_passport(passport_values):
            #print(sorted(passport_values))
            num_of_valid_passports += 1

    print(num_of_valid_passports)


def validate_passport(passport):
    sorted_passport_with_8_entries = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    sorted_password_without_cid = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
    sorted_passport = sorted(passport)
    if sorted_passport == sorted_passport_with_8_entries:
        return True
    elif sorted_passport == sorted_password_without_cid:
        return True

    return False


load_passport_data("input.txt")