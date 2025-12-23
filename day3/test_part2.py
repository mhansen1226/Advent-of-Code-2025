import pytest
from solution import largest_joltage, part2, read_input

DATA = read_input(test=True)


@pytest.mark.parametrize(
    "input, output",
    [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ],
)
def test_cases(input, output):
    assert largest_joltage(input, 12) == output


def test_part2():
    assert part2(DATA) == 3121910778619
