# String
class Solution1(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1:
            return ""
        
        if n == 1:
            return "1"
        
        res = "1"
        
        while n > 1:
            count = 1
            curStr = ""
            for i in range(1, len(res)):
                if res[i] == res[i-1]:
                    count += 1
                else:
                    curStr += str(count)
                    curStr += res[i-1]
                    count = 1 # reset count   
            curStr += str(count)
            curStr += res[-1]
            res = curStr
            n -= 1
        
        return res