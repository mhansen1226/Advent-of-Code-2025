from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from rich import print
from scipy.signal import convolve2d


@dataclass
class Map:
    data: np.ndarray

    def __post_init__(self):
        self.calculate_neighbors()

    def __rich__(self) -> str:
        return str(self.data)

    def plot(self):
        rows, cols = np.where(self.data)
        plt.scatter(cols, rows, c="black")
        plt.imshow(self.neighbors)
        plt.colorbar()
        plt.show()

    def calculate_neighbors(self):
        kernel = np.ones((3, 3))
        kernel[1, 1] = 0
        self.neighbors = convolve2d(self.data, kernel, mode="same")

    def accessible_rolls(self, n: int = 4):
        return np.where(self.data, self.neighbors < n, False)

    def remove_and_update(self):
        self.data[self.accessible_rolls()] = False
        self.calculate_neighbors()


def read_input(test: bool = False) -> Map:
    file_name = "test_input.txt" if test else "input.txt"
    path = Path(__file__).parent.joinpath(file_name)
    with path.open() as f:
        data = [[tp == "@" for tp in line.strip()] for line in f.readlines()]
    return Map(np.array(data))


def part1(map: Map) -> int:
    return np.sum(map.accessible_rolls())


def part2(map: Map):
    total = 0
    removable = np.sum(map.accessible_rolls())
    while removable > 0:
        total += removable
        map.remove_and_update()
        removable = np.sum(map.accessible_rolls())
    return total


def main() -> None:
    map = read_input()
    print(f"Part 1: {part1(map)}")
    print(f"Part 2: {part2(map)}")


if __name__ == "__main__":
    main()
