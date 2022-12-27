def get_data(filename):
    with open(filename) as f:
        return f.read().splitlines()


def find_similarities(list_1, list_2):
    return set(list_1).intersection(set(list_2))


def find_similarities_3(list_1, list_2, list_3):
    return set(list_1).intersection(set(list_2)).intersection(set(list_3))


def get_priorities(items):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    priorities = 0

    for priority in items:
        priorities += letters.find(priority) + 1

    return priorities


def solve_1(data):
    similarities = []

    for sack in data:
        compartment_1 = sack[0:len(sack)//2]
        compartment_2 = sack[len(sack)//2:]
        sims = find_similarities(compartment_1, compartment_2)
        for sim in sims:
            similarities.append(sim)

    print(similarities)
    print(get_priorities(similarities))


def solve_2(data):
    similarities = []

    start = 0
    end = 3
    while end <= len(data):
        sublist = data[start:end]
        sims = find_similarities_3(sublist[0], sublist[1], sublist[2])
        for sim in sims:
            similarities.append(sim)
        start = end
        end += 3

    print(similarities)
    print(get_priorities(similarities))

sacks = get_data("input.txt")
# solve_1(sacks)

solve_2(sacks)