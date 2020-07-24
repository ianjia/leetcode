# Recursion - Time limit exceeded because it will repeatedly caculate some stairs
class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# Fibonacci Number
class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        prevNum = 1
        curNum = 2
        
        for _ in range(0, n - 2):
            curNum = prevNum + curNum
            prevNum = curNum - prevNum
            
        return curNum

# Dynamic Programming
class Solution3(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        
        f = [0] * (n + 1)
        f[1] = 1
        f[2] = 2
        for i in range(3, n + 1):
            f[i] = f[i-1] + f[i-2]
            
        return f[n]