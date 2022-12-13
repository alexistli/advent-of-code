"""AoC 11, 2022: Monkey in the Middle."""


import math
from aoc_2022.helpers import load_day_input

import pathlib

from collections import deque

CWD = pathlib.Path(__file__).parent


class Monkey:
    def __init__(
        self,
        index: int,
        starting_items: list[int],
        operation: str,
        test: tuple[int, int, int],
    ) -> None:
        self.index = index
        self.starting_items: deque[int] = deque(starting_items)
        self.operation = operation
        self.test = test
        self.current_item = None
        self.nb_inspected_items = 0

    def inspect_item(self) -> None:
        self.current_item = old = self.starting_items.popleft()
        self.current_item = new = eval(self.operation)
        self.nb_inspected_items += 1

    def relieve_worry_level(self) -> None:
        self.current_item = self.current_item // 3

    def test_worry_level(self) -> int:
        if self.current_item % self.test[0] == 0:
            return self.test[1]
        else:
            return self.test[2]

    def receive_item(self, item) -> None:
        self.starting_items.append(item)

    def throw_item(self, monkeys: list["Monkey"]) -> None:
        target_monkey = monkeys[self.test_worry_level()]
        target_monkey.receive_item(self.current_item)


def parse_data(puzzle_input: list[str]) -> list[str]:
    """Parse input."""
    return [row.strip("\n") for row in puzzle_input]


def parse_monkey_note(monkey_note: list[str]) -> Monkey:
    monkey_index = int(monkey_note[0][-2])
    monkey_starting_items = [
        int(item) for item in monkey_note[1].strip("Starting items: ").split(", ")
    ]
    monkey_operation = monkey_note[2].split("= ")[1]
    monkey_test_condition = int(monkey_note[3][-2:])
    monkey_test_true = int(monkey_note[4][-2:])
    monkey_test_false = int(monkey_note[5][-2:])
    monkey = Monkey(
        monkey_index,
        monkey_starting_items,
        monkey_operation,
        (monkey_test_condition, monkey_test_true, monkey_test_false),
    )
    return monkey


def part1(data: list[str]):
    """Solve part 1."""
    monkeys: list[Monkey] = []
    for i in range(0, len(data), 7):
        monkey_note = data[i : i + 7]
        monkey = parse_monkey_note(monkey_note)
        monkeys.append(monkey)

    for i in range(20):
        for monkey in monkeys:
            while monkey.starting_items:
                monkey.inspect_item()
                monkey.relieve_worry_level()
                monkey.throw_item(monkeys)

    most_active_monkeys = sorted(
        monkeys, key=lambda m: m.nb_inspected_items, reverse=True
    )[:2]
    monkey_business = math.prod([m.nb_inspected_items for m in most_active_monkeys])
    return monkey_business


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
