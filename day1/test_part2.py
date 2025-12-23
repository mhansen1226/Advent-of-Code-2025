from solution import part2, read_input

DATA = read_input(test=True)


def test_part2():
    assert part2(DATA) == 6


def test_start_at_zero():
    assert part2(["L50", "R301"]) == 4
