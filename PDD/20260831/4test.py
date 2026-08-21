import random
import subprocess
import sys

SOLUTION_FILE = "4.py"


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


def oracle(h,segs):
 return sum(all(not (l<=x<=r) for l,r in segs) for x in range(1,h+1))

cases=[(10,[(5,10),(5,5)]),(1,[(1,1)]),(20,[(1,2),(3,4)]),(30,[(10,20),(15,25)])]
random.seed(18)
for _ in range(300):
 h=random.randint(1,100);segs=[]
 for _ in range(random.randint(1,30)):
  l=random.randint(1,h);r=random.randint(l,h);segs.append((l,r))
 cases.append((h,segs))
text=str(len(cases))+"\n";expected=[]
for h,segs in cases:
 text+=f"{h}\n{len(segs)}\n"+"".join(f"{l} {r}\n" for l,r in segs)
 expected.append(str(oracle(h,segs)))
check(text,"\n".join(expected))
print("all interval tests passed")
