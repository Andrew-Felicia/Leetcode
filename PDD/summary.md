sys.stdin.read() reads everything available until it hits EOF (end-of-file). For a file, EOF happens naturally when the file ends. For an interactive terminal, EOF only happens when you manually signal it (Ctrl+D on Linux/macOS, Ctrl+Z+Enter on Windows) — which is exactly the "won't stop" behavior you saw earlier.
Alternatives: sys.stdin.readline() reads one line at a time; iterating for line in sys.stdin: reads line by line lazily. I used .read() because competitive-programming judges usually feed a whole file at once, and reading everything up front then parsing with .split() is simpler and faster than parsing line-by-line when the token counts per line vary.



