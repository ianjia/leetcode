# Reverse
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string_of_x = str(abs(x))
            
        rev = int(string_of_x[::-1])
        
        if rev > 2147483648:
            return 0
        
        if x > 0:
            return rev
        else:
            rev = rev * -1
            return rev