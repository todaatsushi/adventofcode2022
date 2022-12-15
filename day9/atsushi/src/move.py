from src import data

START = (0, 0)


def apply(directions: data.Moves) -> data.Head:
    head = data.Head(START)

    for direction, distance in directions:
        head.move(direction, distance)

    return head
