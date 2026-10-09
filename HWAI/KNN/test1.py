import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


def run_solution(test_input, monkeypatch, capsys):
    """Run 1.py with fake terminal input and capture its output."""

    fake_input = io.TextIOWrapper(
        io.BytesIO(test_input.encode())
    )

    monkeypatch.setattr(sys, "stdin", fake_input)

    runpy.run_path(
        str(SOLUTION_FILE),
        run_name="__main__"
    )

    return capsys.readouterr().out.strip()


def test_official_sample1(monkeypatch, capsys):
    test_input = """\
3 10 2 3
0.81 0.64
0.19 0.2 1.0
0.18 0.14 0.0
0.76 0.58 1.0
0.4 0.16 1.0
0.98 0.85 0.0
0.42 0.97 1.0
0.75 0.26 1.0
0.24 0.06 1.0
0.97 0.8 0.0
0.21 0.1 2.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "0 2"


def test_official_sample2(monkeypatch, capsys):
    test_input = """\
6 10 2 4
0.78 0.63
0.57 0.07 1.0
0.5 0.13 1.0
0.83 0.07 3.0
0.27 0.87 3.0
0.81 0.44 2.0
0.21 0.73 3.0
0.45 0.91 1.0
0.12 0.22 2.0
0.25 0.48 0.0
0.54 0.87 1.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "1 2"


def test_k_equals_one(monkeypatch, capsys):
    test_input = """\
1 3 2 2
0.0 0.0
1.0 1.0 1.0
0.1 0.1 0.0
0.5 0.5 1.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    # The nearest sample is [0.1, 0.1], label 0.
    assert actual == "0 1"


def test_one_dimensional_samples(monkeypatch, capsys):
    test_input = """\
3 5 1 2
0.5
0.4 0.0
0.6 1.0
0.45 1.0
0.9 0.0
0.0 0.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    # The three nearest labels are 1, 0 and 1.
    assert actual == "1 2"


def test_three_dimensional_samples(monkeypatch, capsys):
    test_input = """\
2 4 3 3
0.0 0.0 0.0
0.1 0.0 0.0 2.0
0.0 0.2 0.0 2.0
1.0 1.0 1.0 0.0
2.0 2.0 2.0 1.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    # Both nearest samples have label 2.
    assert actual == "2 2"


def test_tied_labels_choose_nearest_label(
    monkeypatch,
    capsys
):
    test_input = """\
4 4 1 2
0.0
0.1 1.0
0.2 0.0
0.3 0.0
0.4 1.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    # Label 0 appears twice.
    # Label 1 also appears twice.
    # The nearest sample has label 1.
    assert actual == "1 2"


def test_all_nearest_neighbors_same_label(
    monkeypatch,
    capsys
):
    test_input = """\
3 5 2 2
0.0 0.0
0.1 0.0 1.0
0.0 0.1 1.0
0.1 0.1 1.0
1.0 1.0 0.0
0.9 0.9 0.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "1 3"


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        pytest.param(
            """\
1 2 1 2
0.0
0.2 0.0
0.1 1.0
""",
            "1 1",
            id="nearest-is-label-1",
        ),
        pytest.param(
            """\
2 3 1 2
1.0
0.9 0.0
1.1 0.0
0.0 1.0
""",
            "0 2",
            id="two-neighbors-label-0",
        ),
    ],
)
def test_additional_cases(
    test_input,
    expected,
    monkeypatch,
    capsys
):
    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == expected