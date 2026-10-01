from collections import deque
def snakesAndLadders(board: list[list[int]]) -> int:
        n = len(board)

        def convert(square): #square -> r, c
            r = (n - 1) - (square - 1) // n
            if ((square - 1) // n) % 2 == 0:
                c = (square - 1) % n
            else:
                c = (n - 1) - (square - 1) % n
            return r, c
            


        q = deque() #square, move
        q.append([1, 0])
        visited = set() #prevent duplicate square visiting.
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = convert(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                if nextSquare == n * n:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1
                
# board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
board = [[-1,-1,2,-1],[14,2,12,3],[4,9,1,11],[-1,2,1,16]]
print(snakesAndLadders(board))





# s = {}  s is dictionary
# s = set() s is set



class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        #convert the square number to r, c
        def convert(square): #square -> r, c
            r = (n - 1) - (square - 1) // n
            if ((square - 1) // n) % 2 == 0:
                c = (square - 1) % n
            else:
                c = (n - 1) - (square - 1) % n
            return r, c
            


        q = deque() #square, move(denote the steps it takes to reach the square)
        q.append([1, 0])
        visited = set() #prevent duplicate square visiting.
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                r, c = convert(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]

                if nextSquare == n * n:
                    return moves + 1
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    q.append([nextSquare, moves + 1])
        return -1


# since we using bfs to try every possible path, how can we make sure that this algorithms will return the shortest steps?

# BFS guarantees the shortest answer because it explores positions in increasing order of dice rolls:
# - Square 1 is reached in 0 rolls.
# - Every square added from it is reached in 1 roll.
# - Those squares are processed before any square requiring 2 rolls.
# - This continues layer by layer.
# Each queue transition represents exactly one dice roll—including the optional forced snake or ladder. Therefore, the first time BFS reaches n², it has used the minimum possible number of rolls.
# The visited set is also safe: if a square has already been discovered, BFS discovered it using the same or fewer rolls, so visiting it again cannot produce a shorter route.