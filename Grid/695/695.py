from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        tmp = 0
        
        #return the size of an island.
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            if grid[i][j] == 1:
                tmp += 1
                grid[i][j] = 0
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    ans = max(ans, tmp)
                    tmp = 0
        return ans

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))

# Exception has occurred: UnboundLocalError
# cannot access local variable 'tmp' where it is not associated with a value
#   File "/Users/taoyongli/leetcode/Grid/695/695.py", line 14, in dfs
#     tmp += 1
#     ^^^
#   File "/Users/taoyongli/leetcode/Grid/695/695.py", line 24, in maxAreaOfIsland
#     dfs(i, j)
#     ~~~^^^^^^
#   File "/Users/taoyongli/leetcode/Grid/695/695.py", line 31, in <module>
#     print(maxAreaOfIsland(grid))
#           ~~~~~~~~~~~~~~~^^^^^^
# UnboundLocalError: cannot access local variable 'tmp' where it is not associated with a value

#fix one:
def maxAreaOfIsland(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        tmp = 0

        #return the size of an island.
        def dfs(i, j):
            nonlocal tmp #this line is very important.
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            if grid[i][j] == 1:
                tmp += 1
                grid[i][j] = 0
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    ans = max(ans, tmp)
                    tmp = 0
        return ans

#fix two:

def maxAreaOfIsland(grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        #return the size of an island.
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            return 1 + dfs(i - 1, j) + dfs(i + 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans
