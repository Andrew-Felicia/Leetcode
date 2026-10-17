import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


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
        # Official sample 1
        (
            """\
4 2
2.0 2.0
3.0 0.0
0.0 4.0
1.0 1.0
1 2 1 3
""",
            "600",
        ),

        # Official sample 2
        (
            """\
3 2
1.0 0.0
0.0 1.0
1.0 1.0
1 1 2
""",
            "200",
        ),

        # One-dimensional vectors: normalization gives 1 or -1.
        # Squaring the attention makes both contribute 1.
        (
            """\
2 1
5.0
-4.0
1 1
""",
            "100",
        ),

        # Position 2 may choose only one connection.
        # It must choose the score 2, instead of the smaller score 1.
        (
            """\
3 2
1.0 0.0
1.0 1.0
1.0 0.0
1 1 1
""",
            "300",
        ),

        # RMSNorm removes the effect of vector magnitude.
        (
            """\
2 2
10.0 0.0
3.0 0.0
1 1
""",
            "200",
        ),

        # Attention squared score is 0.4, so integerized output is 40.
        (
            """\
2 2
1.0 0.0
1.0 2.0
1 1
""",
            "40",
        ),
    ],
)
def test_attention_routing(test_input, expected, monkeypatch, capsys):
    assert run_solution(
        test_input,
        monkeypatch,
        capsys,
    ) == expected