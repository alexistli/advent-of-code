"""AoC 9, 2022: Rope Bridge."""

from dataclasses import dataclass
import pathlib
from typing import Iterator

from aoc_2022.utils import get_input, parse_data


@dataclass
class Knot:
    x: int
    y: int


def signum(x: int) -> int:
    """Return sign of an integer."""
    return 1 if (x > 0) else -1 if (x < 0) else 0


def catchup_with_head(head: Knot, tail: Knot, bridge: list[list[str]], tails) -> None:
    relative_position = (head.x - tail.x, head.y - tail.y)

    match relative_position:
        case [i, j] if abs(i) < 2 and abs(j) < 2:
            pass
        case [i, j] if i == 0 and abs(j) == 2:
            tail.y += 1 * signum(j)
            if tail is tails[-1]:
                bridge[tail.x][tail.y] = "#"
        case [i, j] if j == 0 and abs(i) == 2:
            tail.x += 1 * signum(i)
            if tail is tails[-1]:
                bridge[tail.x][tail.y] = "#"
        case [i, j]:
            tail.x += 1 * signum(i)
            tail.y += 1 * signum(j)
            if tail is tails[-1]:
                bridge[tail.x][tail.y] = "#"


def part1(data: list[str]) -> int:
    """Solve part 1."""
    PUZZLE_SIZE = 3000
    bridge = [[" "] * PUZZLE_SIZE for _ in range(PUZZLE_SIZE)]
    start = [PUZZLE_SIZE // 2 + 6, PUZZLE_SIZE // 2 - 6]
    bridge[start[0]][start[1]] = "s"
    head = Knot(*start)
    tail = Knot(*start)

    for row in data:
        match row.split():
            case ["U", steps]:
                for _ in range(int(steps)):
                    head.x -= 1
                    catchup_with_head(head, tail, bridge, [tail])
            case ["R", steps]:
                for s in range(int(steps)):
                    head.y += 1
                    catchup_with_head(head, tail, bridge, [tail])
            case ["D", steps]:
                for s in range(int(steps)):
                    head.x += 1
                    catchup_with_head(head, tail, bridge, [tail])
            case ["L", steps]:
                for s in range(int(steps)):
                    head.y -= 1
                    catchup_with_head(head, tail, bridge, [tail])

    nb_visited_positions = 0
    for bridge_row in bridge:
        nb_visited_positions += len([pos for pos in bridge_row if pos in "#s"])
    return nb_visited_positions


def part2(data: list[str]) -> int:
    """Solve part 2."""
    PUZZLE_SIZE = 3000
    bridge = [[" "] * PUZZLE_SIZE for _ in range(PUZZLE_SIZE)]
    start = [PUZZLE_SIZE // 2 + 6, PUZZLE_SIZE // 2 - 6]
    bridge[start[0]][start[1]] = "s"
    head = Knot(*start)
    tails = [Knot(*start) for _ in range(9)]

    for row in data:
        match row.split():
            case ["U", steps]:
                for _ in range(int(steps)):
                    head.x -= 1
                    catchup_with_head(head, tails[0], bridge, tails)
                    for i, tail in enumerate(tails[1:]):
                        catchup_with_head(tails[i], tail, bridge, tails)
            case ["R", steps]:
                for _ in range(int(steps)):
                    head.y += 1
                    catchup_with_head(head, tails[0], bridge, tails)
                    for i, tail in enumerate(tails[1:]):
                        catchup_with_head(tails[i], tail, bridge, tails)
            case ["D", steps]:
                for _ in range(int(steps)):
                    head.x += 1
                    catchup_with_head(head, tails[0], bridge, tails)
                    for i, tail in enumerate(tails[1:]):
                        catchup_with_head(tails[i], tail, bridge, tails)
            case ["L", steps]:
                for _ in range(int(steps)):
                    head.y -= 1
                    catchup_with_head(head, tails[0], bridge, tails)
                    for i, tail in enumerate(tails[1:]):
                        catchup_with_head(tails[i], tail, bridge, tails)

    nb_visited_positions = 0
    for bridge_row in bridge:
        nb_visited_positions += len([pos for pos in bridge_row if pos in "#s"])
    return nb_visited_positions


def solve(puzzle_input: list[str]) -> Iterator[int]:
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(get_input(pathlib.Path(__file__).parent / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples)))

    examples_2 = solve(get_input(pathlib.Path(__file__).parent / "example2.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples_2)))

    solutions = solve(get_input(pathlib.Path(__file__).parent / "input.txt"))
    print("Solutions:\n\t{}".format("\n\t".join(str(solution) for solution in solutions)))
