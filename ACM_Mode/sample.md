# ACM Input with `sys`

## Read until EOF

Use this when the number of test cases is unknown:

```python
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)
```

`sys.stdin` automatically stops at EOF.

## Stop at a sentinel

Use this when a special value such as `0 0` ends the input:

```python
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    print(a + b)
```

## Faster line input

For large input, replace `input()` with buffered `readline`:

```python
import sys

input = sys.stdin.buffer.readline

n = int(input())
a, b = map(int, input().split())
```

**Remember:** use `for line in sys.stdin` for EOF input, and `sys.stdin.buffer.readline` for fast fixed-format input.
