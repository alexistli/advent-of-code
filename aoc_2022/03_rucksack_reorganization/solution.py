"""AoC 3, 2022: Rucksack Reorganization."""

from collections import Counter
import pathlib
import string
from typing import Iterator

from aoc_2022.utils import get_input, parse_data


PRIORITY_MAPPING = {l: idx + 1 for idx, l in enumerate(string.ascii_lowercase + string.ascii_uppercase)}


def split_compartments(items: str) -> tuple[str, str]:
    nb_items = len(items)
    return items[: nb_items // 2], items[nb_items // 2 :]


def get_items_both_compartments(compartment_1_items: str, compartment_2_items: str) -> str:
    return next(item for item in compartment_2_items if item in compartment_1_items)


def compute_item_priority(item: str) -> int:
    return PRIORITY_MAPPING[item]


def part1(data: list[str]) -> int:
    """Solve part 1."""
    duplicate_compartment_items = []
    for row in data:
        compartment_1_items, compartment_2_items = split_compartments(row)
        items_both_compartments = get_items_both_compartments(compartment_1_items, compartment_2_items)
        duplicate_compartment_items.append(items_both_compartments)

    priority_sum = 0
    for item in duplicate_compartment_items:
        priority_sum += compute_item_priority(item)

    return priority_sum


def chunk_triplets(data: list[str]) -> Iterator[list[str]]:
    for i in range(0, len(data), 3):
        yield data[i : i + 3]


def get_item_common_among_triplet(elf_triplet: list[str]) -> str:
    rucksack_1 = set(elf_triplet[0])
    rucksack_2 = set(elf_triplet[1])
    rucksack_3 = set(elf_triplet[2])
    item_occurrence_by_elf = Counter(list(rucksack_1) + list(rucksack_2) + list(rucksack_3))
    return item_occurrence_by_elf.most_common(1)[0][0]


def part2(data: list[str]) -> int:
    """Solve part 2."""
    elf_triplets = chunk_triplets(data)
    total_priority = 0
    for elf_triplet in elf_triplets:
        item_common_among_triplet = get_item_common_among_triplet(elf_triplet)
        total_priority += PRIORITY_MAPPING[item_common_among_triplet]

    return total_priority


def solve(puzzle_input: list[str]) -> Iterator[int]:
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(get_input(pathlib.Path(__file__).parent / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples)))

    solutions = solve(get_input(pathlib.Path(__file__).parent / "input.txt"))
    print("Solutions:\n\t{}".format("\n\t".join(str(solution) for solution in solutions)))
