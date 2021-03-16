class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 1):
            return True
        else:
            tmp = 1
            while (tmp < n):
                tmp = tmp * 2
            if (tmp == n):
                return True
            
            return False
