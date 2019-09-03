# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        pos = 1
        temp = head
        
        while temp.next:
            pos += 1
            temp = temp.next
        
        mid = (pos // 2) + 1
        
        pos = 1
        temp = head
        
        while pos < mid:
            temp = temp.next
            pos += 1
            
        return temp
        
        
