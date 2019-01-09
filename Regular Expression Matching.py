class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        mem = [[False * (len(p) + 1)] * (len(s) + 1)]

        mem[0][0] = True

        for j in range(2, len(s) + 1):
            mem[0][j] = mem[0] and p[j - 1] == "*"

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if (p[j - 1] == s[i - 1] or p[j - 1] == ".") and mem[i - 1][j - 1]:
                    mem[i][j] = True
                elif p[j - 1] == "*":
                    mem[i][j] = mem[i][j - 2] or mem[i][j - 1]

        return mem[-1][-1]

if __name__ == "__main__":
    driver = Solution()
    s = "aa"
    p = "a*"
    print(driver.isMatch(s , p))