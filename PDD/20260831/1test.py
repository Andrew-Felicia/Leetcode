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


def oracle(a,b):
    graph={x:set() for x in set(a+b)}
    for x,y in zip(a,b):graph[x].add(y);graph[y].add(x)
    components=0
    seen=set()
    for x in graph:
        if x not in seen:
            components+=1; stack=[x];seen.add(x)
            while stack:
                for y in graph[stack.pop()]:
                    if y not in seen:seen.add(y);stack.append(y)
    return len(graph)-components

random.seed(15);cases=[]
for _ in range(400):
    n=random.randint(1,50);m=random.randint(1,30)
    cases.append((n,m,[random.randint(1,m) for _ in range(n)],
                  [random.randint(1,m) for _ in range(n)]))
text=str(len(cases))+"\n";expected=[]
for n,m,a,b in cases:
    text+=f"{n} {m}\n"+" ".join(map(str,a))+"\n"+" ".join(map(str,b))+"\n"
    expected.append(str(oracle(a,b)))
check(text,"\n".join(expected))
print("all replacement tests passed")
