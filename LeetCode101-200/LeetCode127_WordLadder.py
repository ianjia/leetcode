class Queue(object):
    def __init__(self):
        self._items = []

    def isEmpty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)
    
    def pop(self):
        self._items.pop()

# BFS
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordListSet = set(wordList) # uses set of wordList since normal array wouldn't pass time limit
        if endWord not in wordListSet:
            return 0
        
        queue = Queue()
        queue.enqueue([beginWord, 1]) # enqueues the word and the current number of word transformations
        visited = set()
        
        while queue.isEmpty() == False:
            word, numOfTrans = queue.dequeue()
            if word == endWord:
                return numOfTrans
            for i in range(0, len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    curWord = word[:i] + char + word[i+1:len(word)] # adds char in random position in curWord
                    if curWord in wordListSet and curWord not in visited:
                        visited.add(curWord)
                        queue.enqueue([curWord, numOfTrans + 1])
        
        return 0