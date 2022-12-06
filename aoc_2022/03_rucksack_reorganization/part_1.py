from aoc_2022.helpers import load_day_input
import string


PRIORITY_MAPPING = {
    l: idx + 1 for idx, l in enumerate(string.ascii_lowercase + string.ascii_uppercase)
}


def split_compartments(items):
    nb_items = len(items)
    return items[: nb_items // 2], items[nb_items // 2 :]


def get_items_both_compartments(compartment_1_items, compartment_2_items):
    for item in compartment_2_items:
        if item in compartment_1_items:
            return item


def compute_item_priority(item: str):
    return PRIORITY_MAPPING[item]


def main():
    data = [row.strip("\n") for row in load_day_input("aoc_2022/day_03/input.txt")]
    duplicate_compartment_items = []
    for row in data:
        compartment_1_items, compartment_2_items = split_compartments(row)
        items_both_compartments = get_items_both_compartments(
            compartment_1_items, compartment_2_items
        )
        duplicate_compartment_items.append(items_both_compartments)

    priority_sum = 0
    for item in duplicate_compartment_items:
        priority_sum += compute_item_priority(item)

    print(priority_sum)


if __name__ == "__main__":
    main()
