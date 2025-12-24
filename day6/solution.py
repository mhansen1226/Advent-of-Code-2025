from pathlib import Path

import numpy as np
from rich import print

Data = tuple[np.ndarray, list[str]]


def read_input(test: bool = False) -> Data:
    file_name = "test_input.txt" if test else "input.txt"
    path = Path(__file__).parent.joinpath(file_name)
    with path.open() as f:
        data = [line.strip().split() for line in f.readlines()]
    nums = []
    for line in data[:-1]:
        nums.append([int(num) for num in line])
    nums = np.array(nums).T
    operations = data[-1]
    return nums, operations


def do_operation(nums: np.ndarray, operation: str):
    if operation == "+":
        return nums.sum()
    if operation == "*":
        return nums.prod()
    raise ValueError(f"Unknown operation: {operation}")


def part1(nums: np.ndarray, operations: list[str]):
    return sum(do_operation(ns, op) for ns, op in zip(nums, operations))


def part2(nums: np.ndarray, operations: list[str]):
    pass


def main() -> None:
    nums, operations = read_input()
    print(f"Part 1: {part1(nums, operations)}")
    print(f"Part 2: {part2(nums, operations)}")


if __name__ == "__main__":
    main()
