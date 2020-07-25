# Recursion - Time limit exceeded
class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.wordBreakCore(s, wordDict, 0)
    
    def wordBreakCore(self, s, wordDict, start):
        if start == len(s):
            return True
        
        for i in range(start + 1, len(s) + 1): # i has the same meaning as "end".
            if s[start:i] in wordDict and self.wordBreakCore(s, wordDict, i):
                return True
            
        return False

# Recursion with Memorization
class Solution2(object):
    def __init__(self):
        self.memo = {}
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.wordBreakCore(s, wordDict, 0)
    
    def wordBreakCore(self, s, wordDict, start):
        if self.memo.get(start) != None:
            return self.memo[start]
        
        if start == len(s):
            return True
        
        for i in range(start + 1, len(s) + 1): # i has the same meaning as "end".
            if s[start:i] in wordDict and self.wordBreakCore(s, wordDict, i):
                self.memo[i] = True
                return True
            
        self.memo[start] = False
        return False