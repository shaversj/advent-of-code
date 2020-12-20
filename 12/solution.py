def load_actions(filename):
    with open(filename) as f:
        actions = f.read().splitlines()

    return actions


def process_actions(actions):
    directions = {"E": 0, "S": 0, "W": 0, "N": 0}
    compass = ["E", "S", "W", "N"]
    compass_map = {"N": "S", "S": "N", "E": "W", "W": "E"}

    current_direction = "E"

    for command in actions:
        action = command[0]
        value = int(command[1:])

        if action == "F":

            directions[current_direction] += abs(directions[compass_map[current_direction]] - value)
            if directions[compass_map[current_direction]] - value < 0:
                directions[compass_map[current_direction]] = 0
            else:
                directions[compass_map[current_direction]] = directions[compass_map[current_direction]] - value

        elif action in ["N", "S", "E", "W"]:
            directions[action] += abs(directions[compass_map[action]] - value)
            if directions[compass_map[action]] - value < 0:
                directions[compass_map[action]] = 0
            else:
                directions[compass_map[action]] = directions[compass_map[action]] - value
            print(directions)
        else:
            print(action, value)
            print(current_direction)
            current_direction_idx = compass.index(current_direction)
            current_direction = compass[(change_direction(action, value) + current_direction_idx) % 4]
            print(current_direction)

        # if action == "N":
        #     directions["N"] += value - directions["N"]
        #
        # if action == "S":
        #     directions["S"] += value - directions["S"]
        #
        # if action == "E":
        #     directions["E"] += value - directions["E"]
        #
        # if action == "W":
        #     directions["W"] += value - directions["W"]


        # if action == "F":
        #     directions[current_direction] += value - directions[current_direction]
    print(directions)
    print((abs(directions["N"] - directions["S"]) + (directions["E"] - directions["W"])))


def change_direction(turn, degrees):
    if turn == "L":
        return -degrees//90
    else:
        return degrees//90


actions_from_file = load_actions("input.txt")
process_actions(actions_from_file)
