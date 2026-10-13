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
        # Sample 1: only 30 and 35 are ancestors before 40 in inorder,
        # so the third such ancestor does not exist.
        (
            """\
30 15 45 7 20 35 50 # # 18 # # 40
40 3
""",
            "-1",
        ),

        # Sample 2.
        (
            """\
10 5 15 2 7 12 18
7 1
""",
            "5",
        ),

        # For node 40, the qualifying ancestors in inorder order are
        # [30, 35]. Check both valid positions.
        (
            """\
30 15 45 7 20 35 50 # # 18 # # 40
40 1
""",
            "30",
        ),
        (
            """\
30 15 45 7 20 35 50 # # 18 # # 40
40 2
""",
            "35",
        ),

        # The root has no ancestors.
        (
            """\
10 5 15 2 7 12 18
10 1
""",
            "-1",
        ),

        # Ancestors 5 and 10 occur after node 2 in inorder traversal,
        # so neither of them qualifies.
        (
            """\
10 5 15 2 7 12 18
2 1
""",
            "-1",
        ),

        # A direct right child: the root is before it in inorder.
        (
            """\
10 # 15
15 1
""",
            "10",
        ),

        # There is only one qualifying ancestor, so k=2 is invalid.
        (
            """\
10 # 15
15 2
""",
            "-1",
        ),

        # Right-only chain. Its ancestors before 4 are [1, 2, 3].
        (
            """\
1 # 2 # 3 # 4
4 2
""",
            "2",
        ),

        # The root is after 7 in inorder, while node 5 is before 7.
        (
            """\
10 5 # # 7
7 1
""",
            "5",
        ),

        # A tree containing only one node.
        (
            """\
42
42 1
""",
            "-1",
        ),
    ],
)
def test_kth_inorder_ancestor(test_input, expected, monkeypatch, capsys):
    assert run_solution(
        test_input,
        monkeypatch,
        capsys,
    ) == expected
