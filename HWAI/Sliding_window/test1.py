import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


def run_solution(test_input, monkeypatch, capsys):
    """Run 1.py with test_input and return its printed output."""
    fake_stdin = io.TextIOWrapper(io.BytesIO(test_input.encode()))
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    runpy.run_path(str(SOLUTION_FILE), run_name="__main__")

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    "text, expected",
    [
        # Four examples from the problem.
        ("abcabcbb", "3"),
        ("aaaa", "1"),
        ("z", "1"),
        ("A1b2A3", "5"),

        # The left side of the current window must never move backward.
        ("abba", "2"),

        # A repeated character can start a new, longer window.
        ("dvdf", "3"),
        ("pwwkew", "3"),

        # Uppercase and lowercase letters are different characters.
        ("aA1a", "3"),

        # All 62 permitted ASCII letters and digits are distinct.
        (
            "0123456789"
            "abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "62",
        ),

        # The best substring occurs after the repeated character.
        ("abcdeafghij", "10"),
    ],
)
def test_longest_unique_substring(text, expected, monkeypatch, capsys):
    assert run_solution(
        text + "\n",
        monkeypatch,
        capsys,
    ) == expected


def test_large_input(monkeypatch, capsys):
    """Check that the implementation can process a reasonably large input."""
    alphabet = (
        "0123456789"
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    text = alphabet * 2_000

    assert run_solution(
        text + "\n",
        monkeypatch,
        capsys,
    ) == "62"