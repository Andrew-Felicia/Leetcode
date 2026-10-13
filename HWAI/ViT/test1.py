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
        # Three examples from the problem.
        ("224 32 3 512\n", "50 512"),
        ("100 30 3 64\n", "10 64"),
        ("1 1 1 8\n", "2 8"),

        # Exact division: 64 // 16 = 4, so 4 * 4 + 1 = 17 tokens.
        ("64 16 3 256\n", "17 256"),

        # Integer division must discard the incomplete image border.
        # 31 // 8 = 3, so the result has 3 * 3 + 1 = 10 tokens.
        ("31 8 3 128\n", "10 128"),

        # A patch covering the entire image creates one patch token
        # plus one cls token.
        ("128 128 3 768\n", "2 768"),

        # The channel count does not affect the final two dimensions.
        ("32 8 1 64\n", "17 64"),
        ("32 8 64 64\n", "17 64"),

        # Patch size 1: every pixel becomes a patch token.
        # 100 * 100 patches plus one cls token.
        ("100 1 4 1\n", "10001 1"),
    ],
)
def test_vit_embedding_shape(test_input, expected, monkeypatch, capsys):
    assert run_solution(
        test_input,
        monkeypatch,
        capsys,
    ) == expected
