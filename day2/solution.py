from pathlib import Path

from rich import print

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


def find_invalid_ids(start, end, method) -> list[int]:
    return [id for id in range(start, end + 1) if method(id)]


def is_invalid_id1(id: int) -> bool:
    string = str(id)
    length = len(string)
    if length <= 1:
        return False
    if length % 2 == 1:
        return False
    return string[0 : length // 2] == string[length // 2 :]


def divide_string(s: str, n: int) -> list[str]:
    return [s[i : i + n] for i in range(0, len(s), n)]


def is_invalid_id2(id: int) -> bool:
    if is_invalid_id1(id):
        return True
    string = str(id)
    length = len(string)
    result = False
    for substring_length in range(1, length // 2 + 1):
        if length % substring_length != 0:
            continue
        substrings = divide_string(string, substring_length)
        result = result or all(substrings[0] == s for s in substrings[1:])
        if result:
            return True
    return False


def part1(data: Data):
    total = 0
    for start, end in data:
        total += sum(find_invalid_ids(start, end, is_invalid_id1))
    return total


def part2(data: Data):
    total = 0
    for start, end in data:
        total += sum(find_invalid_ids(start, end, is_invalid_id2))
    return total


def main() -> None:
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
