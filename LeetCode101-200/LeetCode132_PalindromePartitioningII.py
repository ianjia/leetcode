# Backtracking - Time limit exceeded
class Solution1(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        partitions = self.partition(s)
        partitions = [len(partition) - 1 for partition in partitions]
        
        return min(partitions)
        
    def partition(self, s):
        if len(s) == 0:
            return 0
        
        res = []
        
        self.backtrack(s, 0, [], res)
        return res
    
    def backtrack(self, s, start, cur, res):
        if start == len(s):
            res.append(cur[:])    
            return

        for i in range(start, len(s)):
            if self.isPalindrome(s[start:i + 1]):
                curChar = s[start:i + 1]
                cur.append(curChar)
                self.backtrack(s, i + 1, cur, res)
                cur.pop()
                
    def isPalindrome(self, s):
        return s == s[::-1]

# Dynamic Programming
import sys

class Solution2(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        f = [sys.maxsize] * (len(s) + 1)
        f[0] = 0
        
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if self.isPalindrome(s[j:i]):
                    f[i] = min(f[i], f[j] + 1) # we want to find least number of cuts so min()
                    
        return f[len(s)] - 1
    
    def isPalindrome(self, s):
        return s == s[::-1]