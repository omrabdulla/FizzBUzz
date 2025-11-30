"""
Core implementation of the FizzBuzz test.
Separated into pure functions for clarity, testability, and reuse.
"""

from typing import List


def fizzbuzz_value(n: int) -> str:
    """
    Return the FizzBuzz representation of a single integer.

    - Multiples of 3 -> "Fizz"
    - Multiples of 5 -> "Buzz"
    - Multiples of 3 and 5 -> "FizzBuzz"
    - Otherwise -> the number as a string.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


def fizzbuzz_sequence(start: int = 1, end: int = 100) -> List[str]:
    """
    Generate the FizzBuzz sequence from start to end (inclusive).

    Parameters
    ----------
    start : int
        Starting integer for the sequence.
    end : int
        Ending integer for the sequence (inclusive).

    Returns
    -------
    List[str]
        List of FizzBuzz values for the range [start, end].
    """
    if start > end:
        raise ValueError("start must be <= end")

    return [fizzbuzz_value(n) for n in range(start, end + 1)]


def main() -> None:
    """
    Entry point: print the FizzBuzz sequence from 1 to 100 to stdout.
    """
    for value in fizzbuzz_sequence(1, 100):  
        print(value)


if __name__ == "__main__":
    main()
