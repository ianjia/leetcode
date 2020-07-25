# Doubly linked list + dictionary (for O(1) time complexity)
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache1(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {} # key: value = node: address of the node
        self.curSize = 0
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        # set head before tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.dic.get(key)
        if node == None:
            return -1
        
        # move to beginning of linked list because it was just accessed
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        node = self.dic.get(key)

        if node == None: # if you need to add the node
            newNode = Node(key, value)

            self.dic[key] = newNode
            self.addNode(newNode)

            self.curSize += 1
            if self.curSize > self.capacity:
                tail = self.deleteTail()
                del self.dic[tail.key]
                self.curSize -= 1
        else: # if you need to move an already existing node to beginning
            node.value = value
            self.moveToHead(node)
        
    def addNode(self, node):
        # adds the new node right after the head (makes it  the most recently accesed)
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        # removes existing node from doubly linked list
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def moveToHead(self, node):
        # move node to head
        self.removeNode(node)
        self.addNode(node)

    def deleteTail(self):
        res = self.tail.prev
        self.removeNode(res)
        return res

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)