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
        # Official sample 1
        (
            """\
3 20 1000
0.11 0.79 0.68 0.97
1.0 0.8 0.13 0.33
0.27 0.02 0.5 0.46
0.83 0.29 0.23 0.75
0.97 0.08 0.84 0.55
0.29 0.71 0.17 0.83
0.03 0.6 0.88 0.28
0.24 0.26 0.82 0.03
0.96 0.12 0.82 0.36
0.13 0.12 0.86 0.44
0.23 0.7 0.35 0.06
0.42 0.49 0.67 0.84
0.8 0.49 0.47 0.7
0.68 0.03 0.11 0.07
0.77 0.19 0.95 0.44
0.25 0.12 0.98 0.04
0.7 0.11 0.53 0.3
0.73 0.67 0.46 0.96
0.11 0.31 0.91 0.57
0.43 0.61 0.13 0.1
""",
            "4 6 10",
        ),
        # Official sample 2
        (
            """\
4 32 800
0.73 0.96 0.2 0.53
0.01 0.19 0.42 0.46
0.27 0.24 0.87 0.8
0.97 0.77 0.42 0.04
0.41 0.69 0.96 0.56
0.27 0.4 0.56 0.56
0.28 0.04 0.74 0.82
0.17 0.2 0.95 0.1
0.2 0.1 0.14 0.93
0.86 0.59 0.42 0.52
0.35 0.77 0.37 0.08
0.52 0.48 0.16 0.56
0.59 0.97 0.21 0.05
0.67 0.94 0.28 0.08
0.09 0.65 0.55 1.0
0.77 0.14 0.35 0.01
0.02 0.18 0.72 0.26
0.71 0.78 0.86 0.11
0.54 0.02 0.75 0.2
0.15 0.76 0.59 0.23
0.71 0.66 0.43 0.32
0.17 0.57 0.53 0.42
0.04 0.34 0.66 0.28
0.79 0.14 0.11 0.6
0.04 0.48 0.05 0.04
0.62 0.43 0.28 0.6
0.47 0.13 0.35 0.17
0.9 0.82 0.97 0.71
0.99 0.53 0.24 0.56
0.83 0.44 0.7 0.4
0.71 0.45 0.64 0.53
0.6 0.54 0.86 0.11
""",
            "6 8 9 9",
        ),
        # Two very clear clusters, each containing two terminals.
        (
            """\
2 4 10
0.00 0.00 0.00 0.00
1.00 1.00 1.00 1.00
0.10 0.10 0.10 0.10
0.90 0.90 0.90 0.90
""",
            "2 2",
        ),
        # The output counts must be sorted from small to large.
        (
            """\
2 5 10
0.00 0.00 0.00 0.00
1.00 1.00 1.00 1.00
0.10 0.10 0.10 0.10
0.20 0.20 0.20 0.20
0.90 0.90 0.90 0.90
""",
            "2 3",
        ),
        # A point exactly equally distant from both initial centers.
        # It should be assigned to the first center.
        (
            """\
2 3 10
0.00 0.00 0.00 0.00
2.00 2.00 2.00 2.00
1.00 1.00 1.00 1.00
""",
            "1 2",
        ),
    ],
)
def test_terminal_kmeans(test_input, expected, monkeypatch, capsys):
    assert run_solution(test_input, monkeypatch, capsys) == expected