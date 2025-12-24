from solution import part1, read_input

RANGES, IDS = read_input(test=True)


def test_part1():
    assert part1(RANGES, IDS) == 3
