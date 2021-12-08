with open("inputs/day_08.txt", "r") as text_file:
    lines = text_file.readlines()
    data = []
    for line in lines:
        patterns, output = line.strip().split("|")
        patterns = patterns.split()
        output = output.split()
        data.append([patterns, output])


# ================ Part 1 ================

ones = fours = sevens = heights = 0
for line in data:
    for digit in line[1]:
        if len(digit) == 2:
            ones += 1
        elif len(digit) == 4:
            fours += 1
        elif len(digit) == 3:
            sevens += 1
        elif len(digit) == 7:
            heights += 1

occurrences = ones + fours + sevens + heights
print("Solution for part 1:", occurrences)

# ================ Part 2 ================
# Hypothesis: we can guess segments by their occurrence

# Verification:
# a = 8
# b = 6
# c = 8
# d = 7
# e = 4
# f = 9
# g = 7

# We can deduct b, e and f
# Then using results from Part 1 we can deduct a, d, e and g

letters = set("abcdefg")

digits = [
    # 0
    {"a", "b", "c", "e", "f", "g"},
    # 1
    {"c", "f"},
    # 2
    {"a", "c", "d", "e", "g"},
    # 3
    {"a", "c", "d", "f", "g"},
    # 4
    {"b", "c", "d", "f"},
    # 5
    {"a", "b", "d", "f", "g"},
    # 6
    {"a", "b", "d", "e", "f", "g"},
    # 7
    {"a", "c", "f"},
    # 8
    {"a", "b", "c", "d", "e", "f", "g"},
    # 9
    {"a", "b", "c", "d", "f", "g"},
]


def segments_counter(pattern):
    counter = {letter: 0 for letter in letters}
    for digit in pattern:
        for segment in list(digit):
            counter[segment] += 1
    return counter


def find_mapping(pattern):
    segments_converter = {}

    given_segments_counter = segments_counter(pattern)
    original_segments_counter = segments_counter(digits)

    for segment, count in given_segments_counter.items():
        for original_segment, original_count in original_segments_counter.items():
            if count == original_count and count != 7 and count != 8:
                segments_converter[segment] = original_segment

    for digit in sorted(pattern, key=len):
        if len(digit) == 2:
            for segment in digit:
                if segment not in segments_converter:
                    segments_converter[segment] = "c"
        elif len(digit) == 3:
            for segment in digit:
                if segment not in segments_converter:
                    segments_converter[segment] = "a"
        elif len(digit) == 4:
            for segment in digit:
                if segment not in segments_converter:
                    segments_converter[segment] = "d"
        elif len(digit) == 7:
            for segment in digit:
                if segment not in segments_converter:
                    segments_converter[segment] = "g"

    return segments_converter


result = 0
for line in data:
    pattern, output = line
    mapping = find_mapping(pattern)
    current_result = 0
    for idx, digit in enumerate(output):
        digit_conversion = {mapping[segment] for segment in digit}
        for original_digit, segments in enumerate(digits):
            if digit_conversion == segments:
                current_result += original_digit * 10**(3-idx)
    result += current_result
print("Solution for part 2:", result)
