"""AoC 9, 2022: Rope Bridge."""


from aoc_2022.helpers import get_input

import pathlib


def parse_data(puzzle_input):
    """Parse input."""
    return [row.strip("\n") for row in puzzle_input]


def signum(x):
    return 1 if (x > 0) else -1 if (x < 0) else 0


def catchup_with_head(
    head: tuple[int, int], tail: tuple[int, int], bridge: list[list[str]], tails
) -> None:
    relative_position = (head[0] - tail[0], head[1] - tail[1])

    match relative_position:
        case [i, j] if abs(i) < 2 and abs(j) < 2:
            pass
        case [i, j] if i == 0 and abs(j) == 2:
            tail[1] += 1 * signum(j)
            if tail is tails[-1]:
                bridge[tail[0]][tail[1]] = "#"
        case [i, j] if j == 0 and abs(i) == 2:
            tail[0] += 1 * signum(i)
            if tail is tails[-1]:
                bridge[tail[0]][tail[1]] = "#"
        case [i, j]:
            tail[0] += 1 * signum(i)
            tail[1] += 1 * signum(j)
            if tail is tails[-1]:
                bridge[tail[0]][tail[1]] = "#"


def part1(data):
    """Solve part 1."""
    PUZZLE_SIZE = 3000
    bridge = [[" "] * PUZZLE_SIZE for _ in range(PUZZLE_SIZE)]
    start = [PUZZLE_SIZE // 2 + 6, PUZZLE_SIZE // 2 - 6]
    bridge[start[0]][start[1]] = "s"
    head = list(start)
    tail = list(start)

    for row in data:
        match row.split():
            case ["U", steps]:
                for _ in range(int(steps)):
                    head[0] -= 1
                    catchup_with_head(head, tail, bridge)
            case ["R", steps]:
                for s in range(int(steps)):
                    head[1] += 1
                    catchup_with_head(head, tail, bridge)
            case ["D", steps]:
                for s in range(int(steps)):
                    head[0] += 1
                    catchup_with_head(head, tail, bridge)
            case ["L", steps]:
                for s in range(int(steps)):
                    head[1] -= 1
                    catchup_with_head(head, tail, bridge)

    nb_visited_positions = 0
    for row in bridge:
        nb_visited_positions += len([pos for pos in row if pos in "#s"])
    return nb_visited_positions


def part2(data):
    """Solve part 2."""
    PUZZLE_SIZE = 3000
    bridge = [[" "] * PUZZLE_SIZE for _ in range(PUZZLE_SIZE)]
    start = [PUZZLE_SIZE // 2 + 6, PUZZLE_SIZE // 2 - 6]
    bridge[start[0]][start[1]] = "s"
    head = list(start)
    tails = [list(start) for _ in range(9)]

    for row in data:
        match row.split():
            case ["U", steps]:
                for _ in range(int(steps)):
                    head[0] -= 1
                    catchup_with_head(head, tails[0], bridge, tails)
                    for i, tail in enumerate(tails[1:]):
                        catchup_with_head(tails[i], tail, bridge, tails)
            case ["R", steps]:
                for s in range(int(steps)):
                    head[1] += 1
                    catchup_with_head(head, tails[0], bridge, tails)
                    for i, tail in enumerate(tails[1:]):
                        catchup_with_head(tails[i], tail, bridge, tails)
            case ["D", steps]:
                for s in range(int(steps)):
                    head[0] += 1
                    catchup_with_head(head, tails[0], bridge, tails)
                    for i, tail in enumerate(tails[1:]):
                        catchup_with_head(tails[i], tail, bridge, tails)
            case ["L", steps]:
                for s in range(int(steps)):
                    head[1] -= 1
                    catchup_with_head(head, tails[0], bridge, tails)
                    for i, tail in enumerate(tails[1:]):
                        catchup_with_head(tails[i], tail, bridge, tails)

    nb_visited_positions = 0
    for row in bridge:
        nb_visited_positions += len([pos for pos in row if pos in "#s"])
    return nb_visited_positions


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    # yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(get_input(pathlib.Path(__file__).parent / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples)))

    examples_2 = solve(get_input(pathlib.Path(__file__).parent / "example2.txt"))
    print(
        "Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples_2))
    )

    solutions = solve(get_input(pathlib.Path(__file__).parent / "input.txt"))
    print(
        "Solutions:\n\t{}".format("\n\t".join(str(solution) for solution in solutions))
    )
