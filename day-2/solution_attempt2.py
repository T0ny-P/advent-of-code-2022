from collections import deque
from pprint import pprint

class RPS():
    round_log = dict()
    round_id = 0

    def __init__(self, opponent_hand, round_input):
        self.decoder_ring ={
            "A":"rock",
            "X":"rock",
            "B":"paper",
            "Y":"paper",
            "C":"scissors",
            "Z":"scissors"
        }
        self.rps_outcome_wheel = deque(["rock","paper","scissors"])
        self.opponent_hand = self.decoder_ring[opponent_hand]
        self.round_input = self.decoder_ring[round_input]

        self._set_outcome_wheel()
        self._process_round()
        pass

    @property
    def total_points(self):
        total_points = 0
        for hand in RPS.round_log:
            total_points += rps_log[hand]["points"]
        return f"Total RPS points: {total_points}"

    def _set_outcome_wheel(self):
        if self.opponent_hand == "rock":
            self.rps_outcome_wheel.rotate(1)
        elif self.opponent_choice == "scissors":
            self.rps_outcome_wheel.rotate(-1)
        pass

    def _process_round(self):
        if self.round_input in ("win","lose","draw"):
            self.round_outcome = self.round_input
            shift_value = [x[1] for x in zip(["win","lose","draw"], [1,0,-1]) if x[0] == self.round_input][0]
            RPS.round_log[f"hand_{RPS.round_id}"]:{
                "opponent_hand":self.opponent_hand,
                "my_hand":self.rps_outcome_wheel[1 + shift_value],
                "outcome":self.round_outcome,
                "points":self._process_points(RPS.round_log[f"hand_{RPS.round_id}"]["my_hand"], RPS.round_log[f"hand_{RPS.round_id}"]["outcome"])
            }

        elif self.round_input in ("rock","paper","scissors"):
            outcome_decoder_value = self.rps_outcome_wheel.index(self.round_input)
            if outcome_decoder_value == 1:
                self.round_outcome == "win"
            elif outcome_decoder_value == 0:
                self.round_outcome == "tie"
            else:
                self.round_outcome == "lose"
            RPS.round_log[f"hand_{RPS.round_id}"]:{
                "opponent_hand":self.opponent_hand,
                "my_hand":self.round_input,
                "outcome":self.round_outcome,
                "points":self._process_points(RPS.round_log[f"hand_{RPS.round_id}"]["my_hand"], RPS.round_log[f"hand_{RPS.round_id}"]["outcome"])
            }
                       
    def _process_points(self, my_choice, outcome):
        points = 0
        if outcome == "win":
            points += 6
        if outcome == "tie":
            points += 3
        if outcome == "lose":
            points += 0
        
        if my_choice == "rock":
            points += 1
        if my_choice == "paper":
            points += 2
        if my_choice == "scissors":
            points += 3
        return points


with open("input.txt", "r") as f:
    rps_games = f.readlines()

for game in rps_games:
    game = game.rstrip()
    player_hands = game.split(" ")
    rps_game = RPS(player_hands[0], player_hands[1])

