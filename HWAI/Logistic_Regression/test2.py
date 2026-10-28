import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("2.py")


def run_solution(test_input, monkeypatch, capsys):
    fake_stdin = io.TextIOWrapper(io.BytesIO(test_input.encode()))
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    # This keeps VS Code breakpoints in 1.py available through Debug Test.
    runpy.run_path(str(SOLUTION_FILE), run_name="__main__")

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        pytest.param(
            """\
10 1000 0.01 0.1 0.0001
25 8 5 0
30 15 15 1
35 20 10 0
40 25 20 1
45 30 25 1
50 35 18 1
55 40 12 0
60 45 8 0
65 50 5 0
70 55 30 1
3
32 18 12
48 33 22
62 48 10
""",
            "1 0.7539\n1 0.9966\n0 0.0004",
            id="official-sample-1",
        ),
        pytest.param(
            """\
10 1000 0.01 0.1 0.0001
25 8 5 0
30 15 15 1
35 20 10 0
40 25 20 1
45 30 25 1
50 35 18 1
55 40 12 0
60 45 8 0
65 50 5 0
70 55 30 1
1
48 30 10
""",
            "0 0.0081",
            id="official-sample-2",
        ),
        # All training labels are positive, so every probability is above 0.5.
        pytest.param(
            """\
4 1000 0.01 0.1 0.0001
1 1 1 1
2 2 2 1
3 3 3 1
4 4 4 1
2
1 1 1
5 5 5
""",
            "1 0.8559\n1 0.9996",
            id="all-positive-training-labels",
        ),
        # All training labels are negative, so every probability is below 0.5.
        pytest.param(
            """\
4 1000 0.01 0.1 0.0001
1 1 1 0
2 2 2 0
3 3 3 0
4 4 4 0
2
1 1 1
5 5 5
""",
            "0 0.1441\n0 0.0004",
            id="all-negative-training-labels",
        ),
        # With max_iter = 0 the parameters stay at zero: p = 0.5, label 1.
        pytest.param(
            """\
2 0 0.01 0.1 0.0001
1 1 1 0
2 2 2 1
1
3 3 3
""",
            "1 0.5000",
            id="max-iter-zero-threshold-is-inclusive",
        ),
        # A huge tol stops training after exactly one step:
        # w0 = -0.1 * 0.25 = -0.025, sigmoid(-0.025) = 0.4938.
        pytest.param(
            """\
2 1000 0.1 0.0 1000
1 0 0 0
0 0 0 1
2
1 0 0
0 0 0
""",
            "0 0.4938\n1 0.5000",
            id="tol-stops-after-first-iteration",
        ),
        # Separable data on the first feature: larger value -> positive class.
        pytest.param(
            """\
6 2000 0.1 0.0 0.0000001
0 0 0 0
1 0 0 0
2 0 0 0
8 0 0 1
9 0 0 1
10 0 0 1
2
0 0 0
10 0 0
""",
            "0 0.0032\n1 0.9993",
            id="separable-data-follows-feature-direction",
        ),
    ],
)
def test_logistic_regression_purchase_predictor(
    test_input,
    expected,
    monkeypatch,
    capsys,
):
    assert run_solution(test_input, monkeypatch, capsys) == expected