import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("4.py")


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
        # Sample 1
        (
            """\
6 2
0 0
1 1
2 2
10 10
11 11
5 5
""",
            "8.67,8.67",
        ),

        # Sample 2:
        # Cluster 0 has the lower silhouette coefficient.
        (
            """\
4 2
0 0
0 1
1 0
10 10
""",
            "0.33,0.33",
        ),

        # Only one point and one cluster.
        # Its center remains unchanged.
        (
            """\
1 1
2 3
""",
            "2.00,3.00",
        ),

        # One cluster with two points.
        # Final center is their average: (2, 4).
        (
            """\
2 1
1 3
3 5
""",
            "2.00,4.00",
        ),
    ],
)
def test_find_worst_coverage_cluster(
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