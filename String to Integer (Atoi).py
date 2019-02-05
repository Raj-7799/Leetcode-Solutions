class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        num = "0"
        for i in range(len(str)):
            if str[i].isdigit():
                num += str[i]
            elif str[i] in '+-' and len(num) == 1:
                num = str[i] + num
            elif str[i] != ' ' or len(num) > 1:
                break

        return max(min(int(num), 2**31-1), -2**31)
