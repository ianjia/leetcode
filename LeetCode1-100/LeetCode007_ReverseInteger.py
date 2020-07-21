# Reverse
class Solution1(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        strOfX = str(abs(x))
            
        rev = int(strOfX[::-1])
        
        if rev > 2147483648:
            return 0
        
        if x > 0:
            return rev
        else:
            return rev * -1