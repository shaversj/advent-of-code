
def load_file(filename):
    data = ""
    with open(filename) as f:
        data = f.read().splitlines()

    return data


def first_problem(data):
    def find_min_or_max_bit(position, get_max=False):
        num_of_0 = len([idx for idx in range(0, len(data)) if data[idx][position] == '0'])
        num_of_1 = len([idx for idx in range(0, len(data)) if data[idx][position] == '1'])
        if get_max:
            return '0' if num_of_0 > num_of_1 else '1'
        else:
            return '0' if num_of_0 < num_of_1 else '1'

    max_bit = ""
    min_bit = ""

    for i in range(0, len(data[0])):
        max_bit += find_min_or_max_bit(i, get_max=True)
        min_bit += find_min_or_max_bit(i, get_max=False)

    max_bit_dec = int(max_bit, 2)
    min_bit_dec = int(min_bit, 2)

    return max_bit_dec * min_bit_dec


def second_problem(data):
    def find_min_or_max_bit(position, input_data, get_max=False):
        num_of_0 = len([idx for idx in range(0, len(input_data)) if input_data[idx][position] == '0'])
        num_of_1 = len([idx for idx in range(0, len(input_data)) if input_data[idx][position] == '1'])
        if get_max:
            return '1' if num_of_0 <= num_of_1 else '0'
        else:
            return '0' if num_of_0 <= num_of_1 else '1'

    def filter_data(position, num, input_data):
        return list(filter(lambda x: x[position] == num, input_data))

    new_data = data
    idx = 0
    while len(new_data) != 1:
        print(new_data)
        bit_to_filter = find_min_or_max_bit(idx, new_data, get_max=True)
        new_data = filter_data(idx, bit_to_filter, new_data)
        idx += 1
    oxygen_generator_rating = new_data[0]

    co2_data = data
    idx = 0
    while len(co2_data) != 1:
        print(co2_data)
        bit_to_filter = find_min_or_max_bit(idx, co2_data, get_max=False)
        co2_data = filter_data(idx, bit_to_filter, co2_data)
        idx += 1
    co2_rating = co2_data[0]

    print(oxygen_generator_rating, co2_rating)

    life_support_rating = int(oxygen_generator_rating, 2) * int(co2_rating, 2)

    print(life_support_rating)

data = load_file("input.txt")

# print(first_problem(data))
print(second_problem(data))