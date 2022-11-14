def get_data(filename):
    with open(filename) as f:
        return list(map(int, f.read().split(",")))


def get_min_fuel_amount(positions):
    min_amount = float('inf')
    min_position = ""

    # 16,1,2,0,4,2,7,1,2,14
    for position_a in positions:
        fuel_cost = 0

        for position_b in positions:
            fuel_cost += abs(position_b - position_a)

        if fuel_cost < min_amount:
            min_amount = fuel_cost
            min_position = position_a

    return min_amount, min_position


def get_min_fuel_amount_2(positions):
    min_amount = float('inf')
    min_position = ""

    # 16,1,2,0,4,2,7,1,2,14
    for position_a in range(max(positions)):
        fuel_cost = 0

        for position_b in positions:
            diff = abs(position_b - position_a)
            fuel_cost += sum(range(diff + 1))

        if fuel_cost < min_amount:
            min_amount = fuel_cost
            min_position = position_a

    return min_amount, min_position


data = get_data("input.txt")

print(get_min_fuel_amount(data))
print(get_min_fuel_amount_2(data))