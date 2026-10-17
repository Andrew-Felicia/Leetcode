import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("2.py")


def run_solution(test_input, monkeypatch, capsys):
    """Run 2.py as a normal program and return its printed result."""
    fake_stdin = io.TextIOWrapper(io.BytesIO(test_input.encode()))
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    # This also lets a breakpoint in 2.py work with VS Code Debug Test.
    runpy.run_path(str(SOLUTION_FILE), run_name="__main__")

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        pytest.param(
            """\
7 3 2
2 3 1 50 0
4 5 2 50 0
6 7 2 50 1
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 1
30 60 1
30 30 1
60 30 1
""",
            "0.800000",
            id="official-sample-1",
        ),
        pytest.param(
            """\
7 3 3
2 3 3 87 1
0 0 1 3 0
4 5 1 38 1
0 0 2 8 1
6 7 2 94 1
0 0 2 44 1
0 0 2 9 0
30 78 73 0
73 99 99 1
72 3 2 0
""",
            "1.000000",
            id="official-sample-2",
        ),
        # Pruning the root to its label 1 improves F1 from 0.5 to 0.8.
        pytest.param(
            """\
3 3 1
2 3 1 5 1
0 0 0 0 0
0 0 0 0 1
1 1
9 1
9 0
""",
            "0.800000",
            id="pruning-root-improves-f1",
        ),
        # In this case keeping the original split is best.
        pytest.param(
            """\
3 3 1
2 3 1 5 0
0 0 0 0 0
0 0 0 0 1
1 1
9 1
9 0
""",
            "0.500000",
            id="keep-original-tree",
        ),
        # A tree that consists of one positive leaf already has F1 = 1.
        pytest.param(
            """\
1 2 2
0 0 0 0 1
10 20 1
30 40 1
""",
            "1.000000",
            id="single-positive-leaf",
        ),
        # No true positive exists: precision/recall/F1 are all zero.
        pytest.param(
            """\
1 2 1
0 0 0 0 0
10 0
20 0
""",
            "0.000000",
            id="no-positive-samples",
        ),
    ],
)
def test_best_pruned_tree_f1(test_input, expected, monkeypatch, capsys):
    assert run_solution(test_input, monkeypatch, capsys) == expected
