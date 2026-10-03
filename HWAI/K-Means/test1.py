import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


def load_solution():
    """Load functions from 1.py without calling main()."""
    return runpy.run_path(str(SOLUTION_FILE))


def run_solution(test_input, monkeypatch, capsys):
    """Run 1.py with fake terminal input and return its output."""
    fake_input = io.TextIOWrapper(io.BytesIO(test_input.encode()))
    monkeypatch.setattr(sys, "stdin", fake_input)

    # Run in this process so VS Code breakpoints in 1.py work.
    runpy.run_path(str(SOLUTION_FILE), run_name="__main__")

    return capsys.readouterr().out.strip()


def test_identical_boxes_have_zero_distance():
    solution = load_solution()
    distance = solution["d_distance"]((20, 30), (20, 30))

    assert distance == pytest.approx(0.0)


def test_iou_distance_for_nested_boxes():
    solution = load_solution()
    distance = solution["d_distance"]((10, 10), (20, 20))

    # IoU is 100 / 400 = 0.25, so distance is 1 - 0.25 = 0.75.
    assert distance == pytest.approx(0.75)


def test_sample1(monkeypatch, capsys):
    test_input = """\
12 4 20
12 23
34 21
43 23
199 23
34 23
108 12
200 107
12 78
123 110
34 23
56 48
78 66
"""

    expected_output = """\
133 94
121 27
36 22
12 50
"""

    actual_output = run_solution(test_input, monkeypatch, capsys)
    assert actual_output == expected_output.strip()


def test_sample2(monkeypatch, capsys):
    test_input = """\
12 3 10
12 23
34 21
43 23
199 23
34 23
108 12
200 107
12 78
123 110
34 23
56 48
78 66
"""

    expected_output = """\
150 76
51 25
12 50
"""

    actual_output = run_solution(test_input, monkeypatch, capsys)
    assert actual_output == expected_output.strip()
