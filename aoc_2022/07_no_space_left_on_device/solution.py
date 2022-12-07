"""AoC 7, 2022: No Space Left On Device."""


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
        self.subdirs_sizes = []

    def add_file(self, file: File) -> None:
        if file not in self:
            self.files.append(file)

    def add_directory(self, directory: "Directory"):
        if directory not in self:
            self.directories.append(directory)

    def compute_size(self):
        subdirs_sizes = sum([d.compute_size() for d in self.directories])
        files_size = sum([f.size for f in self.files])
        self.size = subdirs_sizes + files_size
        return self.size

    def __contains__(self, obj):
        if isinstance(obj, File):
            for file in self.files:
                if obj.name == file.name:
                    print("true")
                    return True
        if isinstance(obj, Directory):
            for directory in self.directories:
                if obj.name == directory.name:
                    print("true")
                    return True
        return False


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
                current_node = current_node.parent or root
            case ["$", "cd", directory_name]:
                current_node = next(
                    d for d in current_node.directories if d.name == directory_name
                )
            case ["$", "ls"]:
                pass
            case ["dir", directory_name]:
                current_node.add_directory(Directory(directory_name, current_node))
            case [size, file_name]:
                current_node.add_file(File(file_name, int(size)))
    return root


def get_all_directories_sizes(root: Directory, directory_sizes: list) -> None:
    for directory in root.directories:
        directory_sizes.append(directory.size)
        get_all_directories_sizes(directory, directory_sizes)


def part1(data: list[str]) -> int:
    """Solve part 1."""
    root = parse_commands(data)
    root.compute_size()
    directory_sizes = []
    get_all_directories_sizes(root, directory_sizes)
    low_sizes = [size for size in directory_sizes if size <= 100000]
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
