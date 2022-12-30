"""Utilities for AoC 2022.

This module will be dedicated to 2022 edition.
"""

def get_input(path: str) -> list[str]:
    """Get input."""
    with open(path) as f:
        data = f.readlines()
    return data


def parse_data(puzzle_input: list[str]) -> list[str]:
    """Parse input."""
    return [row.strip("\n") for row in puzzle_input]
