"""AoC 5, 2022: Supply Stacks."""


import pathlib

from collections import deque
from typing import Iterator


from aoc_2022.helpers import get_input, parse_data


def parse_puzzle(data: list):
    idx = data.index("")

    drawing_raw = data[: idx - 1]
    procedure_raw = data[idx + 1 :]

    drawing_as_list = [drawing_raw[i : i + 3] for i in range(0, len(drawing_raw), 4)]
    drawing_as_list = [
        [row[i : i + 3] for i in range(0, len(row) - 2, 4)] for row in drawing_raw
    ]

    stacks = list(zip(*drawing_as_list))
    trimmed_stacks = [[crate for crate in stack if crate != "   "] for stack in stacks]
    procedure = [p.strip("\n") for p in procedure_raw]

    return trimmed_stacks, procedure


def parse_instruction(instruction):
    _, quantity, _, source, _, destination = instruction.split()
    return int(quantity), int(source), int(destination)


def execute_instruction_part1(queues: list[deque], instruction):
    quantity, source, destination = parse_instruction(instruction)

    for _ in range(quantity):
        crate_to_move = queues[source - 1].popleft()
        queues[destination - 1].appendleft(crate_to_move)


def part1(data: list[str]) -> str:
    """Solve part 1."""
    stacks, procedure = parse_puzzle(data)

    queues = [deque(stack) for stack in stacks]
    for instruction in procedure:
        execute_instruction_part1(queues, instruction)

    return "".join([queue[0].strip("[").strip("]") for queue in queues])


def execute_instruction_part2(queues: list[deque], instruction):
    quantity, source, destination = parse_instruction(instruction)

    crates_to_move = []
    for crate in range(quantity):
        crates_to_move.append(queues[source - 1].popleft())

    for crate in list(reversed(crates_to_move)):
        queues[destination - 1].appendleft(crate)


def part2(data: list[str]) -> str:
    """Solve part 2."""
    stacks, procedure = parse_puzzle(data)

    queues = [deque(stack) for stack in stacks]
    for instruction in procedure:
        execute_instruction_part2(queues, instruction)

    return "".join([queue[0].strip("[").strip("]") for queue in queues])


def solve(puzzle_input: list[str]) -> Iterator[str]:
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(get_input(pathlib.Path(__file__).parent / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples)))

    solutions = solve(get_input(pathlib.Path(__file__).parent / "input.txt"))
    print(
        "Solutions:\n\t{}".format("\n\t".join(str(solution) for solution in solutions))
    )
