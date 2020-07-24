# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Merge
class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyNode = ListNode(-1)
        tailNode = dummyNode
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tailNode.next = l1
                l1 = l1.next
            else:
                tailNode.next = l2
                l2 = l2.next
            tailNode = tailNode.next
        """
        if l1 != None:
            tailNode.next = l1
        if l2 != None:
            tailNode.next = l2
        """
        tailNode.next = l1 if l1 else l2
        
        return dummyNode.next

# Recursion
class Solution2(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2