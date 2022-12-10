
from pprint import pprint

with open("input.txt", "r") as f:
    rps_games = f.readlines()

hand_format = {
    "A":10,
    "B":30,
    "C":50,
    "X":1,
    "Y":3,
    "Z":5
}

choices ={
    11:{
        "opponent_choice":"rock",
        "my_choice":"scissors"
    },
    13:{
        "opponent_choice":"rock",
        "my_choice":"rock"
    },
    15:{
        "opponent_choice":"rock",
        "my_choice":"paper"
    },
    31:{
        "opponent_choice":"paper",
        "my_choice":"rock"
    },
    33:{
        "opponent_choice":"paper",
        "my_choice":"paper"
    },
    35:{
        "opponent_choice":"paper",
        "my_choice":"scissors"
    },
    51:{
        "opponent_choice":"scissors",
        "my_choice":"paper"
    },
    53:{
        "opponent_choice":"scissors",
        "my_choice":"scissors"
    },
    55:{
        "opponent_choice":"scissors",
        "my_choice":"rock"
    }
}

def __process_outcome(outcome):
    if outcome in (13, 33, 53):
        return "tie"
    if outcome in (11, 31, 51):
        return "lose"
    if outcome in (15, 35, 55):
        return "win"
    pass

def process_points(hand_value, choice):
    outcome = __process_outcome(hand_value)
    points = 0
    if outcome == "win":
        points += 6
    if outcome == "tie":
        points += 3
    if outcome == "lose":
        points += 0
    
    if choice == "rock":
        points += 1
    if choice == "paper":
        points += 2
    if choice == "scissors":
        points += 3
    return points


def process_games():
    rps_log = dict()
    id = 1
    for game in rps_games:
        game = game.rstrip()
        player_hands = game.split(" ")
        outcome_value = hand_format[player_hands[0]] + hand_format[player_hands[1]]
        rps_log[f"hand_{id}"] = {
            "opponent_choice": choices[outcome_value]["opponent_choice"],
            "my_choice": choices[outcome_value]["my_choice"],
            "points": process_points(outcome_value, choices[outcome_value]["my_choice"])
            }
        id += 1
    return rps_log

# pprint(process_games())

total_points = 0
rps_log = process_games()
for hand in rps_log:
    total_points += rps_log[hand]["points"]

print(f"Total RPS points: {total_points}")