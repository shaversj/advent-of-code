def get_puzzle_input(filename):
    data = []
    with open(filename) as f:
        for line in f:

            data.append(line.strip().split(" "))

    return data


def get_winner(player_1_move, player_2_move):
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    # a = rock, b = paper, c = scissors
    # x = rock, y = paper, z = scissors

    moves = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }

    if moves.get(player_1_move) == "rock" and moves.get(player_2_move) == "scissors":
        return 1
    elif moves.get(player_1_move) == "scissors" and moves.get(player_2_move) == "paper":
        return 1
    elif moves.get(player_1_move) == "paper" and moves.get(player_2_move) == "rock":
        return 1
    elif moves.get(player_2_move) == "rock" and moves.get(player_1_move) == "scissors":
        return 2
    elif moves.get(player_2_move) == "scissors" and moves.get(player_1_move) == "paper":
        return 2
    elif moves.get(player_2_move) == "paper" and moves.get(player_1_move) == "rock":
        return 2
    else:
        return 0


def get_winner_2(player_1_move, player_2_move):
    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
    # X means you need to lose,
    # Y means you need to end the round in a draw,
    # and Z means you need to win.

    lose_map = {
        "A": "C",
        "B": "A",
        "C": "B",
    }

    win_map = {
        "A": "B",
        "B": "C",
        "C": "A",
    }

    if player_2_move == "X":
        return 1, lose_map[player_1_move]
    elif player_2_move == "Y":
        return 0, player_1_move
    elif player_2_move == "Z":
        return 2, win_map[player_1_move]


def calculate_score_round_1(formatted_data):
    player_1_shape_points = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    player_2_shape_points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    round_points = {
        "win": 6,
        "draw": 3
    }

    player_1_score = 0
    player_2_score = 0

    for player_1_move, player_2_move in formatted_data:
        score_1 = player_1_shape_points.get(player_1_move)
        score_2 = player_2_shape_points.get(player_2_move)

        player_1_score += score_1
        player_2_score += score_2

        # add round score
        winner = get_winner(player_1_move, player_2_move)
        if winner == 0:
            player_1_score += round_points.get("draw")
            player_2_score += round_points.get("draw")
        elif winner == 1:
            player_1_score += round_points.get("win")
        else:
            player_2_score += round_points.get("win")


    print(player_2_score)


def calculate_score_round_2(formatted_data):
    shape_points = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    round_points = {
        "win": 6,
        "draw": 3
    }

    player_1_score = 0
    player_2_score = 0

    for player_1_move, player_2_move in formatted_data:
        winner, player_2_shape = get_winner_2(player_1_move, player_2_move)
        player_1_score += shape_points.get(player_1_move)
        player_2_score += shape_points.get(player_2_shape)

        if winner == 0:
            player_1_score += round_points.get("draw")
            player_2_score += round_points.get("draw")
        elif winner == 1:
            player_1_score += round_points.get("win")
        else:
            player_2_score += round_points.get("win")

    print(player_2_score)


data = get_puzzle_input("input.txt")

calculate_score_round_2(data)