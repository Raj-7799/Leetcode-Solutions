class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        x = str(x)
        return x == x[::-1]
        

if __name__ == "__main__":
    s = Solution()
    s.isPalindrome(-121)