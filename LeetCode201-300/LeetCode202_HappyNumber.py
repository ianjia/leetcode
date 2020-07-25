class Solution1(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.getNextNum(n)

        return n == 1
        
    def getNextNum(self, n):
        total = 0
        
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit ** 2
            
        return total