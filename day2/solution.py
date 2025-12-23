from dataclasses import dataclass
from pathlib import Path

from rich import inspect, print

Data = list[tuple[int, int]]


def read_input(test: bool = False) -> Data:
    file_name = "test_input.txt" if test else "input.txt"
    path = Path(__file__).parent.joinpath(file_name)
    with path.open() as f:
        line = f.readline()
        ranges = line.split(",")
        return [
            (int(start), int(end))
            for start, end in (range.split("-") for range in ranges)
        ]


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
