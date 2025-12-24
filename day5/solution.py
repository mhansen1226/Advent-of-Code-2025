from dataclasses import dataclass
from pathlib import Path
from typing import Self

from rich import print

Data = tuple


@dataclass
class Range:
    start: int
    stop: int

    def __contains__(self, x: int) -> bool:
        return self.start <= x <= self.stop


class RangeList:
    def __init__(self, ranges: list[Range] | None = None):
        self.ranges: list[Range] = ranges or []
        self.merge()

    def __str__(self) -> str:
        return ", ".join(str(range) for range in self.ranges)

    def __contains__(self, x: int) -> bool:
        for range in self.ranges:
            if x in range:
                return True
        return False

    def __add__(self, other: Range):
        self.ranges.append(other)
        self.merge()

    def merge(self):
        self.ranges.sort(key=lambda x: x.start)
        merged = [self.ranges[0]]
        for current in self.ranges[1:]:
            previous = merged[-1]
            if current.start <= previous.stop:
                previous.stop = max(previous.stop, current.stop)
            else:
                merged.append(current)
        self.ranges = merged


def read_input(test: bool = False) -> Data:
    file_name = "test_input.txt" if test else "input.txt"
    path = Path(__file__).parent.joinpath(file_name)
    with path.open() as f:
        data = f.read().split("\n\n")
        ranges = parse_ranges(data[0].strip())
        ids = parse_ids(data[1].strip())
    return ranges, ids


def parse_ranges(data: str) -> RangeList:
    lines = data.split("\n")
    ranges = []
    for line in lines:
        start, end = line.split("-")
        ranges.append(Range(int(start), int(end)))
    return RangeList(ranges)


def parse_ids(data: str):
    lines = data.split("\n")
    return [int(line) for line in lines]


def part1(ranges: RangeList, ids: list[int]):
    return sum(id in ranges for id in ids)


def part2(ranges: RangeList, ids: list[int]):
    pass


def main() -> None:
    ranges, ids = read_input()
    print(f"Part 1: {part1(ranges, ids)}")
    print(f"Part 2: {part2(ranges, ids)}")


if __name__ == "__main__":
    main()
