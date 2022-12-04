from aoc_2022.helpers import load_day_input


def parse_elf_pairs_sections(data: list[str]):
    elf_pairs_sections = []
    for elf_pair_raw in data:
        elf_pair = []
        for elf_section_raw in elf_pair_raw.split(","):
            elf_section = []
            for section_boundary_raw in elf_section_raw.strip("\n").split("-"):
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


def main():
    data = load_day_input("aoc_2022/day_04/input.txt")
    elf_pairs_sections = parse_elf_pairs_sections(data)
    nb_overlapping_sections = compute_number_fully_overlapping_sections(
        elf_pairs_sections
    )
    print(nb_overlapping_sections)


if __name__ == "__main__":
    main()
