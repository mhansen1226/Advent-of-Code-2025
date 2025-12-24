from solution import part1, read_input

NUMS, OPERATIONS = read_input(test=True)


def test_part1():
    assert part1(NUMS, OPERATIONS) == 4277556
