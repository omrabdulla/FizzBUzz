import os
import sys

# Add the 'src' directory to Python path so 'fizzbuzz' can be imported
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_PATH = os.path.join(PROJECT_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from fizzbuzz.fizzbuzz import fizzbuzz_value, fizzbuzz_sequence
import pytest


@pytest.mark.parametrize(
    "n,expected",
    [
        (1, "1"),
        (2, "2"),
        (3, "Fizz"),
        (5, "Buzz"),
        (6, "Fizz"),
        (10, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
    ],
)
def test_fizzbuzz_value_basic_cases(n, expected):
    assert fizzbuzz_value(n) == expected


def test_fizzbuzz_sequence_default_range():
    seq = fizzbuzz_sequence()
    assert len(seq) == 100
    assert seq[0] == "1"       # index 0 corresponds to number 1
    assert seq[-1] == "Buzz"   # 100 is a multiple of 5 only


def test_fizzbuzz_sequence_custom_range():
    seq = fizzbuzz_sequence(1, 15)
    # Spot-check a few key positions
    assert seq[2] == "Fizz"      # 3
    assert seq[4] == "Buzz"      # 5
    assert seq[14] == "FizzBuzz" # 15


def test_fizzbuzz_sequence_invalid_range():
    with pytest.raises(ValueError):
        fizzbuzz_sequence(10, 1)
