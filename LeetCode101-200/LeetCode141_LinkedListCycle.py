# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Two-pointers
class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast: # if fast == slow, that means fast lapped slow
            if fast == None or fast.next == None:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
        return True

# Two-pointers
class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
                
        if fast == None or fast.next == None:
            return False
        
        return True