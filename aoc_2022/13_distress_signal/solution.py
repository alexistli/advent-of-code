"""AoC 13, 2022: Distress Signal."""

import pathlib
from typing import Iterator

from aoc_2022.utils import get_input, parse_data

CWD = pathlib.Path(__file__).parent


def check_pair_right_order(pair: tuple[list[int], list[int]]) -> bool | None:
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


def part1(data: list[str]) -> int:
    """Solve part 1."""
    indexes_right_order = []
    pairs = [data[i : i + 2] for i in range(0, len(data), 3)]
    for index, raw_pair in enumerate(pairs, start=1):
        pair = eval(raw_pair[0]), eval(raw_pair[1])
        if check_pair_right_order(pair):
            indexes_right_order.append(index)
    return sum(indexes_right_order)


def part2(data: list[str]) -> int:
    """Solve part 2."""
    divider_packets = [[[2]], [[6]]]
    pairs = [data[i : i + 2] for i in range(0, len(data), 3)]
    sorted_packets = []
    for raw_pair in pairs:
        pair = [eval(raw_pair[0]), eval(raw_pair[1])]
        if check_pair_right_order(pair):
            sorted_packets.extend(pair)
        else:
            sorted_packets.extend([pair[1], pair[0]])

    sorted_packets += divider_packets

    is_sorted = None
    while not is_sorted:
        is_sorted = True
        for i in range(len(sorted_packets) - 1):
            pair = sorted_packets[i : i + 2]
            if not check_pair_right_order(pair):
                sorted_packets[i], sorted_packets[i + 1] = (
                    sorted_packets[i + 1],
                    sorted_packets[i],
                )
                is_sorted = False

    divider_packet_indexes = (
        sorted_packets.index(divider_packets[0]) + 1,
        sorted_packets.index(divider_packets[1]) + 1,
    )

    return divider_packet_indexes[0] * divider_packet_indexes[1]


def solve(puzzle_input: list[str]) -> Iterator[int]:
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(get_input(CWD / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(e) for e in examples)))

    solutions = solve(get_input(CWD / "input.txt"))
    print("Solutions:\n\t{}".format("\n\t".join(str(s) for s in solutions)))
