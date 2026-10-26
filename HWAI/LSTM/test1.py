import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


def run_solution(test_input, monkeypatch, capsys):
    fake_stdin = io.TextIOWrapper(
        io.BytesIO(test_input.encode())
    )
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    runpy.run_path(
        str(SOLUTION_FILE),
        run_name="__main__",
    )

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        # Official example: seq_len = 3.
        (
            "3 4 1 2 3 4 5 6 7 8 9 10 11 12\n",
            "0.231 0.122 0.062",
        ),

        # A single time step.
        (
            "1 2 100 -999\n",
            "0.231",
        ),

        # Different x_dim and input values do not change the result.
        (
            "4 1 9 8 7 6\n",
            "0.231 0.122 0.062 0.031",
        ),

        # Later values become 0.0 after rounding to three decimals.
        (
            "12 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
            "0.231 0.122 0.062 0.031 0.016 0.008 0.004 0.002 0.001 0.0 0.0 0.0",
        ),
    ],
)
def test_simplified_lstm(test_input, expected, monkeypatch, capsys):
    assert run_solution(
        test_input,
        monkeypatch,
        capsys,
    ) == expected