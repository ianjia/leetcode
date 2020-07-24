# Backtracking
class Solution1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        if n <= 0 or k == 0:
            return res
        
        curCombination = []
        start = 1
        
        self.combinationCore(n, k, curCombination, res, start)  
        return res
    
    def combinationCore(self, n, k, curCombination, res, start):
        if k == len(curCombination):
            res.append(curCombination[:])
            return
        
        for i in range(start, n + 1):
            curCombination.append(i)
            self.combinationCore(n, k, curCombination, res, i + 1)
            curCombination.pop()