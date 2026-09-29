def solve(board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(i, j):
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or board[i][j] != 'O':
                return
            if board[i][j] == 'O':
                board[i][j] = '&'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    dfs(i, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '&':
                    board[i][j] = 'O'



                
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

for i in board:
    print(i)

solve(board)

for i in board:
    print(i)