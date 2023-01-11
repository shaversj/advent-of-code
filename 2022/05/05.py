table = {
    1: ["T", "D", "W", "Z", "V", "P"],
    2: ["L", "S", 'W', "V", "F", "J", "D"],
    3: ["Z", "M", "L", "S", "V", "T", "B", "H"],
    4: ["R", "S", "J"],
    5: ["C", "Z", "B", "G", "F", "M", "L", "W"],
    6: ["Q", "W", "V", "H", "Z", "R", "G", "B"],
    7: ["V", "J", "P", "C", "B", "D", "N"],
    8: ["P", "T", "B", "Q"],
    9: ["H", "G", "Z", "R", "C"]
}

# table = {
#     1: ["Z", "N"],
#     2: ["M", "C", 'D'],
#     3: ["P"],
# }

"""
        [H]     [W] [B]            
    [D] [B]     [L] [G] [N]        
[P] [J] [T]     [M] [R] [D]        
[V] [F] [V]     [F] [Z] [B]     [C]
[Z] [V] [S]     [G] [H] [C] [Q] [R]
[W] [W] [L] [J] [B] [V] [P] [B] [Z]
[D] [S] [M] [S] [Z] [W] [J] [T] [G]
[T] [L] [Z] [R] [C] [Q] [V] [P] [H]
 1   2   3   4   5   6   7   8   9 
"""

def solve_1(filename):
    with open(filename) as f:
        for line in f:
            if line[0] == "m":
                split_line = line.split(" ")
                num_of_containers_to_move = int(split_line[1])
                from_row = int(split_line[3])
                to_row = int(split_line[5])

                for _ in range(num_of_containers_to_move):
                    container = table[from_row].pop()
                    table[to_row].append(container)

    result = ""
    for v in table.values():
        result += v[-1]

    print(result)


def solve_2(filename):
    with open(filename) as f:
        for line in f:
            if line[0] == "m":
                split_line = line.split(" ")
                num_of_containers_to_move = int(split_line[1])
                from_row = int(split_line[3])
                to_row = int(split_line[5])

                neg = -abs(num_of_containers_to_move)
                containers_to_move = table[from_row][neg:]
                containers_to_keep = table[from_row][:neg]
                table[from_row] = containers_to_keep
                table[to_row].extend(containers_to_move)
                print(table)

    result = ""
    for v in table.values():
        result += v[-1]

    print(result)

#solve_1("input.txt")
solve_2("input.txt")