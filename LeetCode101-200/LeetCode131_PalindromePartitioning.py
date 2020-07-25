# Backtracking
class Solution1(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        
        if len(s) == 0:
            return [res]
        
        self.backtrack(s, 0, [], res)
        return res
    
    def backtrack(self, s, start, cur, res):
        if start == len(s):
            res.append(cur[:])    
            return

        for i in range(start, len(s)):
            if self.isPalindrome(s[start:i + 1]): # if substring is palindrome
                curChar = s[start:i + 1] # curChar = substring
                cur.append(curChar)
                self.backtrack(s, i + 1, cur, res)
                cur.pop()
                
    def isPalindrome(self, s):
        return s == s[::-1]