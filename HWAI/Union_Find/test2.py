import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("2.py")


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
        # Official example: duplicate 7 and shared 9.
        (
            """\
6
10 20
30 40
500
7 7 8 9
1
9 11
""",
            """\
1
10 20
11 7 8 9
30 40
500""",
        ),

        # Transitive merge:
        # row 0 shares 23 with row 1;
        # row 1 shares 7 with row 2.
        (
            """\
4
001 23
23 7
7 88
500
""",
            """\
001 23 7 88
500""",
        ),

        # Leading zeros must stay strings.
        # "0005" is not the same identifier as "5".
        (
            """\
4
0005 9
9 11
5 11
123
""",
            """\
0005 11 5 9
123""",
        ),

        # A row can have repeated identifiers only.
        (
            """\
3
8 8 8
100
7 7
""",
            """\
100
7
8""",
        ),
    ],
)
def test_entity_merge(test_input, expected, monkeypatch, capsys):
    actual = run_solution(
        test_input,
        monkeypatch,
        capsys,
    )

    assert actual == expected