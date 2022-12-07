"""AoC {day}, {year}: {puzzle_name}."""


from aoc_2022.helpers import load_day_input

import pathlib


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str, parent: "Directory") -> None:
        self.name = name
        self.directories: list[Directory] = []
        self.files: list[File] = []
        self.parent: Directory = parent
        self.size = 0

    def get_size_list(self) -> list[int]:
        subdirs_sizes = []
        for d in self.directories:
            subdirs_sizes.extend(d.get_size_list())

        files_sizes = []
        for f in self.files:
            files_sizes += [f.size]

        self.size = sum(subdirs_sizes) + sum(files_sizes)

        return [self.size] + subdirs_sizes


def parse_data(puzzle_input: list[str]) -> list[str]:
    """Parse input."""
    return [row.strip("\n") for row in puzzle_input]


def parse_commands(commands: list[str]):
    root = Directory("/", None)
    current_node = root
    for command in commands:
        match command.split():
            case ["$", "cd", "/"]:
                current_node = root
            case ["$", "cd", ".."]:
                current_node = current_node.parent
            case ["$", "cd", directory_name]:
                current_node = next(
                    d for d in current_node.directories if d.name == directory_name
                )
            case ["$", "ls"]:
                pass
            case ["dir", directory_name]:
                current_node.directories.append(Directory(directory_name, current_node))
            case [size, file_name]:
                current_node.files.append(File(file_name, int(size)))
    return root


def part1(data: list[str]) -> int:
    """Solve part 1."""
    root = parse_commands(data)
    sizes = root.get_size_list()
    low_sizes = [size for size in sizes if size <= 100000]
    res = sum(low_sizes)
    return res


def part2(data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(load_day_input(pathlib.Path(__file__).parent / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples)))

    solutions = solve(load_day_input(pathlib.Path(__file__).parent / "input.txt"))
    print(
        "Solutions:\n\t{}".format("\n\t".join(str(solution) for solution in solutions))
    )
