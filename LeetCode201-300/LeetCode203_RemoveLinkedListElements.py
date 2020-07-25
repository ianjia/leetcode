# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        prev = dummy
        dummy.next = head
        
        while prev.next != None:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next

        return dummy.next