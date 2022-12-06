from pathlib import Path
from collections import deque
from aoc_2022.day_05.part_1 import parse_instruction, parse_puzzle


from aoc_2022.helpers import load_day_input


def execute_instruction(queues: list[deque], instruction):
    quantity, source, destination = parse_instruction(instruction)

    crates_to_move = []
    for crate in range(quantity):
        crates_to_move.append(queues[source - 1].popleft())

    for crate in list(reversed(crates_to_move)):
        queues[destination - 1].appendleft(crate)


def main():
    data = load_day_input(Path(__file__).parent / "input.txt")
    stacks, procedure = parse_puzzle(data)

    queues = [deque(stack) for stack in stacks]
    for instruction in procedure:
        execute_instruction(queues, instruction)

    print("".join([queue[0].strip("[").strip("]") for queue in queues]))


if __name__ == "__main__":
    main()
