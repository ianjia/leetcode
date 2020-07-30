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

# Dynamic Programming
class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        
        if n == 0:
            return ""
        
        f = [[False for col in range(n)] for row in range(n)]
        left, length = 0, 1
        
        # Set True for every lenth 1 character
        for i in range(0, n):
            f[i][i] = True
            
        # set True for every length 2 characters if they equal
        for i in range(0, n - 1):
            if s[i] == s[i+1]:
                f[i][i+1] = True
                length = 2
                left = i
                
        # Set True for every length 3 to N characters if they are palindromes
        for curLen in range(3, n + 1):
            for i in range(0, n - curLen + 1):
                j = i + curLen - 1
                f[i][j] = (s[i] == s[j]) and f[i+1][j-1]
                if f[i][j] == True:
                    length = curLen
                    left = i

        return s[left:left + length] # return substring of length "length"