class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        mem = [[False for i in range(len(p + 1))] for j in range(len(s + 1)))
    


if __name__ == "__main__":
    driver = Solution()
    s = "aa"
    p = "a*"
    print(driver.isMatch(s , p))]