from dataclasses import dataclass
from pathlib import Path

from rich import print


@dataclass
class Dial:
    position: int = 50

    def rotate(self, instruction: str) -> int:
        direction, steps = instruction[0], int(instruction[1:])
        start_at_zero = self.position == 0
        zeros = steps // 100
        steps %= 100
        if direction == "L":
            self.position = self.position - steps
        elif direction == "R":
            self.position = self.position + steps
        zeros += (self.position <= 0 and not start_at_zero) or self.position >= 100
        self.position %= 100
        return zeros


def read_input(test: bool = False) -> list[str]:
    file_name = "test_input.txt" if test else "input.txt"
    path = Path(__file__).parent.joinpath(file_name)
    with path.open() as f:
        return [line.strip() for line in f.readlines()]


def part1(moves: list[str]):
    dial = Dial()
    count_zeros = 0
    for move in moves:
        dial.rotate(move)
        if dial.position == 0:
            count_zeros += 1
    return count_zeros


def part2(moves: list[str]):
    dial = Dial()
    count_zeros = 0
    for move in moves:
        zeros = dial.rotate(move)
        count_zeros += zeros
    return count_zeros


def main() -> None:
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
