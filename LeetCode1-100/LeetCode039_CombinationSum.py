# Backtracking
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        
        if len(candidates) == 0:
            return result
        
        curCombination = []
        start = 0
        
        self.combinationCore(candidates, target, result, curCombination, start)
        return result
    
    def combinationCore(self, candidates, target, result, curCombination, start):
        if sum(curCombination) == target:
            result.append(curCombination[:])
            return
        
        if sum(curCombination) > target:
            return
        
        for i in range(start, len(candidates)):
            curCombination.append(candidates[i])
            self.combinationCore(candidates, target, result, curCombination, i)
            curCombination.pop()