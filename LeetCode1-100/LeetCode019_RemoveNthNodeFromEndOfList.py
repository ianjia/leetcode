# Reverse linked list
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        
        dummyNode = ListNode(-1)
        prev = dummyNode
        
        newHead = self.reverseList(head)
        dummyNode.next = newHead
        i = 0
        
        while prev.next != None:
            if i + 1 == n:
                prev.next = prev.next.next
            else:
                prev = prev.next
            i += 1
                
        revDummy = self.reverseList(dummyNode.next)
        return revDummy
        
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

# One pass algorithm
class Solution2(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyNode = ListNode(-1)
        dummyNode.next = head
        first = dummyNode
        second = dummyNode
        
        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(1, n + 2):
            first = first.next
            
        # Move first to the end, maintaining the gap
        while first != None:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return dummyNode.next