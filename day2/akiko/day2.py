# make sure data file is in same dir as this python file
import os

def round_my_score(mine, yours):
    # A for Rock, B for Paper, and C for Scissors.
    # X for Rock, Y for Paper, and Z for Scissors
    opponent_losing_condition = {
        "Y" : "A",
        "Z" : "B",
        "X" : "C"
    }

    drawing_condition = {
        "Y" : "B",
        "Z" : "C",
        "X" : "A"
    }

    outcome_score = {
        "loss": 0,
        "draw": 3,
        "win": 6
    }

    my_shape_score = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    if drawing_condition[mine] == yours:
        return outcome_score['draw'] + my_shape_score[mine]
    elif opponent_losing_condition[mine] == yours:
        return outcome_score['win'] + my_shape_score[mine]
    else:
        return outcome_score['loss'] + my_shape_score[mine]

# path = os.path.join(os.path.dirname(__file__), './sample.csv')
path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    raw_data = f.read().splitlines()
    
strategy_guide = []
for round in raw_data:
    hand = [round[2], round[0]]
    strategy_guide.append(hand)

results = []
for round in strategy_guide:
    mine = round[0]
    yours = round[1]
    results.append(round_my_score(mine, yours))

print(sum(results))
