# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Two-pointers
class Solution1(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        intersect = self.intersection(head)
        
        if head == None or intersect == None:
            return None
        
        slow = head
        fast = intersect
        
        while slow != fast:
            # it is the same distance from slow and fast to where the cycle begins
            slow = slow.next
            fast = fast.next
            
        return fast
    
    def intersection(self, head):
        # find intersection
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return slow
                
        return None