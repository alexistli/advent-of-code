from pathlib import Path
from collections import deque


from aoc_2022.helpers import load_day_input


def parse_puzzle(data: list):
    idx = data.index("\n")

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


def execute_instruction(queues: list[deque], instruction):
    quantity, source, destination = parse_instruction(instruction)

    for _ in range(quantity):
        crate_to_move = queues[source - 1].popleft()
        queues[destination - 1].appendleft(crate_to_move)


def main():
    data = load_day_input(Path(__file__).parent / "input.txt")
    stacks, procedure = parse_puzzle(data)

    queues = [deque(stack) for stack in stacks]
    for instruction in procedure:

        execute_instruction(queues, instruction)

    print("".join([queue[0].strip("[").strip("]") for queue in queues]))


if __name__ == "__main__":
    main()
