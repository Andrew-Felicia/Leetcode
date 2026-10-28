import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("4.py")


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
        # Official example.
        (
            """\
aababa
4
a 1
aa 3
ab 2
ba 2
3
aa ba 2
ba ba -1
ab a 1
""",
            "8",
        ),

        # Cannot fully cover "abc":
        # only "a" and "b" are available.
        (
            """\
abc
2
a 1
b 2
0
""",
            "0",
        ),

        # The transition score makes "aa | a" the best split.
        (
            """\
aaa
2
a 2
aa 3
2
a a -10
aa a 5
""",
            "10",
        ),

        # One word covers the full text.
        (
            """\
hello
3
he 2
llo 3
hello 10
1
he llo 8
""",
            "13",
        ),

        # # The input can also be fully written on one line,
        # # like the official sample format.
        # (
        #     "aababa 4 a 1 aa 3 ab 2 ba 2 "
        #     "3 aa ba 2 ba ba -1 ab a 1\n",
        #     "8",
        # ),
    ],
)
def test_optimal_tokenizer(
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