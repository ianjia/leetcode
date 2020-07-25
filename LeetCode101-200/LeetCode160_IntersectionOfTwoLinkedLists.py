# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Linked List
class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenOfHeadA = self.lenOfList(headA)
        lenOfHeadB = self.lenOfList(headB)
        
        posDiff = abs(lenOfHeadA - lenOfHeadB)
        
        for _ in range(0, posDiff): # move the longer linked list forward so that they have the same length
            if lenOfHeadA > lenOfHeadB:
                headA = headA.next
            else:
                headB = headB.next
        
        while headA != None and headB != None: # since they now have the same length, they can both move forward at the same time
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        return None
    
    def lenOfList(self, head):
        count = 0
        
        while head != None:
            count += 1
            head = head.next
            
        return count