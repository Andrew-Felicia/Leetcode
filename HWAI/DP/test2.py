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
        # Sample 1.
        (
            """\
10
5
3 4 5 6 7
1 2 3 5 5
2 3 4 5 6
""",
            "6",
        ),

        # Sample 2: one tensor reaches the target at recomputation cost 1.
        (
            """\
12
4
18 20 10 12
12 3 13 4
10 14 10 1
""",
            "1",
        ),

        # Even all tensors together cannot free enough memory.
        (
            """\
10
2
3 4
1 1
2 2
""",
            "error",
        ),

        # This also checks that one tensor cannot be selected repeatedly.
        (
            """\
10
1
6
1
2
""",
            "error",
        ),

        # Combining two tensors is cheaper than selecting the large tensor.
        (
            """\
10
3
10 6 4
100 4 5
120 7 8
""",
            "9",
        ),

        # It is valid to exceed the required memory.
        (
            """\
8
3
7 3 5
2 100 3
9 120 8
""",
            "5",
        ),

        # For every selected tensor, use the cheaper of swap and recomputation.
        (
            """\
9
3
4 5 6
2 20 4
10 3 30
""",
            "5",
        ),

        # Smallest permitted target and one tensor.
        (
            """\
1
1
1
4
7
""",
            "4",
        ),
    ],
)
def test_minimum_tensor_release_cost(
    test_input,
    expected,
    monkeypatch,
    capsys,
):
    assert run_solution(
        test_input,
        monkeypatch,
        capsys,
    ) == expected
