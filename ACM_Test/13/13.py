n, m = map(int, input().split())

grid = [input().strip() for _ in range(n)]

for i in range(n - 1, -1, -1):
    #print(grid[i][-1::-1]) #another way
    print(grid[i][::-1])