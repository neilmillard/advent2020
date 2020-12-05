# Day three, counting trees
# The data input repeats right
from lib import get_lines_from_file


def test_count_trees():
    forest = [
        "..##.......",
        "#...#...#..",
        ".#....#..#.",
        "..#.#...#.#",
        ".#...##..#.",
        "..#.##.....",
        ".#.#.#....#",
        ".#........#",
        "#.##...#...",
        "#...##....#",
        ".#..#...#.#"
    ]
    trees = count_trees(forest, 3, 1)
    print(trees)
    assert 7 == trees

    trees = count_trees(forest, 1, 2)
    print(trees)
    assert 2 == trees


def get_trees_from_file(filepath='day3/day3.txt'):
    trees = get_lines_from_file(filepath)
    return trees


def count_trees(trees, x_step=3, y_step=1):
    # starting at 0,0 (top left) check if a tree exists at 3,1 (y is down)
    count = 0
    x = 0
    y = 0
    y_bounds = len(trees) - y_step
    x_bounds = len(trees[0]) - 1

    # start search
    while y < y_bounds:
        y += y_step
        x += x_step
        if x > x_bounds:
            x = x - x_bounds - 1
        # print(f'{y},{x}')
        # print(f'{trees[y][x]}')
        if trees[y][x] == '#':
            count += 1
    return count


def day_three():
    trees = get_trees_from_file()
    print(count_trees(trees, 1, 1))
    print(count_trees(trees, 3, 1))
    print(count_trees(trees, 5, 1))
    print(count_trees(trees, 7, 1))
    print(count_trees(trees, 1, 2))
    # test_count_trees()
    print(57 * 193 * 64 * 55 * 35)
