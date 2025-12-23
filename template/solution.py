from dataclasses import dataclass
from pathlib import Path

from rich import print

Data = list[str]


def read_input(test: bool = False) -> Data:
    file_name = "test_input.txt" if test else "input.txt"
    path = Path(__file__).parent.joinpath(file_name)
    with path.open() as f:
        return [line.strip() for line in f.readlines()]


def part1(data: Data):
    pass


def part2(data: Data):
    pass


def main() -> None:
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
