import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


def run_solution(test_input, monkeypatch, capsys):
    """Run 1.py with the given input and return its output."""

    fake_stdin = io.TextIOWrapper(
        io.BytesIO(test_input.encode())
    )
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    runpy.run_path(
        str(SOLUTION_FILE),
        run_name="__main__"
    )

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        # Sample 1: normal multiclass case
        (
            """\
0 0 1 1 1 2 2 2 2
0 0 0 1 2 0 2 2 2
0.3 0.3 0.4
""",
            "0.70 0.75 0.65",
        ),

        # Sample 2: class 2 does not appear
        (
            """\
0 0 1 1
0 0 1 1
0.4 0.4 0.2
""",
            "0.80 0.80 0.80",
        ),

        # Sample 3: only one class and one sample
        (
            """\
0
0
1.0
""",
            "1.00 1.00 1.00",
        ),

        # Every prediction is wrong
        (
            """\
0 1
1 0
0.5 0.5
""",
            "0.00 0.00 0.00",
        ),

        # All predictions are correct
        (
            """\
0 1 2 0 1 2
0 1 2 0 1 2
0.2 0.3 0.5
""",
            "1.00 1.00 1.00",
        ),

        # Only one prediction is correct
        (
            """\
0 0 0
0 1 1
0.5 0.5
""",
            "0.17 0.50 0.25",
        ),
    ],
)
def test_classification_metrics(
    test_input,
    expected,
    monkeypatch,
    capsys
):
    assert run_solution(
        test_input,
        monkeypatch,
        capsys
    ) == expected