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



readline  readlines  read

The primary difference between sys.stdin.readline() and sys.stdin.readlines() in Python 3 is how much data they read at once and the data type they return. sys.stdin.readline() reads a single line as a string, while sys.stdin.readlines() reads all remaining lines and returns them as a list of strings



`sys.stdin` represents standard input. The main differences are:

- `read()` — read everything.
- `readline()` — read one line.
- `readlines()` — read everything and return a list of lines.
- `.buffer` — read raw bytes instead of strings.
- `.decode()` — convert bytes into a string.

## 1. `readline()`: read one line

```python
import sys

line = sys.stdin.readline()
print(line)
```

Input:

```text
hello world
```

`line` contains:

```python
"hello world\n"
```

The newline character `\n` is included.

You can remove surrounding whitespace with:

```python
line = sys.stdin.readline().strip()
```

For competitive programming:

```python
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
```

Each call to `input()` reads one line.

---

## 2. `read()`: read everything until EOF

```python
import sys

data = sys.stdin.read()
print(data)
```

If the input is:

```text
10
20
30
```

Then `data` is one string:

```python
"10\n20\n30\n"
```

It is common to use:

```python
data = sys.stdin.read().split()
```

The result is:

```python
["10", "20", "30"]
```

Then convert the values:

```python
numbers = list(map(int, sys.stdin.read().split()))
```

### Important terminal behavior

`read()` waits until it receives EOF because it does not know when the input is finished.

On macOS/Linux, press:

```text
Ctrl+D
```

Do not use `Ctrl+C`; that interrupts the program.

---

## 3. `readlines()`: read all lines into a list

```python
import sys

lines = sys.stdin.readlines()
print(lines)
```

Input:

```text
hello
world
```

Result:

```python
["hello\n", "world\n"]
```

You can remove the newlines:

```python
lines = [line.strip() for line in sys.stdin.readlines()]
```

Result:

```python
["hello", "world"]
```

Like `read()`, `readlines()` waits until EOF and loads the entire input into memory.

---

## 4. Iterating over `sys.stdin`

You can also process input one line at a time:

```python
import sys

for line in sys.stdin:
    print(line.strip())
```

This is preferable to `readlines()` when the input may be large because it does not need to store every line at once.

---

## Comparison

| Method | Reads | Returns |
|---|---|---|
| `readline()` | One line | One string |
| `read()` | All remaining input | One large string |
| `readlines()` | All remaining input | List of strings |
| `for line in sys.stdin` | One line per iteration | Strings one by one |

Example input:

```text
10 20
30 40
```

The results are approximately:

```python
sys.stdin.readline()
# "10 20\n"
```

```python
sys.stdin.read()
# "10 20\n30 40\n"
```

```python
sys.stdin.readlines()
# ["10 20\n", "30 40\n"]
```

## 5. What is `.buffer`?

Normal `sys.stdin` returns Python strings:

```python
line = sys.stdin.readline()
print(type(line))
```

Output:

```text
<class 'str'>
```

`sys.stdin.buffer` accesses the underlying binary input and returns bytes:

```python
line = sys.stdin.buffer.readline()
print(type(line))
```

Output:

```text
<class 'bytes'>
```

For input:

```text
hello
```

The values are:

```python
sys.stdin.readline()
# "hello\n"

sys.stdin.buffer.readline()
# b"hello\n"
```

The `b` means that the value is bytes.

You can combine `.buffer` with all three methods:

```python
sys.stdin.buffer.readline()   # One line as bytes
sys.stdin.buffer.read()       # Everything as bytes
sys.stdin.buffer.readlines()  # List of byte lines
```

Binary input can be slightly faster, which is why it is common in competitive programming.

---

## 6. What does `decode()` do?

`decode()` converts bytes into a string:

```python
raw = b"hello"
text = raw.decode()

print(raw)
print(text)
```

Output:

```text
b'hello'
hello
```

Usually UTF-8 is used:

```python
text = raw.decode("utf-8")
```

For example:

```python
line = sys.stdin.buffer.readline()
word = line.strip().decode()

print(type(line))  # bytes
print(type(word))  # str
```

### Do numbers need to be decoded?

Usually not. `int()` and `float()` accept bytes:

```python
int(b"123")       # 123
float(b"0.95")    # 0.95
```

Therefore, this works:

```python
input = sys.stdin.buffer.readline

n = int(input())
numbers = list(map(int, input().split()))
```

But textual values may need decoding:

```python
parts = sys.stdin.buffer.readline().split()

bit_width = parts[0].decode()
loss = float(parts[1])

print(bit_width)  # "8bit"
```

However, you could also compare bytes directly:

```python
if parts[0] == b"8bit":
    print("8-bit option")
```

## 7. `input()` versus `sys.stdin.readline()`

Built-in `input()`:

```python
line = input()
```

- Returns a string.
- Removes the final newline.
- Is simple but slightly slower.

`sys.stdin.readline()`:

```python
line = sys.stdin.readline()
```

- Returns a string.
- Keeps the final newline.
- Returns `""` at EOF.
- Usually faster for large inputs.

Comparison:

```python
# Input: hello

input()
# "hello"

sys.stdin.readline()
# "hello\n"
```

For most algorithm problems, these are the two common patterns:

```python
# Known line structure
input = sys.stdin.buffer.readline

n = int(input())
numbers = list(map(int, input().split()))
```

Or:

```python
# Read all whitespace-separated values
data = sys.stdin.buffer.read().split()
```

Use `readline()` when you want to process the input line by line. Use `read()` when the input format is simple and you want all tokens at once.