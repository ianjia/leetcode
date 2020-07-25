# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Iterative
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        
        while head != None:
            tempNode = head.next
            head.next = newHead
            newHead = head
            head = tempNode
            
        return newHead