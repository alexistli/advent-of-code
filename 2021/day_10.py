"""
[({(<(())[]>[[{[]{<()<>>    < incomplete
[(()[<>])]({[<{<<[]>>(      < incomplete
{([(<{}[<>[]}>{[]{[(<()>        < corrupted
(((({<>}<{<{<>}{[]{[]{}     < incomplete
[[<[([]))<([[{}[[()]]]          < corrupted
[{[{({}]{}}([{[{{{}}([]         < corrupted
{<[[]]>}<{[{[{[]{()[[[]     < incomplete
[<(<(<(<{}))><([]([]()          < corrupted
<{([([[(<>()){}]>(<<{{          < corrupted
<{([{{}}[<[[[<>{}]]]>[]]    < incomplete

"""

OPENING_CHARACTERS = '({[<'
CLOSING_CHARACTERS = ')}]>'
CHARACTERS_PAIRS = {opening: closing for opening, closing in zip(OPENING_CHARACTERS, CLOSING_CHARACTERS)}
SYNTAX_CHECKER_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}


with open('inputs/day_10.txt', mode='r') as f:
    data = [line.strip() for line in f.readlines()]


# ================ Part 1 ================
"""We iterate through the each line and stack characters in a list.
When a closing character meets its equivalent opening character then they cancel each other.
Sequence is corrupted if a closing character is stacked without meeting its opening character.
Sequence is incomplete if at the end it is not corrupted and there is remaining characters is the stack."""

corrupted = []
incomplete = []
first_incorrect_closing = []
for line in data:
    stack = list(line[0])
    for character in line[1:]:
        if character in OPENING_CHARACTERS:
            stack.append(character)
        elif character == CHARACTERS_PAIRS[stack[-1]]:
            stack.pop()
        else:
            first_incorrect_closing.append(character)
            corrupted.append(line)
            break
    if line not in corrupted:
        incomplete.append(line)

total_points = sum(SYNTAX_CHECKER_POINTS[character] for character in first_incorrect_closing)
print("Solution for part 1:", total_points)


# ================ Part 2 ================

AUTOCOMPLETE_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}

scores = []
for line in incomplete:
    stack = list(line[0])
    # Process line
    for character in line[1:]:
        if character in OPENING_CHARACTERS:
            stack.append(character)
        elif character == CHARACTERS_PAIRS[stack[-1]]:
            stack.pop()
    # Process the characters needing completion
    line_score = 0
    for character in reversed(stack):
        matching_character = CHARACTERS_PAIRS[character]
        line_score = line_score * 5 + AUTOCOMPLETE_POINTS[matching_character]
    scores.append(line_score)

scores.sort()
middle_score = scores[len(scores) // 2]
print("Solution for part 2:", middle_score)
