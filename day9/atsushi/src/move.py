from src import data

START = (0, 0)


def apply(directions: data.Moves, num_tails: int) -> data.Head:
    head = data.Head(START, num_tails)

    for direction, distance in directions:
        head.move(direction, distance)

    return head
