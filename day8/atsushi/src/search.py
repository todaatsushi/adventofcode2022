from src import input


def iter_map(
    map: input.Map, visible_trees: set[tuple[int, int]], iter: int, cols: bool
) -> set[tuple[int, int]]:
    for r, row in enumerate(map):
        highest_visible_tree = -1
        indicies = range(len(row)) if iter == 1 else range(len(row) - 1, -1, -1)
        for c in indicies:
            height = row[c]
            if height > highest_visible_tree:
                highest_visible_tree = height

                if cols:
                    visible_trees.add((r, c))
                else:
                    visible_trees.add((c, r))
    return visible_trees


def find_num_visible_trees(map: input.Map) -> int:
    visible_trees: set[tuple[int, int]] = set()

    for m, cols in ((map.T, True), (map, False)):
        for iter in (-1, 1):
            visible_trees = iter_map(m, visible_trees, iter, cols)
    return len(visible_trees)


def walk(
    map: input.Map,
    row_num: int | None,
    col_num: int | None,
    iter: range,
    cols: bool,
    height: int,
) -> int:
    out = 0
    for index in iter:
        if cols:
            _height = map[row_num][index]
        else:
            _height = map[index][col_num]
        out += 1
        if _height >= height:
            break
    return out


def from_tree(map: input.Map, row_num: int, col_num: int) -> int:
    height = map[row_num][col_num]
    tot = 1

    for (iter, cols) in (
        (range(col_num + 1, len(map[row_num])), True),
        (range(row_num + 1, len(map)), False),
        (range(col_num - 1, -1, -1), True),
        (range(row_num - 1, -1, -1), False),
    ):
        tot *= walk(map, row_num, col_num, iter, cols, height)

    return tot


def find_scenic_score(map: input.Map) -> int:
    scores = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]

    for row_num, row in enumerate(map):
        for col_num in range(len(row)):
            scores[row_num][col_num] = from_tree(map, row_num, col_num)

    return max([max(h) for h in scores])
