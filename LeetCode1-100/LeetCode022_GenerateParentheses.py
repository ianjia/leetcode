# Backtracking
class Solution1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        
        if n == 0:
            return [""]
        
        curStr = ""
        self.generateCore(res, curStr, 0, 0, n)
        
        return res
    
    def generateCore(self, res, curStr, left, right, n):
        if len(curStr) == 2 * n:
            res.append(curStr)
            return
        
        if left < n: # if you can generate more left parentheses
            self.generateCore(res, curStr +'(', left + 1, right, n)
        if right < left: # if there is more left parentheses than right parentheses
            self.generateCore(res, curStr +')', left, right + 1, n)