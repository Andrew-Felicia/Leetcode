import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("2.py")


def run_solution(test_input, monkeypatch, capsys):
    fake_stdin = io.TextIOWrapper(io.BytesIO(test_input.encode()))
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    runpy.run_path(str(SOLUTION_FILE), run_name="__main__")

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        # Official sample 1: all four NPU groups are allowed.
        (
            """\
8 4 4 2
0.5 0.01 0.09 0.023 0.027 0.05 0.1 0.2
""",
            "0 7",
        ),

        # Official sample 2: p cannot exceed the NPU count m.
        (
            """\
8 4 5 2
0.3 0.04 0.06 0.45 0.05 0.01 0.03 0.06
""",
            "error",
        ),

        # n cannot be evenly split across m NPUs.
        (
            """\
5 2 1 1
0.1 0.2 0.3 0.4 0.5
""",
            "error",
        ),

        # Select only the best two groups, then select experts from them.
        # Groups:
        # [0, 1] -> max 0.80
        # [2, 3] -> max 0.60
        # [4, 5] -> max 0.90
        # [6, 7] -> max 0.50
        # Keep groups [0, 1] and [4, 5]; select experts 4 and 0.
        (
            """\
8 4 2 2
0.8 0.7 0.6 0.1 0.9 0.2 0.5 0.4
""",
            "0 4",
        ),

        # k equals the number of experts available on the selected NPU.
        (
            """\
6 3 1 2
0.2 0.1 0.9 0.4 0.8 0.3
""",
            "2 3",
        ),

        # One selected NPU has only two experts, so it cannot provide k=3.
        (
            """\
8 4 1 3
0.1 0.2 0.9 0.8 0.3 0.4 0.5 0.6
""",
            "error",
        ),
    ],
)
def test_device_limited_routing(test_input, expected, monkeypatch, capsys):
    assert run_solution(test_input, monkeypatch, capsys) == expected