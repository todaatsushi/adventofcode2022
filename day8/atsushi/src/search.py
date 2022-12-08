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
