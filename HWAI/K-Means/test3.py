
import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("3.py")


def run_solution(test_input, monkeypatch, capsys):
    """
    Run 1.py with fake standard input,
    then return its printed output.
    """
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
        # Sample 1
        (
            """\
3
50 25 30
60 15 60
25 75 90
3
9
50 25 30
30 50 30
60 15 60
25 75 90
10 05 60
26 15 30
32 67.5 90
80 7.5 60
20 100 90
""",
            """\
35.33 30.00 30.00
50.00 9.17 60.00
25.67 80.83 90.00""",
        ),

        # Sample 2
        (
            """\
3
50 20 30
60 10 60
180 180 180
3
8
50 20 30
30 50 30
60 10 60
25 75 90
100 5 60
30 60 90
80 10 60
180 180 180
""",
            """\
40.00 35.00 30.00
59.00 32.00 72.00
180.00 180.00 180.00""",
        ),

        # Only one cluster:
        # After one update, center is the average of two samples:
        # ((2 + 4) / 2, (4 + 6) / 2, (6 + 8) / 2)
        # = (3, 5, 7)
        (
            """\
1
0 0 0
1
2
2 4 6
4 6 8
""",
            "3.00 5.00 7.00",
        ),

        # Initial center is already the average.
        # Repeated iterations should keep it unchanged.
        (
            """\
1
3 5 7
5
2
2 4 6
4 6 8
""",
            "3.00 5.00 7.00",
        ),
    ],
)
def test_kmeans(test_input, expected, monkeypatch, capsys):
    actual = run_solution(
        test_input,
        monkeypatch,
        capsys,
    )

    assert actual == expected