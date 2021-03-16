class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        charArr = list(s)
        charTable = [[False for i in range(len(charArr))]
                     for i in range(len(charArr))]

        for i in range(len(charArr)):
            start = i
            length = 1
            charTable[i][i] = True

        for i in range(1, len(charArr)):
            if charArr[i] == charArr[i - 1]:
                start = i - 1
                length = 2
                charTable[i][i - 1] = True
                charTable[i - 1][i] = True

        k = 3
        while k <= len(charArr):
            i = 0
            while i <= len(charArr) - k:
                j = i + k - 1
                if charArr[i] == charArr[j] and charTable[i + 1][j - 1]:
                    start = i
                    length = k
                    charTable[i][j] = True
                i += 1
            k += 1

        return "".join(charArr[start: start + length])


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome(""))
