# Two-Pointers
class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        for i in range(0, len(s)):
            # makes length of curStr odd
            curStr = self.helper(s, i, i)
            if len(curStr) > len(res):
                res = curStr
                
            # makes lenth of curStr even
            curStr = self.helper(s, i, i + 1)
            if len(curStr) > len(res):
                res = curStr
                
        return res

    # Check if is palindrome from the middle going towards the outside
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return s[left + 1:right]