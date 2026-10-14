import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("3.py")


def run_solution(test_input, monkeypatch, capsys):
    fake_stdin = io.TextIOWrapper(io.BytesIO(test_input.encode()))
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    runpy.run_path(str(SOLUTION_FILE), run_name="__main__")

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        # Sample 1.
        (
            """\
1 1 1 1
5
1
""",
            "5.0",
        ),

        # Sample 2: asymmetric strategy matrix also checks that the
        # strategy is used directly rather than flipped.
        (
            """\
3 3 3 3
1 2 3
4 5 6
7 8 9
1 2 2
1 1 1
1 1 1
""",
            "119.0",
        ),

        # One row: there is only one possible path.
        (
            """\
1 4 1 1
1 2 3 4
2
""",
            "20.0",
        ),

        # One column: select the best starting/ending row.
        (
            """\
3 1 1 1
1
5
3
2
""",
            "10.0",
        ),

        # A center-only 3x3 strategy makes the energy matrix equal
        # to the image. The best path must move between rows.
        (
            """\
3 4 3 3
1 100 1 1
50 1 100 1
1 1 1 100
0 0 0
0 1 0
0 0 0
""",
            "350.0",
        ),

        # Negative energies check that DP does not incorrectly start at 0.
        (
            """\
2 2 1 1
-1 -2
-3 -4
1
""",
            "-3.0",
        ),

        # The strategy is larger than the image; out-of-range values
        # must be treated as zero.
        (
            """\
1 1 3 3
2
1 1 1
1 1 1
1 1 1
""",
            "2.0",
        ),

        # Floating-point strategy values and one-decimal output.
        (
            """\
1 2 1 1
1 3
0.5
""",
            "2.0",
        ),
    ],
)
def test_lane_energy_path(test_input, expected, monkeypatch, capsys):
    assert run_solution(
        test_input,
        monkeypatch,
        capsys,
    ) == expected
