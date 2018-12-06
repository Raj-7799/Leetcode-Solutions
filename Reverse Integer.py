class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        if x < 0:
            x = x * -1
            negative = True

        x = str(x)
        x = x[::-1]
        x = int(x)

        if negative:
            if x < -2147483648 or x > 2147483647:
                return 0
            return x * -1
        if x < -2147483648 or x > 2147483647:
            return 0
        return x
