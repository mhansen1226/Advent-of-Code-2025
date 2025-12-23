import pytest
from solution import find_invalid_ids, is_invalid_id1, part1, read_input

DATA = read_input(test=True)


@pytest.mark.parametrize(
    "input, output",
    [
        (9, False),
        (55, True),
        (6464, True),
        (101, False),
        (123123, True),
    ],
)
def test_is_invalid_id1(input, output):
    assert is_invalid_id1(input) == output


@pytest.mark.parametrize(
    "start, end, output",
    [
        (11, 22, [11, 22]),
        (95, 115, [99]),
        (998, 1012, [1010]),
        (1188511880, 1188511890, [1188511885]),
        (222220, 222224, [222222]),
        (1698522, 1698528, []),
        (446443, 446449, [446446]),
        (38593856, 38593862, [38593859]),
    ],
)
def test_cases(start, end, output):
    assert find_invalid_ids(start, end, is_invalid_id1) == output


def test_part1():
    assert part1(DATA) == 1227775554
