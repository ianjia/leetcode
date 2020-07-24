# Binary Search
class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1
        if x < 2:
            return x
        
        start = 0
        end = x
        
        while start <= end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x and (mid + 1) * (mid + 1) > x: # if mid * mid in the middle of 2 consecutive integers squared. For example, 11 is inbetween 3 * 3 and 4 * 4
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid

# Math
class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x ** 0.5)