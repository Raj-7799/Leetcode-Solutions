class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        INF = -1
        minTransitions = []
        
        # Initialize the DP. Can be done in O(N) as well. Although keeping 2-D matrix incase backtracking is required
        for i in range(len(A)):
            elements = []
            for j in range(len(A[i])):
                elements.append(INF)        
            minTransitions.append(elements)
        
        # Set the base condition
        minTransitions[0] = A[0]
        
        for i in range(len(A) - 1):
            for j in range(len(A[i])):
                
                # See if left 1 position yields better result by transitioning
                if j - 1 > -1:
                    if minTransitions[i + 1][j - 1] == INF:
                        minTransitions[i+ 1][j - 1] = minTransitions[i][j] + A[i + 1][j - 1]
                    elif minTransitions[i][j] + A[i + 1][j - 1] < minTransitions[i+ 1][j - 1]:
                        minTransitions[i+ 1][j - 1] = minTransitions[i][j] + A[i + 1][j - 1]
                
                # See if right 1 position yields better result by transitioning
                if j + 1 < len(A[i]):
                    if minTransitions[i + 1][j + 1] == INF:
                        minTransitions[i+ 1][j + 1] = minTransitions[i][j] + A[i + 1][j + 1]
                    elif minTransitions[i][j] + A[i + 1][j + 1] < minTransitions[i+ 1][j + 1]:
                        minTransitions[i+ 1][j + 1] = minTransitions[i][j] + A[i + 1][j + 1]
                
                # See if current positions yields better result by transitioning
                if minTransitions[i + 1][j] == INF:
                        minTransitions[i+ 1][j] = minTransitions[i][j] + A[i + 1][j]
                elif minTransitions[i][j] + A[i + 1][j] < minTransitions[i+ 1][j]:
                        minTransitions[i+ 1][j] = minTransitions[i][j] + A[i + 1][j]
        
        # print(minTransitions)
        return min(minTransitions[-1])
        
