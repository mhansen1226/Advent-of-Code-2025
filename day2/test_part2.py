import pytest
from solution import find_invalid_ids, is_invalid_id2, part2, read_input

DATA = read_input(test=True)


@pytest.mark.parametrize(
    "input, output",
    [
        (12341234, True),
        (123123123, True),
        (1212121212, True),
        (1111111, True),
        (111, True),
    ],
)
def test_is_invalid_id2(input, output):
    assert is_invalid_id2(input) == output


@pytest.mark.parametrize(
    "start, end, output",
    [
        (11, 22, [11, 22]),
        (95, 115, [99, 111]),
        (998, 1012, [999, 1010]),
        (1188511880, 1188511890, [1188511885]),
        (222220, 222224, [222222]),
        (1698522, 1698528, []),
        (446443, 446449, [446446]),
        (38593856, 38593862, [38593859]),
        (565653, 565659, [565656]),
        (824824821, 824824827, [824824824]),
        (2121212118, 2121212124, [2121212121]),
    ],
)
def test_cases(start, end, output):
    assert find_invalid_ids(start, end, is_invalid_id2) == output


def test_part2():
    assert part2(DATA) == 4174379265
