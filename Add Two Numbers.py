# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        num1 = num1[::-1]
        num2 = num2[::-1]

        ans = int(num1) + int(num2)
        ansNode = ListNode(ans % 10)
        current = ansNode
        ans = ans // 10
        while ans != 0:
            current.next = ListNode(ans % 10)
            ans = ans // 10
            current = current.next

        return ansNode
