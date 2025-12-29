import pytest
from parse import split_add_zeros


@pytest.mark.parametrize(
    "input,output",
    [
        ("123 456", ["123", "456"]),
        ("123  456", ["1230", "456"]),
        ("123   456", ["12300", "456"]),
        ("123   456  789", ["12300", "4560", "789"]),
    ],
)
def test_split_add_zeros(input: str, output: list[str]):
    assert split_add_zeros(input) == output
