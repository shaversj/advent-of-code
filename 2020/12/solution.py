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
            print(action, value)

            opposite_pointing_direction = compass_map[current_direction]
            opposite_pointing_direction_value = directions[compass_map[current_direction]]

            if opposite_pointing_direction_value == 0:
                directions[current_direction] += value

            elif opposite_pointing_direction_value - value > 0:
                directions[opposite_pointing_direction] = opposite_pointing_direction_value - value

                directions[current_direction] += value
            else:
                directions[opposite_pointing_direction] = 0
                directions[current_direction] += abs(opposite_pointing_direction_value - value)

            print(directions)

            # directions[current_direction] += abs(directions[compass_map[current_direction]] - value)
            # if directions[compass_map[current_direction]] - value < 0:
            #     directions[compass_map[current_direction]] = 0
            # else:
            #     directions[compass_map[current_direction]] = directions[compass_map[current_direction]] - value
            # print(directions)

        elif action in ["N", "S", "E", "W"]:
            print(action, value)
            opposite_direction = compass_map[action]
            opposite_direction_value = directions[opposite_direction]

            if opposite_direction_value == 0:
                directions[action] += value

            elif opposite_direction_value - value > 0:
                # Subtract value from opposite direction
                directions[opposite_direction] = opposite_direction_value - value

                # Add value to current direction
                directions[action] += value
            else:
                # Update opposite direction to 0
                directions[opposite_direction] = 0

                # Update curr direction with abs value
                directions[action] += abs(opposite_direction_value - value)

            print(directions)
            # # Updates direction
            # directions[action] += abs(directions[compass_map[action]] - value)
            # print(directions)
            # if directions[compass_map[action]] - value < 0:
            #     directions[compass_map[action]] = 0
            # else:
            #     # Updates corresponding direction
            #     directions[compass_map[action]] = directions[compass_map[action]] - value
            # #print(directions)
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
    print(((abs(directions["N"] - directions["S"])) + abs(directions["E"] - directions["W"])))


def change_direction(turn, degrees):
    if turn == "L":
        return -degrees//90
    else:
        return degrees//90


actions_from_file = load_actions("input.txt")
process_actions(actions_from_file)

# 195931632882400