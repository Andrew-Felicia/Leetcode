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
    "test_input, expected",
    [
        # Sample 1: singular linear part produces an all-zero image.
        (
            """\
2 2 1
5 6
7 8
1 2 0
2 4 0
2 3
""",
            "0 0 0 0 0 0",
        ),

        # Sample 2: translate the source image right and down by one pixel.
        (
            """\
2 2 1
10 20 30
40 50 60
1 0 1
0 1 1
3 4
""",
            "0 0 0 0 0 10 20 30 0 40 50 60",
        ),

        # Sample 3: scale by two and use nearest-neighbor rounding.
        (
            """\
2 2 1
1 2
3 4
2 0 0
0 2 0
4 4
""",
            "1 2 2 0 3 4 4 0 3 4 4 0 0 0 0 0",
        ),

        # Identity transformation keeps every source pixel unchanged.
        (
            """\
2 2 1
1 2 3
4 5 6
1 0 0
0 1 0
2 3
""",
            "1 2 3 4 5 6",
        ),

        # Swap x and y. A 2x3 source becomes a 3x2 output.
        (
            """\
2 2 1
1 2 3
4 5 6
0 1 0
1 0 0
3 2
""",
            "1 4 2 5 3 6",
        ),

        # Forward translation by -1 on x shifts the image left.
        (
            """\
2 2 1
1 2 3
4 5 6
1 0 -1
0 1 0
2 2
""",
            "2 3 5 6",
        ),

        # Scaling x by 0.5 makes output columns sample source columns 0, 2, 4.
        (
            """\
1 2 1
1 2 3 4 5
0.5 0 0
0 1 0
1 3
""",
            "1 3 5",
        ),

        # The first-line value o is read but does not affect the result.
        (
            """\
1 2 99
9 8
1 0 0
0 1 0
1 2
""",
            "9 8",
        ),

        # An output larger than an identity-mapped source is zero outside
        # the source boundaries.
        (
            """\
1 2 1
7 8
1 0 0
0 1 0
2 3
""",
            "7 8 0 0 0 0",
        ),
    ],
)
def test_affine_transformation(test_input, expected, monkeypatch, capsys):
    assert run_solution(
        test_input,
        monkeypatch,
        capsys,
    ) == expected
