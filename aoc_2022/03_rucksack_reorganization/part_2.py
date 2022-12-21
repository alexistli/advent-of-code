from aoc_2022.helpers import get_input
from aoc_2022.day_03.part_1 import PRIORITY_MAPPING
from collections import Counter


def chunk_triplets(data):
    for i in range(0, len(data), 3):
        yield data[i : i + 3]


def get_item_common_among_triplet(elf_triplet):
    rucksack_1 = set(elf_triplet[0])
    rucksack_2 = set(elf_triplet[1])
    rucksack_3 = set(elf_triplet[2])
    item_occurence_by_elf = Counter(
        list(rucksack_1) + list(rucksack_2) + list(rucksack_3)
    )
    return item_occurence_by_elf.most_common(1)[0][0]


def main():
    data = [row.strip("\n") for row in get_input("aoc_2022/day_03/input.txt")]
    elf_triplets = chunk_triplets(data)
    total_priority = 0
    for elf_triplet in elf_triplets:
        item_common_among_triplet = get_item_common_among_triplet(elf_triplet)
        total_priority += PRIORITY_MAPPING[item_common_among_triplet]

    print(total_priority)


if __name__ == "__main__":
    main()
