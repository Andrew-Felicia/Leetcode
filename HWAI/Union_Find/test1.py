import io
import runpy
import sys
from pathlib import Path

import pytest


SOLUTION_FILE = Path(__file__).with_name("1.py")


def load_union_class():
    """Load the Union class without running main()."""

    namespace = runpy.run_path(str(SOLUTION_FILE))

    if "Union" not in namespace:
        pytest.fail("1.py must contain class Union")

    return namespace["Union"]


def run_solution(test_input, monkeypatch, capsys):
    """Run the complete program using fake standard input."""

    fake_input = io.TextIOWrapper(
        io.BytesIO(test_input.encode())
    )

    monkeypatch.setattr(sys, "stdin", fake_input)

    runpy.run_path(
        str(SOLUTION_FILE),
        run_name="__main__"
    )

    return capsys.readouterr().out.strip()


# ==================================================
# Union-Find tests
# ==================================================

def test_union_initial_state():
    Union = load_union_class()
    union = Union(5)

    assert union.parent == [0, 1, 2, 3, 4]
    assert union.size == [1, 1, 1, 1, 1]

    for item in range(5):
        assert union.find(item) == item


def test_union_two_items():
    Union = load_union_class()
    union = Union(5)

    cluster_size = union.union(0, 1)

    assert cluster_size == 2
    assert union.find(0) == union.find(1)


def test_union_same_cluster_again():
    Union = load_union_class()
    union = Union(5)

    assert union.union(0, 1) == 2
    assert union.union(0, 1) == 2
    assert union.union(1, 0) == 2


def test_union_transitive_connection():
    Union = load_union_class()
    union = Union(5)

    union.union(0, 1)
    union.union(1, 2)
    union.union(2, 3)

    root = union.find(0)

    assert union.find(1) == root
    assert union.find(2) == root
    assert union.find(3) == root
    assert union.find(4) != root

    assert union.size[root] == 4


def test_union_two_clusters():
    Union = load_union_class()
    union = Union(6)

    union.union(0, 1)
    union.union(1, 2)

    union.union(3, 4)
    union.union(4, 5)

    cluster_size = union.union(2, 5)

    assert cluster_size == 6

    roots = {
        union.find(item)
        for item in range(6)
    }

    assert len(roots) == 1


# ==================================================
# Complete problem tests
# ==================================================

def test_official_sample1(monkeypatch, capsys):
    test_input = """\
1 1.0 0.0 0.0
2 0.99 0.01 0.0
3 0.0 1.0 0.0
4 0.0 1.0 0.01
5 0.1 0.0 0.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "3"


def test_official_sample2(monkeypatch, capsys):
    test_input = """\
1 1.0 0.0 0.0
2 0.99 0.01 0.0 0.98
3 0.0 1.0 0.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "0"


def test_official_sample3(monkeypatch, capsys):
    test_input = """\
1 0.878434 -0.068245 -0.46237 0.099552
2 0.33961 -0.083281 -0.348141 0.869786
3 0.326485 -0.071012 -0.353166 0.873865
4 0.330106 -0.085155 -0.338106 0.87719
5 0.340185 -0.066865 -0.339054 0.874554
6 0.482266 -0.483077 0.539977 -0.492423
7 0.491966 -0.485237 0.526674 -0.495104
8 0.48426 -0.477249 0.531019 -0.505711
9 -0.669925 -0.330461 0.409454 -0.523778
10 -0.668543 -0.331692 0.403806 -0.529123
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "4"


def test_empty_input(monkeypatch, capsys):
    actual = run_solution(
        "",
        monkeypatch,
        capsys
    )

    assert actual == "0"


def test_single_alert(monkeypatch, capsys):
    test_input = """\
1 1.0 2.0 3.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "1"


def test_all_alerts_are_independent(monkeypatch, capsys):
    test_input = """\
1 1.0 0.0
2 0.0 1.0
3 -1.0 0.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "1"


def test_same_direction_different_lengths(
    monkeypatch,
    capsys
):
    test_input = """\
1 1.0 0.0
2 2.0 0.0
3 0.1 0.0
4 0.0 1.0
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "3"


def test_weak_transitivity(monkeypatch, capsys):
    test_input = """\
1 1.0 0.0
2 0.965925826 0.258819045
3 0.866025404 0.5
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    # 1 is similar to 2.
    # 2 is similar to 3.
    # Therefore all three must be in one cluster.
    assert actual == "3"


def test_two_separate_clusters(monkeypatch, capsys):
    test_input = """\
1 1.0 0.0
2 0.99 0.01
3 0.98 0.02
4 0.0 1.0
5 0.01 0.99
"""

    actual = run_solution(
        test_input,
        monkeypatch,
        capsys
    )

    assert actual == "3"