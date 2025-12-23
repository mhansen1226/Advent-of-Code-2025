from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from rich import inspect, print

Data = list[str]


def concat_ints(arr: Iterable[int]):
    return int("".join([str(x) for x in arr]))


def read_input(test: bool = False) -> Data:
    file_name = "test_input.txt" if test else "input.txt"
    path = Path(__file__).parent.joinpath(file_name)
    with path.open() as f:
        return [line.strip() for line in f.readlines()]


def largest_joltage(bank: str, n: int) -> int:
    values = [int(x) for x in bank]
    maxs = []
    left = 0
    for i in range(n - 1, -1, -1):
        right = -i
        values_subset = values[left:right] if right < 0 else values[left:]
        maxs.append(max(values_subset))
        left += values_subset.index(maxs[-1]) + 1
    return concat_ints(maxs)


def part1(data: Data):
    return sum(largest_joltage(bank, 2) for bank in data)


def part2(data: Data):
    return sum(largest_joltage(bank, 12) for bank in data)


def main() -> None:
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
