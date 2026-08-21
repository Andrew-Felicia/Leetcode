import random
import subprocess
import sys

SOLUTION_FILE = "1.py"


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


def oracle(s):
 return max([0]+[j-i for i in range(len(s)) for j in range(i+1,len(s)+1)
                if s[i:j].count('A')==s[i:j].count('B')])

fixed=['A','B','AB','AABB','AAAA','ABBAAB','BABABA']
for s in fixed:check(f"{len(s)}\n{s}\n",oracle(s))
random.seed(23)
for _ in range(350):
 s=''.join(random.choice('AB') for _ in range(random.randint(1,80)))
 check(f"{len(s)}\n{s}\n",oracle(s))
s='AB'*50000
check(f"{len(s)}\n{s}\n",100000,timeout=5)
print("all balanced-substring tests passed")
