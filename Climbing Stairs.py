class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        if n < 2:
            return 1
        else:
            ways = [0 for i in range(n)]

            ways[-1] = 1
            ways[-2] = 2

            for i in range(n-3, -1, -1):
                ways[i] = ways[i + 1] + ways[i + 2]

            return ways[0]
