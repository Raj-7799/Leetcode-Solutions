class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        answer = 0
        right = 0
        left = 0
        
        while right < len(A):            
            
            if A[right] == 0:
                K -= 1
            
            if K < 0:
                if A[left] == 0:
                    K += 1
                left += 1
            
            # print(left, right, K)
            right += 1
            
        return right - left
            
