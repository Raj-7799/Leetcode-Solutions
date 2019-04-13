class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            a = 0
            b = 1
            c = 0
            for i in range(N-1):
                c = a + b
                a = b
                b = c
            return c
        
