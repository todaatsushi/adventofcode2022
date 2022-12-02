# make sure data file is in same dir as this python file
import os

def part1_my_score(mine, yours):
    # PART 1
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

    my_hand_score = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    if drawing_condition[mine] == yours:
        return outcome_score['draw'] + my_hand_score[mine]
    elif opponent_losing_condition[mine] == yours:
        return outcome_score['win'] + my_hand_score[mine]
    else:
        return outcome_score['loss'] + my_hand_score[mine]

# Part 2
# now you need to figure out what shape to choose so the round ends as indicated

def part2_my_score(result, yours):
    # PART 2
    # A for Rock, B for Paper, and C for Scissors.
    # X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    my_condition_for_losing_given_yours = {
        "A" : "C",
        "B" : "A",
        "C" : "B"
    }

    my_condition_for_winning_given_yours = {
        "A" : "B",
        "B" : "C",
        "C" : "A"
    }

    outcome_score = {
        "loss": 0,
        "draw": 3,
        "win": 6
    }

# 1 for Rock, 2 for Paper, and 3 for Scissors
    my_hand_score = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    if result == 'Y': #draw
        return outcome_score['draw'] + my_hand_score[yours]
    elif result == 'Z': #win
        return outcome_score['win'] + my_hand_score[my_condition_for_winning_given_yours[yours]]
    else: #loss
        return outcome_score['loss'] + my_hand_score[my_condition_for_losing_given_yours[yours]]

# path = os.path.join(os.path.dirname(__file__), './sample.csv')
path = os.path.join(os.path.dirname(__file__), './data.csv')
with open(path,"r") as f:
    raw_data = f.read().splitlines()

strategy_guide = []
for round in raw_data:
    hand = [round[2], round[0]]
    strategy_guide.append(hand)

results_part1 = []
for round in strategy_guide:
    mine = round[0]
    yours = round[1]
    results_part1.append(part1_my_score(mine, yours))

results_part2 = []
for round in strategy_guide:
    result = round[0]
    yours = round[1]
    results_part2.append(part2_my_score(result, yours))

print(sum(results_part1))

print(sum(results_part2))
