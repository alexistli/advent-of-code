"""Utilities for AoC 2022."""

import pathlib


def get_input(path: pathlib.Path) -> list[str]:
    """Get input."""
    with open(path) as f:
        data = f.readlines()
    return data


def parse_data(puzzle_input: list[str]) -> list[str]:
    """Parse input."""
    return [row.strip("\n") for row in puzzle_input]


def parse_ints(input: list[str]) -> list[int]:
    """Parse integers in a list/tuple of strings."""
    if not isinstance(input, (list, tuple)):
        raise TypeError("Unexpected type for input: %s. Type must be string or tuple.", type(input))
    return [int(s) for s in input]
