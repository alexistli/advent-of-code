from aoc_2022.helpers import load_day_input
from aoc_2022.day_04.part_1 import parse_elf_pairs_sections


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


def main():
    data = load_day_input("aoc_2022/day_04/input.txt")
    elf_pairs_sections = parse_elf_pairs_sections(data)
    nb_overlapping_sections = compute_number_overlapping_sections(elf_pairs_sections)
    print(nb_overlapping_sections)


if __name__ == "__main__":
    main()
