# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Elementary Math
class Solution1(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(-1)
        tailNode = dummyNode
        carry = 0
    
        while l1 != None or l2 != None:
            """
            if l1 != None:
                l1Val = l1.val
            else:
                l1Val = 0
            if l2 != None:
                l2Val = l2.val
            else:
                l2Val = 0
            """
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            
            total = carry + l1Val + l2Val
            carry = total // 10
            tailNode.next = ListNode(total % 10)
            tailNode = tailNode.next
            """
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            """
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        if carry > 0:
            tailNode.next = ListNode(carry)
            
        return dummyNode.next