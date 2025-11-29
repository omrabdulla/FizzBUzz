# FizzBuzz Pipeline – Technical Test

This repository contains my solution to the Mars **FizzBuzz Pipeline Technical Test**.

I approached the task the same way I would approach a small slice of production code:  
A focus on **clarity**, **testability**, **modularity**, and **basic CI automation**, while staying  within the **two-hour timebox**.

---

## Project Structure
```
├── .github/
│ └── workflows/
│   └── ci.yml/ # yaml file with code for the pipeline
├── src/
│ └── fizzbuzz/
│ ├── init.py
│ └── fizzbuzz.py # Core implementation
├── tests/
│ └── test_fizzbuzz.py # Unit tests (parametrised + edge cases)
├── .gitignore # gitignore to pevent pushing uneeded files
├── backlog_refienment.txt # What I would do with more time
├── Makefile # Convenience commands: run, test, lint, install
├── README.md # Project documentation
├── requirements.txt # Python dependencies
```

The project uses a **src/ layout**, which mirrors how real Python services and libraries are structured.

---

## Running the Project

### Run the FizzBuzz script

### Example output:

```

1
2
Fizz # 3
4
Buzz # 5
Fizz # 6
...
Buzz # 100
```
---

## Running Tests

The project uses **pytest**.

*Run all tests:*

make test

Tests include:

- parametrised tests for `fizzbuzz_value`
- tests for default and custom ranges
- input validation (raising `ValueError`)
- single-value edge case

---

## Linting & Syntax Check

A lightweight syntax check using Python’s built-in compiler:

make lint

This catches basic syntax issues without adding heavy tooling.

---

## Installation

Install dependencies:

make install

---

## Design & Engineering Decisions

### Separation of Concerns
- `fizzbuzz_value` handles the rule for a single number  
- `fizzbuzz_sequence` handles iteration and input validation  
- `main()` handles I/O  
- The core logic remains pure, deterministic, and easy to test

### Safe Imports (No Side Effects)
The script uses:

```python
if __name__ == "__main__":
    main()
```


**This ensures:**

Running python fizzbuzz.py → executes the script

importing fizzbuzz in tests or other modules → does not auto-run the script

This prevents side effects and makes the module safe to reuse.

**Testability First**

All core logic sits inside small pure functions, making unit tests simple and comprehensive.

**Production-Style Structure**

Using a src/ folder and modular functions mirrors common patterns in data engineering and backend applications.

**Lightweight CI**

A minimal GitHub Actions workflow:

checks out source
sets up Python 3.11
installs dependencies
runs lint/smoke test
runs pytest

This keeps code quality high while staying within the timebox.

