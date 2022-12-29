"""AoC 4, 2022: Camp Cleanup."""


import pathlib
from typing import Iterator

from aoc_2022.helpers import get_input, parse_data


def parse_elf_pairs_sections(data: list[str]):
    elf_pairs_sections = []
    for elf_pair_raw in data:
        elf_pair = []
        for elf_section_raw in elf_pair_raw.split(","):
            elf_section = []
            for section_boundary_raw in elf_section_raw.split("-"):
                section_boundary = int(section_boundary_raw)
                elf_section.append(section_boundary)
            elf_pair.append(elf_section)
        elf_pairs_sections.append(elf_pair)

    return elf_pairs_sections


def get_resulting_section(elf_pair_sections):
    full_section = elf_pair_sections[0] + elf_pair_sections[1]
    return [min(full_section), max(full_section)]


def compute_number_fully_overlapping_sections(elf_pairs_sections):
    number = 0
    for elf_pair_sections in elf_pairs_sections:
        elf_pair_resulting_section = get_resulting_section(elf_pair_sections)
        if elf_pair_resulting_section in elf_pair_sections:
            number += 1
    return number


def part1(data: list[str]) -> int:
    """Solve part 1."""
    elf_pairs_sections = parse_elf_pairs_sections(data)
    nb_overlapping_sections = compute_number_fully_overlapping_sections(
        elf_pairs_sections
    )
    return nb_overlapping_sections


def check_section_overlap(elf_pair_sections):
    section_1, section_2 = elf_pair_sections
    section_1_inf, section_1_sup = section_1
    section_2_inf, section_2_sup = section_2
    if section_1_inf <= section_2_inf:
        if section_1_sup >= section_2_inf:
            return True
    elif section_1_inf > section_2_inf:
        if section_1_inf <= section_2_sup:
            return True
    return False


def compute_number_overlapping_sections(elf_pairs_sections):
    number = 0
    for elf_pair_sections in elf_pairs_sections:
        if check_section_overlap(elf_pair_sections):
            number += 1
    return number


def part2(data: list[str]) -> int:
    """Solve part 2."""
    elf_pairs_sections = parse_elf_pairs_sections(data)
    nb_overlapping_sections = compute_number_overlapping_sections(elf_pairs_sections)
    return nb_overlapping_sections


def solve(puzzle_input: list[str]) -> Iterator[int]:
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
