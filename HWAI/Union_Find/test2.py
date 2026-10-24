import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("2.py")


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
        # Sample 1: all points are noise.
        (
            """\
2 2 10
0 0
3 3
6 6
9 9
12 12
2 6
6 2
9 5
5 9
10 2
""",
            "0 10",
        ),

        # Sample 2: two clusters and two noise points.
        (
            """\
1 5 20
5.05 1.36
-8.19 -6.47
4.5 2.5
5.01 2.06
4.30 2.28
4.22 1.82
4.58 1.82
4.81 2.46
4.81 1.09
4.80 1.78
5.16 2.44
-6.92 -6.38
-6.84 -7.03
-6.70 -7.20
-6.83 -7.87
-6.47 -6.20
-6.70 -6.11
-6.90 -6.10
-6.99 -6.70
5 5
""",
            "2 2",
        ),

        # A simple 3D example:
        # First two points form one cluster.
        # Last point is noise.
        (
            """\
2 1 3
0 0 0
1 0 0
10 10 10
""",
            "1 1",
        ),

        # All points are close enough to become one cluster.
        (
            """\
2 1 4
0 0
0.5 0
1 0
1.5 0
""",
            "1 0",
        ),
    ],
)
def test_dbscan(
    test_input,
    expected,
    monkeypatch,
    capsys,
):
    actual = run_solution(
        test_input,
        monkeypatch,
        capsys,
    )

    assert actual == expected