import pytest
from solution import largest_joltage, part1, read_input

DATA = read_input(test=True)


@pytest.mark.parametrize(
    "input, output",
    [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ],
)
def test_casts(input, output):
    assert largest_joltage(input) == output


def test_part1():
    assert part1(DATA) == 357
