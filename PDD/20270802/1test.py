import subprocess
import sys


SOLUTION_FILE = "1.py"


def run_solution(s, timeout=3):
    test_input = f"{len(s)}\n{s}\n"

    result = subprocess.run(
        [sys.executable, SOLUTION_FILE],
        input=test_input,
        text=True,
        capture_output=True,
        timeout=timeout,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"Runtime error for input {s!r}:\n"
            f"{result.stderr}"
        )

    output = result.stdout.strip()

    try:
        return int(output)
    except ValueError:
        raise AssertionError(
            f"Expected one integer, but received {output!r}"
        )


def check_test(name, s, expected, timeout=3):
    actual = run_solution(s, timeout)

    if actual != expected:
        print(f"FAILED: {name}")
        print(f"Input length: {len(s)}")

        if len(s) <= 100:
            print(f"String: {s}")

        print(f"Expected: {expected}")
        print(f"Actual:   {actual}")
        raise SystemExit(1)

    print(f"PASSED: {name}")


fixed_tests = [
    ("single A", "A", 0),
    ("single B", "B", 0),
    ("two balanced AB", "AB", 2),
    ("two balanced BA", "BA", 2),
    ("two A", "AA", 0),
    ("two B", "BB", 0),
    ("odd alternating", "ABA", 2),
    ("full balanced blocks", "AABB", 4),
    ("full balanced mixed", "ABBA", 4),
    ("all A", "AAAAA", 0),
    ("balanced internal section", "AAAABB", 4),
    ("only one pair", "AAAAAB", 2),
    ("alternating odd length", "ABABABA", 6),
    ("full balanced complex", "BBAAABAB", 8),
    ("internal length four", "AAAABBAA", 4),
    ("internal length six", "AAAABBBA", 6),
    ("full balanced length ten", "AABABBABBA", 10),
    ("best prefix length ten", "AAAAABBBBBA", 10),
    ("best prefix complex", "BBBBAAABAAAA", 10),
]


stress_tests = [
    (
        "maximum all A",
        "A" * 200_000,
        0,
    ),
    (
        "maximum balanced blocks",
        "A" * 100_000 + "B" * 100_000,
        200_000,
    ),
    (
        "maximum alternating",
        "AB" * 100_000,
        200_000,
    ),
    (
        "maximum unbalanced by two",
        "A" * 100_001 + "B" * 99_999,
        199_998,
    ),
    (
        "maximum with one B",
        "A" * 199_999 + "B",
        2,
    ),
]


def main():
    print("Running fixed tests...\n")

    for name, s, expected in fixed_tests:
        check_test(name, s, expected)

    print("\nRunning stress tests...\n")

    for name, s, expected in stress_tests:
        check_test(name, s, expected, timeout=5)

    print("\nAll tests passed!")


if __name__ == "__main__":
    main()