"""AoC 10, 2022: Cathode-Ray Tube."""


from aoc_2022.helpers import load_day_input

import pathlib

CWD = pathlib.Path(__file__).parent


def parse_data(puzzle_input: list[str]) -> list[str]:
    """Parse input."""
    return [row.strip("\n") for row in puzzle_input]


def compute_new_register(register: int, v: int) -> int:
    register += v
    return register


def run_cycle(cycle: int, register: int, v: int, signal_strengths: list[int]):
    if cycle == 20 or (cycle > 20 and (cycle - 20) % 40 == 0):
        signal_strengths.append(cycle * register)
    if v:
        register = compute_new_register(register, v)
    cycle += 1
    return register, cycle


def part1(data: list[str]):
    """Solve part 1."""
    register = 1
    signal_strengths = []
    cycle = 1
    for row in data:
        match row.split():
            case ["noop"]:
                register, cycle = run_cycle(cycle, register, 0, signal_strengths)
            case ["addx", v]:
                register, cycle = run_cycle(cycle, register, 0, signal_strengths)
                register, cycle = run_cycle(cycle, register, int(v), signal_strengths)

    return sum(signal_strengths)


def run_crt_cycle(cycle: int, register: int, v: int, crt_screen: list[int]):
    row, column = (cycle - 1) // 40, (cycle - 1) % 40
    if column in range(register - 1, register + 2):
        crt_screen[row][column] = "#"
    if v:
        register = compute_new_register(register, v)
    cycle += 1
    return register, cycle


def part2(data: list[str]):
    """Solve part 2."""
    register = 1
    crt_screen = [["."] * 40 for _ in range(6)]
    cycle = 1
    for row in data:
        match row.split():
            case ["noop"]:
                register, cycle = run_crt_cycle(cycle, register, 0, crt_screen)
            case ["addx", v]:
                register, cycle = run_crt_cycle(cycle, register, 0, crt_screen)
                register, cycle = run_crt_cycle(cycle, register, int(v), crt_screen)

    for row in crt_screen:
        print(row)


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
