class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        x, y = self.findRook(board)
        ans = 0
        i = x-1
        # left
        while i >= 0:
            if board[i][y] == "p":
                ans += 1
                break
            elif board[i][y] == "B":
                break
            i -= 1
        # right
        i = x + 1
        while i <= len(board) - 1:
            if board[i][y] == "p":
                ans += 1
                break
            elif board[i][y] == "B":
                break
            i += 1
        
        # top
        j = y - 1
        while j >= 0:
            if board[x][j] == "p":
                ans += 1
                break
            elif board[x][j] == "B":
                break
            j -= 1
            
        # bottom
        j = y + 1
        while j <= len(board) - 1:
            if board[x][j] == "p":
                ans += 1
                break
            elif board[x][j] == "B":
                break
            j += 1
        
        return ans
        
    def findRook(self, board: List[List[str]]) -> tuple:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "R":
                    return (i, j)
        
