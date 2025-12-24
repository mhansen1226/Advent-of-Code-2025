from pathlib import Path

from rich import print

Data = tuple[list[list[int]], list[str]]


def read_input(test: bool = False) -> Data:
    file_name = "test_input.txt" if test else "input.txt"
    path = Path(__file__).parent.joinpath(file_name)
    with path.open() as f:
        data = [line.strip().split() for line in f.readlines()]
    nums: list[list[int]] = []
    for line in data[:-1]:
        nums.append([int(num) for num in line])
    operations = data[-1]
    return nums, operations


def part1(nums: list[list[int]], operations: list[str]):
    pass


def part2(nums: list[list[int]], operations: list[str]):
    pass


def main() -> None:
    nums, operations = read_input()
    print(f"Part 1: {part1(nums, operations)}")
    print(f"Part 2: {part2(nums, operations)}")


if __name__ == "__main__":
    main()
