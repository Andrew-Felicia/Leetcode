import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


def run_solution(test_input, monkeypatch, capsys):
    """Run 1.py with fake input and return its output."""

    fake_input = io.TextIOWrapper(
        io.BytesIO(test_input.encode())
    )

    monkeypatch.setattr(sys, "stdin", fake_input)

    # Run 1.py like a normal program
    runpy.run_path(
        str(SOLUTION_FILE),
        run_name="__main__"
    )

    return capsys.readouterr().out.strip()


def test_sample1(monkeypatch, capsys):
    test_input = """\
2 5 2
0 2.5 1 2 -1
-1 -1 -1 -1 1
1 5.0 3 4 -1
-1 -1 -1 -1 2
-1 -1 -1 -1 3
1.2 3.4
5.6 6.0
"""

    expected_output = """\
1
3
"""

    actual_output = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual_output == expected_output.strip()


def test_sample2(monkeypatch, capsys):
    test_input = """\
3 9 2
0 6.1 1 2 -1
2 7.0 3 4 -1
1 6.5 5 6 -1
-1 -1 -1 -1 1
1 10.3 7 8 -1
-1 -1 -1 -1 5
-1 -1 -1 -1 6
-1 -1 -1 -1 3
-1 -1 -1 -1 4
3.2 9.2 6.2
6.3 3.2 12.0
"""

    expected_output = """\
1
5
"""

    actual_output = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual_output == expected_output.strip()


def test_value_equal_to_threshold_goes_left(
    monkeypatch,
    capsys
):
    test_input = """\
1 3 2
0 2.5 1 2 -1
-1 -1 -1 -1 7
-1 -1 -1 -1 9
2.5
2.5001
"""

    expected_output = """\
7
9
"""

    actual_output = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual_output == expected_output.strip()


def test_root_is_leaf(monkeypatch, capsys):
    test_input = """\
2 1 2
-1 -1 -1 -1 4
1.0 2.0
10.0 20.0
"""

    expected_output = """\
4
4
"""

    actual_output = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual_output == expected_output.strip()