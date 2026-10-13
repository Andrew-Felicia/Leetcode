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
        # Sample 1: both tensors contain only one value, so both scales are 0.
        (
            """\
1
3.14
1 1
2.71
""",
            "16384\n0",
        ),

        # Sample 2: both endpoint values can be represented exactly.
        (
            """\
2
0.0 255.0
1 2
0.0 255.0
""",
            "32513\n0",
        ),

        # Sample 3: W must be quantized using one min/max pair for
        # the entire matrix, not separately for every row.
        (
            """\
2
0.0 255.0
2 2
0.0 255.0
127.5 127.5
""",
            "32513 0\n812812500",
        ),

        # Sample 4: negative, positive, and zero values.
        (
            """\
4
-1.2 0.3 2.7 4.1
3 4
0.5 -0.8 1.7 2.9
-2.4 1.1 0.0 3.3
1.2 2.2 -1.5 0.7
""",
            "20023 29629 -12475\n38",
        ),

        # x is constant, so scale_x is 0 and every quantized x value is -128.
        # W contains only its two exactly representable endpoint values.
        (
            """\
2
2.0 2.0
2 2
0.0 255.0
255.0 0.0
""",
            "128 128\n0",
        ),

        # W is constant, so scale_W is 0 and every quantized weight is -128.
        (
            """\
2
0.0 255.0
2 2
3.0 3.0
3.0 3.0
""",
            "128 128\n0",
        ),

        # With min=0 and max=255, values 0.5 and 1.5 test round-to-even:
        # round(0.5) = 0 and round(1.5) = 2.
        (
            """\
4
0.0 0.5 1.5 255.0
1 4
0.0 0.0 255.0 255.0
""",
            "32895\n1625625000",
        ),
    ],
)
def test_int8_asymmetric_quantization(
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
