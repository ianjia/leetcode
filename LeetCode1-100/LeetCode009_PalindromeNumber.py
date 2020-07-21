# Add in reverse
class Solution1(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        curNum, curX = 0, abs(x)
        
        while curX > 0:
            curNum = curNum * 10 + curX % 10
            curX //= 10
            
        return x == curNum

# List (Not follow up)
class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        listX = list(map(int, str(x)))
        
        return listX == listX[::-1]

# String (Not follow up)
class Solution3(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]