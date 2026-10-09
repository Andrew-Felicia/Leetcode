import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


def run_solution(test_input, monkeypatch, capsys):
    fake_input = io.TextIOWrapper(io.BytesIO(test_input.encode()))
    monkeypatch.setattr(sys, "stdin", fake_input)

    # Run in this process so VS Code breakpoints in 1.py work.
    runpy.run_path(str(SOLUTION_FILE), run_name="__main__")

    return capsys.readouterr().out.strip()


@pytest.mark.parametrize(
    ("test_input", "expected_output"),
    [
        pytest.param("3 3 3\n", "18", id="official-sample-1"),
        pytest.param("2 3 1\n", "2", id="official-sample-2"),
        pytest.param("1 1 1\n", "1", id="smallest-input"),
        pytest.param("4 5 3\n", "24", id="h-smaller-than-m"),
        pytest.param("2 3 5\n", "24", id="h-larger-than-m"),
        pytest.param("99 99 99\n", "490050", id="largest-dimensions"),
    ],
)
def test_attention_sum(test_input, expected_output, monkeypatch, capsys):
    actual_output = run_solution(test_input, monkeypatch, capsys)
    assert actual_output == expected_output
