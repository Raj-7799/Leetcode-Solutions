class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
