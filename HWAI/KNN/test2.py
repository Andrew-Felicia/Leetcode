import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("2.py")


def run_solution(test_input, monkeypatch, capsys):
    """Run 2.py like a terminal program and capture stdout."""
    fake_stdin = io.TextIOWrapper(io.BytesIO(test_input.encode()))
    monkeypatch.setattr(sys, "stdin", fake_stdin)

    # runpy lets breakpoints in 2.py work when using VS Code's Debug Test.
    runpy.run_path(str(SOLUTION_FILE), run_name="__main__")

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        pytest.param(
            """\
10 3
0.5 0.3 0.4 0
0.6 0.2 0.5 0
0.4 0.3 0.3 0
0.7 0.4 0.6 0
2.1 2.3 2.2 1
2.3 2.2 2.4 1
2.2 2.4 2.3 1
4.5 4.3 4.4 2
4.4 4.5 4.6 2
4.6 4.4 4.5 2
2.2 2.1 2.3
""",
            "1",
            id="official-sample-1",
        ),
        pytest.param(
            """\
12 4
1 0.9 1 1
0.8 0.9 0.7 1
1.3 1 1.2 1
1.2 0.9 1 1
2 2.2 2.1 2
2.3 2.2 2 2
2 2.2 1.9 2
1.9 2.2 2.1 2
3.1 3.1 3 3
2.8 2.9 3.1 3
2.9 3 3.2 3
3.1 3 3.1 3
2.2 1.2 1.9
""",
            "2",
            id="official-sample-2",
        ),
        # With K=1, the nearest vector's label must be returned.
        pytest.param(
            """\
3 1
0.0 0.0 0.0 7
2.0 2.0 2.0 8
1.0 1.0 1.0 9
0.1 0.1 0.1
""",
            "7",
            id="one-nearest-neighbor",
        ),
        # The nearest three labels are 2, 2, and 4: label 2 wins.
        pytest.param(
            """\
5 3
0.1 0.0 0.0 2
0.2 0.0 0.0 2
0.3 0.0 0.0 4
1.0 0.0 0.0 4
2.0 0.0 0.0 7
0.0 0.0 0.0
""",
            "2",
            id="majority-among-neighbors",
        ),
        # The target exactly matches a known vector.
        pytest.param(
            """\
4 2
1.0 1.0 1.0 3
1.1 1.0 1.0 3
5.0 5.0 5.0 6
5.1 5.0 5.0 6
5.0 5.0 5.0
""",
            "6",
            id="exact-match",
        ),
    ],
)
def test_voice_knn(test_input, expected, monkeypatch, capsys):
    assert run_solution(test_input, monkeypatch, capsys) == expected
