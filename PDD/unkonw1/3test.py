import random
import subprocess
import sys

SOLUTION_FILE = "3.py"


def run_solution(test_input, timeout=3):
    result = subprocess.run(
        [sys.executable, SOLUTION_FILE],
        input=test_input,
        text=True,
        capture_output=True,
        timeout=timeout,
    )
    if result.returncode != 0:
        raise AssertionError(result.stderr)
    return result.stdout.strip()


def check(test_input, expected, timeout=3):
    actual = run_solution(test_input, timeout)
    expected = str(expected).strip()
    if actual != expected:
        raise AssertionError(
            f"input:\n{test_input}\nexpected: {expected!r}\nactual: {actual!r}"
        )


def make_case(rows,cols):
 ids=list(range(1,rows*cols+1));random.shuffle(ids);rels=[]
 for r in range(rows):
  for c in range(cols):
   if c+1<cols:rels.append((ids[r*cols+c+1],ids[r*cols+c],'R'))
   if r+1<rows:rels.append((ids[(r+1)*cols+c],ids[r*cols+c],'B'))
 random.shuffle(rels)
 text=f"{rows} {cols}\n{len(rels)}\n"+"".join(f"{a} {b} {d}\n" for a,b,d in rels)
 expected="\n".join(" ".join(map(str,ids[r*cols:(r+1)*cols])) for r in range(rows))
 return text,expected

random.seed(21)
for rows in range(2,8):
 for cols in range(2,8):
  for _ in range(3):
   text,expected=make_case(rows,cols);check(text,expected)
print("all puzzle tests passed")
