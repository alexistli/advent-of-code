"""AoC 13, 2022: Distress Signal."""


from aoc_2022.helpers import load_day_input

import pathlib

CWD = pathlib.Path(__file__).parent


def parse_data(puzzle_input: list[str]) -> list[str]:
    """Parse input."""
    return [row.strip("\n") for row in puzzle_input]


def check_pair_right_order(pair):
    is_right_order = None
    match pair:
        case [left, right] if left == right:
            pass
        case [int(left), int(right)]:
            is_right_order = left < right  # equality covered above
        case [list(left), list(right)] if not left or not right:
            is_right_order = not left  # left list expired before right list
        case [list(left), int(right)]:
            is_right_order = check_pair_right_order([left, [right]])
        case [int(left), list(right)]:
            is_right_order = check_pair_right_order([[left], right])
        case [list(left), list(right)]:
            is_right_order = check_pair_right_order(pair[0][:1] + pair[1][:1])
            if is_right_order is None:
                is_right_order = check_pair_right_order([pair[0][1:], pair[1][1:]])
    return is_right_order


def part1(data: list[str]):
    """Solve part 1."""
    indexes_right_order = []
    pairs = [data[i : i + 2] for i in range(0, len(data), 3)]
    for index, raw_pair in enumerate(pairs, start=1):
        pair = eval(raw_pair[0]), eval(raw_pair[1])
        if check_pair_right_order(pair):
            indexes_right_order.append(index)
    return sum(indexes_right_order)


def part2(data: list[str]):
    """Solve part 2."""


def solve(puzzle_input: list[str]):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(load_day_input(CWD / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(e) for e in examples)))

    solutions = solve(load_day_input(CWD / "input.txt"))
    print("Solutions:\n\t{}".format("\n\t".join(str(s) for s in solutions)))
