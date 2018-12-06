class Solution:

    def checkPalindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False


    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        charArr = list(s)
        output = ""
        size = 0

        for i in range(len(charArr)):
            p = ""
            for i in range(i, len(charArr)):
                p += charArr[i]
                
                if self.checkPalindrome(p):
                    if len(p) > size:
                        output = p
                        size = len(p)

        return output

    
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abba"))