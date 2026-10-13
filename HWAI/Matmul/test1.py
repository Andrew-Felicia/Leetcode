import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


def run_solution(test_input, monkeypatch, capsys):
    fake_stdin = io.TextIOWrapper(io.BytesIO(test_input.encode()))
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    runpy.run_path(str(SOLUTION_FILE), run_name="__main__")

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    "test_input, expected",
    [
        # Sample 1: remove the row whose L1 norm is 1.
        (
            """\
3 4 3
1 0 0 0
0 1 0 0
0 0 1 0
1 2 3
0 0 1
2 0 1
1 1 0
0.25
""",
            "2 0 0",
        ),

        # Sample 2: ratio 0 means no pruning.
        (
            """\
2 2 2
1 0
0 1
1 -1
-2 3
0
""",
            "0 1",
        ),

        # Sample 3: a positive ratio must remove at least one row.
        (
            """\
2 3 2
1 0 0
0 0 1
1 0
2 0
0 3
0.1
""",
            "0 1",
        ),

        # L1 norms must use absolute values. Row 1 has the smallest norm.
        (
            """\
1 3 2
1 1 0
-5 0
-1 -1
0 3
0.34
""",
            "1",
        ),

        # floor(0.4 * 5) removes exactly two rows.
        # The second sample creates a tie, so class 0 must be selected.
        (
            """\
2 5 3
1 1 1 1 1
2 0 0 0 1
1 0 0
0 0.2 0
0 0 3
-0.5 0 0
0 2 0
0.4
""",
            "2 0",
        ),

        # Pruning all rows leaves zero scores for every class.
        (
            """\
2 2 3
10 -20
-3 7
1 2 3
-4 -5 -6
1.0
""",
            "0 0",
        ),

        # One feature, one sample, and no pruning.
        (
            """\
1 1 4
2
-1 0 3 3
0
""",
            "2",
        ),
    ],
)
def test_l1_structured_pruning(test_input, expected, monkeypatch, capsys):
    assert run_solution(
        test_input,
        monkeypatch,
        capsys,
    ) == expected
