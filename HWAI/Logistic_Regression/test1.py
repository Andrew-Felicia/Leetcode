import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


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
10 2
CBG 0
AFE 0
FGD 1
BFG 0
BBA 0
BDD 0
BEG 1
EGE 0
CAF 0
DGD 1
DBA
DAD
""",
            "0\n0",
            id="official-sample-1",
        ),
        pytest.param(
            """\
10 3
GDEE 0
BDFEA 1
BDFE 0
GECD 0
DDCEE 1
ADA 0
EECBC 0
BACBC 1
DDD 1
FEEEE 0
AADC
BBAE
ECEC
""",
            "1\n0\n0",
            id="official-sample-2",
        ),
        # All training labels are positive, so every test sequence is positive.
        pytest.param(
            """\
10 2
ABC 1
ABC 1
ABC 1
ABC 1
ABC 1
ABC 1
ABC 1
ABC 1
ABC 1
ABC 1
ABC
GFE
""",
            "1\n1",
            id="all-positive-training-labels",
        ),
        # All training labels are negative, so every test sequence is negative.
        pytest.param(
            """\
10 2
ABC 0
ABC 0
ABC 0
ABC 0
ABC 0
ABC 0
ABC 0
ABC 0
ABC 0
ABC 0
ABC
GFE
""",
            "0\n0",
            id="all-negative-training-labels",
        ),
        # Repeating A does not change its presence feature: AAA and A are equal.
        pytest.param(
            """\
10 3
AAA 1
AAA 1
AAA 1
AAA 1
AAA 1
BBB 0
BBB 0
BBB 0
BBB 0
BBB 0
A
AAAAAAA
B
""",
            "1\n1\n0",
            id="presence-encoding-not-frequency-encoding",
        ),
    ],
)
def test_logistic_regression_intent_classifier(
    test_input,
    expected,
    monkeypatch,
    capsys,
):
    assert run_solution(test_input, monkeypatch, capsys) == expected
